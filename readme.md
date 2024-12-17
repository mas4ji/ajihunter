<h1 align="center">Ajihunter - Scraper for JS Files</h1>

<p align="center">Ajihunter adalah alat yang digunakan untuk menemukan dan mengunduh file JavaScript (.js) dari satu domain atau daftar domain. Alat ini dirancang untuk membantu dalam bug hunting dengan mengidentifikasi dan mengunduh file skrip JavaScript yang disematkan pada situs web. Anda dapat menggunakan Ajihunter untuk mengumpulkan file JS yang relevan dari berbagai situs web untuk dianalisis lebih lanjut.</p>


<p align="center">
  <img src="https://github.com/mas4ji/ajitools/blob/main/image%20(19).png" alt="Ajihunter Screenshot">
</p>

## **Usage**
### Opsi:

- **`-d`** : Untuk menentukan satu domain yang akan di-scrape.
  - Contoh: 
    ```bash
    python3 ajihunter.py -d http://example.com
    ```
    Akan men-scrape file JavaScript dari satu domain `http://example.com`.

- **`-f`** : Untuk menentukan file yang berisi daftar domain (satu domain per baris).
  - Contoh: 
    ```bash
    python3 ajihunter.py -f domains.txt
    ```
    Akan men-scrape file JavaScript dari semua domain yang terdapat dalam file `domains.txt`, dimana setiap domain ada pada satu baris.



## **Persyaratan**
- Pastikan Python dan pip telah terinstal di sistem Anda.

## **Instalasi**

### 1. **Clone Repo dan Install Dependensi**
Untuk menginstal dan menggunakan `python3 ajihunter.py`, Anda bisa menjalankan perintah berikut di terminal:

```bash
git clone https://github.com/mas4ji/ajihunter.git && cd ajihunter && python3 ajihunter.py
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
Alat ini ditujukan untuk tujuan pendidikan dan audit keamanan. Pastikan Anda memiliki izin eksplisit sebelum melakukan scraping pada situs web apa pun. Pencipta tidak bertanggung jawab atas segala kerusakan atau aktivitas ilegal yang disebabkan oleh penyalahgunaan alat ini.
