# generator.py - HYDRA-PULSE NEWS ENGINE
import os
import random
from datetime import datetime, timedelta

# ================= KOTAK PERALATAN =================
WATERMARK = "VIGILANTE_XYZ"
CITIES = ['MAKASSAR', 'JAKARTA', 'KUALA LUMPUR', 'SINGAPORE', 'TOKYO', 'LONDON', 'NEW YORK']

# ================= GENERATOR BAHASA JURNALISTIK =================
JUDUL = [
    "Eksklusif: Mengungkap Fakta Tersembunyi di Balik Manipulasi Data Sistem",
    "Investigasi Mendalam: Jejak Digital yang Berusaha Dihapus Penguasa",
    "Laporan Khusus: Residu Kriptografi Membongkar Rekayasa Administratif",
    "Siri' Na Pacce: Penggusuran PKL dan Matinya Hati Nurani Pemerintah",
    "Dokumen Bocor: Bukti Forensik Kehancuran Integritas Sistem"
]

LEAD_PARAGRAPH = [
    "Dalam sebuah temuan yang mengejutkan publik, bukti baru menunjukkan adanya intervensi pihak ketiga dalam sistem dokumen resmi.",
    "Tim investigasi independen kembali membeberkan fakta forensik terkait dugaan kuat mutilasi digital pada dokumen negara.",
    "Jerit tangis rakyat kecil di jalanan berbanding terbalik dengan senyapnya operasi manipulasi di balik meja birokrasi."
]

BODY_PARAGRAPH = [
    "Pemeriksaan metadata secara ekstensif mengungkap celah waktu yang sangat tidak wajar antara penarikan dokumen resmi dan proses manual yang dilakukan menggunakan perangkat lunak tak terenkripsi. Hal ini jelas melanggar protokol keamanan tingkat tinggi.",
    "Sisa-sisa tautan Application Programming Interface (API) yang tertanam mengonfirmasi bahwa sertifikat elektronik telah dihancurkan dengan sengaja. Residu kriptografi tidak bisa berbohong tentang siapa yang bermain di balik layar.",
    "Mereka menggusur lapak-lapak rakyat dengan dalih ketertiban, sementara di ruang digital, mereka sendiri yang mengacak-acak ketertiban hukum dan administrasi negara demi kepentingan segelintir elit."
]

CLOSING = [
    "Kini, publik hanya bisa menunggu langkah konkret penegak hukum atas cacat formil ini.",
    "Bangkai kriptografi telah ditemukan. Saatnya pihak berwenang memberikan jawaban atas anomali ini.",
    "Integritas mungkin bisa direkayasa di atas kertas, namun jejak biner dan perlawanan jalanan akan selalu menemukan jalannya ke permukaan."
]

def get_random_asset(asset_type):
    path = f"assets/{asset_type}"
    if os.path.exists(path) and os.listdir(path):
        filename = random.choice(os.listdir(path))
        # Mengubah path agar bisa dibaca dari dalam folder 'output/'
        return f"../{path}/{filename}" 
    return None

def generate_html_content(city, publish_time, title, p_lead, p_body, p_close):
    img_src = get_random_asset('images')
    audio_src = get_random_asset('audio')

    media_html = ""
    if img_src: media_html += f'<img src="{img_src}" alt="Ilustrasi Forensik" class="hero-image" style="max-width:100%; border: 2px solid #cc0000; margin: 20px 0; filter: grayscale(100%);">\n'
    
    # Audio tersembunyi sebagai background (The Anthem)
    audio_html = ""
    if audio_src: audio_html += f'<audio autoplay loop style="display:none;"><source src="{audio_src}" type="audio/mpeg"></audio>\n'

    return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {WATERMARK} PROTOCOL</title>
    <style>
        body {{ font-family: 'Courier New', monospace; background-color: #050505; color: #00ff00; margin: 0; padding: 0; }}
        header {{ background-color: #111; color: #ff3333; padding: 15px 20px; text-align: center; border-bottom: 2px dashed #00ff00; }}
        .container {{ max-width: 800px; margin: 30px auto; padding: 20px; background: rgba(0, 20, 0, 0.8); border: 1px solid #00ff00; box-shadow: 0 0 15px rgba(0,255,0,0.2); }}
        h1 {{ font-size: 24px; color: #ff3333; text-transform: uppercase; }}
        .dateline {{ color: #888; font-size: 14px; margin-bottom: 20px; border-bottom: 1px solid #333; padding-bottom: 10px; }}
        .reporter {{ font-weight: bold; color: #ffff00; }}
        p {{ font-size: 16px; line-height: 1.6; text-align: justify; }}
        .lead {{ font-weight: bold; font-size: 18px; color: #fff; }}
        footer {{ text-align: center; padding: 20px; color: #444; font-size: 12px; margin-top: 40px; border-top: 1px dashed #00ff00; }}
    </style>
</head>
<body>
    <header>
        <h2>/// SYSTEM OVERRIDE: {WATERMARK} ///</h2>
    </header>
    <div class="container">
        <h1>{title}</h1>
        <div class="dateline">
            <span class="reporter">Sandi Operasi: VIGILANTE</span> - {city} | Waktu Retas: {publish_time}
        </div>
        {media_html}
        <p class="lead">>> {p_lead}</p>
        <p>{p_body}</p>
        <p style="color: #ff3333; font-weight: bold;">{p_close}</p>
    </div>
    {audio_html}
    <footer>
        <p>IDENTIFIER: {WATERMARK} | TERMINAL: {city} | TIMESTAMP: {datetime.now().isoformat()}</p>
    </footer>
</body>
</html>
"""

def generate_news_site():
    os.makedirs('output', exist_ok=True)
    
    # Generate 5 berita acak
    for i in range(1, 6):
        city = random.choice(CITIES)
        publish_time = (datetime.now() - timedelta(minutes=random.randint(5, 120))).strftime("%d %B %Y, %H:%M WIB")
        
        content = generate_html_content(
            city, publish_time, 
            random.choice(JUDUL), random.choice(LEAD_PARAGRAPH), 
            random.choice(BODY_PARAGRAPH), random.choice(CLOSING)
        )
        
        # Simpan file pertama sebagai index.html (Halaman Utama)
        filename = "index.html" if i == 1 else f"berita_{i}.html"
        
        with open(f"output/{filename}", "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[JARVIS] Berhasil merakit: output/{filename}")

if __name__ == "__main__":
    print(f"=== {WATERMARK} PAYLOAD INITIATOR ===")
    for folder in ['images', 'videos', 'audio', 'docs']:
        os.makedirs(f"assets/{folder}", exist_ok=True)
    generate_news_site()
    print("=== TRANSMISI SIAP UNTUK DI-DEPLOY ===")
