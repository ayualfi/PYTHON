from customtkinter import CTk, CTkButton

app = CTk()
app.title("my app")
app.geometry("400x150")

button1 = CTkButton(app,
                   text="My Button",
                   )
button1.grid(row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="ew")
button2=CTkButton(app,
                  text="My Button")
button2.grid(row=0,
            column=1,
            padx=20,
            pady=20,
            sticky="ew")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=9)
app.mainloop()