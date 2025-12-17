from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame, LEFT, Y, TOP,X
from dashboard import DashBoard

class MainApp(CTk):
    def __init__(self):
        super().__init__()
        self.title="Main Application"
        self.geometry("800x600")
        self.configure(fg_color='#e4e5f2')
#frame kiri
        self.left_frame=CTkFrame(master=self,
                                 width=300,
                                 fg_color='#20244d',
                                 corner_radius=0)
        self.left_frame.pack(side="left", fill="y")
        self.left_frame.propagate(False)
#frame kanan
        self.right_frame=CTkFrame(master=self,
                                 width=300,
                                 fg_color='#e4e5f2',
                                 corner_radius=0)
        self.right_frame.pack(side="left", fill="both", expand=True)
        self.current_frame=None 
        self.ganti_frame(DashBoard(self.right_frame))#untuk nyambung ke dashboard
#Def untuk self.currentnya
    def ganti_frame(self, frame):
        if self.current_frame != None:
            self.current_frame.destroy()
            self.current_frame.frame
        frame.pack(fill = "both", expand=True)
        