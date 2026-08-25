import os
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from app.models.schema import AuditReport, PresetItem, ExportRequest
from app.services.gemini_vlm import analyze_document_image
from app.services.mock_engine import (
    get_preset_1_report,
    get_preset_2_report,
    get_preset_3_report,
    get_preset_4_report,
    get_preset_5_report,
    get_preset_6_report,
    audit_mock_image
)

router = APIRouter(prefix="", tags=["Audit"])

@router.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "SuratJalan.AI Backend",
        "engine": "Gemini 2.0 Flash Multimodal VLM + Deterministic Fallback",
        "version": "1.0.0"
    }

@router.get("/presets", response_model=List[PresetItem])
async def get_presets():
    return [
        PresetItem(
            id="preset_1",
            title="Preset 1: Clean Delivery (100% Match)",
            company="PT INDOFOOD CBP SUKSES MAKMUR TBK",
            expected_status="APPROVED_FOR_INVOICING",
            image_url="/samples/preset_1_indofood_clean.png",
            description="Complete delivery to Alfamart DC Cikokol with all 165 cartons accounted for, valid rubber stamp, and verified checker signature."
        ),
        PresetItem(
            id="preset_2",
            title="Preset 2: Partial Return / Damaged Wet Cartons",
            company="PT MAYORA INDAH TBK",
            expected_status="DISCREPANCY_FLAGGED",
            image_url="/samples/preset_2_mayora_discrepancy.png",
            description="Beng Beng delivery with 8 wet cartons returned. Features handwritten strikethrough correction, retur note, and partial receiving stamp."
        ),
        PresetItem(
            id="preset_3",
            title="Preset 3: Critical Damage & Missing Stamp Alert",
            company="PT SAYAP MAS UTAMA (WINGS GROUP)",
            expected_status="CRITICAL_REJECTED",
            image_url="/samples/preset_3_wings_damage_alert.png",
            description="Delivery to Hypermart with leaking SoKlin & crushed Ale-Ale cartons, plus MISSING receiver store stamp."
        ),
        PresetItem(
            id="preset_4",
            title="Preset 4: Cold Chain / Dairy Temperature Breach",
            company="PT FRISIAN FLAG INDONESIA",
            expected_status="DISCREPANCY_FLAGGED",
            image_url="/samples/preset_4_frisianflag_coldchain.png",
            description="Reefer truck delivery to Transmart DC with +14°C temperature abuse. 15 Cartons of UHT milk rejected & returned (Claim: IDR 3,300,000)."
        ),
        PresetItem(
            id="preset_5",
            title="Preset 5: Heavy Industry / Rain Leak Damaged Cement",
            company="PT SEMEN INDONESIA (PERSERO) TBK",
            expected_status="DISCREPANCY_FLAGGED",
            image_url="/samples/preset_5_semenindonesia_damaged.png",
            description="Tronton delivery to Mitra10 with 20 rain-soaked hardened cement sacks. Deducted via checker strikethrough (Claim: IDR 1,360,000)."
        ),
        PresetItem(
            id="preset_6",
            title="Preset 6: Pharma CDOB Expiry Rejection",
            company="PT KALBE FARMA TBK",
            expected_status="CRITICAL_REJECTED",
            image_url="/samples/preset_6_kalbefarma_expired.png",
            description="Kimia Farma DC rejection of Woods Syrup batch with <3 months shelf-life. Red triangular REJEK QC stamp (Claim: IDR 27,000,000)."
        )
    ]

@router.post("/audit", response_model=AuditReport)
async def audit_document(
    file: Optional[UploadFile] = File(None),
    preset_id: Optional[str] = Form(None)
):
    if file:
        content = await file.read()
        filename = file.filename or "uploaded_document.png"
        return await analyze_document_image(content, filename)
    elif preset_id:
        return audit_mock_image(preset_id)
    else:
        raise HTTPException(status_code=400, detail="Either 'file' or 'preset_id' must be provided.")

@router.post("/export")
async def export_to_erp(request: ExportRequest):
    rep = request.report
    target = request.target_system
    
    # Simulate ERP integration payloads
    if target == "SAP_S4HANA":
        erp_payload = {
            "MANDT": "100",
            "DOC_TYPE": "ZPOD_AUDIT",
            "BELNR": rep.metadata.document_number,
            "PURCHASE_ORDER": rep.metadata.po_number,
            "VENDOR": rep.metadata.sender_company,
            "PLANT_DC": rep.metadata.receiver_company,
            "POSTING_STATUS": "POSTED_CLEARED" if rep.overall_status == "APPROVED_FOR_INVOICING" else "PARKED_DISCREPANCY",
            "TOTAL_CLAIM_IDR": rep.total_claim_amount_idr,
            "LINE_ITEMS": [
                {
                    "POSNR": it.item_number,
                    "MAKTX": it.item_name,
                    "MENGE_PO": it.ordered_qty,
                    "MENGE_GR": it.received_qty,
                    "DIF_QTY": it.variance,
                    "MEINS": it.unit,
                    "DMBTR_CLAIM": it.claim_amount_idr,
                    "REMARK": it.handwritten_note
                }
                for it in rep.items
            ]
        }
    elif target == "ODOO_ERP":
        erp_payload = {
            "model": "stock.picking.audit",
            "method": "action_reconcile_pod",
            "args": [{
                "name": rep.metadata.document_number,
                "origin": rep.metadata.po_number,
                "partner_id": rep.metadata.sender_company,
                "state": "done" if rep.overall_status == "APPROVED_FOR_INVOICING" else "assigned_with_discrepancy",
                "deduction_amount": rep.total_claim_amount_idr,
                "move_lines": [
                    {
                        "product_name": it.item_name,
                        "product_uom_qty": it.ordered_qty,
                        "qty_done": it.received_qty,
                        "discrepancy_note": it.handwritten_note
                    }
                    for it in rep.items
                ]
            }]
        }
    elif target == "JURNAL_ID":
        erp_payload = {
            "transaction_type": "Debit Note / Potongan Pembelian",
            "reference_no": f"DN-{rep.metadata.document_number}",
            "source_po": rep.metadata.po_number,
            "vendor_name": rep.metadata.sender_company,
            "transaction_date": rep.metadata.date,
            "total_deduction_idr": rep.total_claim_amount_idr,
            "notes": f"Potongan klaim Surat Jalan: {rep.verification.audit_notes[0] if rep.verification.audit_notes else 'Discrepancy'}",
            "accounts_impacted": [
                {"account_code": "5-50100", "account_name": "Biaya Kerusakan Barang Logistik", "debit": rep.total_claim_amount_idr},
                {"account_code": "2-20100", "account_name": "Hutang Usaha (Trade Payables)", "credit": rep.total_claim_amount_idr}
            ]
        }
    else:
        erp_payload = {"raw_report": rep.model_dump()}

    return {
        "status": "success",
        "target_system": target,
        "message": f"Successfully simulated dispatch to {target} integration gateway.",
        "payload": erp_payload
    }
