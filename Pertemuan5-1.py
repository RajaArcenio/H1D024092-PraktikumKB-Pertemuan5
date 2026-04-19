import tkinter as tk

class AplikasiPakarDeteksiPenyakit(tk.Tk):
    def __init__(self):
        super().__init__()
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
        
        self.gejala_terpilih = {}
        
        self.title("Sistem Pakar Deteksi Penyakit THT")
        self.geometry("790x890")
        
        self.halaman_welcome = tk.Frame(self)
        self.halaman_daftar_gejala = tk.Frame(self)
        self.halaman_hasil = tk.Frame(self)
        
        self.buat_halaman_welcome()
        self.buat_halaman_daftar_gejala()
        self.buat_halaman_hasil()
        
        self.tampilkan_halaman(self.halaman_welcome)
    
    def tampilkan_halaman(self, halaman):
        for frame in (self.halaman_welcome, self.halaman_daftar_gejala, self.halaman_hasil):
            frame.pack_forget()
        
        halaman.pack(fill="both", expand=True)
    
    def buat_halaman_welcome(self):
        tk.Label(self.halaman_welcome, text="Selamat datang di Sistem Pakar Deteksi Penyakit", font=("Arial", 18), wraplength=350)
        tk.Button(self.halaman_welcome, text="Mulai Diagnosa", font=("Arial", 18), command=lambda: self.tampilkan_halaman(self.halaman_daftar_gejala)).pack(pady=300)

    def buat_halaman_daftar_gejala(self):
        tk.Label(self.halaman_daftar_gejala, text="Pilih gejala yang Anda alami:", font=("Arial", 18, "bold")).pack(pady=10)

        kontainer_tengah = tk.Frame(self.halaman_daftar_gejala)
        kontainer_tengah.pack(fill="both", expand=True, padx=20)

        frame_kiri = tk.Frame(kontainer_tengah)
        frame_kiri.pack(side="left", fill="both", expand=True)

        frame_kanan = tk.Frame(kontainer_tengah)
        frame_kanan.pack(side="left", fill="both", expand=True)

        for i, (kode, gejala) in enumerate(self.data_gejala.items()):
            var = tk.BooleanVar()
            self.gejala_terpilih[kode] = var
            
            target_frame = frame_kiri if i <= len(self.data_gejala) // 2 else frame_kanan
            
            cb = tk.Checkbutton(target_frame, font=("Arial", 15),text=f"{kode} - {gejala}", variable=var)
            cb.pack(anchor="w", pady=2)

        frame_bawah = tk.Frame(self.halaman_daftar_gejala)
        frame_bawah.pack(side="bottom", fill="x", pady=20)
        
        tk.Button(frame_bawah, text="Proses Diagnosa", font=("Arial", 18), command=self.proses_diagnosa).pack()
    
    def buat_halaman_hasil(self):
        self.label_hasil = tk.Label(self.halaman_hasil, text="", font=("Arial", 15), justify="left", wraplength=400)
        self.label_hasil.pack(pady=30, padx=20)
        
        tk.Button(self.halaman_hasil, text="Kembali ke Awal", font=("Arial", 18), command=self.reset_dan_kembali).pack()
    
    def proses_diagnosa(self):
        gejala_pasien = [kode for kode, var in self.gejala_terpilih.items() if var.get()]
        
        hasil = []
        for penyakit, syarat in self.data_penyakit.items():
            if all(s in gejala_pasien for s in syarat):
                hasil.append(penyakit)
        
        desk_gejala_terpilih = [self.data_gejala[kode] for kode in gejala_pasien]
        
        if gejala_pasien and hasil:
            self.kesimpulan = "Dari gejala yang Anda pilih:\n- " + "\n- ".join(desk_gejala_terpilih) + "\n\nAnda terdeteksi memiliki penyakit:\n-" + "\n- ".join(hasil)
        elif gejala_pasien and not hasil:
            self.kesimpulan = "Dari gejala yang Anda pilih:\n- " + "\n- ".join(desk_gejala_terpilih) + "\nTidak terdeteksi penyakit yang sesuai.\nSilakan konsultasikan dengan dokter untuk pemeriksaan lebih lanjut."
        else:
            self.kesimpulan = "Anda belum memilih gejala apapun.\nSilakan pilih gejala yang Anda alami untuk mendapatkan hasil diagnosa."
        
        self.label_hasil.config(text=self.kesimpulan)
        self.tampilkan_halaman(self.halaman_hasil)
    
    def reset_dan_kembali(self):
        for var in self.gejala_terpilih.values():
            var.set(False)
        self.tampilkan_halaman(self.halaman_welcome)

if __name__ == "__main__":
    app = AplikasiPakarDeteksiPenyakit()
    app.mainloop()