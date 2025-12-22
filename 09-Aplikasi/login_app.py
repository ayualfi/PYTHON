from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import messagebox


class AppLogin(CTk):
    def __init__(self):
        super().__init__()
        self.title("Login Aplikasi Kasir")
        self.geometry("600x400+500+100")
        self.configure(fg_color='#20244d')
#Frame nya
        self.frame=CTkFrame(master=self, 
                            width=600, 
                            height=300, 
                            fg_color='#fafcfc', 
                            corner_radius=20)
        self.frame.propagate(False)#agar tetap, tidak mengikuti objek
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
        # self.frame.grid(row=0, column=3, padx=30, pady=30, sticky="ew")
        # self.frame.grid_columnconfigure(0, weight=1)
#Nama judul frame
        self.judul = CTkLabel(self.frame,
                              text='Autentifikasi User',
                              text_color='#3b4ba8',
                              font=('Tahoma', 15, 'bold'))
        self.judul.grid(row=0, column=0, padx=30, pady=15, sticky="ew")
        # self.judul.grid_columnconfigure(0, weight=1)
#Input nama
        self.username=CTkEntry(self.frame,
                               placeholder_text="Username",
                               width=200,
                               height=40,
                               corner_radius=15,
                               fg_color='#c5cce0')
        self.username.grid(row=1, column=0, padx=30, pady=10, sticky="ew")
        # self.tombol_login.grid_columnconfigure(1, weight=5)
#Password
        self.password=CTkEntry(self.frame,
                               placeholder_text="password",
                               width=200,
                               height=40,
                               corner_radius=15,
                               fg_color='#c5cce0',
                               show='*')
        self.password.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        # self.tombol_login.grid_columnconfigure(2, weight=5)
#Tombol loginnya
        self.tombol_login=CTkButton(master=self.frame,
                                    text="Log in", 
                                    width=200, height=50, 
                                    corner_radius=15, 
                                    fg_color='#20244d', 
                                    hover_color='#3b4ba8',
                                    font=("Arial", 20,),
                                    command=lambda:self.aksi_login())
        # self.tombol_login.pack(pady=20)
        self.tombol_login.grid(row=3, column=0, padx=30, pady=30, sticky="ew")
        # self.tombol_login.grid_columnconfigure(3, weight=5)
#panggil aksi login
    def aksi_login(self):
        from config.database import Database
        conn = Database().get_connection()
        if conn:
            row = conn.cursor()
            row.execute('select * from user where username =%s and password=%s',
                        (self.username.get(),
                         self.password.get()))
            user = row.fetchone()
            if user:
                messagebox.showinfo('informasi', 'Login berhasil')
            else:
                messagebox.showerror('Login Gagal', 'Username atau password salah')
        else:
            messagebox.showerror('Koneksi gagal', 'Konfigurasi kembali basisdata')
#agar jalan
if __name__=="__main__":
    AppLogin().mainloop()
