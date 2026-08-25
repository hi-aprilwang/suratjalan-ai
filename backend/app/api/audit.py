import os
from typing import List, Optional
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from app.models.schema import AuditReport, PresetItem, ExportRequest
from app.services.gemini_vlm import analyze_document_image
from app.services.mock_engine import get_preset_1_report, get_preset_2_report, get_preset_3_report

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
        if preset_id == "preset_2":
            return get_preset_2_report()
        elif preset_id == "preset_3":
            return get_preset_3_report()
        else:
            return get_preset_1_report()
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
            "delivery_ref": rep.metadata.document_number,
            "origin": rep.metadata.po_number,
            "state": "done" if rep.overall_status == "APPROVED_FOR_INVOICING" else "exception",
            "discrepancy_amount": rep.total_claim_amount_idr,
            "lines": [
                {
                    "product_name": it.item_name,
                    "qty_demand": it.ordered_qty,
                    "qty_done": it.received_qty,
                    "discrepancy": it.variance,
                    "uom": it.unit,
                    "notes": it.handwritten_note
                }
                for it in rep.items
            ]
        }
    else: # JURNAL_ID / ACCURATE
        erp_payload = {
            "transaction_no": rep.metadata.document_number,
            "reference_no": rep.metadata.po_number,
            "status": "APPROVED" if rep.overall_status == "APPROVED_FOR_INVOICING" else "HOLD",
            "debit_memo_amount": rep.total_claim_amount_idr,
            "details": [
                {
                    "item": it.item_name,
                    "ordered": it.ordered_qty,
                    "received": it.received_qty,
                    "unit": it.unit,
                    "claim": it.claim_amount_idr,
                    "note": it.handwritten_note
                }
                for it in rep.items
            ]
        }

    return {
        "success": True,
        "audit_id": rep.audit_id,
        "target_system": target,
        "synced_at": rep.timestamp,
        "erp_payload": erp_payload,
        "message": f"Successfully mapped and synchronized audit record to {target} gateway."
    }
