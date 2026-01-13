from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from pages.dashboard import DashboardPage
# from pages.user import UserPage

class MainApp(CTk):
    def __init__(self):
        super().__init__()
        self.title('Aplikasi Kasir')
        self.geometry('1200x600+800+600')
        # self.geometry('800x600')
        # self.attributes('-fullscreen', True)
        self.state('zoomed')
# top frame
        self.top_frame = CTkFrame(
            self,
            fg_color="#4256c6",
            width=300,
            corner_radius=0
        )
        self.top_frame.pack(side='top', fill='x')
# bottom frame
        self.bottom_frame = CTkFrame(
            self,
            fg_color='white',
            border_color='white',
            corner_radius=0
        )
        self.bottom_frame.pack(side='bottom', 
                              fill='both', 
                              expand=True, 
                              pady=0, 
                              padx=0)
# judul
        self.judul = CTkLabel(
            self.top_frame,
            text='WebDev Community',
            text_color='#101873',
            font=('century gothic', 24, 'bold')
        )
        self.judul.pack(side='left', padx=20)
# keuangan button
        self.btn_keuangan = CTkButton(
            self.top_frame,
            text='Keuangan',
            height=40,
            corner_radius=20,
            fg_color= "#4256c6",
            hover_color= "#4256c6",
            anchor='w',
            font=('century gothic', 16, 'bold')
        )
        self.btn_keuangan.pack(side='right', padx=1, pady=10)
#Fungsi btn_keuangan ketika hover
        self.btn_keuangan.pack(side='right', padx=1, pady=10)
        def on_enter(event):
            self.btn_keuangan.configure(text_color='#20244d')
        def on_leave(event):
            self.btn_keuangan.configure(text_color='white')
        self.btn_keuangan.bind("<Enter>", on_enter)
        self.btn_keuangan.bind("<Leave>", on_leave)
# Kegiatan button
        self.btn_kegiatan = CTkButton(
            self.top_frame,
            text='Kegiatan',
            height=40,
            corner_radius=20,
            fg_color= "#4256c6",
            hover_color= "#4256c6",
            anchor='w',
            font=('century gothic', 16, 'bold')
        )
        self.btn_kegiatan.pack(side='right', padx=1, pady=10)
#Fungsi btn_kegiatan ketika hover
        self.btn_kegiatan.pack(side='right', padx=1, pady=10)
        def on_enter(event):
            self.btn_kegiatan.configure(text_color='#20244d')
        def on_leave(event):
            self.btn_kegiatan.configure(text_color='white')
        self.btn_kegiatan.bind("<Enter>", on_enter)
        self.btn_kegiatan.bind("<Leave>", on_leave)
# anggota button
        self.btn_user = CTkButton(
            self.top_frame,
            text='Anggota',
            height=40,
            corner_radius=20,
            fg_color= "#4256c6",
            hover_color= "#4256c6",
            anchor='w',
            font=('century gothic', 16, 'bold')
            # command=lambda:self.load_page(UserPage) #memanggil user
        )
        self.btn_user.pack(side='right', padx=1, pady=10)
#Fungsi btn_user ketika hover
        self.btn_user.pack(side='right', padx=1, pady=10)
        def on_enter(event):
            self.btn_user.configure(text_color='#20244d')
        def on_leave(event):
            self.btn_user.configure(text_color='white')
        self.btn_user.bind("<Enter>", on_enter)
        self.btn_user.bind("<Leave>", on_leave)
# dashboard button
        self.btn_dashboard = CTkButton(
            self.top_frame,
            text='Dashbord',
            height=40,
            corner_radius=20,
            fg_color= "#4256c6",
            hover_color= "#4256c6",
            anchor='w',
            font=('century gothic', 16, 'bold'),
            command=lambda:self.load_page(DashboardPage) #memanggil dashboard
        )
#Fungsi btn_dashboard ketika hover
        self.btn_dashboard.pack(side='right', padx=1, pady=10)
        def on_enter(event):
            self.btn_dashboard.configure(text_color='#20244d')
        def on_leave(event):
            self.btn_dashboard.configure(text_color='white')
        self.btn_dashboard.bind("<Enter>", on_enter)
        self.btn_dashboard.bind("<Leave>", on_leave)

        self.load_page(DashboardPage) #agar dashboard tampil dulu

# Metod untuk memanggil file dashboard dan user
    def load_page (self,page):
        for widget in self.bottom_frame.winfo_children():
            widget.destroy()
        page(self.bottom_frame).pack(fill='both', expand=True)

# main
if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
        