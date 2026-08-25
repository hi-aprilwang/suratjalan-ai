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
          title: 'CLEARANCE GRANTED // FAKTUR SIAP DITERBITKAN',
          subtitle: '100% Kuantitas PO Sesuai • Stempel Toko & Tanda Tangan Tervalidasi',
          badge: <Badge variant="success">APPROVED (100% MATCH)</Badge>,
          border: 'border-emerald-500/30 dark:border-emerald-800/80 bg-emerald-50/60 dark:bg-emerald-950/20 text-emerald-950 dark:text-emerald-100',
          icon: <CheckCircle2 className="w-6 h-6 text-emerald-600 dark:text-emerald-400 shrink-0 mt-0.5" />
        };
      case 'DISCREPANCY_FLAGGED':
        return {
          title: 'DISCREPANCY DETECTED // AUTO DEBIT CLAIM GENERATED',
          subtitle: `Fisik Retur / Kerusakan Teridentifikasi • Potongan Klaim ${formatIDR(report.total_claim_amount_idr)}`,
          badge: <Badge variant="warning">FLAGGED (DEBIT CLAIM)</Badge>,
          border: 'border-amber-500/30 dark:border-amber-800/80 bg-amber-50/60 dark:bg-amber-950/20 text-amber-950 dark:text-amber-100',
          icon: <AlertTriangle className="w-6 h-6 text-amber-600 dark:text-amber-400 shrink-0 mt-0.5" />
        };
      case 'CRITICAL_REJECTED':
      default:
        return {
          title: 'CRITICAL AUDIT EXCEPTION // INVOICE BLOCKED',
          subtitle: 'Stempel Toko Hilang atau Selisih Batch/Kerusakan Total Ditemukan',
          badge: <Badge variant="destructive">BLOCKED (REJECTED)</Badge>,
          border: 'border-rose-500/30 dark:border-rose-800/80 bg-rose-50/60 dark:bg-rose-950/20 text-rose-950 dark:text-rose-100',
          icon: <XCircle className="w-6 h-6 text-rose-600 dark:text-rose-400 shrink-0 mt-0.5" />
        };
    }
  };

  const verdict = getVerdictDetails();

  return (
    <div className="space-y-5">
      {/* Executive Decision Banner */}
      <div className={`rounded-2xl border p-5 sm:p-6 backdrop-blur-sm transition-all shadow-xs ${verdict.border}`}>
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-start gap-4">
            {verdict.icon}
            <div>
              <h3 className="text-base font-bold uppercase tracking-tight">
                {verdict.title}
              </h3>
              <p className="text-sm opacity-80 font-medium mt-1">
                {verdict.subtitle}
              </p>
            </div>
          </div>
          <div className="shrink-0 flex items-center gap-3">
            <span className="text-sm opacity-60 hidden sm:inline font-semibold">
              ID: {report.audit_id}
            </span>
            {verdict.badge}
          </div>
        </div>
      </div>

      {/* KPI Metrics Ticker Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        {/* Confidence */}
        <Card className="p-4 sm:p-5 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800/80 rounded-xl shadow-xs">
          <div className="flex items-center justify-between text-zinc-500 dark:text-zinc-400 text-sm uppercase font-semibold">
            <span>VLM Confidence</span>
            <Sparkles className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
          </div>
          <div className="mt-2 flex items-baseline gap-1.5">
            <span className="text-2xl font-bold text-emerald-600 dark:text-emerald-400">
              {(report.confidence_score * 100).toFixed(1)}%
            </span>
            <span className="text-sm text-zinc-400 font-medium">Grounded</span>
          </div>
        </Card>

        {/* Physical Quantity vs PO */}
        <Card className="p-4 sm:p-5 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800/80 rounded-xl shadow-xs">
          <div className="flex items-center justify-between text-zinc-500 dark:text-zinc-400 text-sm uppercase font-semibold">
            <span>Fisik / Target PO</span>
            <FileCheck2 className="w-4 h-4 text-blue-600 dark:text-blue-400" />
          </div>
          <div className="mt-2 flex items-baseline gap-1.5">
            <span className="text-2xl font-bold text-zinc-900 dark:text-zinc-100">
              {report.total_received_items}
            </span>
            <span className="text-sm text-zinc-400 font-medium">
              / {report.total_ordered_items} Unit
            </span>
          </div>
        </Card>

        {/* Claim Deduction */}
        <Card className="p-4 sm:p-5 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800/80 rounded-xl shadow-xs">
          <div className="flex items-center justify-between text-zinc-500 dark:text-zinc-400 text-sm uppercase font-semibold">
            <span>Klaim Potongan</span>
            <TrendingDown
              className={`w-4 h-4 ${report.total_claim_amount_idr > 0 ? 'text-rose-600 dark:text-rose-400' : 'text-emerald-600 dark:text-emerald-400'}`}
            />
          </div>
          <div className="mt-2">
            <span
              className={`text-base sm:text-lg font-bold truncate block ${
                report.total_claim_amount_idr > 0 ? 'text-rose-600 dark:text-rose-400' : 'text-emerald-600 dark:text-emerald-400'
              }`}
            >
              {report.total_claim_amount_idr > 0
                ? `-${formatIDR(report.total_claim_amount_idr)}`
                : 'Rp 0 (Clear)'}
            </span>
          </div>
        </Card>

        {/* Latency Speed */}
        <Card className="p-4 sm:p-5 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800/80 rounded-xl shadow-xs">
          <div className="flex items-center justify-between text-zinc-500 dark:text-zinc-400 text-sm uppercase font-semibold">
            <span>Kecepatan Audit</span>
            <Clock className="w-4 h-4 text-amber-600 dark:text-amber-400" />
          </div>
          <div className="mt-2 flex items-baseline gap-1.5">
            <span className="text-2xl font-bold text-zinc-900 dark:text-zinc-100">
              {report.execution_time_ms}
            </span>
            <span className="text-sm text-zinc-400 font-medium">ms</span>
          </div>
        </Card>
      </div>

      {/* Metadata & Forensics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Document Header Metadata */}
        <Card className="p-5 sm:p-6 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800/80 rounded-xl space-y-4 shadow-xs">
          <div className="flex items-center gap-2.5 pb-3 border-b border-zinc-100 dark:border-zinc-800/80">
            <Building2 className="w-4 h-4 text-zinc-400" />
            <span className="text-sm font-bold uppercase tracking-wider text-zinc-800 dark:text-zinc-200">
              Metadata Dokumen & Logistik
            </span>
          </div>

          <div className="grid grid-cols-2 gap-4 text-sm">
            <div>
              <span className="text-sm text-zinc-400 block font-medium">No. Surat Jalan:</span>
              <span className="font-bold text-zinc-900 dark:text-zinc-100">{report.metadata.document_number}</span>
            </div>
            <div>
              <span className="text-sm text-zinc-400 block font-medium">No. PO Pemesan:</span>
              <span className="font-bold text-zinc-900 dark:text-zinc-100">{report.metadata.po_number || '-'}</span>
            </div>
            <div>
              <span className="text-sm text-zinc-400 block font-medium">Pengirim / Vendor:</span>
              <span className="font-medium text-zinc-700 dark:text-zinc-300 truncate block">{report.metadata.sender_company}</span>
            </div>
            <div>
              <span className="text-sm text-zinc-400 block font-medium">Penerima / DC:</span>
              <span className="font-medium text-zinc-700 dark:text-zinc-300 truncate block">{report.metadata.receiver_company}</span>
            </div>
            <div>
              <span className="text-sm text-zinc-400 block font-medium">Nopol Armada:</span>
              <span className="font-semibold text-zinc-800 dark:text-zinc-200">{report.metadata.truck_plate || '-'}</span>
            </div>
            <div>
              <span className="text-sm text-zinc-400 block font-medium">Nama Sopir:</span>
              <span className="font-medium text-zinc-700 dark:text-zinc-300 truncate block">{report.metadata.driver_name || '-'}</span>
            </div>
          </div>
        </Card>

        {/* Legal & Stamping Verification */}
        <Card className="p-5 sm:p-6 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800/80 rounded-xl space-y-4 shadow-xs">
          <div className="flex items-center gap-2.5 pb-3 border-b border-zinc-100 dark:border-zinc-800/80">
            <Stamp className="w-4 h-4 text-zinc-400" />
            <span className="text-sm font-bold uppercase tracking-wider text-zinc-800 dark:text-zinc-200">
              Verifikasi Stempel & Tanda Tangan
            </span>
          </div>

          <div className="space-y-2.5 text-sm">
            <div className="flex items-center justify-between p-3 rounded-lg bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200/80 dark:border-zinc-800/60">
              <span className="text-zinc-700 dark:text-zinc-300 font-medium">Stempel Resmi Gudang/Toko:</span>
              {report.verification.stamp_valid ? (
                <span className="text-emerald-600 dark:text-emerald-400 font-semibold flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4" /> Tervalidasi
                </span>
              ) : (
                <span className="text-rose-600 dark:text-rose-400 font-semibold flex items-center gap-1.5">
                  <XCircle className="w-4 h-4" /> Missing / Ditolak
                </span>
              )}
            </div>

            <div className="flex items-center justify-between p-3 rounded-lg bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200/80 dark:border-zinc-800/60">
              <span className="text-zinc-700 dark:text-zinc-300 font-medium">Tanda Tangan Checker:</span>
              {report.verification.receiver_signature_detected ? (
                <span className="text-emerald-600 dark:text-emerald-400 font-semibold flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4" /> Terdeteksi
                </span>
              ) : (
                <span className="text-rose-600 dark:text-rose-400 font-semibold flex items-center gap-1.5">
                  <XCircle className="w-4 h-4" /> Tidak Ada
                </span>
              )}
            </div>

            <div className="flex items-center justify-between p-3 rounded-lg bg-zinc-50 dark:bg-zinc-900/60 border border-zinc-200/80 dark:border-zinc-800/60">
              <span className="text-zinc-700 dark:text-zinc-300 font-medium">Tanda Tangan Sopir:</span>
              {report.verification.driver_signature_detected ? (
                <span className="text-emerald-600 dark:text-emerald-400 font-semibold flex items-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4" /> Terdeteksi
                </span>
              ) : (
                <span className="text-rose-600 dark:text-rose-400 font-semibold flex items-center gap-1.5">
                  <XCircle className="w-4 h-4" /> Tidak Ada
                </span>
              )}
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
};
