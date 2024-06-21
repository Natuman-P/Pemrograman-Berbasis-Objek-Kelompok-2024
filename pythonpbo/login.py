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
        img1 = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\user.png")
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
        img2 = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\email.png")
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
        loginbtn = Button(frame, command=self.open_pagegrup_window, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=40, y=340, width=120, height=35)

        # Register button
        registerbtn = Button(frame, command=self.open_register_window, text="Register Now", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        registerbtn.place(x=190, y=340, width=120, height=35)

        # Forget password button
        forgetbtn = Button(frame, command=self.open_forget_password_window, text="Forget Password", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        forgetbtn.place(x=110, y=390, width=160)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="userdata"
                )
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
                row = cursor.fetchone()
                if row:
                    messagebox.showinfo("Success", "Welcome to ")
                else:
                    messagebox.showerror("Invalid", "Invalid email or password")
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error connecting to database: {err}")

    def open_register_window(self):
        try:
            register_path = os.path.join(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo", "register.py")
            subprocess.Popen(["python", register_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open register window: {e}")

    def open_pagegrup_window(self):
        try:
            register_path = os.path.join(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo", "profilgrup.py")
            subprocess.Popen(["python", register_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open register window: {e}")

    def open_forget_password_window(self):
        self.new_window = Toplevel(self.root)
        self.app = ForgetPassword_Window(self.new_window)

class ForgetPassword_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Forget Password")
        self.root.geometry("400x550+500+150")

        title = Label(self.root, text="Forget Password", font=("times new roman", 20, "bold"), fg="red")
        title.place(x=0, y=10, relwidth=1)

        email_label = Label(self.root, text="Email", font=("times new roman", 15, "bold"), fg="black")
        email_label.place(x=50, y=80)
        self.email_entry = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=50, y=110, width=300)

        security_q_label = Label(self.root, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black")
        security_q_label.place(x=50, y=160)
        self.security_q_combo = ttk.Combobox(self.root, font=("times new roman", 15, "bold"), state="readonly")
        self.security_q_combo["values"] = ("Your Crush", "Your Birth Place", "Your Bestfriend", "Your School Name")
        self.security_q_combo.place(x=50, y=190, width=300)
        self.security_q_combo.current(0)

        security_a_label = Label(self.root, text="Security Answer", font=("times new roman", 15, "bold"), fg="black")
        security_a_label.place(x=50, y=240)
        self.security_a_entry = ttk.Entry(self.root, font=("times new roman", 15, "bold"))
        self.security_a_entry.place(x=50, y=270, width=300)

        new_pass_label = Label(self.root, text="New Password", font=("times new roman", 15, "bold"), fg="black")
        new_pass_label.place(x=50, y=320)
        self.new_pass_entry = ttk.Entry(self.root, font=("times new roman", 15, "bold"), show='*')
        self.new_pass_entry.place(x=50, y=350, width=300)

        confirm_pass_label = Label(self.root, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black")
        confirm_pass_label.place(x=50, y=390)
        self.confirm_pass_entry = ttk.Entry(self.root, font=("times new roman", 15, "bold"), show='*')
        self.confirm_pass_entry.place(x=50, y=420, width=300)

        reset_btn = Button(self.root, text="Reset Password", command=self.reset_password, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        reset_btn.place(x=125, y=470, width=150)

    def reset_password(self):
        if self.email_entry.get() == "" or self.security_a_entry.get() == "" or self.new_pass_entry.get() == "" or self.confirm_pass_entry.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.new_pass_entry.get() != self.confirm_pass_entry.get():
            messagebox.showerror("Error", "New Password and Confirm Password must match")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="userdata"
                )
                cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.email_entry.get(), self.security_q_combo.get(), self.security_a_entry.get())
                cursor.execute(query, value)
                row = cursor.fetchone()
                if row:
                    query = "UPDATE register SET password=%s WHERE email=%s"
                    value = (self.new_pass_entry.get(), self.email_entry.get())
                    cursor.execute(query, value)
                    conn.commit()
                    messagebox.showinfo("Success", "Your password has been reset successfully")
                    self.root.destroy()
                else:
                    messagebox.showerror("Error", "Incorrect security answer or email")
                conn.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error connecting to database: {err}")

if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
