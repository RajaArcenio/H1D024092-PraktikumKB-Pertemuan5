# 🖥️ Sistem Pakar Diagnosa Penyakit

## 📌 Deskripsi
Program ini merupakan Sistem Pakar sederhana berbasis python yang digunakan untuk mendiagnosa penyakit berdasarkan gejala yang dimiliki pengguna.

Aplikasi ini menggunakan:
- **Tkinter** untuk antarmuka pengguna yang interaktif.
- **Konsep OOP (Object-Oriented Programming)**.
---

## ⚙️ Fitur dan Alur Kerja
Aplikasi dibagi menjadi tiga bagian utama (Halaman):
1. **Halaman Welcome**: Sambutan awal dan tombol untuk memulai diagnosa.
2. **Halaman Diagnosa**: Menampilkan daftar gejala dalam bentuk Checkbox.
3. **Halaman Hasil**: Menampilkan daftar penyakit yang terdeteksi beserta gejala yang dipilih pengguna.
---

## 🧠 Basis Pengetahuan (Knowledge Base)
Terdapat dua dictionary yang digunakan untuk menyimpan basis pengetahuan yaitu:
1. Data Gejala
```python
self.data_gejala = {
    "G1": "Nafas abnormal",
    "G2": "Suara serak",
    "G3": "Perubahan kulit",
    "G4": "Telinga penuh",
    "G5": "Nyeri bicara menelan",
    "G6": "Nyeri tenggorokan",
    "G7": "Nyeri leher",
    "G8": "Pendarahan hidung",
    "G9": "Telinga berdenging",
    "G10": "Airliur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Beratbadan turun",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir merah",
    "G22": "Benjolan leher",
    "G23": "Tubuh tak seimbang",
    "G24": "Bolamata bergerak",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh dimulut",
    "G29": "Benjolan dileher",
    "G30": "Nyeri antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli",
    "G35": "Mual muntah",
    "G36": "Letih lesu",
    "G37": "Demam"
}
```

2. Data Penyakit
```python
self.data_penyakit = {
    "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
    "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
    "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
    "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
    "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
    "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
    "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
    "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
    "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
    "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
    "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
    "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
    "Contact Ulcers": ["G5", "G2"],
    "Abses Parafaringeal": ["G5", "G16"],
    "Barotitis Media": ["G12", "G20"],
    "Kanker Nafasoring": ["G17", "G8"],
    "Kanker Tonsil": ["G6", "G29"],
    "Neuronitis Vestibularis": ["G35", "G24"],
    "Meniere": ["G20", "G35", "G14", "G4"],
    "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
    "Kanker Leher Metastatik": ["G29"],
    "Osteosklerosis": ["G34", "G9"],
    "Vertigo Postular": ["G24"]
}
```

## 🔄 Alur Program
### 1. Halaman Welcome
Fungsi:
```puthon
buat_halaman_welcome(self)
```
- Menampilkan pesan sambutan dan tombol mulai diagnosa

### 2. Input Gejala
Fungsi:
```python
buat_halaman_daftar_gejala(self)
```
- Menampilkan semua data gejala dalam format checkbox
- Menerima input boolean untuk setiap gejala
- Menyimpan semua kode gejala yang bernilai benar/1

```python
proses_diagnosa(self)
```
- Mengecek apakah semua gejala terpenuhi
- Menyimpan semua penyakit yang gejalanya terpenuhi

### 2. Output
Fungsi:
```python
buat_halaman_hasil(self):
```
Menampilkan kesimpulan diagnosa:
- Semua gejala yang dicentang
- Semua penyakit yang gejalanya dialami pengguna
---

## ▶️ Cara Menjalankan Program
### 1. Pastikan Python sudah terinstall
Ceka pakah python sudah terinstall dengan menjalankan command:
```bash
python --version
```
### 2. Jalankan program:
- tekan tombol play di vs code atau
- jalankan command command berikut di terminal
```bash
python nama_file.py
```
### 3. Inputkan semua gejala yang dialami
- Centang semua gejala yang dialami
- Tekan tomvol Proses diagnosa
---
