from tkinter import *
window=Tk()
window.title("My Identity")
window.geometry("300x200")

icon = PhotoImage(file='Pemograman Platform/A (3).png')
window.iconphoto(True,icon)
window.config(bg="#20244d")
#frame utama
main_frame=Frame(window,
             bg='#20244d',
             padx=3,
             pady=3
            )
main_frame.pack()
#frame nya judul dan judul
border=Frame(main_frame,
             bg='#fafcfc',
             padx=3,
             pady=3
)
border.pack(pady=30)
main_label = Label(border,
              text="Hello Ayu, let us know a brief of you !",
              font=('Arial',20, 'bold'),
              fg='#fafcfc',
              bg='#20244d',
              relief=SOLID,
              padx=20,
              pady=20
              )
main_label.pack()
#framenya inputan
input_frame=Frame(main_frame,
                 bg='#20244d')
input_frame.pack(fill="x")
input_frame.columnconfigure(1, weight=1)
#contain
#==================
name_label=Label(input_frame,
                 text='Whats your complete name?',
                 fg='#fafcfc',
                 bg='#20244d',
                 font=('Arial', 15)
                 )
name_label.grid(row=0, column=0, sticky="w", padx=5)
form=Entry(input_frame,
                 fg='#fafcfc',
                 bg='#3b4ba8',
                 font=('Arial', 15)
                 )
form.grid(row=0, column=1, sticky="ew", padx=5)
#==================
name_label=Label(input_frame,
                 text='How can i call you?',
                 fg='#fafcfc',
                 bg='#20244d',
                 font=('Arial', 15)
                 )
name_label.grid(row=1, column=0, sticky="w", padx=5)
form=Entry(input_frame,
                 fg='#fafcfc',
                 bg='#3b4ba8',
                 font=('Arial', 15)
                 )
form.grid(row=1, column=1, sticky="ew", padx=5)
#====================
name_label=Label(input_frame,
                 text='What your age?',
                 fg='#fafcfc',
                 bg='#20244d',
                 font=('Arial', 15)
                 )
name_label.grid(row=2, column=0, sticky="w", padx=5)
form=Entry(input_frame,
                 fg='#fafcfc',
                 bg='#3b4ba8',
                 font=('Arial', 15)
                 )
form.grid(row=2, column=1, sticky="ew", padx=5)
#======================
name_label=Label(input_frame,
                 text='Where are you from?',
                 fg='#fafcfc',
                 bg='#20244d',
                 font=('Arial', 15)
                 )
name_label.grid(row=3, column=0, sticky="w", padx=5)
form=Entry(input_frame,
                 fg='#fafcfc',
                 bg='#3b4ba8',
                 font=('Arial', 15)
                 )
form.grid(row=3, column=1, sticky="ew", padx=5)
#=========================
name_label=Label(input_frame,
                 text='What are you doing right now',
                 fg='#fafcfc',
                 bg='#20244d',
                 font=('Arial', 15)
                 )
name_label.grid(row=4, column=0, sticky="w", padx=5)
form=Entry(input_frame,
                 fg='#fafcfc',
                 bg='#3b4ba8',
                 font=('Arial', 15)
                 )
form.grid(row=4, column=1, sticky="ew", padx=5)
window.mainloop()