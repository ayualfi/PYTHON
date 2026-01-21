from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkToplevel
from tkinter import messagebox, ttk
from config.database import Database


class AnggotaPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,
                         fg_color='white',
                         )
        self.configure(width=800)
        self.pack_propagate(False)
#Frame_left
        self.frame_left =CTkFrame(
            self,
            fg_color='#0356fc',
            corner_radius=0,
            height=50,
            width=250
        )
        self.frame_left.pack(side='left', fill='y')
        self.frame_left.propagate(False)
        self.frame_left.columnconfigure(0, weight=3)
        self.frame_left.columnconfigure(1, weight=0)
        self.frame_left.columnconfigure(2, weight=0)
        self.frame_left.columnconfigure(3, weight=0)
        self.frame_left.columnconfigure(4, weight=0)
        self.frame_left.columnconfigure(5, weight=0)
#judul
        self.judul = CTkLabel(self.frame_left,
                              text='Manajemen\n Pengguna',
                              font=('century gothic', 20, 'bold'),
                              anchor='center',
                              compound='left',
                              width=250,
                              bg_color='yellow',
                              text_color='#101873',
                              pady=20)
        self.judul.grid(row=0, column=0, sticky='ew', pady=20)
#Frame untuk tombol
# 0 mengikuti konten
# 1 mengikuti space
#Tombol Tambah
        self.btn_add=CTkButton(self.frame_left,
                               text='Add',
                               width=200,
                               height=50,
                               corner_radius=10,
                               fg_color='#20244d',
                               hover_color='#3b4ba8',
                               command=lambda:self.tambah())
        self.btn_add.grid(row=1, column=0, pady=10)
#Tombol Edit
        self.btn_edit=CTkButton(self.frame_left,
                               text='Edit',
                               width=200,
                               height=50,
                               corner_radius=10,
                               fg_color='#20244d',
                               hover_color='#3b4ba8',
                               command=lambda:self.edit_data())
        self.btn_edit.grid(row=2, column=0, pady=10)
#Tombol Delete
        self.btn_hapus=CTkButton(self.frame_left,
                               text='Delete',
                               width=200,
                               height=50,
                               corner_radius=10,
                               fg_color='#ff0303',
                               hover_color='#b30202',
                               command=self.hapus)#Memanggil fungsi delete
        self.btn_hapus.grid(row=3, column=0, pady=10)
# right frame
        self.right_frame = CTkFrame(
            self,
            fg_color='white',
            border_color='white'
        )
        self.right_frame.pack(side='right', 
                              fill='both', 
                              expand=True, 
                              pady=0, 
                              padx=0)
#Form cari pengguna
        self.entry_search=CTkEntry(self.right_frame,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Find Anggota......')
        self.entry_search.pack(padx=10, pady=10)
#Tabel data
        self.tabel = ttk.Treeview(self.right_frame,
                                  columns=('id_ang', 'nama_ang', 'nim', 'jabatan'),
                                  show='headings')
        self.tabel.heading('id_ang', text='ID')
        self.tabel.heading('nama_ang', text='Nama Lengkap')
        self.tabel.heading('nim', text='NIM')
        self.tabel.heading('jabatan', text='Jabatan')
        self.tabel.column('id_ang', width=50, anchor='center')
        self.tabel.column('nama_ang', width=200, anchor='center')
        self.tabel.column('nim', width=200, anchor='center')
        self.tabel.column('jabatan', width=100, anchor='center')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=10,
                        padx=10)
        self.load_Anggota() #panggil self load Anggota dibawah
        self.entry_search.bind('<KeyRelease>', self.cari_Anggota) #aturan pencarian
#Fungsi cari Anggota
    def cari_Anggota(self, event):
        nama = self.entry_search.get()
        self.load_Anggota(nama)
# Menyambungkan dengan database
    def load_Anggota(self, nama=''):
        from config.database import Database
        try:
            self.conn=Database().get_connection()
            cursor = self.conn.cursor()
            cursor.execute('select * from anggota where nama_ang like %s', ('%'+nama+'%',))
            rows=cursor.fetchall()
            self.tabel.delete(*self.tabel.get_children())
            for row in rows:
                self.tabel.insert('', 'end', values=(row[0], row[1], row[2], row[3]))
        except Exception as e:
            messagebox.showerror('error', str(e))
        finally:
            if self.conn:
                self.conn.close()
