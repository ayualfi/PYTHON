from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkToplevel, CTkEntry
from tkinter import messagebox, ttk
from config.database import Database

class KegiatanPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, 
                         fg_color='white',
                         )
        db=Database()
        self.db=db.get_connection()
        self.columnconfigure((0,1,2), weight=1)
#Judul
        self.judul=CTkLabel(self,
                            text='Kegiatan DevWebComm',
                            text_color='black',
                            font=('century gothic', 50, 'bold'),
                            fg_color="#ffffff",
                            height=100,
                            corner_radius=10
                            )
        self.judul.grid(row=0,
                        column=0,
                        columnspan=3,
                        padx=50,
                        pady=7,
                        sticky='nsew')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
#=========================================
#Card 1 SELURUH KEGIATAN
        self.kartu_satu=CTkFrame(self,
                               height=80,
                               fg_color="#0611ad",)
        self.kartu_satu.grid(row=1,
                           column=0,
                           columnspan=3,
                           padx=50,
                           pady=1,
                           sticky='nsew')
        self.kartu_satu.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_satu.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_satu.grid_propagate(False)
# Label anggota
        self.label_total = CTkLabel(self.kartu_satu,
                                  text='Total Kegiatan',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_total.grid(row=0,
                           column=0,
                           padx=10,
                           pady=0)
# isi kegiatan
        total=self.get_total_kegiatan()
        self.btn_total = CTkButton(self.kartu_satu,
                                  text='Total kegiatan: '+str(total)+'\nKlik untuk melihat detail',
                                  height=40,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 15, 'bold'),
                                  command=self.open_detail_kegiatan
        )
        self.btn_total.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
#==================================================
#Card 2
        self.kartu_dua=CTkFrame(self,
                               height=80,
                               fg_color="#03850E",)
        self.kartu_dua.grid(row=2,
                           column=0,
                           columnspan=3,
                           padx=50,
                           pady=1,
                           sticky='nsew')
        self.kartu_dua.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_dua.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_dua.grid_propagate(False)
