from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkToplevel, CTkEntry, CTkOptionMenu
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
                            text='Kegiatan Web Development Community',
                            text_color='black',
                            font=('century gothic', 30, 'bold'),
                            fg_color="#ffffff",
                            height=50,
                            corner_radius=10
                            )
        self.judul.grid(row=0,
                        column=0,
                        columnspan=3,
                        padx=50,
                        pady=2,
                        sticky='nsew')
        self.grid_columnconfigure(0, weight=1)  # kiri
        self.grid_columnconfigure(1, weight=0)  # tengah (card)
        self.grid_columnconfigure(2, weight=1)  # kanan
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
#=========================================
#Card 1 SELURUH KEGIATAN
        self.kartu_satu=CTkFrame(self,
                               height=120,
                               fg_color="#ffffff",
                               width=800,
                               border_width=2,
                               border_color='#0611ad',)
        self.kartu_satu.grid(row=1,
                           column=1,
                           #columnspan=2,
                           padx=50,
                           pady=10,
                           #sticky='nsew'
                           )
        self.kartu_satu.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_satu.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_satu.grid_propagate(False)
# Label Total Kegiatan 
        self.label_total = CTkLabel(self.kartu_satu,
                                  text='Total Kegiatan',
                                  text_color='black',
                                  anchor='center',
                                  fg_color='transparent',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_total.grid(row=0,
                           column=0,
                           padx=10,
                           pady=(6, 6))
# isi total kegiatan 
        total=self.get_total_kegiatan()
        self.btn_total = CTkButton(self.kartu_satu,
                                  text='Total kegiatan: '+str(total)+'\nKlik untuk melihat, menambah, mengedit, atau menambah kegiatan',
                                  height=70,
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
                           pady=2)
#==================================================
#Card 2 KEGIATAN MENDATANG
        self.kartu_dua=CTkFrame(self,
                               height=120,
                               fg_color="#ffffff",
                               width=800,
                               border_width=2,
                               border_color='#0611ad',)
        self.kartu_dua.grid(row=2,
                           column=1,
                           #columnspan=3,
                           padx=50,
                           pady=10,
                           #sticky='nsew'
                           )
        self.kartu_dua.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_dua.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_dua.grid_propagate(False)
# Label KEGIATAN MENDATANG
        self.label_datang = CTkLabel(self.kartu_dua,
                                  text='Akan Datang',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_datang.grid(row=0,
                           column=0,
                           padx=10,
                           pady=(6, 6))
# isi KEGIATAN MENDATANG
        total_mendatang=self.get_kegiatan_mendatang()
        self.btn_mendatang = CTkButton(self.kartu_dua,
                                  text=f'Total kegiatan akan datang : {total_mendatang}\nKlik untuk melihat detail',
                                  height=70,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 15, 'bold'),
                                  command=self.open_detail_kegiatan_mendatang
        )
        self.btn_mendatang.grid(row=1,
                           column=0,
                           padx=5,
                           pady=2)
#=========================================================
#Card 3 KEGIATAN SLESAI
        self.kartu_tiga=CTkFrame(self,
                               height=120,
                               fg_color="#ffffff",
                               width=800,
                               border_width=2,
                               border_color='#0611ad',)
        self.kartu_tiga.grid(row=3,
                           column=1,
                           #columnspan=3,
                           padx=50,
                           pady=10,
                           #sticky='nsew'
                           )
        self.kartu_tiga.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_tiga.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_tiga.grid_propagate(False)
# Label KEGIATAN SLESAI
        self.label_selesai = CTkLabel(self.kartu_tiga,
                                  text='Selesai',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_selesai.grid(row=0,
                           column=0,
                           padx=10,
                           pady=(6,6))
# isi KEGIATAN SLESAI
        total_selesai=self.get_kegiatan_selesai()
        self.btn_selesai = CTkButton(self.kartu_tiga,
                                  text=f'Total kegiatan selesai : {total_selesai}\nKlik untuk melihat detail',
                                  height=70,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 15, 'bold'),
                                  command=self.open_detail_kegiatan_selesai
        )
        self.btn_selesai.grid(row=1,
                           column=0,
                           padx=5,
                           pady=2)
#=========================================================
#Card 4 KEGIATAN Tak terlaksanana
        self.kartu_empat=CTkFrame(self,
                               height=120,
                               fg_color="#ffffff",
                               width=800,
                               border_width=2,
                               border_color='#0611ad',)
        self.kartu_empat.grid(row=4,
                           column=1,
                           #columnspan=3,
                           padx=50,
                           pady=10,
                           #sticky='nsew'
                           )
        self.kartu_empat.columnconfigure(0, weight=1)#Konfigurasi kolom didalam frame
        self.kartu_empat.rowconfigure((0,1), weight=1)#Konfigurasi baris didalam frame
        self.kartu_empat.grid_propagate(False)
# Label KEGIATAN tak terlaksana
        self.label_tak_terlaksana = CTkLabel(self.kartu_empat,
                                  text='Tidak Terlaksana',
                                  text_color='black',
                                  anchor='center',
                                  font=('century gothic', 20, 'bold'),
        )
        self.label_tak_terlaksana.grid(row=0,
                           column=0,
                           padx=10,
                           pady=(6,6))
# isi KEGIATAN tak terlaksana
        total_tak_terlaksana=self.get_kegiatan_tak_terlaksana()
        self.btn_tak_terlaksana = CTkButton(self.kartu_empat,
                                  text=f'Total kegiatan Tak terlaksana : {total_tak_terlaksana}\nKlik untuk melihat detail',
                                  height=70,
                                  corner_radius=10,
                                  fg_color= "#4256c6",
                                  hover_color= "#0356fc",
                                  text_color='black',
                                  font=('century gothic', 15, 'bold'),
                                  command=self.open_detail_kegiatan_tak_terlaksana
        )
        self.btn_tak_terlaksana.grid(row=1,
                           column=0,
                           padx=5,
                           pady=2)
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
#Fungsi membuka pop up kegiatan tak terlaksana
    def open_detail_kegiatan_tak_terlaksana(self):
        Total_kegiatan_tak_terlaksana(self)
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
# fungsi total kegiatan tak terlaksana dari database
    def get_kegiatan_tak_terlaksana(self):
        cursor=self.db.cursor()
        cursor.execute("SELECT COUNT(*) from kegiatan WHERE status='Tidak Terlaksana'")
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
        self.frame.pack_propagate(False)
#Form cari total kegiatan 
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Cari Kegiatan......')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
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
#fungsi tambah
    def tambah(self):
        kegiatan_form(self)
#Fungsi untuk selected data unutk di edit
    def edit_data(self):
        selected_item=self.tabel.selection()
        if not selected_item:
            messagebox.showwarning('Peringatan', 'Silahkan pilih baris di tabel terlebih dahulu')
            return
        item_data = self.tabel.item(selected_item[0])['values']
        data_kegiatan = {
            'id_keg': item_data[0],
            'nama_keg' : item_data[1],
            'tgl_keg' : item_data[2],
            'tempat' : item_data [3],
            'status' : item_data [4]
        }
        kegiatan_form(self, kegiatan=data_kegiatan)
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
                cursor.execute('Delete from kegiatan where id_keg=%s', (id,))
                self.conn.commit()
                messagebox.showinfo('informasi', 'Data berhasil dihapus')
                self.load_kegiatan()
            except Exception as e:
                messagebox.showerror('error', f'Gagagl menghapus:{str(e)}')
            # finally:
            #     if self.conn:
            #         self.conn.close()
#Class untuk tambah dan edit data
class kegiatan_form(CTkToplevel):
    def __init__(self, parent, kegiatan=None):
        super().__init__(parent,
                         fg_color="white")
        self.parent = parent
        self.kegiatan = kegiatan
        title = 'Edit Kegiatan' if self.kegiatan else 'Tambah Kegiatan'
        self.title(title)
        self.geometry('400x500+500+200')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
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
#Label Nama kegiatan
        self.label_nama = CTkLabel(self.frame_body,
                              text='Nama',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_nama.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#entry nama kegiatan
        self.entry_nama = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_nama.grid(row=0, column=1, padx=10, pady=10)
#Label tgl kegiatan
        self.label_tgl_keg = CTkLabel(self.frame_body,
                              text='Tanggal Kegiatan',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_tgl_keg.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#entry tgl kegiatan
        self.entry_tgl_keg = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_tgl_keg.grid(row=1, column=1, padx=10, pady=10)
#Label tempat
        self.label_tempat = CTkLabel(self.frame_body,
                              text='Tempat',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_tempat.grid(row=2, column=0, padx=10, pady=10, sticky='w')
#entry tempat
        self.entry_tempat = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_tempat.grid(row=2, column=1, padx=10, pady=10)
#Label status
        self.label_status = CTkLabel(self.frame_body,
                              text='status',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_status.grid(row=3, column=0, padx=10, pady=10, sticky='w')
#entry status
        self.entry_status = CTkOptionMenu(self.frame_body,
                                          width=250,
                                          height=30,
                                          values=["Belum", "Sudah", "Tidak Terlaksana"])
        self.entry_status.grid(row=3, column=1, padx=10, pady=10)
#Untuk mengisi form otomatis ketika mode edit
        if self.kegiatan:
            self.entry_nama.insert(0, self.kegiatan['nama_keg'])
            self.entry_tgl_keg.insert(0, self.kegiatan['tgl_keg'])
            self.entry_tempat.insert(0, self.kegiatan['tempat'])
            self.entry_status.set(self.kegiatan['status'])
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
        nama=self.entry_nama.get()
        tgl_keg=self.entry_tgl_keg.get()
        tempat=self.entry_tempat.get()
        status=self.entry_status.get()
        if not nama or not tgl_keg:
            messagebox.showwarning('Peringatan', 'Nama dan tgl_keg wajib diisi')
            return
        
        from config.database import Database
        if self.kegiatan:
            sql = "UPDATE kegiatan set nama_keg=%s, tgl_keg=%s, tempat=%s, status=%s WHERE id_keg=%s"
            val = (nama, tgl_keg, tempat, status, self.kegiatan['id_keg'])
        else:
            sql = "INSERT INTO kegiatan(nama_keg, tgl_keg, tempat, status) VALUES (%s, %s, %s, %s)"
            val = (nama, tgl_keg, tempat, status)
#apalah niiii
        try:
            self.conn=Database().get_connection()
            cursor = self.conn.cursor()
            cursor.execute(sql,val)
            self.conn.commit()
            messagebox.showinfo('Sukses', 'Data berhasil di simpan')
            self.parent.load_kegiatan()
            self.destroy() 
        except Exception as e:
            messagebox.showerror('error', f'Gagal Menyimpan:{str(e)}')
        finally:
            if hasattr(self, 'conn') and self.conn:
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
#definisi cari kegiatan selesai
    def cari_kegiatan_selesai(self, event):
        nama = self.entry_search.get()
        self.load_kegiatan_selesai(nama)
# Load untuk kegiatan selesai Menyambungkan dengan database
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
#Tak terlaksana POP UP
class Total_kegiatan_tak_terlaksana(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color='white')
        self.parent = parent
        self.user=user
        title='Kegiatan WebDevComm Tidak Terlaksana'
        self.title(title)
        self.geometry('900x550+300+120')
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.focus()
#frame kegiatan tak terlaksana
        self.frame=CTkFrame(self,
                            fg_color='white',
                            height=80)
        self.frame.pack(fill='x')
        self.frame.pack_propagate(False)
#Form cari kegiatan tak lterlaksana
        self.entry_search=CTkEntry(self.frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Cari Kegiatan tak terlaksana......')
        self.entry_search.grid(row=0, column=4, padx=10, pady=10)
#Tabel Data kegiatan Tak terlaksana
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
        self.load_kegiatan_tak_terlaksana()
        self.entry_search.bind('<KeyRelease>', self.cari_kegiatan_tak_terlaksana)
#definisi cari kegiatan mendatang
    def cari_kegiatan_tak_terlaksana(self, event):
        nama = self.entry_search.get()
        self.load_kegiatan_tak_terlaksana(nama)
# Load untuk kegiatan mendatang Menyambungkan dengan database
    def load_kegiatan_tak_terlaksana(self, nama=''):
        try:
            self.conn=Database().get_connection()
            cursor=self.conn.cursor()
            cursor.execute(""" SELECT * FROM kegiatan WHERE status='Tak Terlaksana' AND nama_keg LIKE %s """, ('%'+nama+'%',))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=row)
        finally:
            if self.conn:
                self.conn.close()