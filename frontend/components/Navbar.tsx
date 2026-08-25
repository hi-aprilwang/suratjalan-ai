'use client';

import React from 'react';
import { ShieldCheck, Cpu, Sparkles, FileText, Zap, Keyboard } from 'lucide-react';

interface NavbarProps {
  isLiveModel: boolean;
  onToggleModel: () => void;
  latencyMs: number;
}

export const Navbar: React.FC<NavbarProps> = ({ isLiveModel, onToggleModel, latencyMs }) => {
  return (
    <header className="sticky top-0 z-50 bg-[#060913]/80 backdrop-blur-xl border-b border-white/[0.08] text-slate-100 shadow-[0_4px_30px_rgba(0,0,0,0.4)]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Brand Logo & Tag */}
        <div className="flex items-center gap-3.5">
          <div className="relative group">
            <div className="absolute -inset-0.5 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-xl blur opacity-60 group-hover:opacity-100 transition duration-300" />
            <div className="relative w-10 h-10 rounded-xl bg-slate-950 border border-white/20 flex items-center justify-center shadow-inner">
              <FileText className="w-5 h-5 text-blue-400" />
            </div>
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-extrabold text-lg tracking-tight text-white flex items-center gap-1">
                SuratJalan<span className="text-blue-400">.AI</span>
              </span>
              <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-gradient-to-r from-blue-500/20 to-indigo-500/20 border border-blue-400/30 text-blue-300 shadow-[0_0_10px_rgba(59,130,246,0.2)]">
                COMPFEST 18 AIC
              </span>
            </div>
            <p className="text-[11px] text-slate-400 font-medium hidden sm:block">
              Multimodal Proof-of-Delivery Audit & Invoice Reconciliation Engine
            </p>
          </div>
        </div>

        {/* Status Badges & Controls */}
        <div className="flex items-center gap-2.5">
          
          {/* Keyboard hint */}
          <div className="hidden xl:flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-[11px] bg-white/[0.03] border border-white/[0.06] text-slate-400">
            <Keyboard className="w-3 h-3 text-slate-500" />
            <span>Presets: <kbd className="px-1 py-0.5 rounded bg-slate-800 text-[10px] font-mono text-slate-300">1</kbd> <kbd className="px-1 py-0.5 rounded bg-slate-800 text-[10px] font-mono text-slate-300">2</kbd> <kbd className="px-1 py-0.5 rounded bg-slate-800 text-[10px] font-mono text-slate-300">3</kbd></span>
          </div>

          {/* AI Model Toggle Badge */}
          <button
            onClick={onToggleModel}
            className="flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs font-semibold bg-slate-900/90 border border-white/[0.08] hover:border-blue-500/50 transition-all text-slate-300 shadow-sm hover:shadow-[0_0_15px_rgba(59,130,246,0.2)]"
            title="Toggle between Live Gemini 2.0 Flash VLM and Offline Deterministic Fallback"
          >
            <div className="relative flex items-center justify-center">
              <span className={`w-2 h-2 rounded-full ${isLiveModel ? 'bg-emerald-400' : 'bg-blue-400'}`} />
              <span className={`absolute w-3.5 h-3.5 rounded-full animate-ping opacity-60 ${isLiveModel ? 'bg-emerald-400' : 'bg-blue-400'}`} />
            </div>
            <span className="hidden md:inline text-slate-400">Engine:</span>
            <span className={isLiveModel ? 'text-emerald-400' : 'text-blue-400'}>
              {isLiveModel ? 'Gemini 2.0 Flash' : 'Hybrid VLM'}
            </span>
          </button>

          {/* Latency Pill */}
          <div className="hidden sm:flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-mono bg-white/[0.04] border border-white/[0.06] text-slate-300">
            <Zap className="w-3.5 h-3.5 text-amber-400" />
            <span>{latencyMs}ms</span>
          </div>

          {/* Verification Badge */}
          <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-semibold bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 shadow-[0_0_12px_rgba(16,185,129,0.15)]">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
            <span className="hidden sm:inline">UI Fasilkom Verified</span>
          </div>

        </div>

      </div>
    </header>
  );
};
