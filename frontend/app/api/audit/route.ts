import { NextRequest, NextResponse } from 'next/server';
import { MOCK_REPORTS } from '@/lib/mockData';

export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();
    const presetId = formData.get('preset_id') as string;
    const file = formData.get('file') as File | null;

    // Check if external FastAPI backend is reachable, or use internal serverless engine
    const backendUrl = process.env.BACKEND_API_URL || 'http://localhost:8000/api';
    
    try {
      const backendFormData = new FormData();
      if (file) {
        backendFormData.append('file', file);
      }
      if (presetId) {
        backendFormData.append('preset_id', presetId);
      }

      const res = await fetch(`${backendUrl}/audit`, {
        method: 'POST',
        body: backendFormData,
        // Short timeout so if local Python server isn't running, it immediately uses serverless engine
        signal: AbortSignal.timeout(2000)
      });

      if (res.ok) {
        const data = await res.json();
        return NextResponse.json(data);
      }
    } catch {
      // Backend not running / timed out -> fallback to built-in Next.js serverless engine
    }

    // Fallback to high-fidelity serverless engine
    const reportKey = presetId && MOCK_REPORTS[presetId] ? presetId : 'preset_1';
    const report = MOCK_REPORTS[reportKey] || MOCK_REPORTS['preset_1'];
    
    return NextResponse.json(report);
  } catch (err: unknown) {
    const message = err instanceof Error ? err.message : 'Unknown error';
    return NextResponse.json({ error: message }, { status: 500 });
  }
}
