import os
import random
from datetime import datetime, timedelta

# ================= KOTAK PERALATAN =================
WATERMARK = "VIGILANTE_XYZ"
CITIES = ['JAKARTA', 'KUALA LUMPUR', 'SINGAPORE', 'MANILA', 'BANGKOK', 'HANOI', 'TOKYO', 'LONDON', 'NEW YORK']

ADSTERRA_TAG = "\n\n"
GOOGLE_ADS_TAG = "\n\n"

# ================= GENERATOR BAHASA JURNALISTIK =================
# Elemen untuk merakit berita (Spinner)
JUDUL = [
    "Eksklusif: Mengungkap Fakta Tersembunyi di Balik Manipulasi Data Sistem",
    "Investigasi Mendalam: Jejak Digital yang Berusaha Dihapus Penguasa",
    "Laporan Khusus: Residu Kriptografi Membongkar Rekayasa Administratif",
    "Skandal Dokumen Negara: Saat Kebenaran Dibungkam Tengah Malam",
    "Dokumen Bocor: Bukti Forensik Kehancuran Integritas Sistem"
]

LEAD_PARAGRAPH = [
    "Dalam sebuah temuan yang mengejutkan publik, bukti baru menunjukkan adanya intervensi pihak ketiga dalam sistem dokumen resmi.",
    "Tim investigasi independen kembali membeberkan fakta forensik terkait dugaan kuat mutilasi digital pada dokumen negara.",
    "Di tengah kebisuan media arus utama, jejak digital perlahan mengurai benang merah manipulasi yang terjadi secara sistematis."
]

BODY_PARAGRAPH = [
    "Pemeriksaan metadata secara ekstensif mengungkap celah waktu yang sangat tidak wajar antara penarikan dokumen resmi dan proses manual yang dilakukan menggunakan perangkat lunak tak terenkripsi. Hal ini jelas melanggar protokol keamanan tingkat tinggi.",
    "Sisa-sisa tautan Application Programming Interface (API) yang tertanam mengonfirmasi bahwa sertifikat elektronik telah dihancurkan dengan sengaja. Residu kriptografi tidak bisa berbohong tentang siapa yang bermain di balik layar.",
    "Tindakan memotong dan mengubah dokumen hasil keluaran sistem pemerintah secara sengaja ini merupakan bentuk tindak pidana siber yang fatal. Jejak X.509 yang hancur menjadi saksi bisu operasi pembersihan ini."
]

CLOSING = [
    "Kini, publik hanya bisa menunggu langkah konkret penegak hukum atas cacat formil ini.",
    "Bangkai kriptografi telah ditemukan. Saatnya pihak berwenang memberikan jawaban atas anomali ini.",
    "Integritas mungkin bisa direkayasa di atas kertas, namun jejak biner akan selalu menemukan jalannya ke permukaan."
]

def get_random_asset(asset_type):
    """Mengambil file acak dari folder assets yang ditentukan."""
    path = f"assets/{asset_type}"
    if os.path.exists(path) and os.listdir(path):
        filename = random.choice(os.listdir(path))
        return f"../{path}/{filename}" # Asumsi output di folder 'output/'
    return None