#fungsi tambah
    def tambah(self):
        AnggotaForm(self)
#fungsi edit
    # def edit(self):
    #     AnggotaForm(self)
#Fungsi untuk selected data unutk di edit
    def edit_data(self):
        selected_item=self.tabel.selection()
        if not selected_item:
            messagebox.showwarning('Peringatan', 'Silahkan pilih baris di tabel terlebih dahulu')
            return
        item_data = self.tabel.item(selected_item[0])['values']
        data_anggota = {
            'id_ang': item_data[0],
            'nama_ang' : item_data[1],
            'nim' : item_data[2],
            'jabatan' : item_data [3]
        }
        AnggotaForm(self, Anggota=data_anggota)
#fungsi Delete
    def hapus(self):
        item=self.tabel.selection()
        if not item:
            messagebox.showwarning('peringatan', 'belum ada data yang dihapus')
            return
        id=self.tabel.item(item)['values'][0]
        konfirmasi=messagebox.askyesno('konfirimasi', 'Apkah anda yakin ingin menghapus data ini?')
        if konfirmasi:
            try:
                self.conn=Database().get_connection()
                cursor=self.conn.cursor()
                cursor.execute('Delete from anggota where id_ang=%s', (id,))
                self.conn.commit()
                messagebox.showinfo('informasi', 'Data berhasil dihapus')
                self.load_Anggota()
            except Exception as e:
                messagebox.showerror('error', f'Gagagl menghapus:{str(e)}')
            # finally:
            #     if self.conn:
            #         self.conn.close()
#Class untuk tambah dan edit data
class AnggotaForm(CTkToplevel):
    def __init__(self, parent, Anggota=None):
        super().__init__(parent,
                         fg_color="white")
        self.parent = parent
        self.Anggota = Anggota
        title = 'Edit Pengguna' if self.Anggota else 'Tambah Pengguna'
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
#Label Nama
        self.label_nama = CTkLabel(self.frame_body,
                              text='Nama',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_nama.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#entry nama
        self.entry_nama = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_nama.grid(row=0, column=1, padx=10, pady=10)
#Label NIM
        self.label_nim = CTkLabel(self.frame_body,
                              text='NIM',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_nim.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#entry NIM
        self.entry_nim = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_nim.grid(row=1, column=1, padx=10, pady=10)
#Label jabatan
        self.label_jabatan = CTkLabel(self.frame_body,
                              text='Jabatan',
                              font=('century gothic', 12, 'bold'),
                              text_color='#3b4ba8')
        self.label_jabatan.grid(row=2, column=0, padx=10, pady=10, sticky='w')
#entry jabatan
        self.entry_jabatan = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10,
                                 fg_color='white',
                                 border_color="black",
                                 text_color='black')
        self.entry_jabatan.grid(row=2, column=1, padx=10, pady=10)
#Untuk mengisi form otomatis ketika mode edit
        if self.Anggota:
            self.entry_nama.insert(0, self.Anggota['nama_ang'])
            self.entry_nim.insert(0, self.Anggota['nim'])
            self.entry_jabatan.insert(0, self.Anggota['jabatan'])
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
        nim=self.entry_nim.get()
        jabatan=self.entry_jabatan.get()
        if not nama or not nim:
            messagebox.showwarning('Peringatan', 'Nama dan NIM wajib diisi')
            return
        
        from config.database import Database
        if self.Anggota:
            sql = "UPDATE Anggota set nama_ang=%s, nim=%s, jabatan=%s WHERE id_ang=%s"
            val = (nama, nim, jabatan, self.Anggota['id_ang'])
        else:
            sql = "INSERT INTO Anggota(nama_ang, nim, jabatan) VALUES (%s, %s, %s)"
            val = (nama, nim, jabatan)
#apalah niiii
        try:
            self.conn=Database().get_connection()
            cursor = self.conn.cursor()
            cursor.execute(sql,val)
            self.conn.commit()
            messagebox.showinfo('Sukses', 'Data berhasil di simpan')
            self.parent.load_Anggota()
            self.destroy() 
        except Exception as e:
            messagebox.showerror('error', f'Gagal Menyimpan:{str(e)}')
        finally:
            if hasattr(self, 'conn') and self.conn:
                self.conn.close

