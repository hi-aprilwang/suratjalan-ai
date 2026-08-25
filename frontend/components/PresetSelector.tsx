'use client';

import React, { useRef } from 'react';
import { PresetItem } from '../types/audit';
import { CheckCircle2, AlertTriangle, XCircle, UploadCloud, FileSpreadsheet, Sparkles, FileUp } from 'lucide-react';

interface PresetSelectorProps {
  presets: PresetItem[];
  selectedPresetId: string | null;
  onSelectPreset: (presetId: string) => void;
  onFileUpload: (file: File) => void;
  isAuditing: boolean;
}

export const PresetSelector: React.FC<PresetSelectorProps> = ({
  presets,
  selectedPresetId,
  onSelectPreset,
  onFileUpload,
  isAuditing
}) => {
  const fileInputRef = useRef<HTMLInputElement>(null);

  const getStatusBadge = (status: string) => {
    switch (status) {
      case 'APPROVED_FOR_INVOICING':
        return (
          <span className="flex items-center gap-1 text-[11px] font-bold text-emerald-400 bg-emerald-950/80 border border-emerald-500/30 px-2 py-0.5 rounded-full shadow-[0_0_10px_rgba(16,185,129,0.15)]">
            <CheckCircle2 className="w-3 h-3 text-emerald-400" /> 100% Match (Approved)
          </span>
        );
      case 'DISCREPANCY_FLAGGED':
        return (
          <span className="flex items-center gap-1 text-[11px] font-bold text-amber-400 bg-amber-950/80 border border-amber-500/30 px-2 py-0.5 rounded-full shadow-[0_0_10px_rgba(245,158,11,0.15)]">
            <AlertTriangle className="w-3 h-3 text-amber-400" /> Selisih 8 Dus (Retur)
          </span>
        );
      case 'CRITICAL_REJECTED':
      default:
        return (
          <span className="flex items-center gap-1 text-[11px] font-bold text-rose-400 bg-rose-950/80 border border-rose-500/30 px-2 py-0.5 rounded-full shadow-[0_0_10px_rgba(244,63,94,0.15)]">
            <XCircle className="w-3 h-3 text-rose-400" /> Missing Stamp & Damaged
          </span>
        );
    }
  };

  const getPresetKeyNum = (index: number) => {
    return index + 1;
  };

  return (
    <div className="bg-slate-900/60 backdrop-blur-xl rounded-2xl border border-white/[0.08] p-4 sm:p-5 shadow-[0_8px_32px_rgba(0,0,0,0.37)]">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
        <div>
          <div className="flex items-center gap-2">
            <span className="w-6 h-6 rounded-lg bg-blue-500/20 border border-blue-400/30 flex items-center justify-center text-blue-400">
              <FileSpreadsheet className="w-3.5 h-3.5" />
            </span>
            <h2 className="text-xs font-extrabold uppercase tracking-wider text-slate-200">
              Pilih Sampel Surat Jalan / Upload Dokumen
            </h2>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Uji coba dataset Surat Jalan logistik Indonesia atau unggah foto dokumen fisik langsung
          </p>
        </div>

        {/* Upload Button */}
        <div>
          <input
            type="file"
            ref={fileInputRef}
            className="hidden"
            accept="image/*,.pdf"
            onChange={(e) => {
              if (e.target.files && e.target.files[0]) {
                onFileUpload(e.target.files[0]);
              }
            }}
          />
          <button
            onClick={() => fileInputRef.current?.click()}
            disabled={isAuditing}
            className="group relative flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white transition-all shadow-[0_0_20px_rgba(59,130,246,0.3)] hover:shadow-[0_0_25px_rgba(59,130,246,0.5)] disabled:opacity-50 active:scale-95"
          >
            <FileUp className="w-4 h-4 transition-transform group-hover:-translate-y-0.5" />
            <span>Unggah Dokumen Sendiri</span>
          </button>
        </div>
      </div>

      {/* Preset Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5">
        {presets.map((preset, idx) => {
          const isSelected = selectedPresetId === preset.id;
          return (
            <div
              key={preset.id}
              onClick={() => !isAuditing && onSelectPreset(preset.id)}
              className={`group cursor-pointer rounded-2xl p-4 border transition-all duration-200 relative flex flex-col justify-between ${
                isSelected
                  ? 'bg-gradient-to-b from-blue-950/60 to-slate-900/80 border-blue-500/80 shadow-[0_0_25px_rgba(59,130,246,0.25)] ring-1 ring-blue-400/40'
                  : 'bg-slate-950/40 border-white/[0.06] hover:border-white/20 hover:bg-slate-900/50'
              }`}
            >
              {/* Header & Key Badge */}
              <div className="flex items-start justify-between gap-2 mb-2">
                <div className="flex items-center gap-2">
                  <span className="w-5 h-5 rounded-md bg-white/[0.06] border border-white/[0.08] text-[10px] font-mono font-bold flex items-center justify-center text-slate-400 group-hover:text-blue-400 group-hover:border-blue-400/30 transition-colors">
                    {getPresetKeyNum(idx)}
                  </span>
                  <span className="text-xs font-bold text-slate-100 line-clamp-1">
                    {preset.company}
                  </span>
                </div>
                {isSelected && (
                  <span className="flex h-2 w-2 relative">
                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                    <span className="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                  </span>
                )}
              </div>

              {/* Description */}
              <p className="text-[11px] text-slate-400 line-clamp-2 mb-3 leading-relaxed">
                {preset.description}
              </p>

              {/* Status Badge */}
              <div className="pt-2 border-t border-white/[0.04]">
                {getStatusBadge(preset.expected_status)}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
