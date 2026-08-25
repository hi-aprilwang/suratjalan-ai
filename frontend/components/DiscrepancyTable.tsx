'use client';

import React from 'react';
import { ExtractedItem } from '../types/audit';
import { CheckCircle2, AlertTriangle, AlertOctagon, HelpCircle, FileSpreadsheet, Tag, PenTool } from 'lucide-react';

interface DiscrepancyTableProps {
  items: ExtractedItem[];
  highlightedIndex: number | null;
  onHoverItem: (index: number | null) => void;
}

export const DiscrepancyTable: React.FC<DiscrepancyTableProps> = ({
  items,
  highlightedIndex,
  onHoverItem
}) => {
  const formatIDR = (val: number) => {
    return new Intl.NumberFormat('id-ID', {
      style: 'currency',
      currency: 'IDR',
      maximumFractionDigits: 0
    }).format(val);
  };

  const getItemBadge = (status: string, variance: number) => {
    if (status === 'MATCH' && variance === 0) {
      return (
        <span className="inline-flex items-center gap-1 text-[11px] font-bold text-emerald-400 bg-emerald-950/70 border border-emerald-500/30 px-2.5 py-0.5 rounded-full shadow-[0_0_8px_rgba(16,185,129,0.2)]">
          <CheckCircle2 className="w-3 h-3 text-emerald-400" /> Cocok (0)
        </span>
      );
    } else if (status === 'DISCREPANCY' || variance < 0) {
      return (
        <span className="inline-flex items-center gap-1 text-[11px] font-black text-amber-400 bg-amber-950/90 border border-amber-500/40 px-2.5 py-0.5 rounded-full shadow-[0_0_12px_rgba(245,158,11,0.3)] animate-pulse">
          <AlertTriangle className="w-3 h-3 text-amber-400" /> Selisih ({variance})
        </span>
      );
    } else if (status === 'DAMAGED') {
      return (
        <span className="inline-flex items-center gap-1 text-[11px] font-black text-rose-400 bg-rose-950/90 border border-rose-500/40 px-2.5 py-0.5 rounded-full shadow-[0_0_12px_rgba(244,63,94,0.3)] animate-pulse">
          <AlertOctagon className="w-3 h-3 text-rose-400" /> Rusak ({variance})
        </span>
      );
    } else {
      return (
        <span className="inline-flex items-center gap-1 text-[11px] font-medium text-slate-400 bg-slate-800 px-2 py-0.5 rounded-full">
          <HelpCircle className="w-3 h-3" /> {status}
        </span>
      );
    }
  };

  return (
    <div className="bg-slate-900/60 backdrop-blur-xl rounded-2xl border border-white/[0.08] overflow-hidden shadow-[0_8px_32px_rgba(0,0,0,0.37)]">
      {/* Table Header Section */}
      <div className="px-5 py-3.5 border-b border-white/[0.08] flex items-center justify-between bg-slate-950/70">
        <div className="flex items-center gap-2.5">
          <div className="w-6 h-6 rounded-lg bg-blue-500/20 border border-blue-400/30 flex items-center justify-center text-blue-400">
            <FileSpreadsheet className="w-3.5 h-3.5" />
          </div>
          <div>
            <h3 className="text-xs font-black text-slate-100 uppercase tracking-wider">
              Rekonsiliasi Line Item (PO vs Fisik Surat Jalan)
            </h3>
            <p className="text-[10px] text-slate-400">
              Hover baris untuk melihat titik koordinat fisik pada dokumen
            </p>
          </div>
        </div>
        <span className="text-[11px] text-slate-300 font-mono font-bold px-2.5 py-1 rounded-lg bg-white/[0.04] border border-white/[0.06]">
          {items.length} Baris Produk
        </span>
      </div>

      {/* Table Content */}
      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs border-collapse">
          <thead>
            <tr className="border-b border-white/[0.08] bg-slate-950/40 text-[10px] font-extrabold text-slate-400 uppercase tracking-wider">
              <th className="py-3 px-3.5 w-10 text-center">No</th>
              <th className="py-3 px-3.5">Nama Produk / SKU</th>
              <th className="py-3 px-3 text-center">PO Kirim</th>
              <th className="py-3 px-3 text-center">Terima Fisik</th>
              <th className="py-3 px-3.5 text-center">Status Selisih</th>
              <th className="py-3 px-3.5">Catatan Tulisan Tangan</th>
              <th className="py-3 px-3.5 text-right">Potongan Klaim</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-white/[0.04]">
            {items.map((item, idx) => {
              const isHighlighted = highlightedIndex === idx;
              const hasDiscrepancy = item.variance !== 0 || item.status !== 'MATCH';

              return (
                <tr
                  key={idx}
                  onMouseEnter={() => onHoverItem(idx)}
                  onMouseLeave={() => onHoverItem(null)}
                  className={`transition-all duration-150 cursor-pointer ${
                    isHighlighted
                      ? 'bg-blue-600/20 text-white ring-1 ring-blue-500/40 shadow-inner'
                      : hasDiscrepancy
                      ? 'bg-rose-950/20 hover:bg-rose-950/35 text-slate-200'
                      : 'hover:bg-white/[0.04] text-slate-300'
                  }`}
                >
                  <td className="py-3.5 px-3.5 text-center font-mono font-bold text-slate-500">
                    {item.item_number}
                  </td>
                  <td className="py-3.5 px-3.5">
                    <span className="font-bold text-slate-100 block text-xs">
                      {item.item_name}
                    </span>
                    <span className="text-[10px] text-slate-400 font-mono">
                      Kemasan: {item.unit}
                    </span>
                  </td>
                  <td className="py-3.5 px-3 text-center font-mono font-medium text-slate-300">
                    {item.ordered_qty}
                  </td>
                  <td className="py-3.5 px-3 text-center font-mono font-extrabold text-white text-sm">
                    {item.received_qty}
                  </td>
                  <td className="py-3.5 px-3.5 text-center">
                    {getItemBadge(item.status, item.variance)}
                  </td>
                  <td className="py-3.5 px-3.5">
                    {item.handwritten_note ? (
                      <span className="inline-flex items-center gap-1 text-[11px] font-mono font-bold text-amber-300 bg-amber-950/60 border border-amber-500/40 px-2.5 py-1 rounded-lg shadow-sm">
                        <PenTool className="w-3 h-3 text-amber-400" />
                        &quot;{item.handwritten_note}&quot;
                      </span>
                    ) : (
                      <span className="text-slate-600 text-[11px]">-</span>
                    )}
                  </td>
                  <td className="py-3.5 px-3.5 text-right font-mono font-extrabold">
                    {item.claim_amount_idr > 0 ? (
                      <span className="text-rose-400 text-xs shadow-sm">
                        -{formatIDR(item.claim_amount_idr)}
                      </span>
                    ) : (
                      <span className="text-slate-500 text-xs">Rp 0</span>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
