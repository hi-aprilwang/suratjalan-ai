export interface BoundingBox {
  ymin: number;
  xmin: number;
  ymax: number;
  xmax: number;
  label: string;
  category: 'header' | 'item_row' | 'stamp' | 'signature' | 'handwritten_retur' | 'warning' | 'recipient' | 'transporter' | 'table';
  confidence?: number;
}

export interface ExtractedItem {
  item_number: string;
  item_name: string;
  ordered_qty: number;
  received_qty: number;
  unit: string;
  variance: number;
  status: 'MATCH' | 'DISCREPANCY' | 'DAMAGED' | 'MISSING' | 'RETURNED';
  handwritten_note?: string | null;
  unit_price_estimate_idr: number;
  claim_amount_idr: number;
  bounding_box?: BoundingBox | null;
}

export interface VerificationCheck {
  stamp_detected: boolean;
  stamp_text?: string | null;
  stamp_valid: boolean;
  receiver_signature_detected: boolean;
  driver_signature_detected: boolean;
  all_checks_passed: boolean;
  audit_notes: string[];
}

export interface AuditMetadata {
  document_number: string;
  po_number?: string | null;
  date?: string | null;
  sender_company: string;
  receiver_company: string;
  truck_plate?: string | null;
  driver_name?: string | null;
}

export interface AuditReport {
  audit_id: string;
  timestamp: string;
  overall_status: 'APPROVED_FOR_INVOICING' | 'DISCREPANCY_FLAGGED' | 'CRITICAL_REJECTED';
  confidence_score: number;
  total_ordered_items: number;
  total_received_items: number;
  discrepancy_count: number;
  total_claim_amount_idr: number;
  metadata: AuditMetadata;
  verification: VerificationCheck;
  items: ExtractedItem[];
  bounding_boxes: BoundingBox[];
  raw_remarks?: string | null;
  execution_time_ms: number;
  ai_model_used: string;
}

export interface PresetItem {
  id: string;
  title: string;
  company: string;
  expected_status: 'APPROVED_FOR_INVOICING' | 'DISCREPANCY_FLAGGED' | 'CRITICAL_REJECTED';
  image_url: string;
  description: string;
}
