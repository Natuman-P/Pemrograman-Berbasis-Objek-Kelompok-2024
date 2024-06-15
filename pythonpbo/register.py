from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")



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

        fname_entry=ttk.Entry(frame, font=("poppins", 15,))
        fname_entry.place(x=50,y=130,width=250)

        lname=Label(frame, text="Last Name", font=("poppins", 15, "bold"), bg="white", fg="gray" )
        lname.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame,font=("poppins", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        #======baris kedua
        contact=Label(frame,text="Contact", font=("poppins", 15, "bold"), bg="white", fg="gray")
        contact.place(x=50, y=170)

        self.txt_contact=ttk.Entry(frame,font=("poppins", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email=Label(frame,text="Email", font=("poppins", 15, "bold"), bg="white", fg="gray")
        email.place(x=370, y=170)

        self.txt_contact=ttk.Entry(frame,font=("poppins", 15))
        self.txt_contact.place(x=370, y=200, width=250)

        #========baris ketiga
        security_Q=Label(frame,text="Select Security Questions", font=("poppins",15,"bold"), bg="white", fg="gray")
        security_Q.place(x=50,y=240)


        self.combo_security_Q=ttk.Combobox(frame, font=("poppins",15,"bold"), state="readonly")
        self.combo_security_Q["values"]=("Your Crush", "Your Birth Place", "Your Bestfriend", "Your School Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)
        #self.combo_security_Q.set("")#===== solusi = (ganti line 69 dengan line 70  agar values indeks ke-0 tidak akan muncul saat dijalankan)


        security_A=Label(frame,text="Security Answer", font=("poppins",15,"bold"), bg="white", fg="gray")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,font=("poppins", 15))
        self.txt_security.place(x=370, y=270, width=250)


        #=======baris keempat
        psswd=Label(frame,text="Password", font=("poppins",15,"bold"), bg="white", fg="gray")
        psswd.place(x=50, y=310)

        self.txt_psswd=ttk.Entry(frame,font=("poppins", 15))
        self.txt_psswd.place(x=50, y=340, width=250)

        cnfrmPsswd=Label(frame,text="Confirm Password", font=("poppins",15,"bold"), bg="white", fg="gray")
        cnfrmPsswd.place(x=370, y=310)

        self.txt_cnfrmpsswd=ttk.Entry(frame,font=("poppins", 15))
        self.txt_cnfrmpsswd.place(x=370, y=340, width=250)


        #=========================check button==============================
        checkbtn=Checkbutton(frame,text="I Agree The Terms & Conditions", font=("poppins",15,"bold"), bg="white", fg="black", onvalue=1,offvalue =0)
        checkbtn.place(x=50, y=400)

        #========buttons=======================
        img = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\—Pngtree—register button_8616330.png") 
        img = img.resize((300, 50), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimg, borderwidth=0, cursor="hand2", font=("poppins", 15, "bold"))
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Pongo\Pemrograman-Berbasis-Objek-Kelompok-2024\pythonpbo\login-button_592324-17754.png")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimg1, borderwidth=0, cursor="hand2", font=("poppins", 15, "bold"))
        b1.place(x=370, y=420, width=200)


if __name__=="__main__":  
        root=Tk()
        app=Register(root)
        root.mainloop()