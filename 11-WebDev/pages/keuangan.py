from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkToplevel, CTkEntry, CTkOptionMenu
from tkinter import messagebox, ttk
from config.database import Database

class KeuanganPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, 
                         fg_color='white',
                         )
        db=Database()
        self.db=db.get_connection()
        self.columnconfigure((0,1,2), weight=1)
#Judul
        self.judul=CTkLabel(self,
                            text='Keuangan Web Development Community',
                            text_color='black',
                            font=('century gothic', 25, 'bold'),
                            fg_color="#ffffff",
                            height=100,
                            corner_radius=10
                            )
        self.judul.grid(row=0,
                        column=0,
                        columnspan=3,
                        padx=50,
                        pady=5,
                        sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
#=========================================
#Card 1
        self.kartu_satu=CTkFrame(self,
                               height=400,
                               fg_color="#ffffff",
                               border_width=2,
                               border_color='black')
        self.kartu_satu.grid(row=1,
                           column=0,
                           padx=50,
                           pady=5,
                           sticky='ew')
        self.kartu_satu.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_satu.grid_propagate(False)
        self.kartu_satu.rowconfigure(0, weight=0)
        self.kartu_satu.rowconfigure(1, weight=1)
# Label keuangan
        self.label_user = CTkLabel(self.kartu_satu,
                                  text='Total Saldo',
                                  text_color='#ffffff',
                                  anchor='center',
                                  font=('century gothic', 25, 'bold'),
                                  fg_color="#6d6d6e",
                                  height=280,
                                  corner_radius=0,
        )
        self.label_user.grid(sticky='new',
                             row=0,
                             column=0,
                             padx=0,
                             pady=0)
# isi keuangan
        #total=self.get_total_keuangan()
        self.isi_user = CTkButton(self.kartu_satu,
                                  text='Lihat detail: ',#+str(total)
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#ffffff",
                                  hover_color= "#ffffff",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
# Detail keuangan
        #total=self.get_total_keuangan()
        self.isi_user = CTkButton(self.kartu_satu,
                                  text='Lihat detail: ',#+str(total)
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=2,
                           column=0,
                           padx=0,
                           pady=0,
                           sticky='sew')
#==================================================
#Card 2
        self.kartu_dua=CTkFrame(self,
                               height=400,
                               fg_color="#ffffff",
                               border_width=2,
                               border_color='black',
                               )
        self.kartu_dua.grid(row=1,
                           column=1,
                           padx=50,
                           pady=5,
                           sticky='ew')
        self.kartu_dua.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_dua.grid_propagate(False)
        self.kartu_dua.rowconfigure(0, weight=0)
        self.kartu_dua.rowconfigure(1, weight=1)
# Label kegiatan
        self.label_kegiatan = CTkLabel(self.kartu_dua,
                                  text='Pemasukan',
                                  text_color='#ffffff',
                                  anchor='center',
                                  font=('century gothic', 25, 'bold'),
                                  fg_color='#6d6d6e',
                                  height=280,
                                  corner_radius=0,
        )
        self.label_kegiatan.grid(sticky='new',
                             row=0,
                             column=0,
                             padx=0,
                             pady=0)
# isi keuangan
        #total=self.get_total_keuangan()
        self.isi_user = CTkButton(self.kartu_dua,
                                  text='Lihat detail: ',#+str(total)
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#ffffff",
                                  hover_color= "#ffffff",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
# Detail keuangan
        #total=self.get_total_keuangan()
        self.isi_user = CTkButton(self.kartu_dua,
                                  text='Lihat detail: ',#+str(total)
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=2,
                           column=0,
                           padx=0,
                           pady=0,
                           sticky='sew')

#===============================================================
#Card 3
        self.kartu_tiga=CTkFrame(self,
                               height=400,
                               fg_color="#ffffff",
                               border_width=2,
                               border_color='black')
        self.kartu_tiga.grid(row=1,
                           column=2,
                           padx=50,
                           pady=5,
                           sticky='ew')
        self.kartu_tiga.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_tiga.grid_propagate(False)
        self.kartu_tiga.rowconfigure(0, weight=0)
        self.kartu_tiga.rowconfigure(1, weight=1)
# Label keuangan
        self.label_keuangan = CTkLabel(self.kartu_tiga,
                                  text='Pengeluaran',
                                  text_color='#ffffff',
                                  anchor='center',
                                  font=('century gothic', 25, 'bold'),
                                  fg_color='#6d6d6e',
                                  height=280,
                                  corner_radius=0,
        )
        self.label_keuangan.grid(sticky='new',
                             row=0,
                             column=0,
                             padx=0,
                             pady=0)
# isi keuangan
        #total=self.get_total_keuangan()
        self.isi_user = CTkButton(self.kartu_tiga,
                                  text='Lihat detail: ',#+str(total)
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#ffffff",
                                  hover_color= "#ffffff",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
# Detail keuangan
        #total=self.get_total_keuangan()
        self.isi_user = CTkButton(self.kartu_tiga,
                                  text='Lihat detail: ',#+str(total)
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold')
        )
        self.isi_user.grid(row=2,
                           column=0,
                           padx=0,
                           pady=0,
                           sticky='sew')

#===============================================================

# fungsi total keuangan dari database
    # def get_total_keuangan(self):
    #     cursor=self.db.cursor()
    #     cursor.execute('SELECT COUNT(*) from keuangan')
    #     total=cursor.fetchone()[0]
    #     return total