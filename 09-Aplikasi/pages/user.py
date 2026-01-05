from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton
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
                               hover_color='#3b4ba8')
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
                               hover_color='#b30202')
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
