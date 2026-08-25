'use client';

import React from 'react';
import { ExtractedItem } from '../types/audit';
import { CheckCircle2, AlertTriangle, XCircle, FileSpreadsheet, PenTool } from 'lucide-react';
import { Card } from './ui/card';
import { Badge } from './ui/badge';

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
        <Badge variant="success" className="text-[10px] font-semibold">
          <CheckCircle2 className="w-3 h-3" /> MATCH (0)
        </Badge>
      );
    } else if (status === 'RETURNED' || variance < 0) {
      return (
        <Badge variant="warning" className="text-[10px] font-semibold">
          <AlertTriangle className="w-3 h-3" /> RETUR ({variance})
        </Badge>
      );
    } else if (status === 'DAMAGED') {
      return (
        <Badge variant="destructive" className="text-[10px] font-semibold">
          <XCircle className="w-3 h-3" /> RUSAK ({variance})
        </Badge>
      );
    } else {
      return (
        <Badge variant="outline" className="text-[10px] font-semibold text-zinc-400">
          {status} ({variance})
        </Badge>
      );
    }
  };

  return (
    <Card className="overflow-hidden border-zinc-800 bg-zinc-950">
      {/* Table Header Strip */}
      <div className="px-4 py-2.5 border-b border-zinc-800/80 bg-zinc-900/60 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <FileSpreadsheet className="w-4 h-4 text-zinc-400" />
          <span className="text-xs font-bold text-zinc-200 tracking-tight">
            REKONSILIASI LINE ITEM (PURCHASE ORDER VS FISIK POD)
          </span>
        </div>
        <span className="text-[10px] font-semibold text-zinc-400 bg-zinc-900 border border-zinc-800 px-2 py-0.5 rounded">
          {items.length} LINE ITEMS
        </span>
      </div>

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs border-collapse font-sans">
          <thead>
            <tr className="border-b border-zinc-800/80 bg-zinc-900/40 text-[10px] uppercase tracking-wider text-zinc-400 font-semibold">
              <th className="py-2.5 px-3 w-10 text-center">No</th>
              <th className="py-2.5 px-3">Nama SKU / Produk</th>
              <th className="py-2.5 px-3 text-right">PO Qty</th>
              <th className="py-2.5 px-3 text-right">Terima</th>
              <th className="py-2.5 px-3 text-center">Status Audit</th>
              <th className="py-2.5 px-3">Catatan Tulisan Tangan / OCR</th>
              <th className="py-2.5 px-3 text-right">Klaim Debit</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-zinc-800/60 font-sans">
            {items.map((item, idx) => {
              const isHighlighted = highlightedIndex === idx;
              const hasDiscrepancy = item.variance !== 0 || item.status !== 'MATCH';

              return (
                <tr
                  key={idx}
                  onMouseEnter={() => onHoverItem(idx)}
                  onMouseLeave={() => onHoverItem(null)}
                  className={`transition-colors cursor-pointer ${
                    isHighlighted
                      ? 'bg-zinc-800/90 ring-1 ring-zinc-600'
                      : hasDiscrepancy
                      ? 'bg-rose-950/10 hover:bg-rose-950/20'
                      : 'hover:bg-zinc-900/60'
                  }`}
                >
                  <td className="py-2 px-3 text-center text-[11px] text-zinc-500 font-medium">
                    {item.item_number}
                  </td>
                  <td className="py-2 px-3">
                    <div className="font-medium text-zinc-200 text-xs truncate max-w-[280px]">
                      {item.item_name}
                    </div>
                  </td>
                  <td className="py-2 px-3 text-right text-xs text-zinc-300 font-medium">
                    {item.ordered_qty} <span className="text-[10px] text-zinc-500 font-normal">{item.unit}</span>
                  </td>
                  <td className="py-2 px-3 text-right text-xs font-bold text-zinc-100">
                    {item.received_qty} <span className="text-[10px] text-zinc-500 font-normal">{item.unit}</span>
                  </td>
                  <td className="py-2 px-3 text-center">
                    {getItemBadge(item.status, item.variance)}
                  </td>
                  <td className="py-2 px-3 text-[11px]">
                    {item.handwritten_note ? (
                      <div className="flex items-center gap-1.5 text-zinc-300 text-[10px] font-medium">
                        <PenTool className="w-3 h-3 text-zinc-500 shrink-0" />
                        <span className="truncate max-w-[200px]">{item.handwritten_note}</span>
                      </div>
                    ) : (
                      <span className="text-zinc-600">-</span>
                    )}
                  </td>
                  <td className="py-2 px-3 text-right text-xs font-bold">
                    {item.claim_amount_idr > 0 ? (
                      <span className="text-rose-400">-{formatIDR(item.claim_amount_idr)}</span>
                    ) : (
                      <span className="text-zinc-500 font-medium">Rp 0</span>
                    )}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </Card>
  );
};
