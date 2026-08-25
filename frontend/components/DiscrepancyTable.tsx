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
        <Badge variant="success" className="text-sm font-semibold">
          <CheckCircle2 className="w-4 h-4" /> Match (0)
        </Badge>
      );
    } else if (status === 'RETURNED' || variance < 0) {
      return (
        <Badge variant="warning" className="text-sm font-semibold">
          <AlertTriangle className="w-4 h-4" /> Retur ({variance})
        </Badge>
      );
    } else if (status === 'DAMAGED') {
      return (
        <Badge variant="destructive" className="text-sm font-semibold">
          <XCircle className="w-4 h-4" /> Rusak ({variance})
        </Badge>
      );
    } else {
      return (
        <Badge variant="outline" className="text-sm font-semibold text-zinc-500 dark:text-zinc-400">
          {status} ({variance})
        </Badge>
      );
    }
  };

  return (
    <Card className="overflow-hidden border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 rounded-xl shadow-xs">
      {/* Table Header Strip */}
      <div className="px-5 py-4 border-b border-zinc-100 dark:border-zinc-800/80 bg-zinc-50/70 dark:bg-zinc-900/60 flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <FileSpreadsheet className="w-5 h-5 text-blue-600 dark:text-blue-400" />
          <span className="text-base font-bold text-zinc-900 dark:text-zinc-100 tracking-tight">
            Rekonsiliasi Line Item (Target PO vs Fisik POD)
          </span>
        </div>
        <span className="text-sm font-semibold text-zinc-600 dark:text-zinc-400 bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 px-3 py-1 rounded-lg shadow-2xs">
          {items.length} Line Items
        </span>
      </div>

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm border-collapse font-sans">
          <thead>
            <tr className="border-b border-zinc-100 dark:border-zinc-800/80 bg-zinc-50/40 dark:bg-zinc-900/40 text-sm uppercase tracking-wider text-zinc-500 dark:text-zinc-400 font-semibold">
              <th className="py-3.5 px-4 w-14 text-center">No</th>
              <th className="py-3.5 px-4">Nama SKU / Produk</th>
              <th className="py-3.5 px-4 text-right">PO Target</th>
              <th className="py-3.5 px-4 text-right">Fisik Terima</th>
              <th className="py-3.5 px-4 text-center">Status Audit</th>
              <th className="py-3.5 px-4">Catatan Tangan / OCR</th>
              <th className="py-3.5 px-4 text-right">Klaim Debit</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-zinc-100 dark:divide-zinc-800/60 font-sans">
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
                      ? 'bg-blue-50/80 dark:bg-zinc-800/90 ring-1 ring-blue-300 dark:ring-zinc-600'
                      : hasDiscrepancy
                      ? 'bg-rose-50/40 dark:bg-rose-950/10 hover:bg-rose-50/80 dark:hover:bg-rose-950/20'
                      : 'hover:bg-zinc-50/80 dark:hover:bg-zinc-900/60'
                  }`}
                >
                  <td className="py-3.5 px-4 text-center text-sm text-zinc-400 font-medium">
                    {item.item_number}
                  </td>
                  <td className="py-3.5 px-4">
                    <div className="font-semibold text-zinc-900 dark:text-zinc-100 text-sm truncate max-w-[280px]">
                      {item.item_name}
                    </div>
                  </td>
                  <td className="py-3.5 px-4 text-right text-sm text-zinc-600 dark:text-zinc-400 font-medium">
                    {item.ordered_qty} <span className="text-sm text-zinc-400 font-normal">{item.unit}</span>
                  </td>
                  <td className="py-3.5 px-4 text-right text-sm font-bold text-zinc-900 dark:text-zinc-100">
                    {item.received_qty} <span className="text-sm text-zinc-400 font-normal">{item.unit}</span>
                  </td>
                  <td className="py-3.5 px-4 text-center">
                    {getItemBadge(item.status, item.variance)}
                  </td>
                  <td className="py-3.5 px-4 text-sm">
                    {item.handwritten_note ? (
                      <div className="flex items-center gap-1.5 text-zinc-800 dark:text-zinc-300 text-sm font-medium">
                        <PenTool className="w-4 h-4 text-zinc-400 dark:text-zinc-500 shrink-0" />
                        <span className="truncate max-w-[200px]">{item.handwritten_note}</span>
                      </div>
                    ) : (
                      <span className="text-zinc-300 dark:text-zinc-600">-</span>
                    )}
                  </td>
                  <td className="py-3.5 px-4 text-right text-sm font-bold">
                    {item.claim_amount_idr > 0 ? (
                      <span className="text-rose-600 dark:text-rose-400">-{formatIDR(item.claim_amount_idr)}</span>
                    ) : (
                      <span className="text-zinc-400 font-medium">Rp 0</span>
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
