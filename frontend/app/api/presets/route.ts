import { NextResponse } from 'next/server';
import { PRESETS } from '@/lib/mockData';

export async function GET() {
  return NextResponse.json(PRESETS);
}
