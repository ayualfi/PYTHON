from customtkinter import CTkFrame, CTkLabel
class DashboardPage(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, 
                         fg_color='white')
        self.judul=CTkLabel(self,
                            text='Dashbord',
                            text_color='black',
                            font=('century gothic', 24, 'bold'),
                            )
        self.judul.pack(pady=20)