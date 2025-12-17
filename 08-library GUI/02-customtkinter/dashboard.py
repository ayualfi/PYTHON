from customtkinter import CTkFrame, CTkLabel

class DashBoard(CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(
            fg_color='#fafcfc'
        )
        self.label_judul = CTkLabel(master,
                                    text="Dashboard",
                                    font=("Arial", 12, "bold"),
                                    fg_color='#fafcfc',
                                    text_color='black',
                                   )
        self.label_judul.place(x= 20, y=20)