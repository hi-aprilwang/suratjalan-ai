# 📋 SuratJalan.AI — COMPFEST 18 AIC Submission & Deliverables Checklist

> **Competition**: COMPFEST 18 AI Innovation Challenge (AIC) — Fasilkom Universitas Indonesia  
> **Theme**: *AI for the Backbone of the Economy*  
> **Pillar**: *Smart Logistics (Gudang, Distribusi & Pergerakan Barang)*  
> **Innovation Title**: **SuratJalan.AI (ResiVision)** — *AI-Powered Proof-of-Delivery Audit & Instant Invoice Reconciliation Engine for Indonesian Supply Chains*

---

## 📊 Summary of Required Deliverables & Scoring Weights

| Deliverable Item | Scoring Weight | Target Format | Public / Access |
| :--- | :---: | :--- | :--- |
| **1. Public GitHub Repository** | 25% (Tech & Architecture) + 15% (MVP Readiness) | GitHub Repo URL | **Public** |
| **2. Proposal Document** | 15% (Proposal) + 20% (Originality) + 10% (Theme) | PDF (Max 20 pages) | Direct File / Cloud Link |
| **3. Video Proof of Work (PoW)** | Part of Technical Evaluation | YouTube Video (Max 7 mins) | **Unlisted** |
| **4. Video Promosi Inovasi** | 15% (Promotion Video) | YouTube Video (Max 5 mins) | **Public** |
| **5. Bonus Points Package** | **+5.0% Bonus** | Proposal & UI Sections | Included in Docs & App |

---

## 📦 1. Public GitHub Repository Checklist (Weight: 25% + 15%)

- [x] **Standalone Public Repository**:
  - Repo URL: `https://github.com/hi-aprilwang/suratjalan-ai`
- [x] **0-Config Local Reproducibility**:
  - [x] `docker-compose.yml` configured for 1-command startup (`docker compose up --build`)
  - [x] Offline high-fidelity deterministic fallback engine (app runs 100% without external API keys)
  - [x] Clear setup instructions for both Docker and local development in `README.md`
- [x] **Modular Architecture & Clean Code**:
  - [x] Frontend (`frontend/`): Next.js 16 + React 19 + TypeScript + Tailwind CSS
  - [x] Backend (`backend/`): FastAPI + Pydantic v2 + Pillow
  - [x] AI Engine (`backend/app/services/`): Google Gemini 2.0 Flash VLM with spatial bounding-box grounding
  - [x] Synthetic Generator (`synthetic_generator/`): Indonesian Surat Jalan document synthesis pipeline
- [x] **Git Hygiene & Conventional Commits**:
  - [x] Commits follow standard format: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`
  - [x] Clean `.gitignore` (no `.env`, `node_modules`, `venv`, or `.pyc` tracked)
- [x] **Pre-loaded Indonesian Presets**:
  - [x] Preset 1: PT Indofood CBP Sukses Makmur (100% Matched -> Approved)
  - [x] Preset 2: PT Mayora Indah (8 Wet Cartons Returned -> Flagged Claim IDR 1,440,000)
  - [x] Preset 3: PT Sayap Mas Utama / Wings Group (Damaged Items + Missing Stamp -> Rejected Claim IDR 2,780,000)
- [x] **Enterprise ERP Export Integrations**:
  - [x] SAP S/4HANA BAPI JSON payload generator
  - [x] Odoo ERP Stock Picking payload generator
  - [x] Jurnal.id Auto Debit Memo integration

---

## 📄 2. Proposal Document Checklist (Weight: 45% Combined)

- [ ] **Document Format & Restrictions**:
  - [ ] Format: Single PDF file (`.pdf`)
  - [ ] Page Limit: Maximum **20 pages** (excluding Cover Page and Table of Contents)
  - [ ] Language: Bahasa Indonesia or English (professional tone)
- [ ] **Section 1: Identitas & Executive Summary**:
  - [ ] Nama Tim & Data Anggota (Nama Lengkap, Institusi, Kontak)
  - [ ] Judul Inovasi & Tagline
  - [ ] Executive Summary (1-page snapshot of the Indonesian supply chain crisis & SuratJalan.AI solution)
- [ ] **Section 2: Latar Belakang & Urgensi (Indonesian Problem Context)**:
  - [ ] The 3-ply carbon paper *Surat Jalan* bottleneck in Indonesia
  - [ ] 14–30 day invoice delays causing MSME working capital freeze
  - [ ] FMCG DC check-in friction (Indomaret DC, Alfamart DC, Hypermart)
- [ ] **Section 3: Solusi & Orisinalitas Inovasi**:
  - [ ] Multimodal VLM with spatial coordinate grounding (`[ymin, xmin, ymax, xmax]`)
  - [ ] Handwritten strikethrough detection + physical warehouse stamp verification
  - [ ] Automatic IDR claim calculation vs Purchase Order baseline
- [ ] **Section 4: Metodologi & Arsitektur Teknis**:
  - [ ] System Architecture Diagram (FE, BE, Gemini VLM, ERP Dispatcher)
  - [ ] Data pipeline & synthetic data augmentation methodology
  - [ ] Discrepancy math & deterministic validation logic
- [ ] **Section 5: Analisis Kelayakan, Model Bisnis & Unit Economics (+3.5% Bonus)**:
  - [ ] Unit Economics Table (Cost per document: Rp 2.4 vs Rp 3,500 manual entry)
  - [ ] B2B SaaS pricing model (Tiered per-audit or enterprise volume subscription)
  - [ ] Target market sizing (3PL freight carriers, FMCG principals, distributor networks)
- [ ] **Section 6: Tata Kelola AI Etis, Privasi & Keamanan (AI Governance Bonus)**:
  - [ ] Data privacy: Enterprise PII redaction and secure in-memory processing
  - [ ] Human-in-the-loop (HITL) audit verification for high-risk claims
  - [ ] Model bias mitigation across diverse handwriting and physical stamp ink conditions

---

## 🎥 3. Video Proof of Work (PoW) Checklist (Unlisted YouTube)

- [ ] **Format & Specifications**:
  - [ ] Maximum Duration: **7 minutes**
  - [ ] Privacy Setting: **Unlisted** (bisa diakses via link)
  - [ ] Title Format: `COMPFEST 18 AIC: PROOF OF WORK - [Nama Tim] - SuratJalan.AI`
  - [ ] **STRICT RULE**: **NO CUTS / EDIT CUTS** during the technical execution sequence (Fast-forwarding & voiceover / narration are allowed).
- [ ] **Screen Layout & Visual Elements**:
  - [ ] Split screen or visible layout showing:
    - [ ] Terminal running Docker / startup commands and live backend logs
    - [ ] Web Browser workstation UI (`http://localhost:3000`)
    - [ ] **Visible Real-Time System Clock** (Windows taskbar clock / digital widget)
