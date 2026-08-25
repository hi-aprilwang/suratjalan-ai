'use client';

import React from 'react';
import { AuditReport } from '../types/audit';
import {
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Building2,
  Calendar,
  Truck,
  User,
  Stamp,
  FileCheck2,
  DollarSign,
  Clock,
  Sparkles,
  ArrowRight,
  TrendingDown
} from 'lucide-react';

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
          title: 'FAKTUR SIAP DITERBITKAN (APPROVED)',
          subtitle: '100% Sesuai Purchase Order • Stempel & Tanda Tangan Valid',
          desc: 'Seluruh barang fisik telah diterima lengkap tanpa selisih. Rekonsiliasi akuntansi otomatis disetujui untuk pembayaran.',
          bg: 'bg-gradient-to-r from-emerald-950/80 via-emerald-900/40 to-slate-900/80 border-emerald-500/50 shadow-[0_0_30px_rgba(16,185,129,0.2)]',
          badgeBg: 'bg-emerald-500 text-slate-950 font-black',
          icon: <CheckCircle2 className="w-7 h-7 text-emerald-400 shrink-0" />
        };
      case 'DISCREPANCY_FLAGGED':
        return {
          title: 'SELISIH / RETUR FISIK TERDETEKSI (FLAGGED)',
          subtitle: 'Terdapat 8 Dus Retur Beng Beng • Debit Memo Otomatis',
          desc: 'Tercatat coretan tangan retur fisik pada surat jalan. Sistem telah menghitung pemotongan faktur sebesar IDR 1.440.000.',
          bg: 'bg-gradient-to-r from-amber-950/80 via-amber-900/40 to-slate-900/80 border-amber-500/50 shadow-[0_0_30px_rgba(245,158,11,0.2)]',
          badgeBg: 'bg-amber-500 text-slate-950 font-black',
          icon: <AlertTriangle className="w-7 h-7 text-amber-400 shrink-0" />
        };
      case 'CRITICAL_REJECTED':
      default:
        return {
          title: 'PENGAJUAN FAKTUR DITOLAK (REJECTED)',
          subtitle: 'Stempel Toko Hilang & Kerusakan Parah Melebihi Toleransi',
          desc: 'Stempel resmi toko tidak terdeteksi dan terdapat 16 dus barang pecah/penyok. Tagihan dibekukan hingga ada Berita Acara resmi.',
          bg: 'bg-gradient-to-r from-rose-950/80 via-rose-900/40 to-slate-900/80 border-rose-500/50 shadow-[0_0_30px_rgba(244,63,94,0.2)]',
          badgeBg: 'bg-rose-500 text-white font-black',
          icon: <XCircle className="w-7 h-7 text-rose-400 shrink-0" />
        };
    }
  };

  const verdict = getVerdictDetails();

  return (
    <div className="space-y-4">
      {/* Hero Verdict Banner */}
      <div className={`rounded-2xl border p-5 backdrop-blur-xl transition-all duration-300 ${verdict.bg}`}>
        <div className="flex items-start gap-4">
          <div className="p-2.5 rounded-2xl bg-white/[0.06] border border-white/10 shadow-inner">
            {verdict.icon}
          </div>
          <div className="flex-1 min-w-0">
            <div className="flex flex-wrap items-center justify-between gap-2 mb-1">
              <h3 className="text-base font-black tracking-tight text-white uppercase">
                {verdict.title}
              </h3>
              <span className="text-[11px] font-mono font-bold px-2.5 py-0.5 rounded-full bg-slate-950/80 border border-white/10 text-slate-300">
                AUDIT ID: {report.audit_id}
              </span>
            </div>
            <p className="text-xs font-bold text-slate-200">
              {verdict.subtitle}
            </p>
            <p className="text-xs mt-1.5 text-slate-300 font-normal leading-relaxed">
              {verdict.desc}
            </p>
          </div>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        {/* Confidence Card */}
        <div className="bg-slate-900/60 backdrop-blur-xl border border-white/[0.08] rounded-2xl p-4 shadow-md hover:border-white/20 transition-all">
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-slate-400 uppercase font-bold tracking-wider">
              AI Confidence
            </span>
            <Sparkles className="w-3.5 h-3.5 text-emerald-400" />
          </div>
          <div className="mt-1 flex items-baseline gap-1.5">
            <span className="text-xl font-black text-emerald-400">
              {(report.confidence_score * 100).toFixed(1)}%
            </span>
            <span className="text-[10px] text-emerald-400 font-bold">VLM Grounded</span>
          </div>
        </div>

        {/* Quantity Match Card */}
        <div className="bg-slate-900/60 backdrop-blur-xl border border-white/[0.08] rounded-2xl p-4 shadow-md hover:border-white/20 transition-all">
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-slate-400 uppercase font-bold tracking-wider">
              Fisik vs PO
            </span>
            <FileCheck2 className="w-3.5 h-3.5 text-blue-400" />
          </div>
          <div className="mt-1 flex items-baseline gap-1.5">
            <span className="text-xl font-black text-white">
              {report.total_received_items}
            </span>
            <span className="text-xs text-slate-400">/ {report.total_ordered_items} Dus</span>
          </div>
        </div>

        {/* Claim Deduction Card */}
        <div className="bg-slate-900/60 backdrop-blur-xl border border-white/[0.08] rounded-2xl p-4 shadow-md hover:border-white/20 transition-all">
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-slate-400 uppercase font-bold tracking-wider">
              Potongan Klaim
            </span>
            <TrendingDown className={`w-3.5 h-3.5 ${report.total_claim_amount_idr > 0 ? 'text-rose-400' : 'text-emerald-400'}`} />
          </div>
          <div className="mt-1">
            <span
              className={`text-sm sm:text-base font-black line-clamp-1 ${
                report.total_claim_amount_idr > 0 ? 'text-rose-400' : 'text-emerald-400'
              }`}
            >
              {report.total_claim_amount_idr > 0 ? `-${formatIDR(report.total_claim_amount_idr)}` : 'Rp 0 (Lengkap)'}
            </span>
          </div>
        </div>

        {/* Inference Latency Card */}
        <div className="bg-slate-900/60 backdrop-blur-xl border border-white/[0.08] rounded-2xl p-4 shadow-md hover:border-white/20 transition-all">
          <div className="flex items-center justify-between">
            <span className="text-[10px] text-slate-400 uppercase font-bold tracking-wider">
              Latency Speed
            </span>
            <Clock className="w-3.5 h-3.5 text-amber-400" />
          </div>
          <div className="mt-1 flex items-baseline gap-1.5">
            <span className="text-xl font-black text-blue-400 font-mono">
              {report.execution_time_ms}
            </span>
            <span className="text-xs text-slate-400 font-mono">ms</span>
          </div>
        </div>
      </div>

      {/* Metadata & Legal Verification Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
        {/* Document Header Metadata */}
        <div className="bg-slate-900/60 backdrop-blur-xl border border-white/[0.08] rounded-2xl p-4 space-y-3">
          <div className="flex items-center gap-2 pb-2 border-b border-white/[0.06]">
            <Building2 className="w-4 h-4 text-blue-400" />
            <h4 className="font-extrabold text-slate-200 uppercase tracking-wider text-xs">
              Informasi Dokumen & Pengiriman
            </h4>
          </div>

          <div className="grid grid-cols-2 gap-3 text-xs">
            <div>
              <span className="text-[10px] text-slate-500 font-medium block">Nomor Surat Jalan:</span>
              <span className="font-bold text-slate-200 font-mono">{report.metadata.document_number}</span>
            </div>
            <div>
              <span className="text-[10px] text-slate-500 font-medium block">Nomor Purchase Order:</span>
              <span className="font-bold text-slate-200 font-mono">{report.metadata.po_number || '-'}</span>
            </div>
            <div>
              <span className="text-[10px] text-slate-500 font-medium block">Vendor / Pengirim:</span>
              <span className="font-semibold text-slate-300 line-clamp-1">{report.metadata.sender_company}</span>
            </div>
            <div>
              <span className="text-[10px] text-slate-500 font-medium block">Customer / DC Tujuan:</span>
              <span className="font-semibold text-slate-300 line-clamp-1">{report.metadata.receiver_company}</span>
            </div>
            <div>
              <span className="text-[10px] text-slate-500 font-medium block">Nomor Polisi Armada:</span>
              <span className="font-bold text-amber-300 font-mono">{report.metadata.truck_plate || '-'}</span>
            </div>
            <div>
              <span className="text-[10px] text-slate-500 font-medium block">Nama Driver / Ekspedisi:</span>
              <span className="font-semibold text-slate-300">{report.metadata.driver_name || '-'}</span>
            </div>
          </div>
        </div>

        {/* Legal & Stamping Verification */}
        <div className="bg-slate-900/60 backdrop-blur-xl border border-white/[0.08] rounded-2xl p-4 space-y-3">
          <div className="flex items-center gap-2 pb-2 border-b border-white/[0.06]">
            <Stamp className="w-4 h-4 text-indigo-400" />
            <h4 className="font-extrabold text-slate-200 uppercase tracking-wider text-xs">
              Verifikasi Stempel & Tanda Tangan
            </h4>
          </div>

          <div className="space-y-2 text-xs">
            <div className="flex items-center justify-between p-2 rounded-xl bg-white/[0.02] border border-white/[0.04]">
              <span className="text-slate-300 font-medium">Stempel Resmi Toko/DC:</span>
              {report.verification.stamp_valid ? (
                <span className="text-emerald-400 font-bold flex items-center gap-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Terverifikasi & Valid
                </span>
              ) : (
                <span className="text-rose-400 font-bold flex items-center gap-1.5 animate-pulse">
                  <XCircle className="w-3.5 h-3.5" /> Stempel Tidak Ditemukan
                </span>
              )}
            </div>

            <div className="flex items-center justify-between p-2 rounded-xl bg-white/[0.02] border border-white/[0.04]">
              <span className="text-slate-300 font-medium">TTD Penerima (Checker):</span>
              {report.verification.receiver_signature_detected ? (
                <span className="text-emerald-400 font-bold flex items-center gap-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Terverifikasi
                </span>
              ) : (
                <span className="text-rose-400 font-bold flex items-center gap-1.5">
                  <XCircle className="w-3.5 h-3.5" /> Belum Ditandatangani
                </span>
              )}
            </div>

            <div className="flex items-center justify-between p-2 rounded-xl bg-white/[0.02] border border-white/[0.04]">
              <span className="text-slate-300 font-medium">TTD Sopir Pengemudi:</span>
              {report.verification.driver_signature_detected ? (
                <span className="text-emerald-400 font-bold flex items-center gap-1.5">
                  <CheckCircle2 className="w-3.5 h-3.5" /> Terverifikasi
                </span>
              ) : (
                <span className="text-rose-400 font-bold flex items-center gap-1.5">
                  <XCircle className="w-3.5 h-3.5" /> Belum Ditandatangani
                </span>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
