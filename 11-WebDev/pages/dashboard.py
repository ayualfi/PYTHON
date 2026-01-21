from customtkinter import CTkFrame, CTkLabel, CTkButton
from config.database import Database

class DashboardPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, 
                         fg_color='white',
                         )
        db=Database()
        self.db=db.get_connection()
        self.columnconfigure((0,1,2), weight=1)
#Judul
        self.judul=CTkLabel(self,
                            text='Dashboard',
                            text_color='black',
                            font=('century gothic', 50, 'bold'),
                            fg_color="#0356fc",
                            height=100,
                            corner_radius=10
                            )
        self.judul.grid(row=0,
                        column=0,
                        columnspan=3,
                        padx=50,
                        pady=10,
                        sticky='nsew')
#=========================================
#Card 1
        self.kartu_satu=CTkFrame(self,
                               height=220,
                               fg_color="#030b85",)
        self.kartu_satu.grid(row=1,
                           column=0,
                           padx=50,
                           pady=10,
                           sticky='ew')
        self.kartu_satu.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_satu.grid_propagate(False)
# Label anggota
        self.label_user = CTkLabel(self.kartu_satu,
                                  text='Anggota',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 50, 'bold'),
        )
        self.label_user.grid(row=0,
                           column=0,
                           padx=10,
                           pady=10)
# isi anggota
        total=self.get_total_anggota()
        self.isi_user = CTkButton(self.kartu_satu,
                                  text='Total anggota: '+str(total),
                                  height=50,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
#==================================================
#Card 2
        self.kartu_dua=CTkFrame(self,
                               height=220,
                               fg_color="#030b85",)
        self.kartu_dua.grid(row=1,
                           column=1,
                           padx=50,
                           pady=10,
                           sticky='ew')
        self.kartu_dua.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_dua.grid_propagate(False)
# Label kegiatan
        self.label_kegiatan = CTkLabel(self.kartu_dua,
                                  text='Kegiatan',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 50, 'bold'),
        )
        self.label_kegiatan.grid(row=0,
                           column=0,
                           padx=10,
                           pady=10)
# isi kegiatan
        total=self.get_total_kegiatan()
        self.isi_kegiatan = CTkButton(self.kartu_dua,
                                  text='Total kegiatan: '+str(total),
                                  height=50,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold'),
                                  state='normal'
        )
        self.isi_kegiatan.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
#===============================================================
#Card 2
        self.kartu_tiga=CTkFrame(self,
                               height=220,
                               fg_color="#030b85",)
        self.kartu_tiga.grid(row=1,
                           column=2,
                           padx=50,
                           pady=10,
                           sticky='ew')
        self.kartu_tiga.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_tiga.grid_propagate(False)
# Label keuangan
        self.label_keuangan = CTkLabel(self.kartu_tiga,
                                  text='Keuangan',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 50, 'bold'),
        )
        self.label_keuangan.grid(row=0,
                           column=0,
                           padx=10,
                           pady=10)
# isi keuangan
        saldo=self.get_saldo()
        masuk=self.get_total_pemasukan()
        keluar=self.get_total_pengeluaran()
        self.isi_keuangan = CTkButton(self.kartu_tiga,
                                  text=f"Saldo:{saldo}\nMasuk: {masuk}\nKeluar: {keluar}",
                                  height=50,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold'),
                                  state='normal'
        )
        self.isi_keuangan.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
#===============================================================
#fungsi total pemasukan
    def get_total_pemasukan(self):
        cursor=self.db.cursor()
        cursor.execute("SELECT SUM(jumlah) from keuangan WHERE jenis='masuk'")
        result=cursor.fetchone()[0]
        return result if result else 0
#fungsi total pengeluaran
    def get_total_pengeluaran(self):
        cursor=self.db.cursor()
        cursor.execute("SELECT SUM(jumlah) from keuangan WHERE jenis='keluar'")
        result=cursor.fetchone()[0]
        return result if result else 0
#fungsi total saldo
    def get_saldo(self):
        masuk=self.get_total_pemasukan()
        keluar=self.get_total_pengeluaran()
        return masuk-keluar
# fungsi total anggota dari database
    def get_total_anggota(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT COUNT(*) from anggota')
        total=cursor.fetchone()[0]
        return total
# fungsi total kegiatan dari database
    def get_total_kegiatan(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT COUNT(*) from kegiatan')
        total=cursor.fetchone()[0]
        return total
    
