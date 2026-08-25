'use client';

import React, { useState, useEffect } from 'react';
import { AuditReport } from '../types/audit';
import { X, Check, Copy, Download, Send, CheckCircle2, Server, ArrowRight, ShieldCheck } from 'lucide-react';

interface ExportModalProps {
  isOpen: boolean;
  onClose: () => void;
  report: AuditReport;
}

export const ExportModal: React.FC<ExportModalProps> = ({ isOpen, onClose, report }) => {
  const [selectedTarget, setSelectedTarget] = useState<'SAP_S4HANA' | 'ODOO_ERP' | 'JURNAL_ID'>('SAP_S4HANA');
  const [isSyncing, setIsSyncing] = useState(false);
  const [syncedResult, setSyncedResult] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    if (isOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const getPayload = () => {
    return {
      metadata: {
        integration_gateway: selectedTarget,
        audit_id: report.audit_id,
        sync_timestamp: new Date().toISOString(),
        document_number: report.metadata.document_number,
        po_number: report.metadata.po_number,
        sender_vendor: report.metadata.sender_company,
        receiver_plant_dc: report.metadata.receiver_company
      },
      audit_verdict: {
        approval_status: report.overall_status,
        payment_clearance: report.overall_status === 'APPROVED_FOR_INVOICING' ? 'READY_TO_PAY' : 'DISPUTE_HOLD',
        total_deduction_claim_idr: report.total_claim_amount_idr,
        ai_confidence_score: report.confidence_score,
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
      setSyncedResult(data.message || `Sinkronisasi berhasil dikirim ke gateway ${selectedTarget}!`);
    } catch {
      setSyncedResult(`Simulasi sinkronisasi ${selectedTarget} berhasil (HTTP 200 OK - BAPI Posted).`);
    } finally {
      setIsSyncing(false);
    }
  };

  return (
    <div
      onClick={onClose}
      className="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-md flex items-center justify-center p-4 sm:p-6 animate-fadeIn"
    >
      <div
        onClick={(e) => e.stopPropagation()}
        className="bg-slate-900/95 border border-white/[0.12] rounded-3xl w-full max-w-2xl overflow-hidden shadow-[0_20px_60px_rgba(0,0,0,0.8)] flex flex-col max-h-[90vh]"
      >
        {/* Header */}
        <div className="px-6 py-4 border-b border-white/[0.08] flex items-center justify-between bg-slate-950/80">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-xl bg-blue-500/20 border border-blue-400/30 flex items-center justify-center text-blue-400">
              <Server className="w-4 h-4" />
            </div>
            <div>
              <h3 className="font-extrabold text-slate-100 text-sm">
                ERP Integration & Invoice Clearance Gateway
              </h3>
              <p className="text-[11px] text-slate-400">
                Ekspor hasil rekonsiliasi ke format ERP standar industri
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 hover:bg-white/10 rounded-xl text-slate-400 hover:text-white transition-colors"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-5 overflow-y-auto">
          {/* Target System Picker */}
          <div>
            <label className="text-xs font-bold text-slate-300 block mb-2.5 uppercase tracking-wider">
              Pilih Target Sistem ERP:
            </label>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
              {[
                { id: 'SAP_S4HANA', name: 'SAP S/4HANA', desc: 'BAPI Goods Receipt & Invoice Clearing' },
                { id: 'ODOO_ERP', name: 'Odoo Enterprise', desc: 'Stock Picking & Vendor Bill' },
                { id: 'JURNAL_ID', name: 'Jurnal.id / Mekari', desc: 'Auto Debit Memo & Jurnal Pembelian' }
              ].map((sys) => (
                <button
                  key={sys.id}
                  onClick={() => setSelectedTarget(sys.id as any)}
                  className={`p-3.5 rounded-2xl border text-left transition-all duration-200 ${
                    selectedTarget === sys.id
                      ? 'bg-gradient-to-b from-blue-950/60 to-slate-900 border-blue-500 shadow-[0_0_20px_rgba(59,130,246,0.3)] ring-1 ring-blue-400/30'
                      : 'bg-slate-950/40 border-white/[0.06] text-slate-400 hover:border-white/20'
                  }`}
                >
                  <span className="font-extrabold text-xs block text-slate-100">{sys.name}</span>
                  <span className="text-[10px] text-slate-400 mt-1 block leading-tight">{sys.desc}</span>
                </button>
              ))}
            </div>
          </div>

          {/* Sync Status Banner */}
          {syncedResult && (
            <div className="bg-emerald-950/80 border border-emerald-500/40 rounded-2xl p-3.5 flex items-center gap-3 text-emerald-300 text-xs font-bold shadow-[0_0_20px_rgba(16,185,129,0.2)]">
              <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
              <span>{syncedResult}</span>
            </div>
          )}

          {/* JSON Payload Preview */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">
                JSON Payload ({selectedTarget}):
              </span>
              <button
                onClick={handleCopy}
                className="flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-white/[0.05] hover:bg-white/10 text-xs font-bold text-blue-400 hover:text-blue-300 transition-colors"
              >
                {copied ? <Check className="w-3.5 h-3.5 text-emerald-400" /> : <Copy className="w-3.5 h-3.5" />}
                <span>{copied ? 'Tersalin!' : 'Salin JSON'}</span>
              </button>
            </div>
            <div className="relative rounded-2xl overflow-hidden border border-white/[0.08] bg-slate-950">
              <pre className="p-4 text-[11px] font-mono text-slate-300 max-h-56 overflow-y-auto leading-relaxed">
                {payloadString}
              </pre>
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-4 border-t border-white/[0.08] bg-slate-950/90 flex items-center justify-between gap-3">
          <button
            onClick={handleDownloadJSON}
            className="flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition-all border border-white/10 hover:border-white/20"
          >
            <Download className="w-4 h-4" />
            <span>Unduh File .JSON</span>
          </button>

          <button
            onClick={handleSimulateSync}
            disabled={isSyncing}
            className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs font-extrabold bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white transition-all shadow-[0_0_20px_rgba(59,130,246,0.4)] disabled:opacity-50 active:scale-95"
          >
            <Send className="w-4 h-4" />
            <span>{isSyncing ? 'Mengirim ke Gateway...' : 'Kirim Sinkronisasi Gateway'}</span>
          </button>
        </div>
      </div>
    </div>
  );
};
