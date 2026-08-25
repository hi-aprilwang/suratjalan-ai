import os
import math
from PIL import Image, ImageDraw, ImageFont

def get_font(size=14, bold=False):
    # Try system fonts on macOS
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Geneva.ttf"
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_stamp(draw, center_x, center_y, text_top, text_mid, text_bot, color=(30, 60, 180, 210), radius=55):
    # Draw double circular stamp with rotation texture
    draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], outline=color, width=3)
    draw.ellipse([center_x - radius + 5, center_y - radius + 5, center_x + radius - 5, center_y + radius - 5], outline=color, width=1)
    
    font_s = get_font(10, bold=True)
    font_m = get_font(13, bold=True)
    
    # Text inside stamp
    draw.text((center_x, center_y - 28), text_top, fill=color, font=font_s, anchor="mm")
    draw.text((center_x, center_y), text_mid, fill=color, font=font_m, anchor="mm")
    draw.text((center_x, center_y + 26), text_bot, fill=color, font=font_s, anchor="mm")

def draw_signature(draw, start_x, start_y, color=(20, 30, 80, 220)):
    # Draw realistic cursive signature path
    points = [
        (start_x, start_y + 20),
        (start_x + 15, start_y - 10),
        (start_x + 25, start_y + 15),
        (start_x + 40, start_y - 15),
        (start_x + 55, start_y + 5),
        (start_x + 70, start_y - 5),
        (start_x + 95, start_y + 12),
        (start_x + 120, start_y - 8),
        (start_x + 140, start_y + 15),
    ]
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=color, width=2)
    # underline flourish
    draw.line([(start_x + 10, start_y + 25), (start_x + 150, start_y + 20)], fill=color, width=2)

def generate_preset_1(output_path):
    # Indofood Clean Delivery
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(252, 252, 248))
    draw = ImageDraw.Draw(img)
    
    # Outer border
    draw.rectangle([30, 30, W - 30, H - 30], outline=(180, 180, 180), width=2)
    
    # Header
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    
    draw.text((50, 50), "PT INDOFOOD CBP SUKSES MAKMUR TBK", fill=(20, 20, 20), font=font_h1)
    draw.text((50, 80), "Divisi Logistik & Distribusi Nasional - Cikarang Plant", fill=(90, 90, 90), font=font_text)
    draw.text((50, 100), "Jl. Raya Cikarang Cibarusah KM 40, Bekasi, Jawa Barat", fill=(90, 90, 90), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN / POD", fill=(10, 40, 140), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: SJ/ICBP/2026/08/9481", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(40, 40, 40), width=2)
    
    # Delivery info block
    draw.rectangle([50, 150, 480, 240], outline=(200, 200, 200), width=1)
    draw.text((60, 158), "TUJUAN PENGIRIMAN (RECEIVER):", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "PT SUMBER ALFARIA TRIJAYA TBK (ALFAMART DC)", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "DC Cikokol - Jl. MH Thamrin No. 9, Cikokol, Tangerang", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "No. PO Pelanggan: PO-WHS-2026-881", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(200, 200, 200), width=1)
    draw.text((510, 158), "INFORMASI ARMADA & DRIVER:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "No. Polisi Truk : B 9421 UXZ (CDD Box)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Nama Sopir      : Budi Santoso (PT Surya Logistik)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Waktu Berangkat : 25/08/2026 - 06:30 WIB", fill=(60, 60, 60), font=font_text)
    
    # Table Header
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(235, 240, 250), outline=(150, 150, 150), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "KODE / NAMA BARANG", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY KIRIM", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "QTY TERIMA", fill=(20, 20, 20), font=font_text_b)
    draw.text((810, y_table + 8), "CATATAN / STATUS", fill=(20, 20, 20), font=font_text_b)
    
    # Table Rows
    items = [
        ("1", "INDOMIE GORENG SPESIAL 85G (KARTON @40 PCS)", "50", "KARTON", "50", "Kondisi Baik - Segel Utuh", 125000),
        ("2", "CHITATO SAPI PANGGANG 68G (KARTON @30 PCS)", "30", "KARTON", "30", "Kondisi Baik", 210000),
        ("3", "POP MIE KUAH AYAM BAWANG 75G (KARTON @24 PCS)", "40", "KARTON", "40", "Kondisi Baik", 145000),
        ("4", "INDOFOOD KECAP MANIS POUCH 520ML (DUS @12 PCS)", "25", "DUS", "25", "Kondisi Baik", 180000),
        ("5", "BUMBU RACIK AYAM GORENG (DUS @120 PCS)", "20", "DUS", "20", "Kondisi Baik", 240000),
    ]
    
    row_y = y_table + 32
    for item in items:
        draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(210, 210, 210), width=1)
        draw.text((70, row_y + 12), item[0], fill=(40, 40, 40), font=font_text)
        draw.text((120, row_y + 12), item[1], fill=(20, 20, 20), font=font_text_b)
        draw.text((500, row_y + 12), item[2], fill=(20, 20, 20), font=font_text)
        draw.text((600, row_y + 12), item[3], fill=(70, 70, 70), font=font_text)
        # Handwritten check / received qty
        draw.text((700, row_y + 10), item[4] + " ✓", fill=(10, 30, 140), font=get_font(15, bold=True))
        draw.text((810, row_y + 12), item[5], fill=(30, 120, 40), font=font_text)
        row_y += 40
        
    # Blank filler rows
    for _ in range(4):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    # Summary Box
    draw.rectangle([50, row_y + 20, W - 50, row_y + 100], outline=(190, 190, 190), fill=(248, 248, 248), width=1)
    draw.text((65, row_y + 30), "TOTAL BARANG DIKIRIM : 165 KARTON/DUS", fill=(20, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "TOTAL BARANG DITERIMA : 165 KARTON/DUS (100% SESUAI PO)", fill=(20, 120, 30), font=font_text_b)
    draw.text((65, row_y + 75), "Keterangan: Barang diterima lengkap dalam keadaan bersih dan tersegel.", fill=(90, 90, 90), font=font_text)
    
    # Signatures & Stamps
    sig_y = row_y + 130
    draw.text((120, sig_y), "PENGIRIM / SOPIR", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Budi Santoso )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "PETUGAS GUDANG DC", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( Agus Hendra )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "STEMPEL & VERIFIKASI DC", fill=(50, 50, 50), font=font_text_b)
    draw_stamp(draw, 840, sig_y + 65, "PT SUMBER ALFARIA TRIJAYA", "DITERIMA DC", "25 AGT 2026 - CIKOKOL", color=(25, 55, 175, 230), radius=52)
    
    img.save(output_path, "PNG")
    print(f"Generated clean delivery preset: {output_path}")

