from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1540x800+0+0")
        self.root.configure(backgrounds="powder blue")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        #lblTitle=Label(self.root,bd=20,relief=RIDGE,bg="white",fg="read",font=("times new roman",50,"bold"),text="+ HOSPITAL MANAGEMENT SYSTEM")
        lblTitle.pack(side=TOP,fill=x)

        # ========dataFrame===================================
        DataFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                                    font=("arial",12,"bold"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,padx=20,relief=RIDGE,
                                    font=("arial",12"bold"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=460,height=350)

        # ======ButtonFrame===================================
        ButtonFrame=Frame(self.root,bd=20,padx=20,relief=RIDGE)
        ButtonFrame.place(x=0,y=530,width=1530,height=70)

        # ======frameDetails===================================
        FrameDetails=Frame(self,root,bd=20,padx=20,relief=RIDGE)
        FrameDetails.place(x=0,y=600,width=1530,height=195)

        # =======dataFrame left===============================

        lblNameTablet=Label(DataFrameLeft,font=("arial",12,"bold"),text="Name of Tablets",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readOnly",
                                        font=("arial",12,"bold"),width=33)
        comNameTablet['value']=("Nice","Acetaminophen","Adderall","Amlodipine","Antivan")
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtref.grid(row)


