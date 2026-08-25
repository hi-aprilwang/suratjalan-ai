'use client';

import React from 'react';
import { AuditReport } from '../types/audit';
import {
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Building2,
  Stamp,
  FileCheck2,
  Clock,
  Sparkles,
  TrendingDown
} from 'lucide-react';
import { Card } from './ui/card';
import { Badge } from './ui/badge';

interface AuditSummaryProps {
  report: AuditReport;
}

export const AuditSummary: React.FC<AuditSummaryProps> = ({ report }) => {
  const formatIDR = (val: number) => {
    return new Intl.NumberFormat('id-ID', {
      style: 'currency',
      currency: 'IDR',
      maximumFractionDigits: 0
    }).format(val);
  };

  const getVerdictDetails = () => {
    switch (report.overall_status) {
      case 'APPROVED_FOR_INVOICING':
        return {
          title: 'CLEARANCE GRANTED // READY FOR INVOICE POSTING',
          subtitle: '100% PO Quantity Match • Rubber Stamp & Checker Signatures Validated',
          badge: <Badge variant="success">APPROVED (100% MATCH)</Badge>,
          border: 'border-emerald-800/80 bg-emerald-950/20',
          icon: <CheckCircle2 className="w-5 h-5 text-emerald-400 shrink-0" />
        };
      case 'DISCREPANCY_FLAGGED':
        return {
          title: 'DISCREPANCY DETECTED // AUTO DEBIT CLAIM GENERATED',
          subtitle: `Fisik Retur / Kerusakan Teridentifikasi • Potongan Klaim ${formatIDR(report.total_claim_amount_idr)}`,
          badge: <Badge variant="warning">FLAGGED (DEBIT CLAIM)</Badge>,
          border: 'border-amber-800/80 bg-amber-950/20',
          icon: <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0" />
        };
      case 'CRITICAL_REJECTED':
      default:
        return {
          title: 'CRITICAL AUDIT EXCEPTION // INVOICE BLOCKED',
          subtitle: 'Stempel Toko Hilang atau Selisih Batch/Kerusakan Total Ditemukan',
          badge: <Badge variant="destructive">BLOCKED (REJECTED)</Badge>,
          border: 'border-rose-800/80 bg-rose-950/20',
          icon: <XCircle className="w-5 h-5 text-rose-400 shrink-0" />
        };
    }
  };

  const verdict = getVerdictDetails();

  return (
    <div className="space-y-3">
      {/* Executive Decision Banner */}
      <div className={`rounded-xl border p-4 backdrop-blur-sm transition-all ${verdict.border}`}>
        <div className="flex items-start justify-between gap-3">
          <div className="flex items-start gap-3">
            {verdict.icon}
            <div>
              <div className="flex flex-wrap items-center gap-2">
                <h3 className="text-xs font-bold text-zinc-100 uppercase tracking-tight">
                  {verdict.title}
                </h3>
              </div>
              <p className="text-xs text-zinc-300 font-medium mt-0.5">
                {verdict.subtitle}
              </p>
            </div>
          </div>
          <div className="shrink-0 flex items-center gap-2">
            <span className="text-[10px] text-zinc-500 hidden sm:inline font-semibold">
              ID: {report.audit_id}
            </span>
            {verdict.badge}
          </div>
        </div>
      </div>

      {/* KPI Metrics Ticker Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
        {/* Confidence */}
        <Card className="p-3 bg-zinc-950 border-zinc-800/80">
          <div className="flex items-center justify-between text-zinc-400 text-[10px] uppercase font-semibold">
            <span>VLM Confidence</span>
            <Sparkles className="w-3 h-3 text-emerald-400" />
          </div>
          <div className="mt-1 flex items-baseline gap-1.5">
            <span className="text-lg font-bold text-emerald-400">
              {(report.confidence_score * 100).toFixed(1)}%
            </span>
            <span className="text-[10px] text-zinc-500 font-semibold">Grounded</span>
          </div>
        </Card>

        {/* Physical Quantity vs PO */}
        <Card className="p-3 bg-zinc-950 border-zinc-800/80">
          <div className="flex items-center justify-between text-zinc-400 text-[10px] uppercase font-semibold">
            <span>Fisik / PO Target</span>
            <FileCheck2 className="w-3 h-3 text-blue-400" />
          </div>
          <div className="mt-1 flex items-baseline gap-1.5">
            <span className="text-lg font-bold text-zinc-100">
              {report.total_received_items}
            </span>
            <span className="text-[10px] text-zinc-500 font-medium">
              / {report.total_ordered_items} Unit
            </span>
          </div>
        </Card>

        {/* Claim Deduction */}
        <Card className="p-3 bg-zinc-950 border-zinc-800/80">
          <div className="flex items-center justify-between text-zinc-400 text-[10px] uppercase font-semibold">
            <span>Klaim Pemotongan</span>
            <TrendingDown
              className={`w-3 h-3 ${report.total_claim_amount_idr > 0 ? 'text-rose-400' : 'text-emerald-400'}`}
            />
          </div>
          <div className="mt-1">
            <span
              className={`text-xs sm:text-sm font-bold truncate block ${
                report.total_claim_amount_idr > 0 ? 'text-rose-400' : 'text-emerald-400'
              }`}
            >
              {report.total_claim_amount_idr > 0
                ? `-${formatIDR(report.total_claim_amount_idr)}`
                : 'Rp 0 (Clear)'}
            </span>
          </div>
        </Card>

        {/* Latency Speed */}
        <Card className="p-3 bg-zinc-950 border-zinc-800/80">
          <div className="flex items-center justify-between text-zinc-400 text-[10px] uppercase font-semibold">
            <span>Inference Time</span>
            <Clock className="w-3 h-3 text-amber-400" />
          </div>
          <div className="mt-1 flex items-baseline gap-1.5">
            <span className="text-lg font-bold text-zinc-100">
              {report.execution_time_ms}
            </span>
            <span className="text-[10px] text-zinc-500 font-medium">ms</span>
          </div>
        </Card>
      </div>

      {/* Metadata & Forensics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-2.5">
        {/* Document Header Metadata */}
        <Card className="p-3.5 bg-zinc-950 border-zinc-800/80 space-y-2.5">
          <div className="flex items-center gap-2 pb-2 border-b border-zinc-800/80">
            <Building2 className="w-3.5 h-3.5 text-zinc-400" />
            <span className="text-xs font-semibold uppercase tracking-wider text-zinc-200">
              Metadata Dokumen & Logistik
            </span>
          </div>

          <div className="grid grid-cols-2 gap-2 text-xs">
            <div>
              <span className="text-[10px] text-zinc-500 block font-medium">No. Surat Jalan:</span>
              <span className="font-bold text-zinc-200">{report.metadata.document_number}</span>
            </div>
            <div>
              <span className="text-[10px] text-zinc-500 block font-medium">No. PO Pemesan:</span>
              <span className="font-bold text-zinc-200">{report.metadata.po_number || '-'}</span>
            </div>
            <div>
              <span className="text-[10px] text-zinc-500 block font-medium">Pengirim / Vendor:</span>
              <span className="font-medium text-zinc-300 truncate block">{report.metadata.sender_company}</span>
            </div>
            <div>
              <span className="text-[10px] text-zinc-500 block font-medium">Penerima / DC:</span>
              <span className="font-medium text-zinc-300 truncate block">{report.metadata.receiver_company}</span>
            </div>
            <div>
              <span className="text-[10px] text-zinc-500 block font-medium">Nopol Armada:</span>
              <span className="font-semibold text-zinc-200">{report.metadata.truck_plate || '-'}</span>
            </div>
            <div>
              <span className="text-[10px] text-zinc-500 block font-medium">Nama Sopir:</span>
              <span className="font-medium text-zinc-300 truncate block">{report.metadata.driver_name || '-'}</span>
            </div>
          </div>
        </Card>

        {/* Legal & Stamping Verification */}
        <Card className="p-3.5 bg-zinc-950 border-zinc-800/80 space-y-2.5">
          <div className="flex items-center gap-2 pb-2 border-b border-zinc-800/80">
            <Stamp className="w-3.5 h-3.5 text-zinc-400" />
            <span className="text-xs font-semibold uppercase tracking-wider text-zinc-200">
              Verifikasi Stempel & Tanda Tangan
            </span>
          </div>

          <div className="space-y-1.5 text-xs">
            <div className="flex items-center justify-between p-1.5 rounded-md bg-zinc-900/60 border border-zinc-800/60">
              <span className="text-zinc-300 font-medium">Stempel Resmi Gudang/Toko:</span>
              {report.verification.stamp_valid ? (
                <span className="text-emerald-400 font-semibold flex items-center gap-1">
                  <CheckCircle2 className="w-3 h-3" /> TERVALIDASI
                </span>
              ) : (
                <span className="text-rose-400 font-semibold flex items-center gap-1">
                  <XCircle className="w-3 h-3" /> MISSING / DITOLAK
                </span>
              )}
            </div>

            <div className="flex items-center justify-between p-1.5 rounded-md bg-zinc-900/60 border border-zinc-800/60">
              <span className="text-zinc-300 font-medium">Tanda Tangan Checker:</span>
              {report.verification.receiver_signature_detected ? (
                <span className="text-emerald-400 font-semibold flex items-center gap-1">
                  <CheckCircle2 className="w-3 h-3" /> TERDETEKSI
                </span>
              ) : (
                <span className="text-rose-400 font-semibold flex items-center gap-1">
                  <XCircle className="w-3 h-3" /> TIDAK ADA
                </span>
              )}
            </div>

            <div className="flex items-center justify-between p-1.5 rounded-md bg-zinc-900/60 border border-zinc-800/60">
              <span className="text-zinc-300 font-medium">Tanda Tangan Sopir:</span>
              {report.verification.driver_signature_detected ? (
                <span className="text-emerald-400 font-semibold flex items-center gap-1">
                  <CheckCircle2 className="w-3 h-3" /> TERDETEKSI
                </span>
              ) : (
                <span className="text-rose-400 font-semibold flex items-center gap-1">
                  <XCircle className="w-3 h-3" /> TIDAK ADA
                </span>
              )}
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
};
