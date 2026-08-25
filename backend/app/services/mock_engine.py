import time
import uuid
from datetime import datetime
from app.models.schema import AuditReport, AuditMetadata, VerificationCheck, ExtractedItem, BoundingBox

def get_preset_1_report() -> AuditReport:
    # Indofood Clean Delivery - 100% Match
    return AuditReport(
        audit_id=f"AUD-{uuid.uuid4().hex[:8].upper()}",
        timestamp=datetime.now().isoformat(),
        overall_status="APPROVED_FOR_INVOICING",
        confidence_score=0.985,
        total_ordered_items=165,
        total_received_items=165,
        discrepancy_count=0,
        total_claim_amount_idr=0.0,
        metadata=AuditMetadata(
            document_number="SJ/ICBP/2026/08/9481",
            po_number="PO-WHS-2026-881",
            date="25 Agustus 2026",
            sender_company="PT INDOFOOD CBP SUKSES MAKMUR TBK",
            receiver_company="PT SUMBER ALFARIA TRIJAYA TBK (ALFAMART DC)",
            truck_plate="B 9421 UXZ",
            driver_name="Budi Santoso (PT Surya Logistik)"
        ),
        verification=VerificationCheck(
            stamp_detected=True,
            stamp_text="PT SUMBER ALFARIA TRIJAYA - DITERIMA DC CIKOKOL",
            stamp_valid=True,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=True,
            audit_notes=[
                "Official DC receiving stamp clearly detected and verified.",
                "Warehouse checker and driver signatures present.",
                "100% physical item count matches original Purchase Order."
            ]
        ),
        items=[
            ExtractedItem(
                item_number="1",
                item_name="INDOMIE GORENG SPESIAL 85G (KARTON @40 PCS)",
                ordered_qty=50,
                received_qty=50,
                unit="KARTON",
                variance=0,
                status="MATCH",
                handwritten_note="Kondisi Baik - Segel Utuh",
                unit_price_estimate_idr=125000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=225, xmin=50, ymax=255, xmax=950, label="Item 1: Indomie Goreng", category="item_row")
            ),
            ExtractedItem(
                item_number="2",
                item_name="CHITATO SAPI PANGGANG 68G (KARTON @30 PCS)",
                ordered_qty=30,
                received_qty=30,
                unit="KARTON",
                variance=0,
                status="MATCH",
                handwritten_note="Kondisi Baik",
                unit_price_estimate_idr=210000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=256, xmin=50, ymax=286, xmax=950, label="Item 2: Chitato Sapi Panggang", category="item_row")
            ),
            ExtractedItem(
                item_number="3",
                item_name="POP MIE KUAH AYAM BAWANG 75G (KARTON @24 PCS)",
                ordered_qty=40,
                received_qty=40,
                unit="KARTON",
                variance=0,
                status="MATCH",
                handwritten_note="Kondisi Baik",
                unit_price_estimate_idr=145000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=287, xmin=50, ymax=317, xmax=950, label="Item 3: Pop Mie", category="item_row")
            ),
            ExtractedItem(
                item_number="4",
                item_name="INDOFOOD KECAP MANIS POUCH 520ML (DUS @12 PCS)",
                ordered_qty=25,
                received_qty=25,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Kondisi Baik",
                unit_price_estimate_idr=180000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=318, xmin=50, ymax=348, xmax=950, label="Item 4: Kecap Manis", category="item_row")
            ),
            ExtractedItem(
                item_number="5",
                item_name="BUMBU RACIK AYAM GORENG (DUS @120 PCS)",
                ordered_qty=20,
                received_qty=20,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Kondisi Baik",
                unit_price_estimate_idr=240000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=349, xmin=50, ymax=379, xmax=950, label="Item 5: Bumbu Racik", category="item_row")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=200, xmin=50, ymax=380, xmax=950, label="Reconciliation Items Table", category="item_row"),
            BoundingBox(ymin=620, xmin=750, ymax=740, xmax=930, label="Verified DC Receiving Stamp", category="stamp"),
            BoundingBox(ymin=630, xmin=100, ymax=720, xmax=250, label="Driver Signature (Budi)", category="signature"),
            BoundingBox(ymin=630, xmin=440, ymax=720, xmax=590, label="DC Receiver Signature (Agus)", category="signature")
        ],
        raw_remarks="Barang diterima lengkap dalam keadaan bersih dan tersegel.",
        execution_time_ms=480,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def get_preset_2_report() -> AuditReport:
    # Mayora Partial Return / Discrepancy
    return AuditReport(
        audit_id=f"AUD-{uuid.uuid4().hex[:8].upper()}",
        timestamp=datetime.now().isoformat(),
        overall_status="DISCREPANCY_FLAGGED",
        confidence_score=0.965,
        total_ordered_items=250,
        total_received_items=242,
        discrepancy_count=1,
        total_claim_amount_idr=1440000.0,
        metadata=AuditMetadata(
            document_number="MYR-LOG-JKT-2026-4421",
            po_number="PO-IDM-2026-1049",
            date="25 Agustus 2026",
            sender_company="PT MAYORA INDAH TBK",
            receiver_company="PT INDOMARCO PRISMATAMA (INDOMARET DC ANCOL)",
            truck_plate="B 9081 PQR",
            driver_name="Hendra Gunawan"
        ),
        verification=VerificationCheck(
            stamp_detected=True,
            stamp_text="INDOMARCO PRISMATAMA - DC ANCOL - TERIMA SEBAGIAN / RETUR",
            stamp_valid=True,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=False,
            audit_notes=[
                "Discrepancy detected on Beng Beng Regular: Ordered 60 Dus, Received 52 Dus (Shortage of 8 Dus).",
                "Handwritten strikethrough and annotation 'RETUR 8 DUS (KARDUS BASAH)' extracted with high confidence.",
                "Partial receiving stamp 'TERIMA SEBAGIAN / RETUR' confirmed on document.",
                "Invoice debit claim recommendation generated: IDR 1,440,000 deduction."
            ]
        ),
        items=[
            ExtractedItem(
                item_number="1",
                item_name="ROMA BISKUIT KELAPA 300G (DUS @24)",
                ordered_qty=100,
                received_qty=100,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Lengkap",
                unit_price_estimate_idr=155000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=225, xmin=50, ymax=255, xmax=950, label="Item 1: Roma Kelapa", category="item_row")
            ),
            ExtractedItem(
                item_number="2",
                item_name="BENG BENG REGULAR 20x20G (DUS @12 BOX)",
                ordered_qty=60,
                received_qty=52,
                unit="DUS",
                variance=-8,
                status="DISCREPANCY",
                handwritten_note="RETUR 8 DUS (KARDUS BASAH) - Sopir bawa kembali",
                unit_price_estimate_idr=180000,
                claim_amount_idr=1440000,
                bounding_box=BoundingBox(ymin=256, xmin=50, ymax=295, xmax=950, label="Discrepancy Alert: Beng Beng -8 Dus", category="handwritten_retur")
            ),
            ExtractedItem(
                item_number="3",
                item_name="TORABIKA CAPPUCCINO 10x25G (DUS @10 RCG)",
                ordered_qty=50,
                received_qty=50,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Lengkap",
                unit_price_estimate_idr=165000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=296, xmin=50, ymax=326, xmax=950, label="Item 3: Torabika Cappuccino", category="item_row")
            ),
            ExtractedItem(
                item_number="4",
                item_name="KOPIKO COFFEE CANDY 150G (DUS @24 BAG)",
                ordered_qty=40,
                received_qty=40,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Lengkap",
                unit_price_estimate_idr=190000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=327, xmin=50, ymax=357, xmax=950, label="Item 4: Kopiko Candy", category="item_row")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=256, xmin=50, ymax=295, xmax=950, label="⚠️ Handwritten Retur 8 Dus (Beng Beng)", category="handwritten_retur"),
            BoundingBox(ymin=440, xmin=50, ymax=510, xmax=950, label="Berita Acara Selisih & Retur", category="warning"),
            BoundingBox(ymin=620, xmin=750, ymax=740, xmax=930, label="Partial Receiving Stamp (Retur)", category="stamp"),
            BoundingBox(ymin=630, xmin=100, ymax=720, xmax=250, label="Driver Signature (Hendra)", category="signature"),
            BoundingBox(ymin=630, xmin=440, ymax=720, xmax=590, label="Checker Signature (Wahyu)", category="signature")
        ],
        raw_remarks="Selisih 8 Dus Beng Beng diretur langsung ke pabrik karena kemasan basah saat pembongkaran.",
        execution_time_ms=520,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def get_preset_3_report() -> AuditReport:
    # Wings Group Critical Damage & Incomplete Stamp
    return AuditReport(
        audit_id=f"AUD-{uuid.uuid4().hex[:8].upper()}",
        timestamp=datetime.now().isoformat(),
        overall_status="CRITICAL_REJECTED",
        confidence_score=0.940,
        total_ordered_items=230,
        total_received_items=214,
        discrepancy_count=2,
        total_claim_amount_idr=2780000.0,
        metadata=AuditMetadata(
            document_number="SJ-SMU-2026-7890",
            po_number="PO-HYP-2026-3120",
            date="25 Agustus 2026",
            sender_company="PT SAYAP MAS UTAMA (WINGS GROUP)",
            receiver_company="HYPERMART SUPERMAL KARAWACI",
            truck_plate="B 9552 WXY",
            driver_name="Dedi Kusnadi (Logisly Express)"
        ),
        verification=VerificationCheck(
            stamp_detected=False,
            stamp_text=None,
            stamp_valid=False,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=False,
            audit_notes=[
                "CRITICAL: Store receiving rubber stamp is MISSING from the document.",
                "Major damage reported: 6 Dus SoKlin Liquid broken/leaked (IDR 1,380,000).",
                "Damaged goods reported: 10 Dus Ale-Ale crushed/rejected (IDR 1,400,000).",
                "Invoice status: BLOCKED pending formal store stamp and damage claim sign-off."
            ]
        ),
        items=[
            ExtractedItem(
                item_number="1",
                item_name="SO KLIN LIQUID DETERGENT 750ML (DUS @12)",
                ordered_qty=80,
                received_qty=74,
                unit="DUS",
                variance=-6,
                status="DAMAGED",
                handwritten_note="6 DUS BOCOR/HANCUR",
                unit_price_estimate_idr=230000,
                claim_amount_idr=1380000,
                bounding_box=BoundingBox(ymin=225, xmin=50, ymax=262, xmax=950, label="⚠️ Damaged Goods: 6 Dus SoKlin Bocor", category="warning")
            ),
            ExtractedItem(
                item_number="2",
                item_name="NUVO FAMILY SABUN BATANG 110G (DUS @72)",
                ordered_qty=50,
                received_qty=50,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Lengkap",
                unit_price_estimate_idr=175000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=263, xmin=50, ymax=293, xmax=950, label="Item 2: Nuvo Family", category="item_row")
            ),
            ExtractedItem(
                item_number="3",
                item_name="ALE-ALE MINUMAN RASA JERUK 200ML (DUS @24)",
                ordered_qty=100,
                received_qty=90,
                unit="DUS",
                variance=-10,
                status="DAMAGED",
                handwritten_note="10 DUS PENYOK/RETUR",
                unit_price_estimate_idr=140000,
                claim_amount_idr=1400000,
                bounding_box=BoundingBox(ymin=294, xmin=50, ymax=331, xmax=950, label="⚠️ Crushed Packaging: 10 Dus Ale-Ale", category="warning")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=225, xmin=50, ymax=262, xmax=950, label="⚠️ SoKlin Leakage Discrepancy", category="warning"),
            BoundingBox(ymin=294, xmin=50, ymax=331, xmax=950, label="⚠️ Ale-Ale Crushed Cartons Discrepancy", category="warning"),
            BoundingBox(ymin=440, xmin=50, ymax=510, xmax=950, label="Berita Acara Kerusakan Barang", category="warning"),
            BoundingBox(ymin=620, xmin=750, ymax=740, xmax=930, label="❌ MISSING STORE STAMP", category="warning"),
            BoundingBox(ymin=630, xmin=100, ymax=720, xmax=250, label="Driver Signature (Dedi)", category="signature"),
            BoundingBox(ymin=630, xmin=440, ymax=720, xmax=590, label="Store Receiving Signature (Rahmat)", category="signature")
        ],
        raw_remarks="Ditemukan 6 Dus SoKlin kemasan pecah bocor dan 10 Dus Ale-Ale penyok parah. Barang rusak tidak diterima.",
        execution_time_ms=590,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def audit_mock_image(preset_id: str = "preset_1") -> AuditReport:
    if "preset_2" in preset_id or "mayora" in preset_id.lower() or "discrepancy" in preset_id.lower():
        return get_preset_2_report()
    elif "preset_3" in preset_id or "wings" in preset_id.lower() or "damage" in preset_id.lower():
        return get_preset_3_report()
    else:
        return get_preset_1_report()
