import * as React from 'react';
import { Search, FileText, Share2, RefreshCw } from 'lucide-react';
import { PresetItem } from '@/types/audit';

interface CommandBarProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  presets: PresetItem[];
  onSelectPreset: (id: string) => void;
  onOpenExport: () => void;
  onRerunAudit: () => void;
}

export function CommandBar({
  open,
  onOpenChange,
  presets,
  onSelectPreset,
  onOpenExport,
  onRerunAudit
}: CommandBarProps) {
  const [search, setSearch] = React.useState('');
  const inputRef = React.useRef<HTMLInputElement>(null);

  React.useEffect(() => {
    if (open) {
      const timer = setTimeout(() => inputRef.current?.focus(), 50);
      return () => clearTimeout(timer);
    }
  }, [open]);

  React.useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        onOpenChange(!open);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [open, onOpenChange]);

  if (!open) return null;

  const handleClose = () => {
    setSearch('');
    onOpenChange(false);
  };

  const filteredPresets = presets.filter(
    (p) =>
      p.company.toLowerCase().includes(search.toLowerCase()) ||
      p.title.toLowerCase().includes(search.toLowerCase()) ||
      p.description.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 p-4 sm:p-6">
      <div
        className="fixed inset-0 bg-black/80 backdrop-blur-sm transition-opacity"
        onClick={handleClose}
      />

      <div className="relative z-50 w-full max-w-xl rounded-xl border border-zinc-800 bg-zinc-950 shadow-2xl overflow-hidden animate-in zoom-in-95">
        {/* Search Input */}
        <div className="flex items-center gap-3 px-4 py-3 border-b border-zinc-800/80 bg-zinc-900/60">
          <Search className="w-4 h-4 text-zinc-400 shrink-0" />
          <input
            ref={inputRef}
            type="text"
            placeholder="Ketik perintah atau cari sampel Surat Jalan... (ESC untuk tutup)"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full bg-transparent text-xs text-zinc-100 placeholder:text-zinc-500 focus:outline-none"
          />
          <kbd className="px-1.5 py-0.5 rounded bg-zinc-800 border border-zinc-700 text-[10px] font-medium text-zinc-400">
            ESC
          </kbd>
        </div>

        {/* Action List */}
        <div className="max-h-80 overflow-y-auto p-2 space-y-1 text-xs">
          {/* Quick Actions */}
          <div className="px-2 py-1 text-[10px] font-semibold uppercase tracking-wider text-zinc-500">
            Perintah Cepat
          </div>

          <button
            onClick={() => {
              onOpenExport();
              handleClose();
            }}
            className="w-full flex items-center justify-between px-3 py-2 rounded-lg text-zinc-200 hover:bg-zinc-800/80 hover:text-white transition-colors group"
          >
            <div className="flex items-center gap-2.5">
              <Share2 className="w-4 h-4 text-blue-400 group-hover:text-blue-300" />
              <span>Buka Gateway Sinkronisasi ERP (SAP / Odoo / Jurnal.id)</span>
            </div>
            <kbd className="text-[10px] font-medium text-zinc-500 group-hover:text-zinc-300">Export</kbd>
          </button>

          <button
            onClick={() => {
              onRerunAudit();
              handleClose();
            }}
            className="w-full flex items-center justify-between px-3 py-2 rounded-lg text-zinc-200 hover:bg-zinc-800/80 hover:text-white transition-colors group"
          >
            <div className="flex items-center gap-2.5">
              <RefreshCw className="w-4 h-4 text-emerald-400 group-hover:text-emerald-300" />
              <span>Jalankan Ulang Audit Multimodal VLM</span>
            </div>
            <kbd className="text-[10px] font-medium text-zinc-500 group-hover:text-zinc-300">Re-audit</kbd>
          </button>

          {/* Presets */}
          <div className="px-2 pt-3 py-1 text-[10px] font-semibold uppercase tracking-wider text-zinc-500">
            Skenario Sampel Surat Jalan ({filteredPresets.length})
          </div>

          {filteredPresets.map((p, idx) => (
            <button
              key={p.id}
              onClick={() => {
                onSelectPreset(p.id);
                handleClose();
              }}
              className="w-full flex items-center justify-between px-3 py-2 rounded-lg text-zinc-200 hover:bg-zinc-800/80 hover:text-white transition-colors group text-left"
            >
              <div className="flex items-center gap-2.5 min-w-0">
                <FileText className="w-4 h-4 text-zinc-400 group-hover:text-blue-400 shrink-0" />
                <div className="min-w-0">
                  <div className="font-semibold text-zinc-100 truncate">{p.company}</div>
                  <div className="text-[11px] text-zinc-400 truncate">{p.title}</div>
                </div>
              </div>
              <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-zinc-800 text-zinc-400 shrink-0 ml-2">
                #{idx + 1}
              </span>
            </button>
          ))}
        </div>

        {/* Footer */}
        <div className="px-4 py-2 border-t border-zinc-800/80 bg-zinc-900/40 flex items-center justify-between text-[11px] text-zinc-500 font-medium">
          <span>SuratJalan.AI Command Core</span>
          <div className="flex items-center gap-2">
            <span>Navigasi Cepat</span>
            <kbd className="px-1 py-0.5 rounded bg-zinc-800 border border-zinc-700 text-[10px]">↵ Enter</kbd>
          </div>
        </div>
      </div>
    </div>
  );
}
