import requests
from bs4 import BeautifulSoup
import os
import argparse

# Menambahkan salam pembuka ASCII Art sebagai raw string
def print_welcome_message():
    welcome_message = r"""
     _     _ _       _ ____    _   _             _            
    / \   (_|_)     | / ___|  | | | |_   _ _ __ | |_ ___ _ __ 
   / _ \  | | |  _  | \___ \  | |_| | | | | '_ \| __/ _ \ '__| 
  / ___ \ | | | | |_| |___) | |  _  | |_| | | | | ||  __/ |   
 /_/   \_\/ |_|  \___/|____/  |_| |_|\__,_|_| |_|\__\___|_|   
         |__/                                                  
    """
    print("\033[36m" + welcome_message)  # Cyan

# Fungsi untuk scrape file JS dari sebuah URL
def scrape_js_from_url(url, output_dir="output"):
    domain_name = url.split("//")[-1].split("/")[0]
    domain_folder = os.path.join(output_dir, domain_name)

    # Membuat folder untuk domain jika belum ada
    if not os.path.exists(domain_folder):
        os.makedirs(domain_folder)
    
    try:
        # Request halaman utama
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML-nya
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Cari semua tag <script>
        script_tags = soup.find_all("script", src=True)
        
        print("\033[32m" + f"[INFO] Ditemukan {len(script_tags)} file JS dari {url}")  # Green
        
        # Loop semua <script src="...">
        for script in script_tags:
            js_url = script["src"]
            
            # Handle jika URL JS relatif (convert ke absolut)
            if not js_url.startswith("http"):
                js_url = requests.compat.urljoin(url, js_url)
            
            print("\033[33m" + f"[DOWNLOAD] {js_url}")  # Yellow
            
            # Download file JS
            js_content = requests.get(js_url).text
            js_filename = os.path.join(domain_folder, js_url.split("/")[-1])
            
            # Simpan ke file lokal
            with open(js_filename, "w", encoding="utf-8") as f:
                f.write(js_content)
                print("\033[36m" + f"[SAVED] {js_filename}")  # Cyan
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
    parser.add_argument("-o", "--output", help="Output directory for JS files.", default="output")
    args = parser.parse_args()

    # Mengecek apakah command argument ada
    if args.domain:
        scrape_js_from_url(args.domain, args.output)
    elif args.file:
        scrape_from_file(args.file, args.output)
    else:
        # Menampilkan pesan penggunaan dengan format lebih jelas dan berwarna
        print("\033[33m" + "[USAGE] Silakan gunakan salah satu opsi berikut:")  # Yellow
        print("\033[35m" + "  -d  : Untuk menentukan satu domain yang akan di-scrape.")  # Magenta
        print("\033[35m" + "  -f  : Untuk menentukan file yang berisi daftar domain (satu per baris).")  # Magenta
        print("\033[35m" + "  -o  : Untuk menentukan direktori output tempat file .js disimpan (opsional).")  # Magenta
        print("\033[36m" + "[INFO] Program selesai.")  # Cyan
