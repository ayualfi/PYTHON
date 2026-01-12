from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkToplevel
from tkinter import messagebox, ttk

class UserPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent,
                         fg_color='white')
#Frame
        self.frame_top =CTkFrame(
            self,
            fg_color='white'
        )
        self.frame_top.pack(fill='x')
#judul
        self.judul = CTkLabel(self.frame_top,
                              text='Manajemen Pengguna',
                              font=('century gothic', 24, 'bold'),
                              anchor='w',
                              compound='left',
                              text_color='black')
        self.judul.pack(side='left', pady=10, padx=10)
#Frame untuk tombol
# 0 mengikuti konten
# 1 mengikuti space
        self.frame_top=CTkFrame(self,
                                fg_color='white',
                                height=50)
        self.frame_top.propagate(False)
        self.frame_top.pack(fill='x', padx=10)
        self.frame_top.columnconfigure(0, weight=0)
        self.frame_top.columnconfigure(1, weight=0)
        self.frame_top.columnconfigure(2, weight=0)
        self.frame_top.columnconfigure(3, weight=1)
        self.frame_top.columnconfigure(4, weight=0)
#Tombol Tambah
        self.btn_add=CTkButton(self.frame_top,
                               text='Add',
                               width=100,
                               height=30,
                               corner_radius=10,
                               fg_color='#20244d',
                               hover_color='#3b4ba8',
                               command=lambda:self.tambah())
        self.btn_add.grid(row=0, column=0)
#Tombol Edit
        self.btn_edit=CTkButton(self.frame_top,
                               text='Edit',
                               width=100,
                               height=30,
                               corner_radius=10,
                               fg_color='#20244d',
                               hover_color='#3b4ba8')
        self.btn_edit.grid(row=0, column=1)
#Tombol Delete
        self.btn_hapus=CTkButton(self.frame_top,
                               text='Delete',
                               width=100,
                               height=30,
                               corner_radius=10,
                               fg_color='#ff0303',
                               hover_color='#b30202',
                               command=lambda:self.hapus())#Memanggil fungsi delete
        self.btn_hapus.grid(row=0, column=2)
#Form cari pengguna
        self.entry_search=CTkEntry(self.frame_top,
                                   width=250,
                                   height=30,
                                   corner_radius=10,
                                   fg_color='#ededf0',
                                   text_color='black',
                                   placeholder_text='Find User......')
        self.entry_search.grid(row=0, column=4, padx=10)
#Tabel data
        self.tabel = ttk.Treeview(self,
                                  columns=('id', 'nama', 'alamat', 'telp'),
                                  show='headings')
        self.tabel.heading('id', text='ID')
        self.tabel.heading('nama', text='Nama Lengkap')
        self.tabel.heading('alamat', text='Alamat Pengguna')
        self.tabel.heading('telp', text='Telepon Pengguna')
        self.tabel.column('id', width=50, anchor='center')
        self.tabel.column('nama', width=200, anchor='w')
        self.tabel.column('alamat', width=200, anchor='w')
        self.tabel.column('telp', width=100, anchor='center')
        self.tabel.pack(fill='both',
                        expand=True,
                        pady=10,
                        padx=10)
        self.load_user() #panggil self load user dibawah
        self.entry_search.bind('<KeyRelease>', self.cari_user) #aturan pencarian
#Definisi cari user
    def cari_user(self, event):
        nama = self.entry_search.get()
        self.load_user(nama)
# Menyambungkan dengan database
    def load_user(self, nama=''):
        from config.database import Database
        try:
            self.conn=Database().get_connection()
            cursor = self.conn.cursor()
            cursor.execute('select * from user where nama_pengguna like %s', ('%'+nama+'%'))
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
        UserForm(self)
#fungsi Delete
    def hapus(self):
        item=self.tabel.selection()
        if not item:
            messagebox.showwarning('peringatan', 'belum ada data yang dihapus')
            return
        id=self.tabel.item(item)['values'][0]
        konfirmasi=messagebox.askyesno('konfirimasi', 'Apkah anda yakin ingin menghapus data ini?')
        if konfirmasi:
            from config.database import Database
            try:
                self.conn=Database().get_connection()
                cursor=self.conn.cursor()
                cursor.execute('Delete from user where id_pengguna=%s', (id,))
                self.conn.commit()
                messagebox.showinfo('informasi', 'Data berhasil dihapus')
                self.load_user()
            except Exception as e:
                messagebox.showerror('error', str(e))
            finally:
                if self.conn:
                    self.conn.close()

