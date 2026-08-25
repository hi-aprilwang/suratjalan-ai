'use client';

import React, { useState, useRef } from 'react';
import { BoundingBox } from '../types/audit';
import { ZoomIn, ZoomOut, RotateCcw, Eye, EyeOff, Layers, Scan, Crosshair, Sparkles } from 'lucide-react';

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
  const [showBoxes, setShowBoxes] = useState(true);
  const containerRef = useRef<HTMLDivElement>(null);

  const getBoxStyle = (category: string, isHighlighted: boolean) => {
    if (isHighlighted) {
      return {
        border: 'border-yellow-400 border-2 bg-yellow-400/30 ring-4 ring-yellow-400/40 shadow-[0_0_20px_rgba(250,204,21,0.6)] z-20',
        badge: 'bg-yellow-400 text-slate-950 font-black scale-105'
      };
    }
    switch (category) {
      case 'stamp':
        return {
          border: 'border-cyan-400/90 border-2 bg-cyan-500/15 hover:bg-cyan-500/30 shadow-[0_0_15px_rgba(34,211,238,0.3)]',
          badge: 'bg-cyan-500 text-slate-950 font-bold'
        };
      case 'signature':
        return {
          border: 'border-purple-400/90 border-2 bg-purple-500/15 hover:bg-purple-500/30 shadow-[0_0_15px_rgba(192,132,252,0.3)]',
          badge: 'bg-purple-500 text-white font-bold'
        };
      case 'handwritten_retur':
      case 'warning':
        return {
          border: 'border-rose-500 border-2 bg-rose-500/20 hover:bg-rose-500/35 shadow-[0_0_20px_rgba(244,63,94,0.5)] animate-pulse',
          badge: 'bg-rose-600 text-white font-black'
        };
      case 'header':
        return {
          border: 'border-slate-400/80 border bg-slate-500/10 hover:bg-slate-500/25',
          badge: 'bg-slate-800 text-slate-200 font-semibold'
        };
      default:
        return {
          border: 'border-emerald-400/80 border bg-emerald-500/15 hover:bg-emerald-500/30 shadow-[0_0_10px_rgba(52,211,153,0.2)]',
          badge: 'bg-emerald-600 text-white font-bold'
        };
    }
  };

  return (
    <div className="bg-slate-900/60 backdrop-blur-xl rounded-2xl border border-white/[0.08] flex flex-col h-full overflow-hidden shadow-[0_8px_32px_rgba(0,0,0,0.37)]">
      {/* Viewer Header Toolbar */}
      <div className="px-4 py-3 border-b border-white/[0.08] flex items-center justify-between bg-slate-950/70">
        <div className="flex items-center gap-2">
          <div className="w-6 h-6 rounded-lg bg-blue-500/20 border border-blue-400/30 flex items-center justify-center text-blue-400">
            <Scan className="w-3.5 h-3.5" />
          </div>
          <div>
            <span className="text-xs font-bold text-slate-100 uppercase tracking-wider block">
              Spatial Coordinate Grounding
            </span>
            <span className="text-[10px] text-slate-400">
              {boundingBoxes.length} Visual Grounding Anchors
            </span>
          </div>
        </div>

        {/* Floating Controls */}
        <div className="flex items-center gap-1.5 bg-slate-950/80 p-1 rounded-xl border border-white/[0.08] text-slate-300">
          <button
            onClick={() => setZoom((z) => Math.max(0.6, z - 0.15))}
            className="p-1.5 hover:bg-white/10 rounded-lg hover:text-white transition-colors"
            title="Zoom Out"
          >
            <ZoomOut className="w-3.5 h-3.5" />
          </button>
          <span className="text-[11px] font-mono font-bold px-1.5 text-slate-300">
            {Math.round(zoom * 100)}%
          </span>
          <button
            onClick={() => setZoom((z) => Math.min(2.2, z + 0.15))}
            className="p-1.5 hover:bg-white/10 rounded-lg hover:text-white transition-colors"
            title="Zoom In"
          >
            <ZoomIn className="w-3.5 h-3.5" />
          </button>
          <div className="w-[1px] h-3.5 bg-white/10 mx-0.5" />
          <button
            onClick={() => setZoom(1)}
            className="p-1.5 hover:bg-white/10 rounded-lg hover:text-white transition-colors"
            title="Reset Zoom"
          >
            <RotateCcw className="w-3.5 h-3.5" />
          </button>
          <div className="w-[1px] h-3.5 bg-white/10 mx-0.5" />
          <button
            onClick={() => setShowBoxes(!showBoxes)}
            className={`p-1.5 rounded-lg transition-colors flex items-center gap-1 text-[11px] font-semibold px-2 ${
              showBoxes
                ? 'bg-blue-600/30 text-blue-300 border border-blue-400/30 shadow-[0_0_10px_rgba(59,130,246,0.2)]'
                : 'hover:bg-white/10 text-slate-400'
            }`}
            title="Toggle Bounding Boxes"
          >
            {showBoxes ? <Eye className="w-3.5 h-3.5" /> : <EyeOff className="w-3.5 h-3.5" />}
            <span className="hidden md:inline">Grounding</span>
          </button>
        </div>
      </div>

      {/* Image & Bounding Box Viewport */}
      <div
        ref={containerRef}
        className="flex-1 relative overflow-auto p-4 sm:p-6 flex items-center justify-center min-h-[500px] max-h-[720px] bg-slate-950/60"
      >
        {/* Laser Scanner Line while Auditing */}
        {isAuditing && (
          <>
            <div className="absolute inset-0 z-30 bg-slate-950/80 backdrop-blur-md flex flex-col items-center justify-center gap-4">
              <div className="relative">
                <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center shadow-[0_0_30px_rgba(59,130,246,0.5)] animate-pulse">
                  <Sparkles className="w-8 h-8 text-white animate-spin" />
                </div>
              </div>
              <div className="text-center space-y-1">
                <p className="text-sm font-extrabold text-white tracking-wide">
                  Gemini 2.0 Flash VLM Grounding...
                </p>
                <p className="text-xs text-blue-400 font-mono">
                  Extracting Indonesian handwriting, stamps & line items
                </p>
              </div>
            </div>
          </>
        )}

        <div
          className="relative inline-block transition-transform duration-200 origin-top shadow-[0_12px_40px_rgba(0,0,0,0.6)] rounded-xl overflow-hidden border border-white/15"
          style={{ transform: `scale(${zoom})` }}
        >
          {/* Laser scanning line overlay */}
          {isAuditing && (
            <div className="absolute left-0 right-0 h-1 bg-gradient-to-r from-transparent via-cyan-400 to-transparent shadow-[0_0_15px_#22d3ee] z-20 animate-laser" />
          )}

          {/* Document Base Image */}
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={imageUrl}
            alt="Surat Jalan Physical Scan"
            className="w-full max-w-[650px] object-contain rounded-xl select-none pointer-events-none"
          />

          {/* Spatial Grounding Bounding Boxes Overlay */}
          {showBoxes &&
            boundingBoxes.map((box, idx) => {
              const isHighlighted = highlightedIndex === idx;
              const style = getBoxStyle(box.category, isHighlighted);

              // Convert normalized 0-1000 coordinates to percentages
              const topPct = (box.ymin / 1000) * 100;
              const leftPct = (box.xmin / 1000) * 100;
              const heightPct = ((box.ymax - box.ymin) / 1000) * 100;
              const widthPct = ((box.xmax - box.xmin) / 1000) * 100;

              return (
                <div
                  key={idx}
                  onMouseEnter={() => onHoverBox(idx)}
                  onMouseLeave={() => onHoverBox(null)}
                  className={`absolute transition-all duration-150 cursor-pointer rounded-sm ${style.border}`}
                  style={{
                    top: `${topPct}%`,
                    left: `${leftPct}%`,
                    height: `${heightPct}%`,
                    width: `${widthPct}%`
                  }}
                >
                  {/* Floating Box Tag */}
                  <span
                    className={`absolute -top-3.5 left-1 text-[9px] px-2 py-0.5 rounded-full shadow-lg whitespace-nowrap pointer-events-none transition-all ${style.badge}`}
                  >
                    {box.label}
                  </span>
                </div>
              );
            })}
        </div>
      </div>

      {/* Legend Footer */}
      <div className="px-4 py-2.5 border-t border-white/[0.08] bg-slate-950/90 flex flex-wrap items-center justify-between gap-3 text-[11px] text-slate-400">
        <div className="flex flex-wrap items-center gap-3">
          <span className="font-bold text-slate-300 text-xs">Entity Types:</span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.5)]" />
            <span className="text-slate-300">Verified Item</span>
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-500 shadow-[0_0_8px_rgba(244,63,94,0.5)]" />
            <span className="text-rose-300 font-semibold">Selisih / Retur</span>
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-cyan-400 shadow-[0_0_8px_rgba(34,211,238,0.5)]" />
            <span className="text-cyan-300 font-semibold">Stempel DC</span>
          </span>
          <span className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-purple-400 shadow-[0_0_8px_rgba(192,132,252,0.5)]" />
            <span className="text-purple-300 font-semibold">Tanda Tangan</span>
          </span>
        </div>

        <span className="text-[10px] font-mono text-slate-500 hidden sm:inline">
          Format Grounding: Normalized [0, 1000]
        </span>
      </div>
    </div>
  );
};
