# 📄 PROPOSAL INOVASI: SuratJalan.AI

> **Cabang Kompetisi**: AI Innovation Challenge (AIC) — COMPFEST 18  
> **Tema**: *AI for the Backbone of the Economy*  
> **Pilar**: *Smart Logistics (Gudang, Distribusi & Pergerakan Barang)*  
> **Judul Inovasi**: **SuratJalan.AI — Platform Multimodal Vision-Language Model untuk Audit Surat Jalan Fisik dan Rekonsiliasi Faktur Otomatis pada Rantai Pasok B2B Indonesia**

---

## 1. 👥 Nama Kelompok & Identitas Proyek

- **Nama Tim**: `[Nama Tim Anda]`
- **Judul Proyek**: `SuratJalan.AI (ResiVision)`
- **Kategori**: `Smart Logistics & Supply Chain Automation`
- **Repository Publik**: `https://github.com/okihita/suratjalan-ai`

---

## 2. 🔍 Latar Belakang & Urgensi Masalah

Sektor logistik dan distribusi Fast-Moving Consumer Goods (FMCG) merupakan tulang punggung ekonomi Indonesia yang bernilai lebih dari Rp1.500 triliun per tahun. Namun, **lebih dari 90% transaksi pengiriman B2B di Indonesia masih bergantung pada dokumen fisik 3-ply carbon paper *Surat Jalan* (Proof of Delivery / POD)**.

### Titik Friksi di Lapangan:
1. **Inefisiensi Audit Manual**: Staf administrasi logistik menghabiskan rata-rata 5-10 menit per lembar surat jalan untuk memeriksa stempel basah, tanda tangan, dan mencocokkan coretan tangan barang retur (*"8 dus basah"*, *"6 botol bocor"*) ke dalam sistem ERP.
2. **Keterlambatan Penagihan Faktur (14–30 Hari)**: Faktur tagihan tidak dapat diterbitkan ke pihak pembeli (principal/distributor) sebelum surat jalan fisik kembali dari perjalanan luar pulau atau selesai diaudit manual, menciptakan risiko piutang macet dan menahan arus kas jutaan UMKM pengangkut (*transporter*).
3. **Perselisihan Nilai Klaim (*Discrepancy Disputes*)**: Tulisan tangan yang buram, stempel yang tidak jelas, dan salah ketik admin sering menimbulkan perselisihan pembayaran antar pihak senilai miliaran rupiah.

---

## 3. 🎯 Tujuan dan Manfaat Pengembangan

### Tujuan:
1. Membangun model AI multimodal yang mampu mengekstraksi metadata, tabel barang, stempel legalitas, tanda tangan, dan tulisan tangan retur dari foto surat jalan dalam waktu $<1.5\text{ detik}$.
2. Mengotomatiskan rekonsiliasi antara surat jalan fisik dengan Purchase Order digital serta menghitung potongan klaim secara presisi dalam mata uang Rupiah (IDR).
3. Mempercepat penerbitan dan pembayaran faktur dari 14–30 hari menjadi *Same-Day Clearance* melalui integrasi API ERP (SAP S/4HANA, Odoo, Jurnal.id).

### Manfaat Ekonomi & Sosial:
- **Penghematan Biaya Operasional**: Menurunkan biaya pemrosesan dokumen logistik dari Rp3.500–Rp5.000 per lembar menjadi ~Rp2.4 per lembar ($>99.9\%$ efisiensi).
- **Akselerasi Arus Kas UMKM**: Membuka likuiditas modal kerja bagi 3PL carrier dan suplier lokal Indonesia.
- **Transparansi & Akuntabilitas**: Menghadirkan jejak audit visual (*visual spatial grounding*) yang objektif dan bebas kecurangan (*fraud*).

---

## 4. 🔬 Metodologi Teknis

### A. Alur Perolehan Dataset
1. **Pengumpulan Dokumen Fisik & Anotasi Realistis**:
   - Mengumpulkan format surat jalan dari ekosistem FMCG dan logistik nasional (Indofood, Mayora, Wings Group, Alfamart DC, Indomaret DC, Hypermart).
   - Melakukan sintesis data dengan variasi tulisan tangan asli Indonesia, stempel stensil/karet, coretan retur, dan augmentasi noise fisik (sudut kemiringan, lipatan kertas, noda cairan).
2. **Standardisasi Label**:
   - Format koordinat ternormalisasi $[y_{\min}, x_{\min}, y_{\max}, x_{\max}]$ pada skala $0-1000$ untuk visual grounding.

### B. Arsitektur Model Multimodal & Fine-Tuning
1. **Multimodal Vision-Language Model (Gemini 2.0 Flash VLM)**:
   - Memproses dokumen visual secara holistik tanpa memecah menjadi pipeline OCR tradisional yang terfragmentasi.
   - Menggunakan *Domain-Specific Few-Shot Prompting* dengan penegakan skema JSON Pydantic v2 untuk menjamin konsistensi matematis (zero hallucination).
2. **Spatial Grounding & Anchor Mapping**:
   - Setiap entitas teks, stempel, dan paraf dikaitkan langsung dengan koordinat bounding box pada citra asli dokumen.

### C. Alur Integrasi ke Environment Kode
- **Frontend**: Next.js 16 + React 19 + TypeScript + Tailwind CSS + Canvas Bounding-Box Overlay.
- **Backend**: FastAPI (Python 3.11) + Pydantic v2 Schemas + Pillow Image Processing.
- **Packaging**: Docker Compose multi-stage build yang dapat dijalankan secara lokal dalam 1 langkah (`docker compose up --build`).

---

## 5. 💡 Model Bisnis, Skalabilitas & Tata Kelola AI Etis

### Model Bisnis (B2B SaaS):
- **Starter (UMKM & Ekspedisi Kecil)**: Gratis 100 scan per bulan.
- **Growth (3PL Fleets)**: Rp499.000 / bulan (hingga 5.000 dokumen).
- **Enterprise (FMCG Principals & Retail DCs)**: Rp79 / dokumen dengan integrasi langsung API SAP/Odoo/Jurnal.id.

### Tata Kelola AI Etis (*Responsible AI*):
1. **Human-in-the-Loop Safeguard**: Tingkat keyakinan model di bawah $90\%$ otomatis dialihkan ke antarmuka konfirmasi manual staf logistik.
2. **Stateless Privacy**: Data identitas driver tidak disimpan permanen di memori server untuk menjaga kerahasiaan data pribadi.
