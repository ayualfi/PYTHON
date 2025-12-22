from customtkinter import CTk, CTkButton

app = CTk()
app.title("my app")
app.geometry("400x150")

button = CTkButton(app,
                   text="My Button",
                   )
button.grid(row=0,
            column=0,
            padx=20,
            pady=20)
app.mainloop()