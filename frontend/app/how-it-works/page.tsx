'use client';

import React from 'react';
import { Navbar } from '@/components/Navbar';
import { HowItWorks } from '@/components/HowItWorks';
import { Button } from '@/components/ui/button';
import { ArrowLeft } from 'lucide-react';
import Link from 'next/link';

export default function HowItWorksPage() {
  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-zinc-950 text-zinc-900 dark:text-zinc-100 flex flex-col font-sans antialiased selection:bg-blue-600 selection:text-white transition-colors duration-200">
      <Navbar
        isLiveModel={false}
        onToggleModel={() => {}}
        latencyMs={850}
        onOpenCommandBar={() => {}}
        onOpenExport={() => {}}
      />

      <main className="flex-1 max-w-[1600px] w-full mx-auto px-4 sm:px-6 py-6 space-y-6">
        <div className="flex items-center justify-between">
          <Link href="/">
            <Button
              variant="outline"
              size="sm"
              className="gap-2 font-medium text-sm border-zinc-300 dark:border-zinc-800 bg-white dark:bg-zinc-900 text-zinc-800 dark:text-zinc-300 h-9"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Kembali ke Audit Workstation</span>
            </Button>
          </Link>
        </div>

        <HowItWorks />
      </main>

      <footer className="mt-auto border-t border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-950 py-4 text-center text-sm text-zinc-500 font-medium transition-colors">
        <p>
          SURATJALAN.AI // COMPFEST 18 AI INNOVATION CHALLENGE (AIC) // UNIVERSITAS INDONESIA
        </p>
      </footer>
    </div>
  );
}
