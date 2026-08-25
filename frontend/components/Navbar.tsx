'use client';

import React from 'react';
import { Search, Terminal, ArrowUpRight, Activity } from 'lucide-react';
import { Button } from './ui/button';
import { ThemeToggle } from './ThemeToggle';

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
    <header className="sticky top-0 z-40 w-full border-b border-zinc-200/80 dark:border-zinc-800/80 bg-white/95 dark:bg-zinc-950/95 backdrop-blur-md transition-colors duration-200">
      <div className="max-w-[1600px] mx-auto px-6 sm:px-8 h-18 flex items-center justify-between gap-6">
        
        {/* Left: Brand */}
        <div className="flex items-center gap-3.5">
          <div className="h-10 w-10 rounded-xl bg-zinc-100 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-700/80 flex items-center justify-center text-zinc-900 dark:text-zinc-100 shadow-xs">
            <Terminal className="h-5 w-5 text-blue-600 dark:text-blue-400" />
          </div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-lg tracking-tight text-zinc-900 dark:text-zinc-100">
              SURATJALAN<span className="text-blue-600 dark:text-blue-400">.AI</span>
            </span>
          </div>
        </div>

        {/* Center: Command Palette Trigger */}
        <div className="flex-1 max-w-lg hidden md:block">
          <button
            onClick={onOpenCommandBar}
            className="w-full flex items-center justify-between px-4 py-2.5 rounded-xl bg-zinc-50 dark:bg-zinc-900/80 border border-zinc-200 dark:border-zinc-800 text-sm text-zinc-500 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-200 hover:border-zinc-300 dark:hover:border-zinc-700 transition-all shadow-xs group"
          >
            <div className="flex items-center gap-2.5">
              <Search className="w-4 h-4 text-zinc-400 dark:text-zinc-500 group-hover:text-zinc-600 dark:group-hover:text-zinc-300 transition-colors" />
              <span>Cari dokumen, skenario, atau perintah...</span>
            </div>
            <div className="flex items-center gap-1 text-sm text-zinc-400 font-medium">
              <kbd className="px-2 py-0.5 rounded-md bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 text-zinc-600 dark:text-zinc-300 text-sm shadow-2xs">⌘K</kbd>
            </div>
          </button>
        </div>

        {/* Right: Telemetry & Actions */}
        <div className="flex items-center gap-3">
          {/* Latency badge */}
          <div className="hidden sm:flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-zinc-50 dark:bg-zinc-900 border border-zinc-200 dark:border-zinc-800 text-sm font-medium text-zinc-600 dark:text-zinc-300">
            <Activity className="w-4 h-4 text-emerald-500 dark:text-emerald-400" />
            <span>{latencyMs}ms</span>
          </div>

          {/* AI Engine Switcher */}
          <Button
            variant="outline"
            size="sm"
            onClick={onToggleModel}
            className="text-sm font-medium h-10 px-3.5 gap-2 border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900/80 text-zinc-700 dark:text-zinc-300 hover:bg-zinc-50 dark:hover:bg-zinc-800 rounded-lg"
            title="Toggle Live Gemini Flash / Zero-Config Engine"
          >
            <span className={`h-2 w-2 rounded-full ${isLiveModel ? 'bg-emerald-500 dark:bg-emerald-400' : 'bg-blue-500 dark:bg-blue-400'}`} />
            <span>{isLiveModel ? 'Gemini 2.0 Flash' : 'Hybrid VLM'}</span>
          </Button>

          {/* Light / Dark Mode Toggle Switch */}
          <ThemeToggle />

          {/* Quick ERP Sync Button */}
          <Button
            variant="tactical"
            size="sm"
            onClick={onOpenExport}
            className="font-semibold text-sm h-10 px-4 gap-2 rounded-lg shadow-sm bg-blue-600 hover:bg-blue-500 text-white"
          >
            <span>ERP Gateway</span>
            <ArrowUpRight className="w-4 h-4" />
          </Button>
        </div>

      </div>
    </header>
  );
};