#Class untuk tambah dan edit data
class UserForm(CTkToplevel):
    def __init__(self, parent, user=None):
        super().__init__(parent,
                         fg_color="yellow")
        self.parent = parent
        self.user = user
        title = 'ubah pengguna' if self.user else 'tambah pengguna'
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
#Isi frame
#judul
        self.title=CTkLabel(self.frame_top,
                            text=title,
                            font=('century gothic', 24, 'bold'), 
                            anchor='w', 
                            compound='left')
        self.title.pack(pady=10, padx=10, anchor='w')
#Frame body
        self.frame_body = CTkFrame(self,
                                   fg_color='white')
        self.frame_body.propagate(False)
        self.frame_body.pack(fill='x')
#Id nya
#Label id
        self.label_id = CTkLabel(self.frame_body,
                              text='ID Pengguna',
                              font=('century gothic', 12, 'bold'))
        self.label_id.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#entry id
        self.entry_id = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)
#Label nama
        self.label_nama = CTkLabel(self.frame_body,
                              text='nama Pengguna',
                              font=('century gothic', 12, 'bold'))
        self.label_nama.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#entry nama
        self.entry_nama = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10)
        self.entry_nama.grid(row=1, column=1, padx=10, pady=10)
#Label telepon
        self.label_telepon = CTkLabel(self.frame_body,
                              text='Telepon Pengguna',
                              font=('century gothic', 12, 'bold'))
        self.label_telepon.grid(row=2, column=0, padx=10, pady=10, sticky='w')
#entry telepon
        self.entry_telepon = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10)
        self.entry_telepon.grid(row=2, column=1, padx=10, pady=10)
#Label alamat
        self.label_alamat = CTkLabel(self.frame_body,
                              text='alamat Pengguna',
                              font=('century gothic', 12, 'bold'))
        self.label_alamat.grid(row=3, column=0, padx=10, pady=10, sticky='w')
#entry alamat
        self.entry_alamat = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10)
        self.entry_alamat.grid(row=3, column=1, padx=10, pady=10)
#Label username
        self.label_username = CTkLabel(self.frame_body,
                              text='username Pengguna',
                              font=('century gothic', 12, 'bold'))
        self.label_username.grid(row=4, column=0, padx=10, pady=10, sticky='w')
#entry username
        self.entry_username = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10)
        self.entry_username.grid(row=4, column=1, padx=10, pady=10)
#Label password
        self.label_password = CTkLabel(self.frame_body,
                              text='password Pengguna',
                              font=('century gothic', 12, 'bold'))
        self.label_password.grid(row=5, column=0, padx=10, pady=10, sticky='w')
#entry password
        self.entry_password = CTkEntry(self.frame_body,
                                 width=250,
                                 height=30,
                                 corner_radius=10)
        self.entry_password.grid(row=5, column=1, padx=10, pady=10)

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
            id=self.entry_id.get()
            nama=self.entry_nama.get()
            telepon=self.entry_telepon.get()
            alamat=self.entry_alamat.get()
            username=self.entry_username.get()
            password=self.entry_password.get()
            
            from config.database import Database
            if self.user:
                sql = "update user set nama_pengguna=%s, tlp_pengguna=%s "\
                        "alamat_pengguna=%s, username=%s, password=%s where "\
                        "id_pengguna=%s"
            else:
                sql = "insert user set nama_pengguna=%s, tlp_pengguna=%s "\
                        "alamat_pengguna=%s, username=%s, password=%s, "\
                        "id_pengguna=%s"

#apalah niiii
                try:
                    self.conn=Database().get_connection()
                    cursor = self.conn.cursor()
                    cursor.execute(sql,(nama, alamat, telepon, username, password, id))
                    self.conn.commit()
                    self.destroy() 
                except Exception as e:
                    messagebox.showerror('error', str(e))
