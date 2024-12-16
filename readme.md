# **Ajihunter - Scraper for JS Files**

Ajihunter adalah alat untuk mengunduh file JavaScript (.js) dari satu domain atau daftar domain. Anda dapat menggunakannya untuk mengunduh skrip yang disematkan di situs web dan menyimpannya ke dalam folder tertentu. Tool ini sangat berguna untuk pengumpulan file JS dari berbagai situs web.

## **Usage**
Silakan gunakan salah satu opsi berikut:
- **`-d`** : Untuk menentukan satu domain yang akan di-scrape.
- **`-f`** : Untuk menentukan file yang berisi daftar domain (satu per baris).
- **`-o`** : Untuk menentukan direktori output tempat file `.js` disimpan (opsional).


## **Prasyarat**
- Pastikan Python dan pip telah terinstal di sistem Anda.

## **Instalasi**

### 1. **Clone Repo dan Install Dependensi**
Untuk menginstal dan menggunakan `ajihunter`, Anda bisa menjalankan perintah berikut di terminal:

```bash
git clone https://github.com/mas4ji/ajihunter.git && cd ajihunter && ./install.sh && ajihunter -h