def generate_preset_2(output_path):
    # Mayora Partial Return / Discrepancy
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(254, 252, 245))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(170, 170, 170), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT MAYORA INDAH TBK", fill=(180, 20, 20), font=font_h1)
    draw.text((50, 80), "Supply Chain & Logistics Center - Tangerang", fill=(80, 80, 80), font=font_text)
    draw.text((50, 100), "Jl. Telesonic Ujung No. 10, Jatake, Tangerang", fill=(80, 80, 80), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN PENGIRIMAN", fill=(180, 20, 20), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: MYR-LOG-JKT-2026-4421", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(180, 30, 30), width=2)
    
    # Destination
    draw.rectangle([50, 150, 480, 240], outline=(200, 200, 200), width=1)
    draw.text((60, 158), "KEPADA YTH (DISTRIBUTION CENTER):", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "PT INDOMARCO PRISMATAMA (INDOMARET)", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "DC Ancol Barat No. 8, Pademangan, Jakarta Utara", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "Nomor PO: PO-IDM-2026-1049", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(200, 200, 200), width=1)
    draw.text((510, 158), "EKSPEDISI & KENDARAAN:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "Nopol Truk: B 9081 PQR (Fuso Box 8 Ton)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Driver    : Hendra Gunawan", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Gate/Slot : Dock 04 - Masuk: 08:15 WIB", fill=(60, 60, 60), font=font_text)
    
    # Table Header
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(255, 240, 240), outline=(180, 150, 150), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "NAMA PRODUK", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY KIRIM", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "QTY FISIK DITERIMA", fill=(20, 20, 20), font=font_text_b)
    draw.text((830, y_table + 8), "KETERANGAN RETUR", fill=(20, 20, 20), font=font_text_b)
    
    row_y = y_table + 32
    # Row 1: Roma Kelapa
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "1", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "ROMA BISKUIT KELAPA 300G (DUS @24)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "100", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "100 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 2: Beng Beng (Discrepancy: 60 ordered, 52 received, 8 damaged/wet)
    draw.rectangle([50, row_y, W - 50, row_y + 50], fill=(255, 245, 235), outline=(220, 150, 150), width=1)
    draw.text((70, row_y + 15), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 15), "BENG BENG REGULAR 20x20G (DUS @12 BOX)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 15), "60", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 15), "DUS", fill=(70, 70, 70), font=font_text)
    
    # Handwritten strike-through and correction
    draw.line([(695, row_y + 22), (725, row_y + 22)], fill=(200, 20, 20), width=2)
    draw.text((700, row_y + 12), "60", fill=(120, 120, 120), font=font_text)
    draw.text((735, row_y + 8), "52", fill=(180, 20, 20), font=get_font(18, bold=True))
    draw.text((830, row_y + 10), "RETUR 8 DUS (KARDUS BASAH)", fill=(190, 20, 20), font=get_font(11, bold=True))
    draw.text((830, row_y + 28), "Sopir bawa kembali", fill=(120, 30, 30), font=get_font(10))
    row_y += 50
    
    # Row 3: Torabika Cappuccino
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "3", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "TORABIKA CAPPUCCINO 10x25G (DUS @10 RCG)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "50", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "50 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 4: Kopiko Candy
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "4", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "KOPIKO COFFEE CANDY 150G (DUS @24 BAG)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "40", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "40 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Filler rows
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    # Handwritten Discrepancy Note Block
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 80, 80), fill=(255, 248, 248), width=2)
    draw.text((65, row_y + 30), "PERNYATAAN SELISIH & RETUR GUDANG :", fill=(180, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Telah diterima 242 Dus dari total 250 Dus yang dikirim.", fill=(30, 30, 30), font=font_text)
    draw.text((65, row_y + 75), "Selisih 8 Dus Beng Beng diretur langsung ke pabrik karena kemasan basah saat pembongkaran.", fill=(160, 20, 20), font=font_text_b)
    
    # Signatures & Stamps
    sig_y = row_y + 140
    draw.text((120, sig_y), "PENGEMUDI / SOPIR", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Hendra Gunawan )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "CHECKER DC INDOMARET", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( Wahyu Purnomo )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "STEMPEL INDOMARET DC", fill=(50, 50, 50), font=font_text_b)
    draw_stamp(draw, 840, sig_y + 65, "INDOMARCO PRISMATAMA", "DC ANCOL", "TERIMA SEBAGIAN / RETUR", color=(180, 30, 30, 230), radius=54)
    
    img.save(output_path, "PNG")
    print(f"Generated discrepancy delivery preset: {output_path}")

def generate_preset_3(output_path):
    # Wings Group Critical Damage & Incomplete Stamp
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(250, 252, 252))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(170, 170, 170), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT SAYAP MAS UTAMA (WINGS GROUP)", fill=(10, 80, 150), font=font_h1)
    draw.text((50, 80), "Consumer Goods Logistics & Distribution Hub", fill=(80, 80, 80), font=font_text)
    draw.text((50, 100), "Jl. Tipar Cakung Kav. F 5-7, Cakung Barat, Jakarta Timur", fill=(80, 80, 80), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN EKSPEDISI", fill=(10, 80, 150), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: SJ-SMU-2026-7890", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(10, 80, 150), width=2)
    
    draw.rectangle([50, 150, 480, 240], outline=(200, 200, 200), width=1)
    draw.text((60, 158), "PENERIMA BARANG (STORE):", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "HYPERMART SUPERMAL KARAWACI", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "Lantai LG, Supermal Karawaci, Tangerang", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "No. PO: PO-HYP-2026-3120", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(200, 200, 200), width=1)
    draw.text((510, 158), "DATA ARMADA:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "Nopol Truk: B 9552 WXY (Engkel Box)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Driver    : Dedi Kusnadi", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Ekspedisi : Logisly Express", fill=(60, 60, 60), font=font_text)
    
    # Table
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(235, 245, 255), outline=(160, 180, 210), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "ITEM BARANG", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY PO", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "TERIMA FISIK", fill=(20, 20, 20), font=font_text_b)
    draw.text((830, y_table + 8), "CATATAN CHECKER", fill=(20, 20, 20), font=font_text_b)
    
    row_y = y_table + 32
    # Row 1: SoKlin Liquid (Discrepancy: 80 sent, 74 good, 6 leaked/damaged)
    draw.rectangle([50, row_y, W - 50, row_y + 48], fill=(255, 245, 245), outline=(220, 180, 180), width=1)
    draw.text((70, row_y + 14), "1", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 14), "SO KLIN LIQUID DETERGENT 750ML (DUS @12)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 14), "80", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 14), "DUS", fill=(70, 70, 70), font=font_text)
    draw.line([(695, row_y + 20), (725, row_y + 20)], fill=(200, 20, 20), width=2)
    draw.text((700, row_y + 10), "80", fill=(120, 120, 120), font=font_text)
    draw.text((735, row_y + 8), "74", fill=(180, 20, 20), font=get_font(18, bold=True))
    draw.text((830, row_y + 10), "6 DUS BOCOR/HANCUR", fill=(190, 20, 20), font=get_font(11, bold=True))
    row_y += 48
    
    # Row 2: Nuvo Family (Clean: 50)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "NUVO FAMILY SABUN BATANG 110G (DUS @72)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "50", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "50 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 3: Ale Ale (Discrepancy: 100 sent, 90 received, 10 dented/rejected)
    draw.rectangle([50, row_y, W - 50, row_y + 48], fill=(255, 245, 245), outline=(220, 180, 180), width=1)
    draw.text((70, row_y + 14), "3", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 14), "ALE-ALE MINUMAN RASA JERUK 200ML (DUS @24)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 14), "100", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 14), "DUS", fill=(70, 70, 70), font=font_text)
    draw.line([(695, row_y + 20), (730, row_y + 20)], fill=(200, 20, 20), width=2)
    draw.text((700, row_y + 10), "100", fill=(120, 120, 120), font=font_text)
    draw.text((740, row_y + 8), "90", fill=(180, 20, 20), font=get_font(18, bold=True))
    draw.text((830, row_y + 10), "10 DUS PENYOK/RETUR", fill=(190, 20, 20), font=get_font(11, bold=True))
    row_y += 48
    
    # Filler rows
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    # Discrepancy Alert Box
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 50, 50), fill=(255, 245, 245), width=2)
    draw.text((65, row_y + 30), "BERITA ACARA KERUSAKAN BARANG SAAT SERAH TERIMA :", fill=(200, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Ditemukan 6 Dus SoKlin kemasan pecah bocor dan 10 Dus Ale-Ale penyok parah.", fill=(40, 40, 40), font=font_text)
    draw.text((65, row_y + 75), "Barang rusak tidak diterima oleh pihak Hypermart. Faktur tagihan wajib dipotong.", fill=(180, 20, 20), font=font_text_b)
    
    # Signatures (Note: missing stamp)
    sig_y = row_y + 140
    draw.text((120, sig_y), "DRIVER LOGISLY", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Dedi Kusnadi )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "STORE RECEIVING HYPERMART", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( Rahmat Hidayat )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "STEMPEL TOKO (BELUM DICAP)", fill=(180, 50, 50), font=font_text_b)
    draw.rectangle([760, sig_y + 30, 920, sig_y + 110], outline=(200, 100, 100), fill=(255, 240, 240), width=1)
    draw.text((840, sig_y + 70), "[ STEMPEL MISSING ]", fill=(180, 50, 50), font=font_text_b, anchor="mm")
    
    img.save(output_path, "PNG")
    print(f"Generated damaged delivery preset: {output_path}")

if __name__ == "__main__":
    out_dir = "/Users/okihita/WebstormProjects/suratjalan-ai/datasets/samples"
    os.makedirs(out_dir, exist_ok=True)
    generate_preset_1(os.path.join(out_dir, "preset_1_indofood_clean.png"))
    generate_preset_2(os.path.join(out_dir, "preset_2_mayora_discrepancy.png"))
    generate_preset_3(os.path.join(out_dir, "preset_3_wings_damage_alert.png"))
    print("All presets generated successfully.")
