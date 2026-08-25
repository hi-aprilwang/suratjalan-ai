'use client';

import React, { useRef } from 'react';
import { PresetItem } from '../types/audit';
import { CheckCircle2, AlertTriangle, XCircle, Layers, Upload } from 'lucide-react';
import { Badge } from './ui/badge';
import { Button } from './ui/button';

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

  const getStatusBadge = (status: string, presetId: string) => {
    switch (status) {
      case 'APPROVED_FOR_INVOICING':
        return (
          <Badge variant="success" className="text-sm font-semibold">
            <CheckCircle2 className="w-4 h-4" /> MATCH (APPROVED)
          </Badge>
        );
      case 'DISCREPANCY_FLAGGED':
        const label =
          presetId === 'preset_4'
            ? 'COLD-ABUSE (+14°C)'
            : presetId === 'preset_5'
            ? 'DAMAGED (20 ZAK)'
            : 'RETUR (8 DUS)';
        return (
          <Badge variant="warning" className="text-sm font-semibold">
            <AlertTriangle className="w-4 h-4" /> {label}
          </Badge>
        );
      case 'CRITICAL_REJECTED':
      default:
        const rejectLabel =
          presetId === 'preset_6' ? 'QC REJECT (EXPIRED)' : 'MISSING STAMP';
        return (
          <Badge variant="destructive" className="text-sm font-semibold">
            <XCircle className="w-4 h-4" /> {rejectLabel}
          </Badge>
        );
    }
  };

  const getCategoryCode = (index: number) => {
    const codes = ['FMCG-01', 'CONF-02', 'HSHLD-03', 'COLD-04', 'HEAVY-05', 'PHRMA-06'];
    return codes[index] || `DOC-0${index + 1}`;
  };

  return (
    <div className="space-y-3">
      {/* Header bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 px-1">
        <div className="flex items-center gap-2">
          <Layers className="w-5 h-5 text-zinc-400" />
          <span className="text-sm font-semibold uppercase tracking-wider text-zinc-300">
            Skenario Sampel Uji Coba Logistik // 6 Industri Rantai Pasok
          </span>
        </div>

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
          <Button
            variant="outline"
            size="sm"
            onClick={() => fileInputRef.current?.click()}
            disabled={isAuditing}
            className="gap-2 font-medium text-sm border-zinc-800 bg-zinc-900/60 hover:bg-zinc-800 text-zinc-300"
          >
            <Upload className="w-4 h-4 text-zinc-400" />
            <span>Unggah Dokumen Fisik Sendiri</span>
          </Button>
        </div>
      </div>

      {/* Preset Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-3">
        {presets.map((preset, idx) => {
          const isSelected = selectedPresetId === preset.id;
          return (
            <div
              key={preset.id}
              onClick={() => !isAuditing && onSelectPreset(preset.id)}
              className={`group cursor-pointer rounded-lg p-3.5 border transition-all duration-150 relative flex flex-col justify-between ${
                isSelected
                  ? 'bg-zinc-900 border-zinc-500 shadow-md ring-1 ring-zinc-500/50'
                  : 'bg-zinc-950/80 border-zinc-800/80 hover:border-zinc-700 hover:bg-zinc-900/50'
              }`}
            >
              {/* Card Top */}
              <div>
                <div className="flex items-center justify-between gap-1 mb-2">
                  <span className="text-sm font-bold text-zinc-500 group-hover:text-zinc-300 transition-colors">
                    {getCategoryCode(idx)}
                  </span>
                  <kbd className="text-sm font-semibold px-1.5 py-0.5 rounded bg-zinc-900 border border-zinc-800 text-zinc-400">
                    {idx + 1}
                  </kbd>
                </div>
                <h4 className="text-sm font-semibold text-zinc-100 truncate line-clamp-1 leading-snug">
                  {preset.company.replace('PT ', '')}
                </h4>
                <p className="text-sm text-zinc-400 line-clamp-2 mt-1.5 leading-relaxed">
                  {preset.description}
                </p>
              </div>

              {/* Card Bottom */}
              <div className="mt-3.5 pt-2.5 border-t border-zinc-800/60 flex items-center justify-between">
                {getStatusBadge(preset.expected_status, preset.id)}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
