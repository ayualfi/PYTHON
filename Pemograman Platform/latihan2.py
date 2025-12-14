from tkinter import *
window=Tk()
window.title("My Identity")
window.geometry("300x200")

icon = PhotoImage(file='Pemograman Platform/A (3).png')
window.iconphoto(True,icon)
window.config(bg="#20244d")
border=Frame(window,
             bg='#fafcfc',
             padx=3,
             pady=3
)
border.pack(pady=30)
label = Label(border,
              text="Hi Everyone",
              font=('Arial',20, 'bold'),
              fg='#fafcfc',
              bg='#20244d',
              relief=SOLID,
              padx=20,
              pady=20
              )
label.pack()
window.mainloop()