- [ ] **Demonstration Flow**:
  - [ ] 1. Clone repo & launch via `docker compose up --build` (or start backend & frontend)
  - [ ] 2. Open `http://localhost:3000` on browser
  - [ ] 3. Run Preset 1 (Indofood Clean Match -> Approved)
  - [ ] 4. Run Preset 2 (Mayora Return Discrepancy -> Show spatial bounding boxes on canvas & claim math)
  - [ ] 5. Run Preset 3 (Wings Group Missing Stamp -> Rejected alert)
  - [ ] 6. Trigger ERP Export modal (demonstrate SAP / Odoo / Jurnal.id JSON payload dispatch)

---

## 🎬 4. Video Promosi Inovasi Checklist (Public YouTube, Max 5 Mins)

- [ ] **Format & Specifications**:
  - [ ] Maximum Duration: **5 minutes**
  - [ ] Privacy Setting: **Public**
  - [ ] Title Format: `COMPFEST 18 AIC: [Nama Tim] - SuratJalan.AI`
  - [ ] Description: Include brief project summary, team members, and GitHub repository link
- [ ] **Content & Storyboard Structure**:
  - [ ] **0:00 - 1:00 (The Hook & Indonesian Problem)**:
    - Indonesian logistics reality: delivery trucks queuing at DCs, stacks of crumpled carbon *Surat Jalan*, 30-day invoice delays.
  - [ ] **1:00 - 2:30 (Introducing SuratJalan.AI & Solution)**:
    - What is SuratJalan.AI? Explain Gemini 2.0 Flash VLM + Spatial Grounding + Automated Reconciliation.
  - [ ] **2:30 - 3:45 (Product Walkthrough / UI Highlights)**:
    - Crisp showcase of the interactive workstation UI, hoverable bounding boxes, instant discrepancy claims.
  - [ ] **3:45 - 4:30 (Business Value & Economic Impact)**:
    - >99.9% cost reduction (Rp 2.4/doc), instant cash flow clearance for Indonesian MSMEs.
  - [ ] **4:30 - 5:00 (Vision & Closing Call-to-Action)**:
    - Aligned with COMPFEST 18 theme: *AI for the Backbone of the Economy* `#EncloseTheGap`.

---

## 🏆 5. Bonus Points Checklist (+5.0% Total)

- [x] **Realistic Unit Economics & ROI Impact (+3.5%)**:
  - Documented in Proposal & `README.md` comparing manual audit vs AI audit.
- [x] **Responsible AI & Governance (+3.5%)**:
  - Documented in Proposal & Architecture docs (HITL, explainability with spatial bounding boxes).
- [ ] **AIC Talks Attendance (+1.5%)**:
  - Team presence confirmed during official COMPFEST 18 AIC Talks webinar session.

---

## 🚀 6. Final Pre-Submission Validation

- [ ] Verify GitHub repository is set to **Public** and accessible without login.
- [ ] Test YouTube video links in an incognito / private browser window:
  - [ ] Proof of Work video link (Unlisted) plays properly with clear audio.
  - [ ] Promosi video link (Public) is live.
- [ ] Ensure Proposal PDF file size complies with submission upload limits (< 20MB).
- [ ] Double-check all team member information (Nama, NIM/NIK, Email, No. HP, Universitas) on the official COMPFEST submission portal.
