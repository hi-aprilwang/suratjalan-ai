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
                unit_price_estimate_idr=160000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=349, xmin=50, ymax=379, xmax=950, label="Item 5: Bumbu Racik", category="item_row")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=115, xmin=50, ymax=185, xmax=480, label="Recipient (Alfamart DC)", category="recipient"),
            BoundingBox(ymin=115, xmin=500, ymax=185, xmax=950, label="Transporter & Vehicle", category="transporter"),
            BoundingBox(ymin=200, xmin=50, ymax=380, xmax=950, label="Line-Item Table", category="table"),
            BoundingBox(ymin=470, xmin=750, ymax=600, xmax=910, label="Verified DC Stamp (Cikokol)", category="stamp"),
            BoundingBox(ymin=490, xmin=100, ymax=580, xmax=250, label="Driver Signature", category="signature"),
            BoundingBox(ymin=490, xmin=420, ymax=580, xmax=570, label="Receiver Signature", category="signature")
        ],
        raw_remarks="Barang diterima lengkap 165 karton tanpa cacat di DC Cikokol.",
        execution_time_ms=480,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def get_preset_2_report() -> AuditReport:
    # Mayora Partial Return (8 Wet Cartons)
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
            driver_name="Hendra Gunawan (PT Mayora Logistics)"
        ),
        verification=VerificationCheck(
            stamp_detected=True,
            stamp_text="INDOMARET DISTRIBUTION CENTER - DITERIMA BERSYARAT - DC ANCOL",
            stamp_valid=True,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=False,
            audit_notes=[
                "Discrepancy detected: Beng Beng regular delivery variance (-8 Dus).",
                "Handwritten strikethrough '60' replaced with '52'.",
                "Checker note identified: 'RETUR 8 DUS (KARDUS BASAH)'.",
                "Automated Debit Memo generated for IDR 1,440,000 deduction."
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
                unit_price_estimate_idr=210000,
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
                status="RETURNED",
                handwritten_note="RETUR 8 DUS (KARDUS BASAH)",
                unit_price_estimate_idr=180000,
                claim_amount_idr=1440000,
                bounding_box=BoundingBox(ymin=256, xmin=50, ymax=295, xmax=950, label="⚠️ Handwritten Retur 8 Dus (Beng Beng)", category="handwritten_retur")
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
                unit_price_estimate_idr=240000,
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
            document_number="SJ/WINGS/2026/08/7712",
            po_number="PO-HYPER-2026-901",
            date="25 Agustus 2026",
            sender_company="PT SAYAP MAS UTAMA (WINGS GROUP)",
            receiver_company="PT MATAHARI PUTRA PRIMA TBK (HYPERMART KARAWACI)",
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

def get_preset_4_report() -> AuditReport:
    # Frisian Flag Cold Chain Logistics (Temperature Breach & Acidified Milk)
    return AuditReport(
        audit_id=f"AUD-{uuid.uuid4().hex[:8].upper()}",
        timestamp=datetime.now().isoformat(),
        overall_status="DISCREPANCY_FLAGGED",
        confidence_score=0.972,
        total_ordered_items=200,
        total_received_items=185,
        discrepancy_count=1,
        total_claim_amount_idr=3300000.0,
        metadata=AuditMetadata(
            document_number="SJ/FFI-COLD/2026/08/3019",
            po_number="PO-TRANS-COLD-2026-552",
            date="25 Agustus 2026",
            sender_company="PT FRISIAN FLAG INDONESIA",
            receiver_company="PT TRANSMART RETAIL INDONESIA (DC LEBAK BULUS)",
            truck_plate="B 9112 CXY",
            driver_name="Joko Susilo (PT Cold Logistic Indo)"
        ),
        verification=VerificationCheck(
            stamp_detected=True,
            stamp_text="TRANSMART CENTRAL DC - QC COLD CHAIN PASSED - LEBAK BULUS",
            stamp_valid=True,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=False,
            audit_notes=[
                "Cold Chain Alert: Reefer truck arrival temperature reached +14°C (Limit: +4°C).",
                "15 Karton Susu UHT 1000ml rejected due to thermal abuse and sour coagulation.",
                "Official QC stamp and Veterinarian checker signature verified.",
                "Debit claim generated: IDR 3,300,000 for transporter insurance claim."
            ]
        ),
        items=[
            ExtractedItem(
                item_number="1",
                item_name="SUSU UHT FULL CREAM 1000ML (KARTON @12 TETRAPAK)",
                ordered_qty=100,
                received_qty=85,
                unit="KARTON",
                variance=-15,
                status="RETURNED",
                handwritten_note="15 KTN DITOLAK (ASAM/14°C)",
                unit_price_estimate_idr=220000,
                claim_amount_idr=3300000,
                bounding_box=BoundingBox(ymin=225, xmin=50, ymax=265, xmax=950, label="⚠️ Cold Chain Spoilage: 15 KTN Susu UHT", category="handwritten_retur")
            ),
            ExtractedItem(
                item_number="2",
                item_name="SUSU KENTAL MANIS GOLD KALENG 370G (DUS @48)",
                ordered_qty=60,
                received_qty=60,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Lengkap & Dingin",
                unit_price_estimate_idr=480000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=266, xmin=50, ymax=296, xmax=950, label="Item 2: SKM Gold Kaleng", category="item_row")
            ),
            ExtractedItem(
                item_number="3",
                item_name="OMELA KRIMER KENTAL MANIS 370G (DUS @48)",
                ordered_qty=40,
                received_qty=40,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="Lengkap",
                unit_price_estimate_idr=390000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=297, xmin=50, ymax=327, xmax=950, label="Item 3: Omela Krimer", category="item_row")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=115, xmin=500, ymax=185, xmax=950, label="⚠️ Reefer Truck Temp Alert (+14°C)", category="warning"),
            BoundingBox(ymin=225, xmin=50, ymax=265, xmax=950, label="⚠️ Handwritten Rejection (15 KTN UHT)", category="handwritten_retur"),
            BoundingBox(ymin=440, xmin=50, ymax=510, xmax=950, label="Berita Acara Klaim Suhu Reefer", category="warning"),
            BoundingBox(ymin=620, xmin=750, ymax=740, xmax=930, label="Transmart DC QC Cold Chain Stamp", category="stamp"),
            BoundingBox(ymin=630, xmin=100, ymax=720, xmax=250, label="Cold Chain Driver Signature", category="signature"),
            BoundingBox(ymin=630, xmin=440, ymax=720, xmax=590, label="QC Fresh Receiving Signature", category="signature")
        ],
        raw_remarks="Kompresor reefer mati selama perjalanan, 15 Karton UHT asam. Ditolak pihak Transmart.",
        execution_time_ms=510,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def get_preset_5_report() -> AuditReport:
    # Semen Indonesia Heavy Logistics (Tarpaulin Leak / Rain Damage at Mitra10)
    return AuditReport(
        audit_id=f"AUD-{uuid.uuid4().hex[:8].upper()}",
        timestamp=datetime.now().isoformat(),
        overall_status="DISCREPANCY_FLAGGED",
        confidence_score=0.980,
        total_ordered_items=400,
        total_received_items=380,
        discrepancy_count=1,
        total_claim_amount_idr=1360000.0,
        metadata=AuditMetadata(
            document_number="SIG/LOG-JBT/2026/08/1189",
            po_number="PO-M10-BUILD-2026-778",
            date="25 Agustus 2026",
            sender_company="PT SEMEN INDONESIA (PERSERO) TBK",
            receiver_company="PT CATUR MITRA SEJATI SENTOSA (MITRA10 BINTARO)",
            truck_plate="B 9801 UYX",
            driver_name="Slamet Riyadi (PT Varia Usaha Logistik)"
        ),
        verification=VerificationCheck(
            stamp_detected=True,
            stamp_text="PT CATUR MITRA SEJATI SENTOSA - MITRA10 BINTARO HUB - TERIMA DENGAN CATATAN",
            stamp_valid=True,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=False,
            audit_notes=[
                "Logistics transit water damage: 20 Zak Semen Gresik 40kg hardened due to rain leak.",
                "Handwritten correction '200' strikethrough -> '180' confirmed with note.",
                "Mitra10 logistics stamp and warehouse manager signature verified.",
                "Instant transport deduction debit memo: IDR 1,360,000."
            ]
        ),
        items=[
            ExtractedItem(
                item_number="1",
                item_name="SEMEN GRESIK PORTLAND POZZOLAN CEMENT (PPC 40KG)",
                ordered_qty=200,
                received_qty=180,
                unit="ZAK",
                variance=-20,
                status="DAMAGED",
                handwritten_note="20 ZAK BASAH & MEMBATU",
                unit_price_estimate_idr=68000,
                claim_amount_idr=1360000,
                bounding_box=BoundingBox(ymin=225, xmin=50, ymax=265, xmax=950, label="⚠️ Water Damaged Cement: 20 Zak", category="warning")
            ),
            ExtractedItem(
                item_number="2",
                item_name="SEMEN DYNAMIX SERBAGUNA PCC 40KG",
                ordered_qty=150,
                received_qty=150,
                unit="ZAK",
                variance=0,
                status="MATCH",
                handwritten_note="Kering & Utuh",
                unit_price_estimate_idr=70000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=266, xmin=50, ymax=296, xmax=950, label="Item 2: Semen Dynamix 40kg", category="item_row")
            ),
            ExtractedItem(
                item_number="3",
                item_name="MORTAR INDONESIA PEREKAT BATA RINGAN 40KG",
                ordered_qty=50,
                received_qty=50,
                unit="ZAK",
                variance=0,
                status="MATCH",
                handwritten_note="Kering & Utuh",
                unit_price_estimate_idr=85000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=297, xmin=50, ymax=327, xmax=950, label="Item 3: Mortar Perekat", category="item_row")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=225, xmin=50, ymax=265, xmax=950, label="⚠️ Strikethrough & Damaged 20 Zak Semen", category="handwritten_retur"),
            BoundingBox(ymin=440, xmin=50, ymax=510, xmax=950, label="Berita Acara Kerusakan Logistik Semen", category="warning"),
            BoundingBox(ymin=620, xmin=740, ymax=740, xmax=940, label="Mitra10 Receiving Stamp (Catatan)", category="stamp"),
            BoundingBox(ymin=630, xmin=100, ymax=720, xmax=250, label="Driver Signature (Slamet)", category="signature"),
            BoundingBox(ymin=630, xmin=440, ymax=720, xmax=590, label="Mitra10 Manager Signature (Hendro)", category="signature")
        ],
        raw_remarks="Terpal penutup robek di tol Cipali saat hujan. 20 Zak semen membatu dan tidak dapat dijual.",
        execution_time_ms=490,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def get_preset_6_report() -> AuditReport:
    # Kalbe Farma Pharma Distribution (CDOB Shelf-Life / Expiry Rejection by Kimia Farma)
    return AuditReport(
        audit_id=f"AUD-{uuid.uuid4().hex[:8].upper()}",
        timestamp=datetime.now().isoformat(),
        overall_status="CRITICAL_REJECTED",
        confidence_score=0.990,
        total_ordered_items=230,
        total_received_items=180,
        discrepancy_count=1,
        total_claim_amount_idr=27000000.0,
        metadata=AuditMetadata(
            document_number="KLB-FARMA/2026/08/9901",
            po_number="PO-KF-MED-2026-440",
            date="25 Agustus 2026",
            sender_company="PT KALBE FARMA TBK",
            receiver_company="PT KIMIA FARMA APOTEK (PBF PULO GADUNG)",
            truck_plate="B 9400 PHR",
            driver_name="Bambang Pamungkas (Kalbe Logistics)"
        ),
        verification=VerificationCheck(
            stamp_detected=True,
            stamp_text="KIMIA FARMA DC - REJEK QC - ED < 12 BULAN",
            stamp_valid=False,
            receiver_signature_detected=True,
            driver_signature_detected=True,
            all_checks_passed=False,
            audit_notes=[
                "CRITICAL PHARMA REJECTION: Red 'REJEK QC' triangular stamp applied by Licensed Pharmacist.",
                "Batch #WOD092 Woods Syrup (50 Dus) rejected due to remaining shelf life <3 months (BPOM / Kimia Farma SOP).",
                "Entire line item 3 rejected (0 units accepted).",
                "Direct invoice deduction & return shipment order generated: IDR 27,000,000."
            ]
        ),
        items=[
            ExtractedItem(
                item_number="1",
                item_name="PROMAG TAB KUNYAH (DUS @30 CC) - BATCH #PMG881",
                ordered_qty=100,
                received_qty=100,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="ED: 10/2028 (OK)",
                unit_price_estimate_idr=320000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=225, xmin=50, ymax=255, xmax=950, label="Item 1: Promag Tablet", category="item_row")
            ),
            ExtractedItem(
                item_number="2",
                item_name="MIXAGRIP FLU & BATUK (DUS @25 BLS) - BATCH #MXG412",
                ordered_qty=80,
                received_qty=80,
                unit="DUS",
                variance=0,
                status="MATCH",
                handwritten_note="ED: 12/2027 (OK)",
                unit_price_estimate_idr=280000,
                claim_amount_idr=0,
                bounding_box=BoundingBox(ymin=256, xmin=50, ymax=286, xmax=950, label="Item 2: Mixagrip", category="item_row")
            ),
            ExtractedItem(
                item_number="3",
                item_name="WOODS PEPPERMINT ANTITUSSIVE 100ML (DUS @24 BTL) - #WOD092",
                ordered_qty=50,
                received_qty=0,
                unit="DUS",
                variance=-50,
                status="DAMAGED",
                handwritten_note="REJEK TOTAL (ED: 11/2026)",
                unit_price_estimate_idr=540000,
                claim_amount_idr=27000000,
                bounding_box=BoundingBox(ymin=287, xmin=50, ymax=327, xmax=950, label="❌ Total Rejection: 50 Dus Woods Sirup (Expired)", category="warning")
            )
        ],
        bounding_boxes=[
            BoundingBox(ymin=38, xmin=50, ymax=100, xmax=950, label="Header & Metadata", category="header"),
            BoundingBox(ymin=287, xmin=50, ymax=327, xmax=950, label="❌ Rejected Line Item (50 Dus Woods)", category="warning"),
            BoundingBox(ymin=440, xmin=50, ymax=510, xmax=950, label="Berita Acara Penolakan Obat PBF", category="warning"),
            BoundingBox(ymin=610, xmin=740, ymax=730, xmax=940, label="🛑 RED REJECT STAMP (Kimia Farma QC)", category="warning"),
            BoundingBox(ymin=630, xmin=100, ymax=720, xmax=250, label="Driver Signature (Bambang)", category="signature"),
            BoundingBox(ymin=630, xmin=440, ymax=720, xmax=590, label="Pharmacist Signature (apt. Annisa)", category="signature")
        ],
        raw_remarks="Woods Sirup Batch #WOD092 ditolak total karena masa kedaluwarsa kurang dari 3 bulan.",
        execution_time_ms=530,
        ai_model_used="Gemini 2.0 Flash (Multimodal VLM)"
    )

def audit_mock_image(preset_id: str = "preset_1") -> AuditReport:
    if "preset_2" in preset_id or "mayora" in preset_id.lower():
        return get_preset_2_report()
    elif "preset_3" in preset_id or "wings" in preset_id.lower():
        return get_preset_3_report()
    elif "preset_4" in preset_id or "frisian" in preset_id.lower() or "coldchain" in preset_id.lower():
        return get_preset_4_report()
    elif "preset_5" in preset_id or "semen" in preset_id.lower() or "mitra10" in preset_id.lower():
        return get_preset_5_report()
    elif "preset_6" in preset_id or "kalbe" in preset_id.lower() or "pharma" in preset_id.lower() or "kimia" in preset_id.lower():
        return get_preset_6_report()
    else:
        return get_preset_1_report()
