import os
import subprocess
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Pongo\Downloads\18773520_6025383.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for login
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # User icon
        img1 = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\walpaper.jpg")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=120, y=20, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=140)

        # Label for email
        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        email_lbl.place(x=40, y=185)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=210, width=270)

        # Label for password
        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password_lbl.place(x=40, y=255)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show='*')
        self.txtpass.place(x=40, y=280, width=270)

        # Icon images
        img2 = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\walpaper.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(frame, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=10, y=210, width=25, height=25)

        img3 = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\walpaper.jpg")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(frame, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=10, y=280, width=25, height=25)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=40, y=340, width=120, height=35)

        # Register button
        registerbtn = Button(frame, command=self.open_register_window, text="New User Register", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        registerbtn.place(x=190, y=340, width=120, height=35)

        # Forget password button
        forgetbtn = Button(frame, text="Forget Password", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        forgetbtn.place(x=110, y=390, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="your_mysql_username",
                    password="your_mysql_password",
                    database="userdata"
                )
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
                row = cursor.fetchone()
                if row:
                    messagebox.showinfo("Success", "Welcome to ")
                else:
                    messagebox.showerror("Invalid", "Invalid email & password")
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error connecting to database: {err}")

    def open_register_window(self):
        try:
            # Pastikan path ke register.py sesuai dengan struktur Anda
            register_path = os.path.join(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo", "register.py")

            # Menjalankan register.py menggunakan subprocess.Popen
            subprocess.Popen(["python", register_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open register window: {e}")

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
