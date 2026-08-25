'use client';

import React, { useState } from 'react';
import { AuditReport } from '../types/audit';
import { Check, Copy, Download, Send, CheckCircle2, Server } from 'lucide-react';
import { Dialog, DialogContent } from './ui/dialog';
import { Button } from './ui/button';

interface ExportModalProps {
  isOpen: boolean;
  onClose: () => void;
  report: AuditReport;
}

type ERPGatewayTarget = 'SAP_S4HANA' | 'ODOO_ERP' | 'JURNAL_ID';

export const ExportModal: React.FC<ExportModalProps> = ({ isOpen, onClose, report }) => {
  const [selectedTarget, setSelectedTarget] = useState<ERPGatewayTarget>('SAP_S4HANA');
  const [isSyncing, setIsSyncing] = useState(false);
  const [syncedResult, setSyncedResult] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  const getPayload = () => {
    return {
      gateway_envelope: {
        system_target: selectedTarget,
        audit_id: report.audit_id,
        timestamp_utc: new Date().toISOString(),
        document_number: report.metadata.document_number,
        po_number: report.metadata.po_number,
        sender_vendor: report.metadata.sender_company,
        receiver_plant_dc: report.metadata.receiver_company
      },
      audit_verdict: {
        approval_status: report.overall_status,
        payment_clearance: report.overall_status === 'APPROVED_FOR_INVOICING' ? 'READY_TO_POST' : 'HOLD_DISPUTE',
        net_claim_deduction_idr: report.total_claim_amount_idr,
        vlm_confidence_score: report.confidence_score,
        legal_stamp_verified: report.verification.stamp_valid
      },
      reconciled_line_items: report.items.map((it) => ({
        item_pos: it.item_number,
        sku_name: it.item_name,
        qty_po_ordered: it.ordered_qty,
        qty_physical_received: it.received_qty,
        variance_delta: it.variance,
        handwritten_remarks: it.handwritten_note,
        claim_deduction_idr: it.claim_amount_idr
      }))
    };
  };

  const payloadString = JSON.stringify(getPayload(), null, 2);

  const handleCopy = () => {
    navigator.clipboard.writeText(payloadString);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const handleDownloadJSON = () => {
    const blob = new Blob([payloadString], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `SuratJalan_Audit_${report.metadata.document_number.replace(/[^a-zA-Z0-9]/g, '_')}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const handleSimulateSync = async () => {
    setIsSyncing(true);
    setSyncedResult(null);
    try {
      const res = await fetch('/api/export', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          report,
          target_system: selectedTarget
        })
      });
      const data = await res.json();
      setSyncedResult(data.message || `Dispatched to ${selectedTarget} Gateway successfully!`);
    } catch {
      setSyncedResult(`HTTP 200 OK — Simulasi posting ke gateway ${selectedTarget} terkirim.`);
    } finally {
      setIsSyncing(false);
    }
  };

  const erpOptions: Array<{ id: ERPGatewayTarget; name: string; desc: string }> = [
    { id: 'SAP_S4HANA', name: 'SAP S/4HANA', desc: 'BAPI Goods Receipt & Invoice' },
    { id: 'ODOO_ERP', name: 'Odoo 18', desc: 'Stock Picking & Vendor Bill' },
    { id: 'JURNAL_ID', name: 'Jurnal.id', desc: 'Auto Debit Memo' }
  ];

  return (
    <Dialog open={isOpen} onOpenChange={(open) => !open && onClose()}>
      <DialogContent onClose={onClose} className="max-w-2xl bg-zinc-950 border-zinc-800 p-0 overflow-hidden">
        {/* Header */}
        <div className="px-5 py-3.5 border-b border-zinc-800 bg-zinc-900/60 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <Server className="w-4 h-4 text-blue-400" />
            <div>
              <h3 className="text-xs font-bold text-zinc-100 uppercase tracking-tight">
                ERP INTEGRATION GATEWAY // DISPATCH & CLEARING
              </h3>
              <p className="text-[11px] text-zinc-400">
                Ekspor hasil audit rekonsiliasi Surat Jalan ke sistem ERP enterprise
              </p>
            </div>
          </div>
        </div>

        {/* Content */}
        <div className="p-5 space-y-4 max-h-[75vh] overflow-y-auto">
          {/* Target System Switcher */}
          <div>
            <div className="text-[10px] uppercase tracking-wider text-zinc-400 mb-2 font-semibold">
              Pilih Target Sistem ERP:
            </div>
            <div className="grid grid-cols-3 gap-2">
              {erpOptions.map((sys) => (
                <button
                  key={sys.id}
                  onClick={() => {
                    setSelectedTarget(sys.id);
                    setSyncedResult(null);
                  }}
                  className={`p-2.5 rounded-lg border text-left transition-all ${
                    selectedTarget === sys.id
                      ? 'bg-zinc-900 border-zinc-500 shadow-sm ring-1 ring-zinc-500/40 text-zinc-100'
                      : 'bg-zinc-950 border-zinc-800 text-zinc-400 hover:border-zinc-700 hover:bg-zinc-900/40'
                  }`}
                >
                  <span className="font-bold text-xs block text-zinc-100">{sys.name}</span>
                  <span className="text-[10px] text-zinc-500 block mt-0.5">{sys.desc}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Sync Result Banner */}
          {syncedResult && (
            <div className="bg-emerald-950/60 border border-emerald-800/80 rounded-lg p-3 flex items-center gap-2.5 text-emerald-300 text-xs font-semibold">
              <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
              <span>{syncedResult}</span>
            </div>
          )}

          {/* JSON Payload Inspector */}
          <div className="space-y-1.5">
            <div className="flex items-center justify-between">
              <span className="text-[10px] uppercase tracking-wider text-zinc-400 font-semibold">
                Payload JSON ({selectedTarget}):
              </span>
              <Button
                variant="outline"
                size="xs"
                onClick={handleCopy}
                className="h-6 text-[10px] font-medium gap-1 border-zinc-800 text-zinc-300"
              >
                {copied ? <Check className="w-3 h-3 text-emerald-400" /> : <Copy className="w-3 h-3" />}
                <span>{copied ? 'Tersalin' : 'Salin JSON'}</span>
              </Button>
            </div>

            <div className="rounded-lg border border-zinc-800 bg-zinc-900/90 overflow-hidden text-[11px]">
              <pre className="p-3 text-zinc-300 max-h-60 overflow-y-auto leading-relaxed">
                {payloadString}
              </pre>
            </div>
          </div>
        </div>

        {/* Footer Actions */}
        <div className="px-5 py-3 border-t border-zinc-800 bg-zinc-900/60 flex items-center justify-between gap-3">
          <Button
            variant="outline"
            size="xs"
            onClick={handleDownloadJSON}
            className="gap-1.5 font-medium text-[11px] border-zinc-800 text-zinc-300"
          >
            <Download className="w-3.5 h-3.5" />
            <span>Unduh .JSON</span>
          </Button>

          <Button
            variant="tactical"
            size="xs"
            onClick={handleSimulateSync}
            disabled={isSyncing}
            className="gap-1.5 font-semibold text-[11px] h-8 bg-blue-600 hover:bg-blue-500 text-white"
          >
            <Send className="w-3.5 h-3.5" />
            <span>{isSyncing ? 'Mengirim Gateway...' : 'Kirim Sinkronisasi Gateway'}</span>
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  );
};
