'use client';

import React from 'react';
import { Search, Terminal, ArrowUpRight, Activity } from 'lucide-react';
import { Button } from './ui/button';
import { Badge } from './ui/badge';
import { Separator } from './ui/separator';

interface NavbarProps {
  isLiveModel: boolean;
  onToggleModel: () => void;
  latencyMs: number;
  onOpenCommandBar: () => void;
  onOpenExport: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  isLiveModel,
  onToggleModel,
  latencyMs,
  onOpenCommandBar,
  onOpenExport
}) => {
  return (
    <header className="sticky top-0 z-40 w-full border-b border-zinc-800 bg-zinc-950/90 backdrop-blur-md">
      <div className="max-w-[1600px] mx-auto px-4 sm:px-6 h-14 flex items-center justify-between gap-4">
        
        {/* Left: Brand & Telemetry */}
        <div className="flex items-center gap-3.5">
          <div className="flex items-center gap-2.5">
            <div className="h-8 w-8 rounded-lg bg-zinc-900 border border-zinc-700/80 flex items-center justify-center text-zinc-100 shadow-inner">
              <Terminal className="h-4 w-4 text-blue-400" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-sm tracking-tight text-zinc-100">
                  SURATJALAN<span className="text-blue-400">.AI</span>
                </span>
                <Badge variant="outline" className="text-[10px] border-zinc-800 text-zinc-400 font-medium">
                  AIC-v1.0
                </Badge>
              </div>
            </div>
          </div>

          <Separator orientation="vertical" className="h-5 hidden md:block" />

          {/* Subtitle / Department */}
          <div className="hidden lg:flex items-center gap-2 text-xs text-zinc-400">
            <span className="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-[11px] text-zinc-400 font-medium">
              AUDIT ENGINE ACTIVE // INDONESIAN SUPPLY CHAINS
            </span>
          </div>
        </div>

        {/* Center: Command Palette Trigger */}
        <div className="flex-1 max-w-md hidden md:block">
          <button
            onClick={onOpenCommandBar}
            className="w-full flex items-center justify-between px-3 py-1.5 rounded-lg bg-zinc-900/80 border border-zinc-800 text-xs text-zinc-400 hover:text-zinc-200 hover:border-zinc-700 transition-all shadow-inner group"
          >
            <div className="flex items-center gap-2">
              <Search className="w-3.5 h-3.5 text-zinc-500 group-hover:text-zinc-300 transition-colors" />
              <span>Cari dokumen, skenario, atau perintah...</span>
            </div>
            <div className="flex items-center gap-1 text-[10px] text-zinc-500 font-medium">
              <kbd className="px-1.5 py-0.5 rounded bg-zinc-800 border border-zinc-700 text-zinc-300">⌘K</kbd>
            </div>
          </button>
        </div>

        {/* Right: Telemetry & Actions */}
        <div className="flex items-center gap-2.5">
          {/* Latency badge */}
          <div className="hidden sm:flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-zinc-900 border border-zinc-800 text-[11px] font-medium text-zinc-300">
            <Activity className="w-3 h-3 text-emerald-400" />
            <span>{latencyMs}ms</span>
          </div>

          {/* AI Engine Switcher */}
          <Button
            variant="outline"
            size="xs"
            onClick={onToggleModel}
            className="text-[11px] font-medium h-7 gap-1.5 border-zinc-800 bg-zinc-900/80 text-zinc-300 hover:bg-zinc-800"
            title="Toggle Live Gemini Flash / Zero-Config Engine"
          >
            <span className={`h-1.5 w-1.5 rounded-full ${isLiveModel ? 'bg-emerald-400' : 'bg-blue-400'}`} />
            <span>{isLiveModel ? 'Gemini 2.0 Flash' : 'Hybrid VLM'}</span>
          </Button>

          {/* Quick ERP Sync Button */}
          <Button
            variant="tactical"
            size="xs"
            onClick={onOpenExport}
            className="font-semibold text-[11px] h-7 gap-1 shadow-none bg-blue-600 hover:bg-blue-500"
          >
            <span>ERP Gateway</span>
            <ArrowUpRight className="w-3 h-3" />
          </Button>
        </div>

      </div>
    </header>
  );
};
