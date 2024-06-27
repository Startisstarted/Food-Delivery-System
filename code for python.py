import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LoginForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Form")
        self.geometry("300x150")

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_field = ttk.Entry(self)
        self.username_field.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_field = ttk.Entry(self, show="*")
        self.password_field.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_field.get()
        password = self.password_field.get()

        if username == "admin" and password == "admin":
            self.destroy()
            MainMenu().mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("300x150")

        # Add your main menu code here

if __name__ == "__main__":
    login_form = LoginForm()
    login_form.mainloop()