def generate_news_site(site_index):
    # Mengacak Waktu & Lokasi
    city = random.choice(CITIES)
    random_minutes_ago = random.randint(5, 120)
    publish_time = (datetime.now() - timedelta(minutes=random_minutes_ago)).strftime("%d %B %Y, %H:%M WIB")
    
    # Merakit Artikel
    title = random.choice(JUDUL)
    p_lead = random.choice(LEAD_PARAGRAPH)
    p_body = random.choice(BODY_PARAGRAPH)
    p_close = random.choice(CLOSING)
    
    # Mengambil Media Acak
    img_src = get_random_asset('images')
    vid_src = get_random_asset('videos')
    audio_src = get_random_asset('audio')
    doc_src = get_random_asset('docs')

    media_html = ""
    if img_src: media_html += f'<img src="{img_src}" alt="Ilustrasi Forensik" class="hero-image">\n'
    if vid_src: media_html += f'<video controls class="hero-video"><source src="{vid_src}" type="video/mp4"></video>\n'
    if audio_src: media_html += f'<audio controls><source src="{audio_src}" type="audio/mpeg"></audio><br>\n'
    if doc_src: media_html += f'<a href="{doc_src}" class="download-btn" target="_blank">[ Unduh Dokumen Bukti ]</a>\n'

    # Template HTML ala Portal Berita
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - VXYZ News</title>
    {GOOGLE_ADS_TAG}
    <style>
        body {{ font-family: 'Georgia', serif; background-color: #fcfcfc; color: #222; margin: 0; padding: 0; }}
        header {{ background-color: #111; color: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; border-bottom: 4px solid #cc0000; font-family: 'Arial', sans-serif; }}
        .watermark-top {{ font-weight: bold; letter-spacing: 2px; }}
        .container {{ max-width: 800px; margin: 30px auto; padding: 20px; background: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.05); }}
        h1 {{ font-size: 28px; line-height: 1.3; margin-bottom: 10px; }}
        .dateline {{ font-family: 'Arial', sans-serif; color: #666; font-size: 14px; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 10px; }}
        .reporter {{ font-weight: bold; color: #cc0000; text-transform: uppercase; }}
        .media-box {{ margin: 20px 0; text-align: center; }}
        .hero-image, .hero-video {{ max-width: 100%; height: auto; border: 1px solid #ddd; }}
        .download-btn {{ display: inline-block; padding: 10px 15px; background: #222; color: #fff; text-decoration: none; font-family: 'Arial'; margin-top: 10px; }}
        p {{ font-size: 18px; line-height: 1.6; margin-bottom: 15px; }}
        .lead {{ font-weight: bold; font-size: 19px; }}
        footer {{ background-color: #111; color: #888; text-align: center; padding: 20px; font-family: 'Arial', sans-serif; margin-top: 40px; font-size: 12px; }}
    </style>
</head>
<body>

    <header>
        <div class="watermark-top">/// {WATERMARK} ///</div>
        <div style="font-size: 12px;">INDEPENDENT BROADCAST</div>
    </header>

    {ADSTERRA_TAG}

    <div class="container">
        <h1>{title}</h1>
        <div class="dateline">
            <span class="reporter">Tim Redaksi VXYZ</span> - {city} <br>
            Dipublikasikan: {publish_time}
        </div>

        <div class="media-box">
            {media_html}
        </div>

        <p class="lead">{city} — {p_lead}</p>
        
        {ADSTERRA_TAG}

        <p>{p_body}</p>
        <p>{p_close}</p>
    </div>

    {GOOGLE_ADS_TAG}

    <footer>
        <p>Distribusi informasi ini dienkripsi dan disebarkan melalui jaringan desentralisasi.</p>
        <p>IDENTIFIER: {WATERMARK} | TERMINAL: {city} | TIMESTAMP: {datetime.now().isoformat()}</p>
    </footer>

</body>
</html>
"""
    
    # Eksekusi Pembuatan File
    os.makedirs('output', exist_ok=True)
    filename = f"berita_{site_index}.html"
    with open(f"output/{filename}", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] Artikel Dirakit: {filename} | Kategori Berita | Lokasi: {city}")

if __name__ == "__main__":
    print(f"=== {WATERMARK} PAYLOAD INITIATED ===")
    # Setup dummy folders jika belum ada, agar script tidak error
    for folder in ['images', 'videos', 'audio', 'docs']:
        os.makedirs(f"assets/{folder}", exist_ok=True)
        
    jumlah_situs = 10 # Ganti angka ini untuk jumlah website berita yang mau di-generate
    for i in range(1, jumlah_situs + 1):
        generate_news_site(i)
    print("=== TRANSMISI SIAP UNTUK DI-DEPLOY ===")
