from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter import messagebox

class AppLogin(CTk):
    def __init__(self):
        super().__init__()
        self.title("WEB Aplication login")
        self.geometry("600x400")
        self.configure(fg_color='#20244d')
#Frame nya
        self.frame=CTkFrame(master=self, 
                            width=400, height=300, fg_color='#fafcfc', corner_radius=20)
        self.frame.propagate(False)#agar tetap, tidak mengikuti objek
        self.frame.place(relx=0.5, rely=0.5, anchor="center")
#Tombol loginnya
        self.tombol_login=CTkButton(master=self.frame,
                                    text="Log in", 
                                    width=200, height=50, corner_radius=15, fg_color='#20244d', hover_color='#3b4ba8',
                                    font=("Arial", 20))
        self.tombol_login.pack(pady=20)
if __name__=="__main__":
    app = AppLogin()
    app.mainloop()
