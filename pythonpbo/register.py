from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #=================VARIABLE=======
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #==============bg image==========
        self.bg=ImageTk.PhotoImage(file =r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\walpaper.jpg")
        bg_lbl=Label(self.root, image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        #==============left image==========
        self.bg=ImageTk.PhotoImage(file =r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\walpaper.jpg")
        left_bg_lbl=Label(self.root, image=self.bg)
        left_bg_lbl.place(x=50,y=100,width=470,height=550)

        #===========main Frame=============
        frame=Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl =Label(frame, text="REGISTER HERE", font=("poppins", 25, "bold"), fg="darkgray", bg="white" )
        register_lbl.place(x=20, y=20)

        #============label and entry=============
        
        #=====baris pertama
        fname=Label(frame, text="First Name", font=("poppins", 15, "bold"), bg="white", fg="gray")
        fname.place(x=50, y=100)

        fname_entry=ttk.Entry(frame, textvariable=self.var_fname, font=("poppins", 15,))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame, text="Last Name", font=("poppins", 15, "bold"), bg="white", fg="gray" )
        lname.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame, textvariable=self.var_lname, font=("poppins", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #======baris kedua
        contact=Label(frame,text="Contact", font=("poppins", 15, "bold"), bg="white", fg="gray")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame, textvariable=self.var_contact, font=("poppins", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email=Label(frame,text="Email", font=("poppins", 15, "bold"), bg="white", fg="gray")
        email.place(x=370, y=170)

        self.txt_email=ttk.Entry(frame, textvariable=self.var_email, font=("poppins", 15))
        self.txt_email.place(x=370, y=200, width=250)

        #========baris ketiga
        security_Q=Label(frame,text="Select Security Questions", font=("poppins",15,"bold"), bg="white", fg="gray")
        security_Q.place(x=50,y=240)


        self.combo_security_Q=ttk.Combobox(frame, textvariable=self.var_securityQ, font=("poppins",15,"bold"), state="readonly")
        self.combo_security_Q["values"]=("Your Crush", "Your Birth Place", "Your Bestfriend", "Your School Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)
        #self.combo_security_Q.set("")#===== solusi = (ganti line 69 dengan line 70  agar values indeks ke-0 tidak akan muncul saat dijalankan)


        security_A=Label(frame,text="Security Answer", font=("poppins",15,"bold"), bg="white", fg="gray")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame, textvariable=self.var_securityA, font=("poppins", 15))
        self.txt_security.place(x=370, y=270, width=250)


        #=======baris keempat
        psswd=Label(frame,text="Password", font=("poppins",15,"bold"), bg="white", fg="gray")
        psswd.place(x=50, y=310)

        self.txt_psswd=ttk.Entry(frame, textvariable=self.var_pass, font=("poppins", 15))
        self.txt_psswd.place(x=50, y=340, width=250)

        cnfrmPsswd=Label(frame,text="Confirm Password", font=("poppins",15,"bold"), bg="white", fg="gray")
        cnfrmPsswd.place(x=370, y=310)

        self.txt_cnfrmpsswd=ttk.Entry(frame, textvariable=self.var_confpass, font=("poppins", 15))
        self.txt_cnfrmpsswd.place(x=370, y=340, width=250)


        #=========================check button==============================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("poppins",15,"bold"), bg="white", fg="black", onvalue=1,offvalue =0)
        checkbtn.place(x=50, y=400)

        #========buttons=======================
        register_btn = Button(frame, text="Register", command=self.register_data, font=("poppins", 15, "bold"), bg="green", fg="white")
        register_btn.place(x=10, y=450, width=200)

        login_btn = Button(frame, text="Login", font=("poppins", 15, "bold"), bg="blue", fg="white")
        login_btn.place(x=370, y=450, width=200)

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                # Connect to the MySQL database
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="userdata")
                my_cursor = conn.cursor()

                # Check if the email already exists in the database
                query = "SELECT * FROM register WHERE email=%s"
                value = (self.var_email.get(),)  # Corrected to be a tuple
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    # Insert the new user's data into the register table
                    my_cursor.execute(
                        "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Register Success")
                    
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}")









if __name__=="__main__":  
        root=Tk()
        app=Register(root)
        root.mainloop()