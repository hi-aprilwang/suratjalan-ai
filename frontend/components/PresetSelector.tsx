'use client';

import React, { useRef } from 'react';
import { PresetItem } from '../types/audit';
import { CheckCircle2, AlertTriangle, XCircle, Sparkles, Upload } from 'lucide-react';
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
            <CheckCircle2 className="w-4 h-4" /> 100% Match
          </Badge>
        );
      case 'DISCREPANCY_FLAGGED':
        const label =
          presetId === 'preset_4'
            ? 'Cold-Abuse'
            : presetId === 'preset_5'
            ? '20 Zak Rusak'
            : '8 Dus Retur';
        return (
          <Badge variant="warning" className="text-sm font-semibold">
            <AlertTriangle className="w-4 h-4" /> {label}
          </Badge>
        );
      case 'CRITICAL_REJECTED':
      default:
        const rejectLabel =
          presetId === 'preset_6' ? 'QC Expired' : 'Tanpa Stempel';
        return (
          <Badge variant="destructive" className="text-sm font-semibold">
            <XCircle className="w-4 h-4" /> {rejectLabel}
          </Badge>
        );
    }
  };

  const getCategoryCode = (index: number) => {
    const codes = ['FMCG', 'Confectionery', 'Household', 'Cold Chain', 'Semen/Konstruksi', 'Pharma CDOB'];
    return codes[index] || `Industri 0${index + 1}`;
  };

  return (
    <div className="space-y-4">
      {/* Header bar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-blue-600 dark:text-blue-400" />
            <h3 className="text-base font-bold text-zinc-900 dark:text-zinc-100">
              Pilih Dokumen Sampel Uji Coba
            </h3>
          </div>
          <p className="text-sm text-zinc-500 dark:text-zinc-400 mt-1">
            Simulasi 6 skenario rantai pasok nyata di Indonesia dengan berbagai tingkat verifikasi dan catatan retur
          </p>
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
            className="gap-2 font-medium text-sm border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900/60 hover:bg-zinc-50 dark:hover:bg-zinc-800 text-zinc-800 dark:text-zinc-300 h-10 px-4 rounded-xl shadow-xs"
          >
            <Upload className="w-4 h-4 text-zinc-500 dark:text-zinc-400" />
            <span>Unggah Dokumen Sendiri</span>
          </Button>
        </div>
      </div>

      {/* Preset Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-4">
        {presets.map((preset, idx) => {
          const isSelected = selectedPresetId === preset.id;
          return (
            <div
              key={preset.id}
              onClick={() => !isAuditing && onSelectPreset(preset.id)}
              className={`group cursor-pointer rounded-xl p-4 sm:p-5 border transition-all duration-200 relative flex flex-col justify-between ${
                isSelected
                  ? 'bg-blue-50/50 dark:bg-zinc-900 border-blue-500/80 dark:border-zinc-500 shadow-md ring-2 ring-blue-500/20 dark:ring-zinc-500/30'
                  : 'bg-white dark:bg-zinc-950/80 border-zinc-200 dark:border-zinc-800/80 hover:border-zinc-300 dark:hover:border-zinc-700 hover:bg-zinc-50/60 dark:hover:bg-zinc-900/40 shadow-xs'
              }`}
            >
              {/* Card Top */}
              <div className="space-y-2.5">
                <div className="flex items-center justify-between gap-1">
                  <span className="text-sm font-semibold text-blue-600 dark:text-blue-400">
                    {getCategoryCode(idx)}
                  </span>
                  <kbd className="text-sm font-semibold px-2 py-0.5 rounded-md bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 text-zinc-500 dark:text-zinc-400">
                    {idx + 1}
                  </kbd>
                </div>
                <h4 className="text-base font-bold text-zinc-900 dark:text-zinc-100 truncate leading-snug">
                  {preset.company.replace('PT ', '')}
                </h4>
                <p className="text-sm text-zinc-500 dark:text-zinc-400 line-clamp-2 leading-relaxed">
                  {preset.description}
                </p>
              </div>

              {/* Card Bottom */}
              <div className="mt-4 pt-3 border-t border-zinc-100 dark:border-zinc-800/80 flex items-center justify-between">
                {getStatusBadge(preset.expected_status, preset.id)}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
