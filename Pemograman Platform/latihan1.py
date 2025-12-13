from tkinter import *
class latihan1(Tk):
    def __init__(self):
        super().__init__()
        self.title("Form latihan 1")
        self.geometry("800x600")
        self.configure(bg="black")
        self.create_widgets()
    def create_widgets(self):
        frame = Frame(self,
                      bg="black",
                      bd=2,
                      relief="ridge",
                      highlightthickness=2,
                      highlightbackground="darkblue",
                      padx=15,
                      pady=15,
                      width=400,
                      height=300)
        frame.propagate(False)
        frame.place(relx=0.5, rely=0.3, anchor="center")
        label_judul=Label(frame,
                          text="Login User",
                          font=("Arial", 12, "bold"),
                          bg="darkblue",
                          fg="lightgray",
                          width=10,
                          height=2
        )
        label_judul.pack(pady=10)
        label_username=Label(frame,
                             text="Username",
                             font=("Arial", 12),
                             bg="black",
                             fg="lightgray")
        label_username.place(x=20, y=60)
        entry_username=Entry(frame,
                             font=("Arial", 12))
        entry_username.place(x=150, y=60)
        label_password=Label(frame,
                             text="Password",
                             font=("Arial", 12),
                             bg="black",
                             fg="lightgray")
        label_password.place(x=20, y=100)
        entry_password=Entry(frame,
                             font=("Arial", 12),
                             show="*")
        entry_password.place(x=150, y=100)
        btn_login=Button(frame,
                         text="Log in",
                         font=("Arial", 12, "bold"),
                         width=10,
                         bg="darkblue",
                         bd=3,
                         relief="ridge",
                         highlightthickness=3,
                         highlightbackground="darkblue",
                         fg="White")
        btn_login.place(x=60, y=150)
        btn_cancel=Button(frame,
                         text="Cancel",
                         font=("Arial", 12, "bold"),
                         width=10,
                         bg="darkblue",
                         bd=3,
                         relief="ridge",
                         highlightthickness=3,
                         highlightbackground="darkblue",
                         fg="White")
        btn_cancel.place(x=190, y=150)
if __name__ =="__main__":
    app = latihan1()
    app.mainloop()