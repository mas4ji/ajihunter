import requests
from bs4 import BeautifulSoup
import os
import re
import argparse

# Adding the opening greeting ASCII Art as raw string
def print_welcome_message():
    welcome_message = r"""
     _     _ _       _ ____    _   _             _            
    / \   (_|_)     | / ___|  | | | |_   _ _ __ | |_ ___ _ __ 
   / _ \  | | |  _  | \___ \  | |_| | | | | '_ \| __/ _ \ '__| 
  / ___ \ | | | | |_| |___) | |  _  | |_| | | | | ||  __/ |   
 /_/   \_\/ |_|  \___/|____/  |_| |_|\__,_|_| |_|\__\___|_|   
         |__/                                                   """
    print("\033[36m" + welcome_message)  # Cyan
    print("\033[37m" + "[INFO] Welcome to Ajihunter - Scraper for JavaScript Files!")  # White

# Function to ensure the URL starts with http:// if not present
def ensure_http(url):
    if not url.startswith("http"):
        return "http://" + url
    return url

# Function to check and display sensitive data
def find_sensitive_data(js_content):
    patterns = {
        'email': r'[a-zA-Z0-9._%+-]+@[a-zAZ0-9.-]+\.[a-zA-Z]{2,}',  # Email
        'phone': r'\+?\d{1,4}[\s\-]?\(?\d{1,3}\)?[\s\-]?\d{3}[\s\-]?\d{4,6}',  # Phone numbers
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

# Function to scrape JS files from a URL and save the results in an output folder
def scrape_js_from_url(url, output_dir="output"):
    url = ensure_http(url)  # Ensure URL has 'http://'
    domain_name = url.split("//")[-1].split("/")[0]
    
    # Create output folder if not exists
    domain_folder = os.path.join(output_dir, domain_name)
    os.makedirs(domain_folder, exist_ok=True)

    output_file = os.path.join(domain_folder, f"{domain_name}_js_data.txt")

    try:
        # Request the main page
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all <script> tags
        script_tags = soup.find_all("script", src=True)
        
        print("\033[32m" + f"[INFO] Found {len(script_tags)} JS files from {url}")  # Green
        
        with open(output_file, "a", encoding="utf-8") as f:
            # Write the domain URL
            f.write(f"[INFO] Scraping JS files from: {url}\n")
            
            # Loop through each <script src="...">
            for script in script_tags:
                js_url = script["src"]
                
                # Handle relative JS URLs (convert to absolute)
                if not js_url.startswith("http"):
                    js_url = requests.compat.urljoin(url, js_url)
                
                # Write the JS URL found
                f.write(f"JS URL: {js_url}\n")
                print("\033[32m" + f"[DOWNLOAD] {js_url}")  # Green
                
                # Download the JS file
                js_content = requests.get(js_url).text
                
                # Display sensitive data if found
                sensitive_data = find_sensitive_data(js_content)
                for category, items in sensitive_data.items():
                    if items:
                        f.write(f"[WARNING] Found {category} in {js_url}:\n")
                        for item in items:
                            f.write(f"  - {item}\n")
                        print(f"\033[31m[WARNING] Found {category} in {js_url}:")
                        for item in items:
                            print(f"  - {item}")

        # Display completion message and file save location
        print(f"\033[32m[INFO] Scraping completed. Data saved in {output_file}")
            
    except Exception as e:
        print("\033[31m" + f"[ERROR] {e}")  # Red

# Function to scrape from a file containing a list of domains
def scrape_from_file(file_path, output_dir="output"):
    with open(file_path, "r") as f:
        domains = f.read().splitlines()
        for domain in domains:
            scrape_js_from_url(domain, output_dir=output_dir)

# Main Program
if __name__ == "__main__":
    # Display the opening message
    print_welcome_message()

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Scrape all .js files from a website or list of domains.")
    parser.add_argument("-d", "--domain", help="Single domain to scrape.")
    parser.add_argument("-f", "--file", help="File containing list of domains (one per line).")
    args = parser.parse_args()

    # Check if command argument is present
    if args.domain:
        scrape_js_from_url(args.domain)
    elif args.file:
        scrape_from_file(args.file)
    else:
        # Display usage instructions with clearer formatting
        print("\033[32m" + "[USAGE] Please use one of the following options:")  # Green
        print("\033[32m" + "  -d  : To specify a single domain to scrape.")  # Green
        print("\033[32m" + "  -f  : To specify a file containing a list of domains (one per line).")  # Green
        print("\033[32m" + "[INFO] Program finished.")  # Green
