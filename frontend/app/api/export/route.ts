import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { report, target_system } = body;

    const erpPayload = {
      MANDT: "100",
      DOC_TYPE: "ZPOD_AUDIT",
      BELNR: report?.metadata?.document_number || "SJ-UNKNOWN",
      PURCHASE_ORDER: report?.metadata?.po_number || "PO-UNKNOWN",
      VENDOR: report?.metadata?.sender_company || "VENDOR",
      PLANT_DC: report?.metadata?.receiver_company || "DC",
      POSTING_STATUS: report?.overall_status === "APPROVED_FOR_INVOICING" ? "POSTED_CLEARED" : "PARKED_DISCREPANCY",
      TOTAL_CLAIM_IDR: report?.total_claim_amount_idr || 0,
      LINE_ITEMS: report?.items || []
    };

    return NextResponse.json({
      success: true,
      audit_id: report?.audit_id,
      target_system: target_system || "SAP_S4HANA",
      synced_at: new Date().toISOString(),
      erp_payload: erpPayload,
      message: `Successfully generated export integration payload for ${target_system || 'SAP S/4HANA'}.`
    });
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : 'Unknown error';
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
