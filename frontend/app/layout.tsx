import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SuratJalan.AI • AI Proof-of-Delivery Audit & Invoice Reconciliation",
  description: "Multimodal AI platform converting physical, handwritten Indonesian Surat Jalan (POD) into instant verified digital invoice clearances. Built for COMPFEST 18 AIC.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="id" className="dark h-full antialiased">
      <body className="min-h-full flex flex-col bg-slate-950 text-slate-100">{children}</body>
    </html>
  );
}
