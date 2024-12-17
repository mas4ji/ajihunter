import requests
from bs4 import BeautifulSoup
import os
import re
import argparse

# Menambahkan salam pembuka ASCII Art sebagai raw string
def print_welcome_message():
    welcome_message = r"""
     _     _ _       _ ____    _   _             _            
    / \   (_|_)     | / ___|  | | | |_   _ _ __ | |_ ___ _ __ 
   / _ \  | | |  _  | \___ \  | |_| | | | | '_ \| __/ _ \ '__| 
  / ___ \ | | | | |_| |___) | |  _  | |_| | | | | ||  __/ |   
 /_/   \_\/ |_|  \___/|____/  |_| |_|\__,_|_| |_|\__\___|_|   
         |__/                                                   """
    print("\033[36m" + welcome_message)  # Cyan

# Fungsi untuk memastikan URL dimulai dengan http:// jika tidak ada
def ensure_http(url):
    if not url.startswith("http"):
        return "http://" + url
    return url

# Fungsi untuk memeriksa dan menampilkan data sensitif
def find_sensitive_data(js_content):
    patterns = {
        'email': r'[a-zA-Z0-9._%+-]+@[a-zAZ0-9.-]+\.[a-zA-Z]{2,}',  # Email
        'phone': r'\+?\d{1,4}[\s\-]?\(?\d{1,3}\)?[\s\-]?\d{3}[\s\-]?\d{4,6}',  # Nomor telepon
        'api_key': r'(?i)\b(?:api[_-]?key|apikey|auth[_-]?token|access[_-]?token)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # API Key
        'jwt_token': r'eyJ[a-zA-Z0-9\-_\.]+',  # JWT Token
        'db_credential': r'(?i)\b(?:db[_-]?user|db[_-]?password|db[_-]?host|db[_-]?port|db[_-]?name)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # Database Credentials
        'aws_secret': r'(?i)\b(?:aws[_-]?secret[_-]?key)[=\s]?[\'"]?([a-zA-Z0-9/+=]+)[\'"]?\b',  # AWS Secret Key
        'stripe_key': r'(?i)\b(?:stripe[_-]?secret[_-]?key)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # Stripe API Key
        'github_token': r'(?i)\b(?:github[_-]?token)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # GitHub Token
        'google_api_key': r'(?i)\b(?:google[_-]?api[_-]?key)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # Google API Key
        'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',  # IP Address (IPv4)
        'private_key': r'(?i)\b(?:private[_-]?key)[=\s]?[\'"]?([a-zA-Z0-9/+_=-]+)[\'"]?\b',  # Private Key
        'oauth_token': r'(?i)\b(?:oauth[_-]?token)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # OAuth Token
        'slack_token': r'(?i)\b(?:slack[_-]?token)[=\s]?[\'"]?([a-zA-Z0-9_-]+)[\'"]?\b',  # Slack Token
    }
    matches = {}

    for key, pattern in patterns.items():
        matches[key] = re.findall(pattern, js_content)

    return matches

# Fungsi untuk scrape file JS dari sebuah URL dan menyimpan hasilnya dalam file di folder output
def scrape_js_from_url(url, output_dir="output"):
    url = ensure_http(url)  # Pastikan URL memiliki 'http://'
    domain_name = url.split("//")[-1].split("/")[0]
    
    # Membuat folder output jika belum ada
    domain_folder = os.path.join(output_dir, domain_name)
    os.makedirs(domain_folder, exist_ok=True)

    output_file = os.path.join(domain_folder, f"{domain_name}_js_data.txt")

    try:
        # Request halaman utama
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML-nya
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Cari semua tag <script>
        script_tags = soup.find_all("script", src=True)
        
        print("\033[32m" + f"[INFO] Ditemukan {len(script_tags)} file JS dari {url}")  # Green
        
        with open(output_file, "a", encoding="utf-8") as f:
            # Tulis URL domain
            f.write(f"[INFO] Scraping file JS dari: {url}\n")
            
            # Loop semua <script src="...">
            for script in script_tags:
                js_url = script["src"]
                
                # Handle jika URL JS relatif (convert ke absolut)
                if not js_url.startswith("http"):
                    js_url = requests.compat.urljoin(url, js_url)
                
                # Tulis URL JS yang ditemukan
                f.write(f"JS URL: {js_url}\n")
                print("\033[33m" + f"[DOWNLOAD] {js_url}")  # Yellow
                
                # Download file JS
                js_content = requests.get(js_url).text
                
                # Menampilkan data sensitif jika ditemukan
                sensitive_data = find_sensitive_data(js_content)
                for category, items in sensitive_data.items():
                    if items:
                        f.write(f"[WARNING] Ditemukan {category} dalam {js_url}:\n")
                        for item in items:
                            f.write(f"  - {item}\n")
                        print(f"\033[31m[WARNING] Ditemukan {category} dalam {js_url}:")
                        for item in items:
                            print(f"  - {item}")

        # Menampilkan pesan selesai dan lokasi penyimpanan
        print(f"\033[32m[INFO] Scraping selesai. Data disimpan di {output_file}")
            
    except Exception as e:
        print("\033[31m" + f"[ERROR] {e}")  # Red

# Fungsi untuk scrape dari file yang berisi daftar domain
def scrape_from_file(file_path, output_dir="output"):
    with open(file_path, "r") as f:
        domains = f.read().splitlines()
        for domain in domains:
            scrape_js_from_url(domain, output_dir=output_dir)

# Main Program
if __name__ == "__main__":
    # Menampilkan salam pembuka
    print_welcome_message()

    # Parse argumentasi command line
    parser = argparse.ArgumentParser(description="Scrape all .js files from a website or list of domains.")
    parser.add_argument("-d", "--domain", help="Single domain to scrape.")
    parser.add_argument("-f", "--file", help="File containing list of domains (one per line).")
    args = parser.parse_args()

    # Mengecek apakah command argument ada
    if args.domain:
        scrape_js_from_url(args.domain)
    elif args.file:
        scrape_from_file(args.file)
    else:
        # Menampilkan pesan penggunaan dengan format lebih jelas dan berwarna
        print("\033[33m" + "[USAGE] Silakan gunakan salah satu opsi berikut:")  # Yellow
        print("\033[35m" + "  -d  : Untuk menentukan satu domain yang akan di-scrape.")  # Magenta
        print("\033[35m" + "  -f  : Untuk menentukan file yang berisi daftar domain (satu per baris).")  # Magenta
        print("\033[36m" + "[INFO] Program selesai.")  # Cyan
