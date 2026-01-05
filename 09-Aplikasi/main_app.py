from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
from pages.dashboard import DashboardPage
from pages.user import UserPage

class MainApp(CTk):
    def __init__(self):
        super().__init__()
        self.title('Aplikasi Kasir')
        self.geometry('800x600+400+100')
# left frame
        self.left_frame = CTkFrame(
            self,
            fg_color='#3b4ba8',
            width=300,
            corner_radius=0
        )
        self.left_frame.pack(side='left', fill='y')
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
# judul
        self.judul = CTkLabel(
            self.left_frame,
            text='Kasir App',
            text_color='#101873',
            font=('century gothic', 24, 'bold')
        )
        self.judul.pack(pady=20)
# dashboard button
        self.btn_dashboard = CTkButton(
            self.left_frame,
            text='Dashbord',
            height=40,
            corner_radius=20,
            fg_color= '#3b4ba8',
            hover_color= '#20244d',
            anchor='w',
            command=lambda:self.load_page(DashboardPage) #memanggil dashboard
        )
        self.btn_dashboard.pack(fill = 'x', padx=10)
# user button
        self.btn_user = CTkButton(
            self.left_frame,
            text='User',
            height=40,
            corner_radius=20,
            fg_color= '#3b4ba8',
            hover_color= '#20244d',
            anchor='w',
            command=lambda:self.load_page(UserPage) #memanggil user
        )
        self.btn_user.pack(fill = 'x', padx=10)
# product button
        self.btn_produk = CTkButton(
            self.left_frame,
            text='Product',
            height=40,
            corner_radius=20,
            fg_color= '#3b4ba8',
            hover_color= '#20244d',
            anchor='w'
        )
        self.btn_produk.pack(fill = 'x', padx=10)

        self.load_page(DashboardPage) #agar dashboard tampil dulu

# Metod untuk memanggil file dashboard dan user
    def load_page (self,page):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        page(self.right_frame).pack(fill='both', expand=True)

# main
if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
        