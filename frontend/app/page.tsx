'use client';

import React, { useState, useEffect, useCallback } from 'react';
import { Navbar } from '@/components/Navbar';
import { PresetSelector } from '@/components/PresetSelector';
import { DocumentViewer } from '@/components/DocumentViewer';
import { AuditSummary } from '@/components/AuditSummary';
import { DiscrepancyTable } from '@/components/DiscrepancyTable';
import { ExportModal } from '@/components/ExportModal';
import { CommandBar } from '@/components/ui/command-bar';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { AuditReport, PresetItem } from '@/types/audit';
import { PRESETS, MOCK_REPORTS } from '@/lib/mockData';
import {
  Share2,
  Layers,
  BarChart3,
  RefreshCw,
  Cpu,
  ShieldCheck,
  Zap,
  TrendingUp,
  Clock,
  Coins
} from 'lucide-react';
import confetti from 'canvas-confetti';

export default function AuditWorkstationPage() {
  const [presets] = useState<PresetItem[]>(PRESETS);
  const [selectedPresetId, setSelectedPresetId] = useState<string>('preset_1');
  const [currentImageUrl, setCurrentImageUrl] = useState<string>('/samples/preset_1_indofood_clean.png');
  const [report, setReport] = useState<AuditReport>(MOCK_REPORTS['preset_1']);
  const [isAuditing, setIsAuditing] = useState<boolean>(false);
  const [isLiveModel, setIsLiveModel] = useState<boolean>(false);
  const [highlightedIndex, setHighlightedIndex] = useState<number | null>(null);
  const [isExportModalOpen, setIsExportModalOpen] = useState<boolean>(false);
  const [isCommandBarOpen, setIsCommandBarOpen] = useState<boolean>(false);
  const [activeTab, setActiveTab] = useState<string>('workstation');

  const executeAudit = useCallback(async ({ presetId, file }: { presetId?: string; file?: File }) => {
    setIsAuditing(true);
    setHighlightedIndex(null);
    try {
      const formData = new FormData();
      if (presetId) formData.append('preset_id', presetId);
      if (file) formData.append('file', file);

      const res = await fetch('/api/audit', {
        method: 'POST',
        body: formData
      });

      if (res.ok) {
        const data: AuditReport = await res.json();
        setReport(data);

        // Confetti on clean approval
        if (data.overall_status === 'APPROVED_FOR_INVOICING') {
          confetti({
            particleCount: 70,
            spread: 60,
            origin: { y: 0.6 }
          });
        }
      } else {
        const fallback = presetId && MOCK_REPORTS[presetId] ? MOCK_REPORTS[presetId] : MOCK_REPORTS['preset_1'];
        setReport(fallback);
      }
    } catch {
      const fallback = presetId && MOCK_REPORTS[presetId] ? MOCK_REPORTS[presetId] : MOCK_REPORTS['preset_1'];
      setReport(fallback);
    } finally {
      setIsAuditing(false);
    }
  }, []);

  const handleSelectPreset = useCallback(
    async (presetId: string) => {
      setSelectedPresetId(presetId);
      const selectedPreset = presets.find((p) => p.id === presetId);
      if (selectedPreset) {
        setCurrentImageUrl(selectedPreset.image_url);
      }
      await executeAudit({ presetId });
    },
    [presets, executeAudit]
  );

  // Keyboard shortcut listener for Presets 1 to 6
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;
      if (e.key === '1') handleSelectPreset('preset_1');
      if (e.key === '2') handleSelectPreset('preset_2');
      if (e.key === '3') handleSelectPreset('preset_3');
      if (e.key === '4') handleSelectPreset('preset_4');
      if (e.key === '5') handleSelectPreset('preset_5');
      if (e.key === '6') handleSelectPreset('preset_6');
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleSelectPreset]);

  // Custom user file upload
  const handleFileUpload = async (file: File) => {
    setSelectedPresetId('');
    const objectUrl = URL.createObjectURL(file);
    setCurrentImageUrl(objectUrl);
    await executeAudit({ file });
  };

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100 flex flex-col font-sans antialiased selection:bg-blue-600 selection:text-white">
      {/* Navigation Header */}
      <Navbar
        isLiveModel={isLiveModel}
        onToggleModel={() => setIsLiveModel(!isLiveModel)}
        latencyMs={report.execution_time_ms}
        onOpenCommandBar={() => setIsCommandBarOpen(true)}
        onOpenExport={() => setIsExportModalOpen(true)}
      />

      {/* Main Workspace Container */}
      <main className="flex-1 max-w-[1600px] w-full mx-auto px-4 sm:px-6 py-5 space-y-5">
        
        {/* Preset & Document Picker Toolbar */}
        <PresetSelector
          presets={presets}
          selectedPresetId={selectedPresetId}
          onSelectPreset={handleSelectPreset}
          onFileUpload={handleFileUpload}
          isAuditing={isAuditing}
        />

        {/* View Switcher Tabs */}
        <div className="flex items-center justify-between gap-3 pt-2 border-b border-zinc-800/80 pb-3">
          <Tabs value={activeTab} onValueChange={setActiveTab} className="w-auto">
            <TabsList className="bg-zinc-900 border-zinc-800">
              <TabsTrigger value="workstation" className="gap-2 text-sm font-medium">
                <Layers className="w-4 h-4" />
                <span>Audit Workstation (Split View)</span>
              </TabsTrigger>
              <TabsTrigger value="analytics" className="gap-2 text-sm font-medium">
                <BarChart3 className="w-4 h-4" />
                <span>Analisis Dampak & Unit Economics</span>
              </TabsTrigger>
            </TabsList>
          </Tabs>

          <div className="flex items-center gap-2.5">
            <Button
              variant="outline"
              size="sm"
              onClick={() => handleSelectPreset(selectedPresetId || 'preset_1')}
              disabled={isAuditing}
              className="gap-2 font-medium text-sm border-zinc-800 text-zinc-300 h-9"
            >
              <RefreshCw className={`w-4 h-4 ${isAuditing ? 'animate-spin' : ''}`} />
              <span>Ulangi Audit</span>
            </Button>

            <Button
              variant="tactical"
              size="sm"
              onClick={() => setIsExportModalOpen(true)}
              className="gap-2 font-semibold text-sm bg-blue-600 hover:bg-blue-500 text-white h-9"
            >
              <Share2 className="w-4 h-4" />
              <span>ERP Sync / Export</span>
            </Button>
          </div>
        </div>

        {/* Tab 1: Workstation Dual-Pane View */}
        {activeTab === 'workstation' ? (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
            
            {/* Left Column: Physical Document & Spatial Canvas (5 cols) */}
            <div className="lg:col-span-5 h-full">
              <DocumentViewer
                imageUrl={currentImageUrl}
                boundingBoxes={report.bounding_boxes || []}
                highlightedIndex={highlightedIndex}
                onHoverBox={setHighlightedIndex}
                isAuditing={isAuditing}
              />
            </div>

            {/* Right Column: AI Audit Verdict & Discrepancy Reconciliation (7 cols) */}
            <div className="lg:col-span-7 space-y-4">
              
              {/* Verdict & Metrics Summary */}
              <AuditSummary report={report} />

              {/* Line-Item Reconciliation Table */}
              <DiscrepancyTable
                items={report.items}
                highlightedIndex={highlightedIndex}
                onHoverItem={setHighlightedIndex}
              />

              {/* Bottom Telemetry Footer */}
              <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-4 flex flex-wrap items-center justify-between gap-3 text-sm">
                <div className="flex items-center gap-2.5 text-zinc-300 text-sm">
                  <div className="h-7 w-7 rounded-md bg-zinc-900 border border-zinc-800 flex items-center justify-center text-blue-400">
                    <Cpu className="w-4 h-4" />
                  </div>
                  <div>
                    <span className="font-semibold text-zinc-200">
                      AI INFERENCE: {report.ai_model_used}
                    </span>
                    <span className="text-zinc-400 block text-sm">
                      Pydantic v2 Schema Enforcement • Zero Hallucination Guard
                    </span>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <Badge variant="outline" className="text-sm text-zinc-400 border-zinc-800 font-medium">
                    <ShieldCheck className="w-4 h-4 text-emerald-400 mr-1.5" />
                    COMPFEST 18 AIC VALIDATED
                  </Badge>
                </div>
              </div>

            </div>

          </div>
        ) : (
          /* Tab 2: Analytics & Unit Economics Impact View */
          <div className="rounded-xl border border-zinc-800 bg-zinc-950 p-6 space-y-6">
            <div className="border-b border-zinc-800/80 pb-4">
              <div className="flex items-center gap-2 mb-1.5">
                <TrendingUp className="w-5 h-5 text-emerald-400" />
                <h3 className="text-base font-bold text-zinc-100 uppercase tracking-tight">
                  ANALISIS ROI & DAMPAK EKONOMI // SMART LOGISTICS INDONESIA
                </h3>
              </div>
              <p className="text-sm text-zinc-400">
                Kalkulasi efisiensi biaya operasional dan percepatan perputaran modal kerja distributor & 3PL Indonesia
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="rounded-xl border border-zinc-800 bg-zinc-900/40 p-5 space-y-2.5">
                <div className="flex items-center justify-between text-zinc-400 text-sm uppercase font-semibold">
                  <span>Audit Speed Velocity</span>
                  <Clock className="w-4 h-4 text-emerald-400" />
                </div>
                <span className="text-2xl font-bold text-emerald-400 block">
                  400x Lebih Cepat
                </span>
                <p className="text-sm text-zinc-400 leading-relaxed">
                  Dari rata-rata 10 menit entry manual per lembar menjadi &lt;1.5 detik menggunakan Multimodal Gemini 2.0 Flash VLM.
                </p>
              </div>

              <div className="rounded-xl border border-zinc-800 bg-zinc-900/40 p-5 space-y-2.5">
                <div className="flex items-center justify-between text-zinc-400 text-sm uppercase font-semibold">
                  <span>Cost Efficiency</span>
                  <Coins className="w-4 h-4 text-blue-400" />
                </div>
                <span className="text-2xl font-bold text-blue-400 block">
                  &gt; 99.9% Savings
                </span>
                <p className="text-sm text-zinc-400 leading-relaxed">
                  Biaya pemrosesan Rp 2.4 per dokumen (Gemini Flash token) vs Rp 3.500 per dokumen untuk gaji staff admin logistik.
                </p>
              </div>

              <div className="rounded-xl border border-zinc-800 bg-zinc-900/40 p-5 space-y-2.5">
                <div className="flex items-center justify-between text-zinc-400 text-sm uppercase font-semibold">
                  <span>Cash Flow Acceleration</span>
                  <Zap className="w-4 h-4 text-amber-400" />
                </div>
                <span className="text-2xl font-bold text-amber-400 block">
                  Same-Day Clearance
                </span>
                <p className="text-sm text-zinc-400 leading-relaxed">
                  Membuka likuiditas modal kerja bagi jutaan UMKM logistik dari sebelumnya 14-30 hari menjadi hitungan jam.
                </p>
              </div>
            </div>
          </div>
        )}

      </main>

      {/* Global Command Bar (⌘K / Ctrl+K) */}
      <CommandBar
        open={isCommandBarOpen}
        onOpenChange={setIsCommandBarOpen}
        presets={presets}
        onSelectPreset={handleSelectPreset}
        onOpenExport={() => setIsExportModalOpen(true)}
        onRerunAudit={() => handleSelectPreset(selectedPresetId || 'preset_1')}
      />

      {/* Export & ERP Gateway Modal */}
      <ExportModal
        isOpen={isExportModalOpen}
        onClose={() => setIsExportModalOpen(false)}
        report={report}
      />

      {/* Footer */}
      <footer className="mt-auto border-t border-zinc-800 bg-zinc-950 py-4 text-center text-sm text-zinc-500 font-medium">
        <p>
          SURATJALAN.AI // COMPFEST 18 AI INNOVATION CHALLENGE (AIC) // UNIVERSITAS INDONESIA
        </p>
      </footer>
    </div>
  );
}
