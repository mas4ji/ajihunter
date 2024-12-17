<h1 align="center">Ajihunter - Scraper for JS Files</h1>

<p align="center">Ajihunter is a tool used to find and download JavaScript (.js) files from a single domain or a list of domains. This tool is designed to assist in bug hunting by identifying and downloading embedded JavaScript files on websites. You can use Ajihunter to gather relevant JS files from various websites for further analysis.</p>

<p align="center">
  <img src="https://github.com/mas4ji/ajitools/blob/main/image%20(19).png" alt="Ajihunter Screenshot">
</p>

## **Usage**
### Options:

- **`-d`** : To specify a single domain to scrape.
  - Example:
    ```bash
    python3 ajihunter.py -d http://example.com
    ```
    This will scrape JavaScript files from the domain `http://example.com`.

- **`-f`** : To specify a file containing a list of domains (one domain per line).
  - Example:
    ```bash
    python3 ajihunter.py -f domains.txt
    ```
    This will scrape JavaScript files from all the domains listed in the `domains.txt` file, with each domain on a new line.

## **Requirements**
- Ensure that Python and pip are installed on your system.

## **Clone Repo and Install Dependencies**

To install and use `Ajihunter`, follow these steps:

- **Clone the repository**:
   - Run the following command to clone the Ajihunter repository to your local system:
   ```bash
   git clone https://github.com/mas4ji/ajihunter.git
    ```
   - Navigate into the repository folder:
   ```bash
   cd ajihunter
    ```
   - Install required dependencies:
   ```bash
   pip3 install -r requirements.txt
    ```
   - Run the script:
   ```bash
   python3 ajihunter.py -d http://example.com or python3 ajihunter.py -f domains.txt
   ```
   
## Connect with me:
<p align="left">
<a href="https://linkedin.com/in/fazriansyahmuh" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="0xkayala" height="30" width="40" /></a>
<a href="https://instagram.com/fazriansyahmuh" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="0xkayala" height="30" width="40" /></a>
<a href="https://medium.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/medium.svg" alt="@0xkayala" height="30" width="40" /></a>
<a href="https://www.youtube.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="0xkayala" height="30" width="40" /></a>
</p>


## Acknowledgements
- Thanks to [Root Bakar](https://github.com/RootBakar) for the inspiration to create this tool.
- Special thanks to the open-source community for their amazing libraries and support!


## Security Notice
This tool is intended for educational and security auditing purposes. Ensure you have explicit permission before scraping any website. The creators are not responsible for any damage or illegal activities resulting from the misuse of this tool.
