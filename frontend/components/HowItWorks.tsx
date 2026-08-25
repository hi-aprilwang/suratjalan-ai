'use client';

import React from 'react';
import {
  Truck,
  FileCheck2,
  BrainCircuit,
  TrendingUp,
  ShieldCheck,
  Zap,
  Database,
  Check,
  Building,
  UserCheck,
  Coins,
  Receipt
} from 'lucide-react';
import { Card } from './ui/card';
import { Badge } from './ui/badge';

export const HowItWorks: React.FC = () => {
  return (
    <div className="space-y-8">
      {/* Header Banner */}
      <div className="rounded-xl border border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 p-6 sm:p-8 shadow-xs">
        <div className="max-w-3xl">
          <Badge variant="tactical" className="text-sm font-semibold mb-3">
            WORKFLOW & SYSTEM ARCHITECTURE
          </Badge>
          <h2 className="text-xl sm:text-2xl font-bold tracking-tight text-zinc-900 dark:text-zinc-100">
            Cara Kerja SuratJalan.AI // Rekonsiliasi Otomatis POD & Tagihan
          </h2>
          <p className="text-sm text-zinc-600 dark:text-zinc-400 mt-2 leading-relaxed">
            Menghubungkan dokumen fisik kertas Surat Jalan (Proof of Delivery) bertanda tangan & stempel basah 
            langsung ke sistem ERP enterprise dalam hitungan detik menggunakan Multimodal Gemini 2.0 Flash VLM.
          </p>
        </div>
      </div>

      {/* Target User Personas */}
      <div className="space-y-4">
        <div className="flex items-center gap-2">
          <UserCheck className="w-5 h-5 text-blue-600 dark:text-blue-400" />
          <h3 className="text-base font-bold text-zinc-900 dark:text-zinc-100 uppercase tracking-tight">
            Siapa Pengguna Sistem Ini? (Target Stakeholders)
          </h3>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Persona 1 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800">
            <div className="h-10 w-10 rounded-lg bg-blue-50 dark:bg-blue-950/60 border border-blue-200 dark:border-blue-800/60 flex items-center justify-center text-blue-600 dark:text-blue-400">
              <Truck className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
                Sopir Logistik & 3PL
              </h4>
              <p className="text-sm text-zinc-500 font-medium mt-0.5">
                Transporter / Ekspedisi
              </p>
            </div>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Mengunggah foto Surat Jalan bertanda tangan & stempel resmi langsung di dermaga bongkar (dock DC) saat serah terima barang selesai.
            </p>
          </Card>

          {/* Persona 2 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800">
            <div className="h-10 w-10 rounded-lg bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800/60 flex items-center justify-center text-emerald-600 dark:text-emerald-400">
              <Receipt className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
                Staf Finance & AR / AP
              </h4>
              <p className="text-sm text-zinc-500 font-medium mt-0.5">
                Principal & Distributor
              </p>
            </div>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Menerima hasil rekonsiliasi instan PO vs Fisik, otomatis menghitung potongan klaim retur/rusak, dan memposting faktur penagihan.
            </p>
          </Card>

          {/* Persona 3 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800">
            <div className="h-10 w-10 rounded-lg bg-amber-50 dark:bg-amber-950/60 border border-amber-200 dark:border-amber-800/60 flex items-center justify-center text-amber-600 dark:text-amber-400">
              <Building className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
                Warehouse DC Checker
              </h4>
              <p className="text-sm text-zinc-500 font-medium mt-0.5">
                Pusat Distribusi Retail
              </p>
            </div>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Memastikan catatan tangan barang retur/rusak terbaca akurat tanpa sengketa selisih stok saat proses Good Receipt (GR).
            </p>
          </Card>

          {/* Persona 4 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800">
            <div className="h-10 w-10 rounded-lg bg-purple-50 dark:bg-purple-950/60 border border-purple-200 dark:border-purple-800/60 flex items-center justify-center text-purple-600 dark:text-purple-400">
              <TrendingUp className="w-5 h-5" />
            </div>
            <div>
              <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
                CFO & Supply Chain Head
              </h4>
              <p className="text-sm text-zinc-500 font-medium mt-0.5">
                Direksi & Manajemen
              </p>
            </div>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Mempercepat perputaran piutang (DSO) dari 30 hari menjadi kliring hari yang sama (Same-Day Factoring), memperkuat arus kas.
            </p>
          </Card>
        </div>
      </div>

      {/* 4-Stage Workflow Pipeline */}
      <div className="space-y-4">
        <div className="flex items-center gap-2">
          <Zap className="w-5 h-5 text-emerald-600 dark:text-emerald-400" />
          <h3 className="text-base font-bold text-zinc-900 dark:text-zinc-100 uppercase tracking-tight">
            Alur Tahapan Eksekusi Sistem (4-Stage Pipeline)
          </h3>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Step 1 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800 relative">
            <div className="flex items-center justify-between">
              <span className="text-sm font-bold text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-950/60 border border-blue-200 dark:border-blue-800/60 px-2.5 py-0.5 rounded">
                TAHAP 01
              </span>
              <FileCheck2 className="w-4 h-4 text-zinc-400" />
            </div>
            <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
              Ingest Dokumen Fisik
            </h4>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Sopir atau staf admin memotret atau memindai Surat Jalan fisik asli yang telah dibubuhi stempel toko/DC dan tanda tangan penerima.
            </p>
            <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800 text-sm text-zinc-500 font-medium">
              Format: JPG, PNG, PDF Scan
            </div>
          </Card>

          {/* Step 2 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800 relative">
            <div className="flex items-center justify-between">
              <span className="text-sm font-bold text-emerald-600 dark:text-emerald-400 bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200 dark:border-emerald-800/60 px-2.5 py-0.5 rounded">
                TAHAP 02
              </span>
              <BrainCircuit className="w-4 h-4 text-zinc-400" />
            </div>
            <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
              Multimodal VLM Inference (&lt;1.5s)
            </h4>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Gemini 2.0 Flash mengekstrak metadata header, memverifikasi stempel/TTD, membaca coretan catatan tangan retur, dan mendeteksi koordinat piksel spasial.
            </p>
            <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800 text-sm text-emerald-600 dark:text-emerald-400 font-medium flex items-center gap-1">
              <Check className="w-3.5 h-3.5" /> Spatial Grounding Bounding Box
            </div>
          </Card>

          {/* Step 3 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800 relative">
            <div className="flex items-center justify-between">
              <span className="text-sm font-bold text-amber-600 dark:text-amber-400 bg-amber-50 dark:bg-amber-950/60 border border-amber-200 dark:border-amber-800/60 px-2.5 py-0.5 rounded">
                TAHAP 03
              </span>
              <ShieldCheck className="w-4 h-4 text-zinc-400" />
            </div>
            <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
              Rekonsiliasi & Klaim Finansial
            </h4>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Pydantic v2 mencocokkan target PO vs Qty Fisik, menghitung selisih matematis (delta variance), dan menerbitkan nominal klaim debit (IDR).
            </p>
            <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800 text-sm text-zinc-500 font-medium">
              Zero Hallucination Validation
            </div>
          </Card>

          {/* Step 4 */}
          <Card className="p-5 space-y-3 bg-white dark:bg-zinc-950 border-zinc-200 dark:border-zinc-800 relative">
            <div className="flex items-center justify-between">
              <span className="text-sm font-bold text-purple-600 dark:text-purple-400 bg-purple-50 dark:bg-purple-950/60 border border-purple-200 dark:border-purple-800/60 px-2.5 py-0.5 rounded">
                TAHAP 04
              </span>
              <Database className="w-4 h-4 text-zinc-400" />
            </div>
            <h4 className="font-bold text-sm text-zinc-900 dark:text-zinc-100">
              Ekspor & Integrasi ERP
            </h4>
            <p className="text-sm text-zinc-600 dark:text-zinc-400 leading-relaxed">
              Hasil kliring dikirim otomatis via API Gateway ke SAP S/4HANA (BAPI), Odoo 18, atau Jurnal.id untuk penagihan invoice instan.
            </p>
            <div className="pt-2 border-t border-zinc-100 dark:border-zinc-800 text-sm text-zinc-500 font-medium">
              SAP • Odoo • Mekari Jurnal
            </div>
          </Card>
        </div>
      </div>

      {/* Comparison: Traditional vs SuratJalan.AI */}
      <div className="space-y-4">
        <div className="flex items-center gap-2">
          <Coins className="w-5 h-5 text-blue-600 dark:text-blue-400" />
          <h3 className="text-base font-bold text-zinc-900 dark:text-zinc-100 uppercase tracking-tight">
            Perbandingan Efisiensi: Cara Manual vs SuratJalan.AI
          </h3>
        </div>

        <Card className="overflow-hidden border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm border-collapse">
              <thead>
                <tr className="border-b border-zinc-200 dark:border-zinc-800 bg-zinc-50 dark:bg-zinc-900/60 text-sm uppercase tracking-wider text-zinc-600 dark:text-zinc-400 font-semibold">
                  <th className="py-3.5 px-4">Parameter Operasional</th>
                  <th className="py-3.5 px-4 text-rose-600 dark:text-rose-400">Proses Manual Konvensional</th>
                  <th className="py-3.5 px-4 text-emerald-600 dark:text-emerald-400">Dengan SuratJalan.AI</th>
                  <th className="py-3.5 px-4 text-right">Dampak Efisiensi</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-zinc-200 dark:divide-zinc-800/60">
                <tr>
                  <td className="py-3 px-4 font-semibold text-zinc-900 dark:text-zinc-100">
                    Durasi Audit per Lembar
                  </td>
                  <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                    5 – 10 menit (ketik manual excel)
                  </td>
                  <td className="py-3 px-4 text-emerald-600 dark:text-emerald-400 font-bold">
                    &lt; 1.5 detik
                  </td>
                  <td className="py-3 px-4 text-right font-bold text-emerald-600 dark:text-emerald-400">
                    400x Lebih Cepat
                  </td>
                </tr>

                <tr>
                  <td className="py-3 px-4 font-semibold text-zinc-900 dark:text-zinc-100">
                    Biaya Pemrosesan per Dokumen
                  </td>
                  <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                    Rp 3.500 – Rp 5.000 (biaya gaji staff admin)
                  </td>
                  <td className="py-3 px-4 text-emerald-600 dark:text-emerald-400 font-bold">
                    Rp 2.4 (token Gemini Flash)
                  </td>
                  <td className="py-3 px-4 text-right font-bold text-emerald-600 dark:text-emerald-400">
                    &gt; 99.9% Hemat Biaya
                  </td>
                </tr>

                <tr>
                  <td className="py-3 px-4 font-semibold text-zinc-900 dark:text-zinc-100">
                    Resolusi Sengketa Selisih & Retur
                  </td>
                  <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                    14 – 30 hari (dokumen fisik tercecer/hilang)
                  </td>
                  <td className="py-3 px-4 text-emerald-600 dark:text-emerald-400 font-bold">
                    Instan (Bukti visual bounding box & klaim)
                  </td>
                  <td className="py-3 px-4 text-right font-bold text-emerald-600 dark:text-emerald-400">
                    Zero Dispute Delay
                  </td>
                </tr>

                <tr>
                  <td className="py-3 px-4 font-semibold text-zinc-900 dark:text-zinc-100">
                    Kecepatan Penagihan Faktur (DSO)
                  </td>
                  <td className="py-3 px-4 text-zinc-600 dark:text-zinc-400">
                    Tertahan 30 – 60 hari menunggu berkas fisik
                  </td>
                  <td className="py-3 px-4 text-emerald-600 dark:text-emerald-400 font-bold">
                    Kliring di Hari yang Sama (Same-Day Factoring)
                  </td>
                  <td className="py-3 px-4 text-right font-bold text-emerald-600 dark:text-emerald-400">
                    Likuiditas Kas Kilat
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </Card>
      </div>
    </div>
  );
};
