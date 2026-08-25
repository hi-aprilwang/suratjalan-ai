import os
import math
from PIL import Image, ImageDraw, ImageFont

def get_font(size=14, bold=False):
    font_paths = [
        # Windows
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
        # macOS
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNSMono.ttf",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_stamp(draw, center_x, center_y, text_top, text_mid, text_bot, color=(30, 60, 180, 210), radius=55):
    # Draw double circular stamp
    draw.ellipse([center_x - radius, center_y - radius, center_x + radius, center_y + radius], outline=color, width=3)
    draw.ellipse([center_x - radius + 5, center_y - radius + 5, center_x + radius - 5, center_y + radius - 5], outline=color, width=1)
    
    font_s = get_font(10, bold=True)
    font_m = get_font(12, bold=True)
    
    draw.text((center_x, center_y - 28), text_top, fill=color, font=font_s, anchor="mm")
    draw.text((center_x, center_y), text_mid, fill=color, font=font_m, anchor="mm")
    draw.text((center_x, center_y + 26), text_bot, fill=color, font=font_s, anchor="mm")

def draw_rect_stamp(draw, x1, y1, x2, y2, text_1, text_2, text_3, color=(30, 80, 180, 220)):
    # Draw rectangular warehouse stamp
    draw.rectangle([x1, y1, x2, y2], outline=color, width=3)
    draw.rectangle([x1 + 4, y1 + 4, x2 - 4, y2 - 4], outline=color, width=1)
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    draw.text((cx, cy - 24), text_1, fill=color, font=get_font(11, bold=True), anchor="mm")
    draw.text((cx, cy), text_2, fill=color, font=get_font(14, bold=True), anchor="mm")
    draw.text((cx, cy + 24), text_3, fill=color, font=get_font(10, bold=True), anchor="mm")

def draw_triangle_stamp(draw, center_x, center_y, text_top, text_mid, text_bot, color=(200, 30, 30, 220), size=65):
    # Draw triangular reject stamp
    p1 = (center_x, center_y - size)
    p2 = (center_x - int(size * 1.15), center_y + int(size * 0.8))
    p3 = (center_x + int(size * 1.15), center_y + int(size * 0.8))
    draw.polygon([p1, p2, p3], outline=color, width=3)
    
    draw.text((center_x, center_y - 12), text_top, fill=color, font=get_font(10, bold=True), anchor="mm")
    draw.text((center_x, center_y + 10), text_mid, fill=color, font=get_font(13, bold=True), anchor="mm")
    draw.text((center_x, center_y + 32), text_bot, fill=color, font=get_font(9, bold=True), anchor="mm")

def draw_signature(draw, start_x, start_y, color=(20, 30, 80, 220)):
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
    draw.line([(start_x + 10, start_y + 25), (start_x + 150, start_y + 20)], fill=color, width=2)

# ==========================================
# PRESET 1: INDOFOOD CLEAN DELIVERY (100% MATCH)
# ==========================================
def generate_preset_1(output_path):
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(252, 252, 248))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(180, 180, 180), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT INDOFOOD CBP SUKSES MAKMUR TBK", fill=(20, 20, 20), font=font_h1)
    draw.text((50, 80), "Divisi Logistik & Distribusi Nasional - Cikarang Plant", fill=(90, 90, 90), font=font_text)
    draw.text((50, 100), "Jl. Raya Cikarang Cibarusah KM 40, Bekasi, Jawa Barat", fill=(90, 90, 90), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN / POD", fill=(10, 40, 140), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: SJ/ICBP/2026/08/9481", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(40, 40, 40), width=2)
    
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
    
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(235, 240, 250), outline=(150, 150, 150), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "KODE / NAMA BARANG", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY KIRIM", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "QTY TERIMA", fill=(20, 20, 20), font=font_text_b)
    draw.text((810, y_table + 8), "CATATAN / STATUS", fill=(20, 20, 20), font=font_text_b)
    
    items = [
        ("1", "INDOMIE GORENG SPESIAL 85G (KARTON @40 PCS)", "50", "KARTON", "50 ✓", "Lengkap & Segel"),
        ("2", "CHITATO SAPI PANGGANG 68G (KARTON @30 PCS)", "30", "KARTON", "30 ✓", "Lengkap & Segel"),
        ("3", "POP MIE KUAH AYAM BAWANG 75G (KARTON @24 PCS)", "40", "KARTON", "40 ✓", "Lengkap & Segel"),
        ("4", "INDOFOOD KECAP MANIS POUCH 520ML (DUS @12 PCS)", "25", "DUS", "25 ✓", "Lengkap"),
        ("5", "BUMBU RACIK AYAM GORENG (DUS @120 PCS)", "20", "DUS", "20 ✓", "Lengkap")
    ]
    
    row_y = y_table + 32
    for item in items:
        draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
        draw.text((70, row_y + 12), item[0], fill=(40, 40, 40), font=font_text)
        draw.text((120, row_y + 12), item[1], fill=(20, 20, 20), font=font_text_b)
        draw.text((500, row_y + 12), item[2], fill=(20, 20, 20), font=font_text)
        draw.text((600, row_y + 12), item[3], fill=(70, 70, 70), font=font_text)
        draw.text((700, row_y + 10), item[4], fill=(10, 30, 140), font=font_hand)
        draw.text((820, row_y + 12), item[5], fill=(40, 120, 40), font=font_text)
        row_y += 40
        
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(235, 235, 235), width=1)
        row_y += 35
        
    sig_y = row_y + 40
    draw.text((120, sig_y), "PENGIRIM (LOGISTIK ICBP)", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((120, sig_y + 115), "( Budi Santoso )", fill=(30, 30, 30), font=font_text)
    
    draw.text((430, sig_y), "PENERIMA (CHECKER ALFAMART)", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 420, sig_y + 30)
    draw.text((430, sig_y + 115), "( Agus Kurniawan )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "CAP STEMPEL DITERIMA", fill=(50, 50, 50), font=font_text_b)
    draw_stamp(draw, 820, sig_y + 60, "PT SUMBER ALFARIA TRIJAYA", "DITERIMA GUDANG", "DC CIKOKOL - TANGERANG")
    
    img.save(output_path, "PNG")
    print(f"Generated clean preset: {output_path}")

# ==========================================
# PRESET 2: MAYORA DISCREPANCY (RETUR BASAH)
# ==========================================
def generate_preset_2(output_path):
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
    
    # Row 2: Beng Beng (Discrepancy: 60 sent, 52 received, 8 wet)
    draw.rectangle([50, row_y, W - 50, row_y + 50], fill=(255, 245, 235), outline=(220, 150, 150), width=1)
    draw.text((70, row_y + 15), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 15), "BENG BENG REGULAR 20x20G (DUS @12 BOX)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 15), "60", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 15), "DUS", fill=(70, 70, 70), font=font_text)
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
    
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 80, 80), fill=(255, 248, 248), width=2)
    draw.text((65, row_y + 30), "PERNYATAAN SELISIH & RETUR GUDANG :", fill=(180, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Telah diterima 242 Dus dari total 250 Dus yang dikirim.", fill=(30, 30, 30), font=font_text)
    draw.text((65, row_y + 75), "Selisih 8 Dus Beng Beng diretur langsung ke pabrik karena kemasan basah saat pembongkaran.", fill=(160, 20, 20), font=font_text_b)
    
    sig_y = row_y + 140
    draw.text((120, sig_y), "DRIVER EKSPEDISI", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Hendra Gunawan )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "CHECKER DC INDOMARET", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( Wahyu Pratama )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "CAP STEMPEL DC ANCOL", fill=(50, 50, 50), font=font_text_b)
    draw_stamp(draw, 820, sig_y + 60, "INDOMARET DISTRIBUTION CENTER", "DITERIMA BERSYARAT", "DC ANCOL BARAT - JKT", color=(180, 50, 50, 220))
    
    img.save(output_path, "PNG")
    print(f"Generated discrepancy preset: {output_path}")

# ==========================================
# PRESET 3: WINGS GROUP (CRITICAL REJECTED)
# ==========================================
def generate_preset_3(output_path):
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(255, 250, 250))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(160, 160, 160), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT SAYAP MAS UTAMA (WINGS GROUP)", fill=(10, 40, 150), font=font_h1)
    draw.text((50, 80), "Logistics & Distribution Center Jakarta Timur", fill=(80, 80, 80), font=font_text)
    draw.text((50, 100), "Jl. Tipar Cakung Kav. F 5-7, Cakung Barat, Jakarta Timur", fill=(80, 80, 80), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN & BERITA ACARA", fill=(180, 20, 20), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: SJ/WINGS/2026/08/7712", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(10, 40, 150), width=2)
    
    draw.rectangle([50, 150, 480, 240], outline=(200, 200, 200), width=1)
    draw.text((60, 158), "TUJUAN PENGIRIMAN:", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "PT MATAHARI PUTRA PRIMA TBK (HYPERMART)", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "Hypermart Supermal Karawaci - Tangerang", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "PO Number: PO-HYPER-2026-901", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(200, 200, 200), width=1)
    draw.text((510, 158), "DATA ANGKUTAN:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "Nopol Truk: B 9552 WXY (Engkel Box)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Driver    : Dedi Kusnadi", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Ekspedisi : Logisly Express", fill=(60, 60, 60), font=font_text)
    
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(235, 245, 255), outline=(160, 180, 210), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "ITEM BARANG", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY PO", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "TERIMA FISIK", fill=(20, 20, 20), font=font_text_b)
    draw.text((830, y_table + 8), "CATATAN CHECKER", fill=(20, 20, 20), font=font_text_b)
    
    row_y = y_table + 32
    # Row 1: SoKlin Liquid (80 sent, 74 good, 6 leaked)
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
    
    # Row 2: Nuvo Family (50 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "NUVO FAMILY SABUN BATANG 110G (DUS @72)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "50", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "50 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 3: Ale Ale (100 sent, 90 received, 10 crushed)
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
    
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 50, 50), fill=(255, 245, 245), width=2)
    draw.text((65, row_y + 30), "BERITA ACARA KERUSAKAN BARANG SAAT SERAH TERIMA :", fill=(200, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Ditemukan 6 Dus SoKlin kemasan pecah bocor dan 10 Dus Ale-Ale penyok parah.", fill=(40, 40, 40), font=font_text)
    draw.text((65, row_y + 75), "Barang rusak tidak diterima oleh pihak Hypermart. Faktur tagihan wajib dipotong.", fill=(180, 20, 20), font=font_text_b)
    
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

# ==========================================
# PRESET 4: FRISIAN FLAG (COLD CHAIN / DAIRY DISCREPANCY)
# ==========================================
def generate_preset_4(output_path):
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(250, 253, 255))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(150, 190, 220), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT FRISIAN FLAG INDONESIA", fill=(0, 102, 179), font=font_h1)
    draw.text((50, 80), "Cold Chain & Dairy Logistics Plant Pasar Rebo", fill=(80, 80, 80), font=font_text)
    draw.text((50, 100), "Jl. Raya Bogor KM 5, Pasar Rebo, Jakarta Timur 13760", fill=(80, 80, 80), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN COLD CHAIN", fill=(0, 102, 179), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: SJ/FFI-COLD/2026/08/3019", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(0, 102, 179), width=2)
    
    draw.rectangle([50, 150, 480, 240], outline=(180, 210, 230), width=1)
    draw.text((60, 158), "TUJUAN PENGIRIMAN (DC FRESH):", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "PT TRANSMART RETAIL INDONESIA", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "Central DC Lebak Bulus - Jl. RA Kartini No. 8, Jaksel", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "PO Number: PO-TRANS-COLD-2026-552", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(180, 210, 230), width=1)
    draw.text((510, 158), "DATA REEFER TRUCK & SUHU:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "Nopol Truk : B 9112 CXY (Reefer Box ThermoKing)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Driver     : Joko Susilo (PT Cold Logistic Indo)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Suhu Awal  : +4°C | Suhu Tiba: +14°C (WARNING)", fill=(180, 20, 20), font=font_text_b)
    
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(230, 244, 255), outline=(150, 190, 220), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "NAMA PRODUK SUSU / DAIRY", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY KIRIM", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "TERIMA FISIK", fill=(20, 20, 20), font=font_text_b)
    draw.text((830, y_table + 8), "CATATAN QC DC", fill=(20, 20, 20), font=font_text_b)
    
    row_y = y_table + 32
    # Row 1: Susu UHT 1000ml (Discrepancy: 100 sent, 85 received, 15 rejected - temp breach)
    draw.rectangle([50, row_y, W - 50, row_y + 50], fill=(255, 245, 245), outline=(220, 160, 160), width=1)
    draw.text((70, row_y + 15), "1", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 15), "SUSU UHT FULL CREAM 1000ML (KARTON @12 TETRAPAK)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 15), "100", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 15), "KARTON", fill=(70, 70, 70), font=font_text)
    draw.line([(695, row_y + 22), (725, row_y + 22)], fill=(200, 20, 20), width=2)
    draw.text((700, row_y + 12), "100", fill=(120, 120, 120), font=font_text)
    draw.text((735, row_y + 8), "85", fill=(180, 20, 20), font=get_font(18, bold=True))
    draw.text((830, row_y + 10), "15 KTN DITOLAK (ASAM/14°C)", fill=(190, 20, 20), font=get_font(11, bold=True))
    draw.text((830, row_y + 28), "Thermal abuse di perjalanan", fill=(120, 30, 30), font=get_font(10))
    row_y += 50
    
    # Row 2: SKM Gold 370g (60 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "SUSU KENTAL MANIS GOLD KALENG 370G (DUS @48)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "60", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "60 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap & Dingin", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 3: Omela 370g (40 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "3", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "OMELA KRIMER KENTAL MANIS 370G (DUS @48)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "40", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "40 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Lengkap", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 80, 80), fill=(255, 248, 248), width=2)
    draw.text((65, row_y + 30), "BERITA ACARA KLAIM SUHU REEFER (COLD CHAIN AUDIT) :", fill=(180, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Kompresor reefer mati selama 3 jam, suhu kabin naik ke 14°C. 15 Karton UHT mengalami penggumpalan rasa asam.", fill=(30, 30, 30), font=font_text)
    draw.text((65, row_y + 75), "QC DC Transmart menolak 15 Karton. Nilai klaim pemotongan invoice: Rp 3.300.000.", fill=(160, 20, 20), font=font_text_b)
    
    sig_y = row_y + 140
    draw.text((120, sig_y), "DRIVER COLD CHAIN", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Joko Susilo )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "QC FRESH TRANSMART", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( Drh. Fitri Handayani )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "CAP STEMPEL QC DC", fill=(50, 50, 50), font=font_text_b)
    draw_stamp(draw, 820, sig_y + 60, "TRANSMART CENTRAL DC", "QC COLD CHAIN PASSED", "LEBAK BULUS JAKARTA", color=(0, 102, 179, 220))
    
    img.save(output_path, "PNG")
    print(f"Generated Cold Chain preset: {output_path}")

# ==========================================
# PRESET 5: SEMEN INDONESIA (HEAVY RETAIL / MITRA10 DISCREPANCY)
# ==========================================
def generate_preset_5(output_path):
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(252, 252, 250))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(140, 140, 140), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT SEMEN INDONESIA (PERSERO) TBK", fill=(180, 0, 0), font=font_h1)
    draw.text((50, 80), "Distribusi Logistik Semen Nasional - Packing Plant Tuban/Jakarta", fill=(80, 80, 80), font=font_text)
    draw.text((50, 100), "Kawasan Industri Marunda Center Kav. 12, Bekasi Utara", fill=(80, 80, 80), font=font_text)
    
    draw.text((W - 50, 50), "SURAT JALAN ANGKUTAN", fill=(180, 0, 0), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: SIG/LOG-JBT/2026/08/1189", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(180, 0, 0), width=2)
    
    draw.rectangle([50, 150, 480, 240], outline=(200, 200, 200), width=1)
    draw.text((60, 158), "TUJUAN PROYEK / DC PENERIMA:", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "PT CATUR MITRA SEJATI SENTOSA (MITRA10)", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "Mitra10 Logistics Hub Bintaro Jaya - Tangerang Selatan", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "PO Supplier: PO-M10-BUILD-2026-778", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(200, 200, 200), width=1)
    draw.text((510, 158), "INFORMASI TRUK TRONTON:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "Nopol Truk : B 9801 UYX (Tronton Wingbox 20 Ton)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Driver     : Slamet Riyadi (PT Varia Usaha Logistik)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Muatan     : 400 Zak (Total 16 Ton Semen)", fill=(60, 60, 60), font=font_text)
    
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(245, 245, 245), outline=(160, 160, 160), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "JENIS & MERK SEMEN", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY KIRIM", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "TERIMA FISIK", fill=(20, 20, 20), font=font_text_b)
    draw.text((830, y_table + 8), "CATATAN BONGKAR", fill=(20, 20, 20), font=font_text_b)
    
    row_y = y_table + 32
    # Row 1: Semen Gresik 40kg (Discrepancy: 200 sent, 180 received, 20 damaged water soaked)
    draw.rectangle([50, row_y, W - 50, row_y + 50], fill=(255, 245, 245), outline=(220, 150, 150), width=1)
    draw.text((70, row_y + 15), "1", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 15), "SEMEN GRESIK PORTLAND POZZOLAN CEMENT (PPC 40KG)", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 15), "200", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 15), "ZAK", fill=(70, 70, 70), font=font_text)
    draw.line([(695, row_y + 22), (725, row_y + 22)], fill=(200, 20, 20), width=2)
    draw.text((700, row_y + 12), "200", fill=(120, 120, 120), font=font_text)
    draw.text((735, row_y + 8), "180", fill=(180, 20, 20), font=get_font(18, bold=True))
    draw.text((830, row_y + 10), "20 ZAK BASAH & MEMBATU", fill=(190, 20, 20), font=get_font(11, bold=True))
    draw.text((830, row_y + 28), "Terkena rembesan terpal hujan", fill=(120, 30, 30), font=get_font(10))
    row_y += 50
    
    # Row 2: Semen Dynamix 40kg (150 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "SEMEN DYNAMIX SERBAGUNA PCC 40KG", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "150", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "ZAK", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "150 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Kering & Utuh", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 3: Mortar Perekat 40kg (50 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "3", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "MORTAR INDONESIA PEREKAT BATA RINGAN 40KG", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "50", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "ZAK", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "50 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "Kering & Utuh", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 80, 80), fill=(255, 248, 248), width=2)
    draw.text((65, row_y + 30), "BERITA ACARA KLAIM KERUSAKAN LOGISTIK SEMEN :", fill=(180, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Terpal penutup robek di jalan saat hujan lebat tol Cipali. 20 Zak Semen Gresik mengeras dan tidak dapat dijual.", fill=(30, 30, 30), font=font_text)
    draw.text((65, row_y + 75), "Barang rusak disisihkan di zona retur Mitra10. Potongan tagihan faktur: Rp 1.360.000.", fill=(160, 20, 20), font=font_text_b)
    
    sig_y = row_y + 140
    draw.text((120, sig_y), "PENGEMUDI TRUK", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Slamet Riyadi )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "KEPALA GUDANG MITRA10", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( Hendro Wicaksono )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "CAP STEMPEL PENERIMAAN", fill=(50, 50, 50), font=font_text_b)
    draw_rect_stamp(draw, 740, sig_y + 20, 940, sig_y + 110, "PT CATUR MITRA SEJATI SENTOSA", "MITRA10 BINTARO HUB", "TERIMA DENGAN CATATAN")
    
    img.save(output_path, "PNG")
    print(f"Generated Cement Logistics preset: {output_path}")

# ==========================================
# PRESET 6: KALBE FARMA (PHARMA / REJECTED BATCH)
# ==========================================
def generate_preset_6(output_path):
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), color=(255, 250, 250))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([30, 30, W - 30, H - 30], outline=(180, 140, 140), width=2)
    
    font_h1 = get_font(22, bold=True)
    font_h2 = get_font(16, bold=True)
    font_text = get_font(13)
    font_text_b = get_font(13, bold=True)
    font_hand = get_font(14, bold=True)
    
    draw.text((50, 50), "PT KALBE FARMA TBK", fill=(0, 128, 55), font=font_h1)
    draw.text((50, 80), "Pharma Distribution Division - Cikarang Industrial Estate", fill=(80, 80, 80), font=font_text)
    draw.text((50, 100), "Kawasan Industri Delta Silicon II, Cikarang, Jawa Barat", fill=(80, 80, 80), font=font_text)
    
    draw.text((W - 50, 50), "SURAT PENGANTAR OBAT (CDOB)", fill=(180, 20, 20), font=font_h1, anchor="ra")
    draw.text((W - 50, 80), "NO: KLB-FARMA/2026/08/9901", fill=(30, 30, 30), font=font_h2, anchor="ra")
    draw.text((W - 50, 105), "TANGGAL: 25 AGUSTUS 2026", fill=(70, 70, 70), font=font_text, anchor="ra")
    
    draw.line([(50, 135), (W - 50, 135)], fill=(0, 128, 55), width=2)
    
    draw.rectangle([50, 150, 480, 240], outline=(200, 200, 200), width=1)
    draw.text((60, 158), "DISTRIBUTOR / APOTEK TUJUAN:", fill=(30, 30, 30), font=font_text_b)
    draw.text((60, 180), "PT KIMIA FARMA APOTEK (DC NASIONAL)", fill=(20, 20, 20), font=font_text_b)
    draw.text((60, 200), "Central Warehouse PBF Kimia Farma - Pulo Gadung, Jaktim", fill=(60, 60, 60), font=font_text)
    draw.text((60, 218), "PO Apotek: PO-KF-MED-2026-440", fill=(10, 10, 10), font=font_text_b)
    
    draw.rectangle([500, 150, W - 50, 240], outline=(200, 200, 200), width=1)
    draw.text((510, 158), "INFORMASI KURIR KHUSUS FARMASI:", fill=(30, 30, 30), font=font_text_b)
    draw.text((510, 180), "Nopol Truk : B 9400 PHR (Box Berpendingin Khusus Obat)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 200), "Driver     : Bambang Pamungkas (Kalbe Logistics)", fill=(60, 60, 60), font=font_text)
    draw.text((510, 218), "Sertifikasi: CDOB (Cara Distribusi Obat yang Baik)", fill=(60, 60, 60), font=font_text)
    
    y_table = 260
    draw.rectangle([50, y_table, W - 50, y_table + 32], fill=(240, 250, 240), outline=(140, 180, 140), width=1)
    draw.text((65, y_table + 8), "NO", fill=(20, 20, 20), font=font_text_b)
    draw.text((120, y_table + 8), "NAMA OBAT & NO. BATCH", fill=(20, 20, 20), font=font_text_b)
    draw.text((480, y_table + 8), "QTY PO", fill=(20, 20, 20), font=font_text_b)
    draw.text((590, y_table + 8), "SATUAN", fill=(20, 20, 20), font=font_text_b)
    draw.text((680, y_table + 8), "TERIMA QC", fill=(20, 20, 20), font=font_text_b)
    draw.text((830, y_table + 8), "AUDIT EXPIRY DATE", fill=(20, 20, 20), font=font_text_b)
    
    row_y = y_table + 32
    # Row 1: Promag (100 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "1", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "PROMAG TAB KUNYAH (DUS @30 CC) - BATCH #PMG881", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "100", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "100 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "ED: 10/2028 (OK)", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 2: Mixagrip (80 Match)
    draw.rectangle([50, row_y, W - 50, row_y + 40], outline=(220, 220, 220), width=1)
    draw.text((70, row_y + 12), "2", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 12), "MIXAGRIP FLU & BATUK (DUS @25 BLS) - BATCH #MXG412", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 12), "80", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 12), "DUS", fill=(70, 70, 70), font=font_text)
    draw.text((700, row_y + 10), "80 ✓", fill=(10, 30, 140), font=font_hand)
    draw.text((830, row_y + 12), "ED: 12/2027 (OK)", fill=(40, 120, 40), font=font_text)
    row_y += 40
    
    # Row 3: Woods Peppermint (50 sent, 0 received, 50 rejected due to expiry < 6 months)
    draw.rectangle([50, row_y, W - 50, row_y + 50], fill=(255, 240, 240), outline=(220, 140, 140), width=1)
    draw.text((70, row_y + 15), "3", fill=(40, 40, 40), font=font_text)
    draw.text((120, row_y + 15), "WOODS PEPPERMINT ANTITUSSIVE 100ML (DUS @24 BTL) - #WOD092", fill=(20, 20, 20), font=font_text_b)
    draw.text((500, row_y + 15), "50", fill=(20, 20, 20), font=font_text)
    draw.text((600, row_y + 15), "DUS", fill=(70, 70, 70), font=font_text)
    draw.line([(695, row_y + 22), (725, row_y + 22)], fill=(200, 20, 20), width=2)
    draw.text((700, row_y + 12), "50", fill=(120, 120, 120), font=font_text)
    draw.text((735, row_y + 8), "0", fill=(220, 20, 20), font=get_font(20, bold=True))
    draw.text((830, row_y + 10), "REJEK TOTAL (ED: 11/2026)", fill=(200, 20, 20), font=get_font(11, bold=True))
    draw.text((830, row_y + 28), "SOP Kimia Farma: Min 12 Bulan", fill=(160, 20, 20), font=get_font(10))
    row_y += 50
    
    for _ in range(3):
        draw.rectangle([50, row_y, W - 50, row_y + 35], outline=(230, 230, 230), width=1)
        row_y += 35
        
    draw.rectangle([50, row_y + 20, W - 50, row_y + 110], outline=(220, 50, 50), fill=(255, 245, 245), width=2)
    draw.text((65, row_y + 30), "BERITA ACARA PENOLAKAN OBAT (PENGAWAS FARMASI PBF) :", fill=(200, 20, 20), font=font_text_b)
    draw.text((65, row_y + 55), "Batch #WOD092 Woods Sirup memiliki sisa masa simpan kurang dari 3 bulan (ED: November 2026).", fill=(30, 30, 30), font=font_text)
    draw.text((65, row_y + 75), "Sesuai regulasi CDOB BPOM & SOP Kimia Farma, seluruh 50 Dus ditolak total. Potongan tagihan: Rp 27.000.000.", fill=(180, 20, 20), font=font_text_b)
    
    sig_y = row_y + 140
    draw.text((120, sig_y), "KURIR DISTRIBUSI", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 100, sig_y + 30)
    draw.text((110, sig_y + 120), "( Bambang Pamungkas )", fill=(30, 30, 30), font=font_text)
    
    draw.text((450, sig_y), "APOTEKER PENANGGUNG JAWAB", fill=(50, 50, 50), font=font_text_b)
    draw_signature(draw, 440, sig_y + 30)
    draw.text((450, sig_y + 120), "( apt. Annisa Zahra, S.Farm )", fill=(30, 30, 30), font=font_text)
    
    draw.text((750, sig_y), "STEMPEL REJEK QC APOTEK", fill=(180, 50, 50), font=font_text_b)
    draw_triangle_stamp(draw, 840, sig_y + 60, "KIMIA FARMA DC", "REJEK QC", "ED < 12 BLN", color=(200, 20, 20, 220))
    
    img.save(output_path, "PNG")
    print(f"Generated Pharma preset: {output_path}")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dirs = [
        os.path.join(base_dir, "datasets", "samples"),
        os.path.join(base_dir, "frontend", "public", "samples")
    ]
    for d in target_dirs:
        os.makedirs(d, exist_ok=True)
        generate_preset_1(os.path.join(d, "preset_1_indofood_clean.png"))
        generate_preset_2(os.path.join(d, "preset_2_mayora_discrepancy.png"))
        generate_preset_3(os.path.join(d, "preset_3_wings_damage_alert.png"))
        generate_preset_4(os.path.join(d, "preset_4_frisianflag_coldchain.png"))
        generate_preset_5(os.path.join(d, "preset_5_semenindonesia_damaged.png"))
        generate_preset_6(os.path.join(d, "preset_6_kalbefarma_expired.png"))
    print("All 6 presets generated successfully across datasets and frontend public folders!")
