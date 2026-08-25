'use client';

import React, { useState, useRef } from 'react';
import { BoundingBox } from '../types/audit';
import {
  ZoomIn,
  ZoomOut,
  RotateCcw,
  Eye,
  EyeOff,
  Crosshair,
  ScanLine
} from 'lucide-react';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Card } from './ui/card';

interface DocumentViewerProps {
  imageUrl: string;
  boundingBoxes: BoundingBox[];
  highlightedIndex: number | null;
  onHoverBox: (index: number | null) => void;
  isAuditing: boolean;
}

export const DocumentViewer: React.FC<DocumentViewerProps> = ({
  imageUrl,
  boundingBoxes,
  highlightedIndex,
  onHoverBox,
  isAuditing
}) => {
  const [zoom, setZoom] = useState(1);
  const [activeLayer, setActiveLayer] = useState<'all' | 'items' | 'stamps' | 'signatures' | 'warnings'>('all');
  const [showCoordinates, setShowCoordinates] = useState(true);
  const containerRef = useRef<HTMLDivElement>(null);

  const filterBoxes = (boxes: BoundingBox[]) => {
    if (activeLayer === 'all') return boxes;
    if (activeLayer === 'items') return boxes.filter((b) => b.category === 'item_row' || b.category === 'table');
    if (activeLayer === 'stamps') return boxes.filter((b) => b.category === 'stamp');
    if (activeLayer === 'signatures') return boxes.filter((b) => b.category === 'signature');
    if (activeLayer === 'warnings')
      return boxes.filter((b) => b.category === 'warning' || b.category === 'handwritten_retur');
    return boxes;
  };

  const getBoxStyle = (category: string, isHighlighted: boolean) => {
    if (isHighlighted) {
      return {
        border: 'border-yellow-500 dark:border-yellow-400 border-2 bg-yellow-400/20 ring-2 ring-yellow-400/60 z-30 shadow-lg',
        badge: 'bg-yellow-400 text-zinc-950 font-bold'
      };
    }
    switch (category) {
      case 'stamp':
        return {
          border: 'border-cyan-500 dark:border-cyan-400 border-2 bg-cyan-500/10 hover:bg-cyan-500/25',
          badge: 'bg-cyan-100 dark:bg-cyan-950 text-cyan-800 dark:text-cyan-300 border border-cyan-300 dark:border-cyan-800'
        };
      case 'signature':
        return {
          border: 'border-purple-500 dark:border-purple-400 border-2 bg-purple-500/10 hover:bg-purple-500/25',
          badge: 'bg-purple-100 dark:bg-purple-950 text-purple-800 dark:text-purple-300 border border-purple-300 dark:border-purple-800'
        };
      case 'handwritten_retur':
      case 'warning':
        return {
          border: 'border-rose-500 border-2 bg-rose-500/15 hover:bg-rose-500/30',
          badge: 'bg-rose-100 dark:bg-rose-950 text-rose-800 dark:text-rose-300 border border-rose-300 dark:border-rose-800 font-bold'
        };
      case 'header':
      case 'recipient':
      case 'transporter':
        return {
          border: 'border-zinc-400 dark:border-zinc-500 border bg-zinc-500/10 hover:bg-zinc-500/20',
          badge: 'bg-zinc-100 dark:bg-zinc-900 text-zinc-800 dark:text-zinc-300 border border-zinc-300 dark:border-zinc-700'
        };
      default:
        return {
          border: 'border-emerald-500 border-2 bg-emerald-500/10 hover:bg-emerald-500/25',
          badge: 'bg-emerald-100 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800 font-semibold'
        };
    }
  };

  const visibleBoxes = filterBoxes(boundingBoxes);

  return (
    <Card className="flex flex-col h-full overflow-hidden border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 rounded-xl shadow-xs">
      {/* Header Toolbar */}
      <div className="px-5 py-4 border-b border-zinc-100 dark:border-zinc-800/80 bg-zinc-50/70 dark:bg-zinc-900/60 flex items-center justify-between gap-4">
        <div className="flex items-center gap-2.5">
          <Crosshair className="w-5 h-5 text-blue-600 dark:text-blue-400" />
          <span className="text-base font-bold text-zinc-900 dark:text-zinc-100 tracking-tight">
            Spatial Grounding Canvas
          </span>
          <Badge variant="outline" className="text-sm font-medium border-zinc-200 dark:border-zinc-800 text-zinc-600 dark:text-zinc-400">
            {visibleBoxes.length} Anchors
          </Badge>
        </div>

        {/* View Controls */}
        <div className="flex items-center gap-2">
          <Button
            variant="outline"
            size="icon"
            onClick={() => setZoom((z) => Math.max(0.6, z - 0.15))}
            className="h-9 w-9 rounded-lg border-zinc-200 dark:border-zinc-800 text-zinc-700 dark:text-zinc-300"
            title="Zoom Out"
          >
            <ZoomOut className="w-4 h-4" />
          </Button>

          <span className="text-sm font-semibold px-1 text-zinc-700 dark:text-zinc-300 min-w-11 text-center">
            {Math.round(zoom * 100)}%
          </span>

          <Button
            variant="outline"
            size="icon"
            onClick={() => setZoom((z) => Math.min(2.2, z + 0.15))}
            className="h-9 w-9 rounded-lg border-zinc-200 dark:border-zinc-800 text-zinc-700 dark:text-zinc-300"
            title="Zoom In"
          >
            <ZoomIn className="w-4 h-4" />
          </Button>

          <Button
            variant="outline"
            size="icon"
            onClick={() => setZoom(1)}
            className="h-9 w-9 rounded-lg border-zinc-200 dark:border-zinc-800 text-zinc-700 dark:text-zinc-300 ml-0.5"
            title="Reset Zoom"
          >
            <RotateCcw className="w-4 h-4" />
          </Button>

          <Button
            variant={showCoordinates ? 'secondary' : 'outline'}
            size="sm"
            onClick={() => setShowCoordinates(!showCoordinates)}
            className="h-9 px-3 text-sm font-medium gap-1.5 rounded-lg border-zinc-200 dark:border-zinc-800 ml-1"
          >
            {showCoordinates ? <Eye className="w-4 h-4 text-blue-600 dark:text-blue-400" /> : <EyeOff className="w-4 h-4 text-zinc-400" />}
            <span className="hidden sm:inline">Overlay</span>
          </Button>
        </div>
      </div>

      {/* Layer Filter Toolbar */}
      <div className="px-5 py-2.5 border-b border-zinc-100 dark:border-zinc-800/60 bg-zinc-50/40 dark:bg-zinc-950 flex items-center gap-2 overflow-x-auto text-sm">
        <span className="text-zinc-400 mr-1 text-sm font-medium">Filter Layer:</span>
        {(
          [
            { id: 'all', label: 'Semua Objek' },
            { id: 'items', label: 'Line Items' },
            { id: 'stamps', label: 'Stempel' },
            { id: 'signatures', label: 'Tanda Tangan' },
            { id: 'warnings', label: 'Selisih Retur' }
          ] as const
        ).map((layer) => (
          <button
            key={layer.id}
            onClick={() => setActiveLayer(layer.id)}
            className={`px-3 py-1.5 rounded-lg text-sm transition-all ${
              activeLayer === layer.id
                ? 'bg-white dark:bg-zinc-800 text-zinc-900 dark:text-zinc-100 font-bold border border-zinc-200 dark:border-zinc-700 shadow-2xs'
                : 'text-zinc-500 hover:text-zinc-900 dark:hover:text-zinc-300 hover:bg-zinc-100 dark:hover:bg-zinc-900 font-medium'
            }`}
          >
            {layer.label}
          </button>
        ))}
      </div>

      {/* Viewport */}
      <div
        ref={containerRef}
        className="flex-1 relative overflow-auto p-6 flex items-center justify-center min-h-[520px] max-h-[740px] bg-zinc-50/60 dark:bg-zinc-950 select-none"
      >
        {/* Inference Loading State */}
        {isAuditing && (
          <div className="absolute inset-0 z-40 bg-white/80 dark:bg-zinc-950/80 backdrop-blur-sm flex flex-col items-center justify-center gap-3.5">
            <div className="h-16 w-16 rounded-2xl bg-white dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700 flex items-center justify-center shadow-xl">
              <ScanLine className="w-8 h-8 text-blue-600 dark:text-blue-400 animate-spin" />
            </div>
            <div className="text-center text-sm">
              <p className="font-bold text-zinc-900 dark:text-zinc-100 text-base uppercase">MEMPROSES AUDIT VLM...</p>
              <p className="text-zinc-500 dark:text-zinc-400 text-sm mt-1">Ekstraksi Spasial Dokumen & Rekonsiliasi Otomatis</p>
            </div>
          </div>
        )}

        {/* Document Render Container */}
        <div
          className="relative inline-block transition-transform duration-150 origin-top rounded-xl border border-zinc-200 dark:border-zinc-800 shadow-xl overflow-hidden bg-white"
          style={{ transform: `scale(${zoom})` }}
        >
          {/* Laser Reticle Bar */}
          {isAuditing && (
            <div className="absolute left-0 right-0 h-0.5 bg-blue-500 dark:bg-blue-400 shadow-[0_0_8px_#38bdf8] z-30 animate-reticle" />
          )}

          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={imageUrl}
            alt="Surat Jalan POD Physical Document"
            className="w-full max-w-[650px] object-contain select-none pointer-events-none"
          />

          {/* Spatial Grounding Bounding Box Overlays */}
          {showCoordinates &&
            visibleBoxes.map((box, idx) => {
              const isHighlighted = highlightedIndex === idx;
              const style = getBoxStyle(box.category, isHighlighted);

              const topPct = (box.ymin / 1000) * 100;
              const leftPct = (box.xmin / 1000) * 100;
              const heightPct = ((box.ymax - box.ymin) / 1000) * 100;
              const widthPct = ((box.xmax - box.xmin) / 1000) * 100;

              return (
                <div
                  key={idx}
                  onMouseEnter={() => onHoverBox(idx)}
                  onMouseLeave={() => onHoverBox(null)}
                  className={`absolute transition-all duration-100 cursor-pointer rounded-xs ${style.border}`}
                  style={{
                    top: `${topPct}%`,
                    left: `${leftPct}%`,
                    height: `${heightPct}%`,
                    width: `${widthPct}%`
                  }}
                >
                  <span
                    className={`absolute -top-4 left-0.5 text-sm px-2 py-0.5 rounded font-semibold shadow-md whitespace-nowrap pointer-events-none ${style.badge}`}
                  >
                    {box.label}
                  </span>
                </div>
              );
            })}
        </div>
      </div>

      {/* Legend Footer */}
      <div className="px-5 py-3 border-t border-zinc-100 dark:border-zinc-800/80 bg-zinc-50/70 dark:bg-zinc-900/40 flex flex-wrap items-center justify-between gap-4 text-sm text-zinc-500 dark:text-zinc-400">
        <div className="flex flex-wrap items-center gap-4 font-medium">
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-xs bg-emerald-500" />
            <span className="text-zinc-700 dark:text-zinc-300">Barang Cocok</span>
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-xs bg-rose-500" />
            <span className="text-rose-600 dark:text-rose-300">Selisih / Retur</span>
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-xs bg-cyan-500 dark:bg-cyan-400" />
            <span className="text-cyan-700 dark:text-cyan-300">Stempel DC</span>
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-xs bg-purple-500 dark:bg-purple-400" />
            <span className="text-purple-700 dark:text-purple-300">Tanda Tangan</span>
          </span>
        </div>

        <span className="text-sm text-zinc-400 font-medium">
          Koordinat Normalisasi [0..1000]
        </span>
      </div>
    </Card>
  );
};
