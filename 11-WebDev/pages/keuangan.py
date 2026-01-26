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
        self.kartu_satu.rowconfigure((0,1,2), weight=1)
# Label keuangan
        self.label_user = CTkLabel(self.kartu_satu,
                                  text='Total Saldo',
                                  text_color='#ffffff',
                                  anchor='center',
                                  font=('century gothic', 25, 'bold'),
                                  fg_color="#4256c6",
                                  height=280,
                                  corner_radius=0,
        )
        self.label_user.grid(sticky='new',
                             row=0,
                             column=0,
                             padx=0,
                             pady=0)
# isi keuangan
        saldo=self.get_total_saldo()
        self.isi_user = CTkButton(self.kartu_satu,
                                  text=f"Saldo:{saldo}",
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
        self.isi_user = CTkButton(self.kartu_satu,
                                  text='Click here \nto see detail saldo,\nadd, edit, or delete',
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#6d6d6e",
                                  hover_color= "#5b5b5b",
                                  text_color='black',
                                  font=('century gothic', 20, 'bold'),
                                  command=self.open_detail_saldo
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
        self.kartu_dua.rowconfigure((0,1,2), weight=1)
# Label keuangan
        self.label_kegiatan = CTkLabel(self.kartu_dua,
                                  text='Pemasukan',
                                  text_color='#ffffff',
                                  anchor='center',
                                  font=('century gothic', 25, 'bold'),
                                  fg_color='#4256c6',
                                  height=280,
                                  corner_radius=0,
        )
        self.label_kegiatan.grid(sticky='new',
                             row=0,
                             column=0,
                             padx=0,
                             pady=0)
# isi keuangan
        masuk=self.get_total_pemasukan()
        self.isi_user = CTkButton(self.kartu_dua,
                                  text=f"Masuk: {masuk}",
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
        self.isi_user = CTkButton(self.kartu_dua,
                                  text='Lihat detail',
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#6d6d6e",
                                  hover_color= "#5b5b5b",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold'),
                                  command=self.open_detail_pemasukan
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
        self.kartu_tiga.rowconfigure((0,1,2), weight=1)
# Label keuangan
        self.label_keuangan = CTkLabel(self.kartu_tiga,
                                  text='Pengeluaran',
                                  text_color='#ffffff',
                                  anchor='center',
                                  font=('century gothic', 25, 'bold'),
                                  fg_color='#4256c6',
                                  height=280,
                                  corner_radius=0,
        )
        self.label_keuangan.grid(sticky='new',
                             row=0,
                             column=0,
                             padx=0,
                             pady=0)
# isi keuangan
        keluar=self.get_total_pengeluaran()
        self.isi_user = CTkButton(self.kartu_tiga,
                                  text=f"Keluar: {keluar}",
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
        self.isi_user = CTkButton(self.kartu_tiga,
                                  text='Lihat detail',
                                  height=50,
                                  corner_radius=0,
                                  fg_color= "#6d6d6e",
                                  hover_color= "#5b5b5b",
                                  text_color='black',
                                  font=('century gothic', 25, 'bold'),
                                  command=self.open_detail_pengeluaran
        )
        self.isi_user.grid(row=2,
                           column=0,
                           padx=0,
                           pady=0,
                           sticky='sew')
#=========================================================
#Fungsi fungsi membuka Pop Up
#Fungsi membuka pop_up_total kegiatan
    def open_detail_saldo(self):
        Total_saldo(self)
#Fungsi membuka pop up kegiatan mendatang
    def open_detail_pemasukan(self):
        Total_pemasukan(self)
#Fungsi membuka pop up kegiatan selesai
    def open_detail_pengeluaran(self):
        Total_pengeluaran(self)
#============================================
#Fungsi fungsi total, mendatang, dan selesai kegiatan
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
# fungsi total keuangan dari database
    def get_total_saldo(self):
        return self.get_total_pemasukan() - self.get_total_pengeluaran()
#==========================
#Total saldo POP UP
class Total_saldo(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Saldo WebDevComm'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame total saldo
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.frame.pack_propagate(False)
#Form cari total saldo
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Saldo kegiatan apa?')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#=================================================
#Tombol Tambah
        self.btn_add=CTkButton(self.frame,
                               text='Add',
                               width=100,
                               height=30,
                               corner_radius=10,
                               fg_color='#20244d',
                               hover_color='#3b4ba8',
                               command=lambda:self.tambah()
                               )
        self.btn_add.grid(row=0, column=5, padx=10, pady=10)
#Tombol Edit
        self.btn_edit=CTkButton(self.frame,
                               text='Edit',
                               width=100,
                               height=30,
                               corner_radius=10,
                               fg_color='#20244d',
                               hover_color='#3b4ba8',
                               command=lambda:self.edit_data()
                               )
        self.btn_edit.grid(row=0, column=6, padx=10, pady=10)
#Tombol Delete
        self.btn_hapus=CTkButton(self.frame,
                               text='Delete',
                               width=100,
                               height=30,
                               corner_radius=10,
                               fg_color='#ff0303',
                               hover_color='#b30202',
                               command=self.hapus
                               )#Memanggil fungsi delete
        self.btn_hapus.grid(row=0, column=7, pady=10)
#Tabel Data total saldo
        self.tabel = ttk.Treeview(self,
                                  columns=('id_keu', 'tgl_trans', 'jenis', 'jumlah', 'nama_keg', 'keterangan'),
                                  show='headings')
        self.tabel.heading('id_keu', text='Id Keuangan')
        self.tabel.heading('tgl_trans', text='Tanggal Transaksi')
        self.tabel.heading('jenis', text='Jenis (Masuk/keluar)')
        self.tabel.heading('jumlah', text='Jumlah Uang')
        #self.tabel.heading('kegiatan_id', text='Nama Kegiatan')
        self.tabel.heading('nama_keg', text='Nama Kegiatan')
        self.tabel.heading('keterangan', text='Keterangan')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=20,
                        padx=20)
        self.load_total_saldo()
        self.entry_search.bind('<KeyRelease>', self.cari_total_saldo)
#Atur lebar kolom
        self.tabel.column('id_keu', width=80, anchor='center')
        self.tabel.column('tgl_trans', width=120, anchor='center')
        self.tabel.column('jenis', width=100, anchor='center')
        self.tabel.column('jumlah', width=120, anchor='center')
        #self.tabel.column('kegiatan_id', width=80, anchor='center')
        self.tabel.column('nama_keg', width=200, anchor='center')
        self.tabel.column('keterangan', width=150, anchor='center')
#definisi cari total saldo
    def cari_total_saldo(self, event):
        nama = self.entry_search.get()
        self.load_total_saldo(nama)
# Load untuk total saldo Menyambungkan dengan database
    def load_total_saldo(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute(""" 
                        SELECT 
                           keu.id_keu,
                           keu.tgl_trans,
                           keu.jenis,
                           keu.jumlah,
                           keg.nama_keg,
                           keu.keterangan
                        FROM keuangan keu
                        LEFT JOIN kegiatan keg
                           ON keu.kegiatan_id=keg.id_keg
                        WHERE keg.nama_keg LIKE %s
                        """, (f"%{nama}%",))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=row)
        finally:
            if self.conn:
                self.conn.close()
#Fungsi Fungsi tombol
#fungsi tambah
    def tambah(self):
        keuangan_form(self)
#Fungsi untuk selected data unutk di edit
    def edit_data(self):
        selected_item=self.tabel.selection()
        if not selected_item:
            messagebox.showwarning('Peringatan', 'Silahkan pilih baris di tabel terlebih dahulu')
            return
        item_data = self.tabel.item(selected_item[0])['values']
        data_keuangan = {
            'id_keu': item_data[0],
            'tgl_trans' : item_data[1],
            'jenis' : item_data[2],
            'jumlah' : item_data [3],
            'nama_keg' : item_data [4],
            'keterangan' : item_data [5]
        }
        keuangan_form(self, keuangan=data_keuangan)
#fungsi Delete
    def hapus(self):
        item=self.tabel.selection()
        if not item:
            messagebox.showwarning('peringatan', 'belum ada data yang dihapus')
            return
        id=self.tabel.item(item[0])['values'][0]
        konfirmasi=messagebox.askyesno('konfirimasi', 'Apkah anda yakin ingin menghapus data ini?')
        if konfirmasi:
            try:
                self.conn=Database().get_connection()
                cursor=self.conn.cursor()
                cursor.execute('DELETE FROM keuangan where id_keu=%s', (id,))
                self.conn.commit()
                messagebox.showinfo('informasi', 'Data berhasil dihapus')
                self.load_total_saldo()
            except Exception as e:
                messagebox.showerror('error', f'Gagagl menghapus:{str(e)}')
            # finally:
            #     if self.conn:
            #         self.conn.close()
#Class untuk tambah dan edit data
class keuangan_form(CTkToplevel):
    def __init__(self, parent, keuangan=None):
        super().__init__(parent,
                         fg_color="white")
        self.parent = parent
        self.keuangan = keuangan
        title = 'Edit Keuangan' if self.keuangan else 'Tambah Keuangan'
        self.title(title)
        self.geometry('400x500+500+200')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
        self.kegiatan_map={} # untuk nama: id
        kegiatan_list=[]
        for id_keg, nama_keg in self.get_kegiatan():
            self.kegiatan_map[nama_keg]=id_keg
            kegiatan_list.append(nama_keg)
#Frame nya
        self.frame_top = CTkFrame(self, 
                                  fg_color='white',
                                  height=80)
        self.frame_top.pack(fill='x')
#judul
        self.title=CTkLabel(self.frame_top,
                            text=title,
                            font=('century gothic', 24, 'bold'), 
                            anchor='w', 
                            compound='left',
                            text_color='#20244d')
        self.title.pack(pady=10, padx=10, anchor='w')
#Frame body
        self.frame_body = CTkFrame(self,
                                   fg_color='white')
        self.frame_body.propagate(False)
        self.frame_body.pack(fill='x')
#Nama nya
#Label tanggal transaksi keuangan
        self.label_tgl_trans = CTkLabel(self.frame_body,
                              text='Tanggal Transaksi',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_tgl_trans.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#entry tgl_trans keuangan
        self.entry_tgl_trans = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_tgl_trans.grid(row=0, column=1, padx=10, pady=10)
#Label jenis keuangan
        self.label_jenis = CTkLabel(self.frame_body,
                              text='Jenis',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_jenis.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#entry jenis keuangan
        self.entry_jenis = CTkOptionMenu(self.frame_body,
                                 width=250,
                                 height=30,
                                 values=["masuk", "keluar"])
        self.entry_jenis.grid(row=1, column=1, padx=10, pady=10)
#Label jumlah
        self.label_jumlah = CTkLabel(self.frame_body,
                              text='Jumlah nominal',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_jumlah.grid(row=2, column=0, padx=10, pady=10, sticky='w')
#entry jumlah
        self.entry_jumlah = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_jumlah.grid(row=2, column=1, padx=10, pady=10)
#Label Kegiatan_id
        self.label_kegiatan_id = CTkLabel(self.frame_body,
                              text='Nama Kegiatan',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_kegiatan_id.grid(row=3, column=0, padx=10, pady=10, sticky='w')
#entry Kegiatan_id
        self.entry_kegiatan_id = CTkOptionMenu(self.frame_body,
                                          width=250,
                                          height=30,
                                          values=kegiatan_list)
        self.entry_kegiatan_id.grid(row=3, column=1, padx=10, pady=10)
#Label keterangan
        self.label_keterangan = CTkLabel(self.frame_body,
                              text='keterangan',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_keterangan.grid(row=4, column=0, padx=10, pady=10, sticky='w')
#entry keterangan
        self.entry_keterangan = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_keterangan.grid(row=4, column=1, padx=10, pady=10)
#Untuk mengisi form otomatis ketika mode edit
        if self.keuangan:
            self.entry_tgl_trans.insert(0, self.keuangan['tgl_trans'])
            self.entry_jenis.set(self.keuangan['jenis'])
            self.entry_jumlah.insert(0, self.keuangan['jumlah'])
            self.entry_kegiatan_id.set(self.keuangan['nama_keg'])
            self.entry_keterangan.insert(0, self.keuangan['keterangan'])
#button save
        self.btn_simpan = CTkButton(self.frame_body,
                                    text='simpan',
                                    height=35,
                                    width=100,
                                    corner_radius=10,
                                    command=lambda:self.simpan())#memanggil fungsi simpan
        self.btn_simpan.grid(row=6, column=1, padx=10, pady=10, sticky='e')
#Fungsi simpan
    def simpan(self):
        tgl_trans=self.entry_tgl_trans.get()
        jenis=self.entry_jenis.get()
        jumlah=self.entry_jumlah.get()
        nama_kegiatan=self.entry_kegiatan_id.get()
        kegiatan_id=self.kegiatan_map[nama_kegiatan]
        keterangan=self.entry_keterangan.get()
        if not tgl_trans or not jenis:
            messagebox.showwarning('Peringatan', 'Tanggal transaksi dan jenis wajib diisi')
            return
        
        from config.database import Database
        if self.keuangan:
            sql = "UPDATE keuangan set tgl_trans=%s, jenis=%s, jumlah=%s, kegiatan_id=%s, keterangan=%s WHERE id_keu=%s"
            val = (tgl_trans, jenis, jumlah, kegiatan_id, keterangan, self.keuangan['id_keu'])
        else:
            sql = "INSERT INTO keuangan(tgl_trans, jenis, jumlah, kegiatan_id, keterangan) VALUES (%s, %s, %s, %s, %s)"
            val = (tgl_trans, jenis, jumlah, kegiatan_id, keterangan)
#apalah niiii
        try:
            self.conn=Database().get_connection()
            cursor = self.conn.cursor()
            cursor.execute(sql,val)
            self.conn.commit()
            messagebox.showinfo('Sukses', 'Data berhasil di simpan')
            self.parent.load_total_saldo()
            self.destroy() 
        except Exception as e:
            messagebox.showerror('error', f'Gagal Menyimpan:{str(e)}')
        finally:
            if hasattr(self, 'conn') and self.conn:
                self.conn.close()
#Fungsi ambil kegiatan
    def get_kegiatan(self):
        conn = Database().get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_keg, nama_keg FROM kegiatan")
        data=cursor.fetchall()
        conn.close()
        return data

#===============================================
#Total pemasukan POP UP
class Total_pemasukan(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Saldo Pemasukan WebDevComm'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame total saldo pemasukan
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.frame.pack_propagate(False)
#Form cari total saldo pemasukan
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Saldo kegiatan apa ?')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#Tabel Data total saldo pemasukan
        self.tabel = ttk.Treeview(self,
                                  columns=('id_keu', 'tgl_trans', 'jenis', 'jumlah', 'nama_keg', 'keterangan'),
                                  show='headings')
        self.tabel.heading('id_keu', text='Id Keuangan')
        self.tabel.heading('tgl_trans', text='Tanggal Transaksi')
        self.tabel.heading('jenis', text='Jenis (Masuk/keluar)')
        self.tabel.heading('jumlah', text='Jumlah Uang')
        self.tabel.heading('nama_keg', text='Nama Kegiatan')
        self.tabel.heading('keterangan', text='Keterangan')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=20,
                        padx=20)
#Atur lebar kolom
        self.tabel.column('id_keu', width=80, anchor='center')
        self.tabel.column('tgl_trans', width=120, anchor='center')
        self.tabel.column('jenis', width=100, anchor='center')
        self.tabel.column('jumlah', width=120, anchor='center')
        #self.tabel.column('kegiatan_id', width=80, anchor='center')
        self.tabel.column('nama_keg', width=200, anchor='center')
        self.tabel.column('keterangan', width=150, anchor='center')
#======================
        self.load_total_saldo_pemasukan()
        self.entry_search.bind('<KeyRelease>', self.cari_total_saldo_pemasukan)
#definisi cari total saldo pemasukan
    def cari_total_saldo_pemasukan(self, event):
        nama = self.entry_search.get()
        self.load_total_saldo_pemasukan(nama)
# Load untuk total saldo pemasukan Menyambungkan dengan database
    def load_total_saldo_pemasukan(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute(""" 
                        SELECT 
                           keu.id_keu,
                           keu.tgl_trans,
                           keu.jenis,
                           keu.jumlah,
                           keg.nama_keg,
                           keu.keterangan
                        FROM keuangan keu
                        LEFT JOIN kegiatan keg
                           ON keu.kegiatan_id=keg.id_keg
                        WHERE LOWER(keu.jenis)='masuk'
                           AND LOWER(keg.nama_keg) LIKE %s
                        """,(f"%{nama.lower()}%",))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=row)
        finally:
            if self.conn:
                self.conn.close()
#===============================================
#Total pengeluaran POP UP
class Total_pengeluaran(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Saldo Pengeluaran WebDevComm'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame total saldo pengeluaran
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.frame.pack_propagate(False)
#Form cari total saldo pengeluaran
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Cari Pengeluaran......')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#Tabel Data total saldo pengeluaran
        self.tabel = ttk.Treeview(self,
                                  columns=('id_keu', 'tgl_trans', 'jenis', 'jumlah', 'nama_keg', 'keterangan'),
                                  show='headings')
        self.tabel.heading('id_keu', text='Id Keuangan')
        self.tabel.heading('tgl_trans', text='Tanggal Transaksi')
        self.tabel.heading('jenis', text='Jenis (Masuk/keluar)')
        self.tabel.heading('jumlah', text='Jumlah Uang')
        self.tabel.heading('nama_keg', text='Nama Kegiatan')
        self.tabel.heading('keterangan', text='Keterangan')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=20,
                        padx=20)
#Atur lebar kolom
        self.tabel.column('id_keu', width=80, anchor='center')
        self.tabel.column('tgl_trans', width=120, anchor='center')
        self.tabel.column('jenis', width=100, anchor='center')
        self.tabel.column('jumlah', width=120, anchor='center')
        #self.tabel.column('kegiatan_id', width=80, anchor='center')
        self.tabel.column('nama_keg', width=200, anchor='center')
        self.tabel.column('keterangan', width=150, anchor='center')
#======================
        self.load_total_saldo_pengeluaran()
        self.entry_search.bind('<KeyRelease>', self.cari_total_saldo_pengeluaran)
#definisi cari total saldo pengeluaran
    def cari_total_saldo_pengeluaran(self, event):
        nama = self.entry_search.get()
        self.load_total_saldo_pengeluaran(nama)
# Load untuk total saldo pengeluaran Menyambungkan dengan database
    def load_total_saldo_pengeluaran(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute(""" 
                        SELECT 
                           keu.id_keu,
                           keu.tgl_trans,
                           keu.jenis,
                           keu.jumlah,
                           keg.nama_keg,
                           keu.keterangan
                        FROM keuangan keu
                        LEFT JOIN kegiatan keg
                           ON keu.kegiatan_id=keg.id_keg
                        WHERE LOWER(keu.jenis)='keluar'
                           AND LOWER(keg.nama_keg) LIKE %s
                        """,(f"%{nama.lower()}%",))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=row)
        finally:
            if self.conn:
                self.conn.close()
#===============================================