# Label anggota
        self.label_datang = CTkLabel(self.kartu_dua,
                                  text='Akan Datang',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_datang.grid(row=0,
                           column=0,
                           padx=10,
                           pady=0)
# isi kegiatan
        total_mendatang=self.get_kegiatan_mendatang()
        self.btn_mendatang = CTkButton(self.kartu_dua,
                                  text=f'Total kegiatan akan datang : {total_mendatang}\nKlik untuk melihat detail',
                                  height=40,
                                  corner_radius=10,
                                  fg_color= "#42c64b",
                                  hover_color= "#24fc03",
                                  text_color='black',
                                  font=('century gothic', 15, 'bold'),
                                  command=self.open_detail_kegiatan_mendatang
        )
        self.btn_mendatang.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
#=========================================================
#Card 3
        self.kartu_tiga=CTkFrame(self,
                               height=80,
                               fg_color="#85037C",)
        self.kartu_tiga.grid(row=3,
                           column=0,
                           columnspan=3,
                           padx=50,
                           pady=1,
                           sticky='nsew')
        self.kartu_tiga.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_tiga.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_tiga.grid_propagate(False)
# Label anggota
        self.label_datang = CTkLabel(self.kartu_tiga,
                                  text='Selesai',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_datang.grid(row=0,
                           column=0,
                           padx=10,
                           pady=0)
# isi kegiatan
        total_mendatang=self.get_kegiatan_selesai()
        self.btn_mendatang = CTkButton(self.kartu_tiga,
                                  text=f'Total kegiatan selesai : {total_mendatang}\nKlik untuk melihat detail',
                                  height=40,
                                  corner_radius=10,
                                  fg_color= "#c442c6",
                                  hover_color= "#fc03f8",
                                  text_color='black',
                                  font=('century gothic', 15, 'bold'),
                                  command=self.open_detail_kegiatan_selesai
        )
        self.btn_mendatang.grid(row=1,
                           column=0,
                           padx=5,
                           pady=5)
#=========================================================
#Fungsi fungsi membuka Pop Up
#Fungsi membuka pop_up_total kegiatan
    def open_detail_kegiatan(self):
        Total_kegiatan(self)
#Fungsi membuka pop up kegiatan mendatang
    def open_detail_kegiatan_mendatang(self):
        Total_kegiatan_mendatang(self)
#Fungsi membuka pop up kegiatan selesai
    def open_detail_kegiatan_selesai(self):
        Total_kegiatan_selesai(self)
#=======================================================
#Fungsi fungsi total, mendatang, dan selesai kegiatan
# fungsi total kegiatan dari database
    def get_total_kegiatan(self):
        cursor=self.db.cursor()
        cursor.execute('SELECT COUNT(*) from kegiatan')
        total=cursor.fetchone()[0]
        return total
# fungsi total kegiatan akan datang dari database
    def get_kegiatan_mendatang(self):
        cursor=self.db.cursor()
        cursor.execute("SELECT COUNT(*) from kegiatan WHERE status='Belum'")
        total=cursor.fetchone()[0]
        return total
# fungsi total kegiatan selesai dari database
    def get_kegiatan_selesai(self):
        cursor=self.db.cursor()
        cursor.execute("SELECT COUNT(*) from kegiatan WHERE status='Sudah'")
        total=cursor.fetchone()[0]
        return total
#===================================================
#POP UP KEGIATAN KEGIATAN
#DETAIL KEGIATAN POP UP
class Total_kegiatan(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Kegiatan WebDevComm'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame pop up total kegiatan
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.pack_propagate(False)
        self.frame.columnconfigure(4, weight=1)
#Form cari total kegiatan 
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Cari Kegiatan......')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#Tabel Data total kegiatan
        self.tabel = ttk.Treeview(self,
                                  columns=('id_keg', 'nama_keg', 'tgl_keg', 'tempat', 'status'),
                                  show='headings')
        self.tabel.heading('id_keg', text='Id Kegiatan')
        self.tabel.heading('nama_keg', text='Kegiatan')
        self.tabel.heading('tgl_keg', text='Tanggal Pelaksanaan')
        self.tabel.heading('tempat', text='Lokasi')
        self.tabel.heading('status', text='Status')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=10,
                        padx=15)
        self.load_kegiatan()
        self.entry_search.bind('<KeyRelease>', self.cari_total_kegiatan)
        self.entry_search.bind('<KeyRelease>', self.cari_total_kegiatan)
#definisi cari total kegiatan
    def cari_total_kegiatan(self, event):
        nama = self.entry_search.get()
        self.load_kegiatan(nama)
# Load untuk total kegiatan Menyambungkan dengan database
    def load_kegiatan(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute('select * from kegiatan where nama_keg like %s', ('%'+nama+'%',))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))
        except Exception as e:
            messagebox.showerror('error', str(e))
        finally:
            if self.conn:
                self.conn.close()
#===============================================
#AKAN DATANG POP UP
class Total_kegiatan_mendatang(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Kegiatan WebDevComm'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame kegiatan mendatang
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.frame.pack_propagate(False)
#Form cari kegiatan mendatang
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Cari Kegiatan mendatang......')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#Tabel Data kegiatan mendatang
        self.tabel = ttk.Treeview(self,
                                  columns=('id_keg', 'nama_keg', 'tgl_keg', 'tempat', 'status'),
                                  show='headings')
        self.tabel.heading('id_keg', text='Id Kegiatan')
        self.tabel.heading('nama_keg', text='Kegiatan')
        self.tabel.heading('tgl_keg', text='Tanggal Pelaksanaan')
        self.tabel.heading('tempat', text='Lokasi')
        self.tabel.heading('status', text='Status')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=20,
                        padx=20)
        self.load_kegiatan_mendatang()
        self.entry_search.bind('<KeyRelease>', self.cari_kegiatan_mendatang)
#definisi cari kegiatan mendatang
    def cari_kegiatan_mendatang(self, event):
        nama = self.entry_search.get()
        self.load_kegiatan_mendatang(nama)
# Load untuk kegiatan mendatang Menyambungkan dengan database
    def load_kegiatan_mendatang(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute(""" SELECT * FROM kegiatan WHERE status='Belum' AND nama_keg LIKE %s """, ('%'+nama+'%',))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=row)
        finally:
            if self.conn:
                self.conn.close()
#===============================================
#SELESAI POP UP
class Total_kegiatan_selesai(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Kegiatan selesai WebDevComm'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame kegiatan selesai
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.frame.pack_propagate(False)
#Form cari kegiatan selesai
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Cari Kegiatan selesai......')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#Tabel Data kegiatan selesai
        self.tabel = ttk.Treeview(self,
                                  columns=('id_keg', 'nama_keg', 'tgl_keg', 'tempat', 'status'),
                                  show='headings')
        self.tabel.heading('id_keg', text='Id Kegiatan')
        self.tabel.heading('nama_keg', text='Kegiatan')
        self.tabel.heading('tgl_keg', text='Tanggal Pelaksanaan')
        self.tabel.heading('tempat', text='Lokasi')
        self.tabel.heading('status', text='Status')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=20,
                        padx=20)
        self.load_kegiatan_selesai()
        self.entry_search.bind('<KeyRelease>', self.cari_kegiatan_selesai)
#definisi cari kegiatan mendatang
    def cari_kegiatan_selesai(self, event):
        nama = self.entry_search.get()
        self.load_kegiatan_selesai(nama)
# Load untuk kegiatan mendatang Menyambungkan dengan database
    def load_kegiatan_selesai(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute(""" SELECT * FROM kegiatan WHERE status='Sudah' AND nama_keg LIKE %s """, ('%'+nama+'%',))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=row)
        finally:
            if self.conn:
                self.conn.close()