from customtkinter import CTkFrame, CTkLabel, CTkEntry
from tkinter import messagebox

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
