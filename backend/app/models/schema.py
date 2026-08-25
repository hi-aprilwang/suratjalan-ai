from typing import List, Optional
from pydantic import BaseModel, Field

class BoundingBox(BaseModel):
    # Normalized coordinates: 0.0 - 1000.0 or 0.0 - 1.0
    ymin: float = Field(..., description="Top coordinate normalized (0-1000)")
    xmin: float = Field(..., description="Left coordinate normalized (0-1000)")
    ymax: float = Field(..., description="Bottom coordinate normalized (0-1000)")
    xmax: float = Field(..., description="Right coordinate normalized (0-1000)")
    label: str = Field(..., description="Label or text description")
    category: str = Field(..., description="header | item_row | stamp | signature | handwritten_retur | warning")
    confidence: float = Field(default=0.95)

class ExtractedItem(BaseModel):
    item_number: str
    item_name: str
    ordered_qty: float
    received_qty: float
    unit: str
    variance: float = Field(..., description="received_qty - ordered_qty")
    status: str = Field(..., description="MATCH | DISCREPANCY | DAMAGED | MISSING")
    handwritten_note: Optional[str] = None
    unit_price_estimate_idr: float = Field(default=0.0)
    claim_amount_idr: float = Field(default=0.0)
    bounding_box: Optional[BoundingBox] = None

class VerificationCheck(BaseModel):
    stamp_detected: bool
    stamp_text: Optional[str] = None
    stamp_valid: bool
    receiver_signature_detected: bool
    driver_signature_detected: bool
    all_checks_passed: bool
    audit_notes: List[str] = []

class AuditMetadata(BaseModel):
    document_number: str
    po_number: Optional[str] = None
    date: Optional[str] = None
    sender_company: str
    receiver_company: str
    truck_plate: Optional[str] = None
    driver_name: Optional[str] = None

class AuditReport(BaseModel):
    audit_id: str
    timestamp: str
    overall_status: str = Field(..., description="APPROVED_FOR_INVOICING | DISCREPANCY_FLAGGED | CRITICAL_REJECTED")
    confidence_score: float
    total_ordered_items: float
    total_received_items: float
    discrepancy_count: int
    total_claim_amount_idr: float
    metadata: AuditMetadata
    verification: VerificationCheck
    items: List[ExtractedItem]
    bounding_boxes: List[BoundingBox]
    raw_remarks: Optional[str] = None
    execution_time_ms: int
    ai_model_used: str

class PresetItem(BaseModel):
    id: str
    title: str
    company: str
    expected_status: str
    image_url: str
    description: str

class ExportRequest(BaseModel):
    audit_id: str
    target_system: str = Field(default="SAP_S4HANA", description="SAP_S4HANA | ODOO_ERP | JURNAL_ID | ACCURATE")
    report: AuditReport
