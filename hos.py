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

        lblTitle=Label(self.root,bd=20,relief=RIDGE,bg="white",fg="read",font=("times new roman",50,"bold"),text="+ HOSPITAL MANAGEMENT SYSTEM")
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
        FrameDetails=Frame(self.root,bd=20,padx=20,relief=RIDGE)
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
        txtref=Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Dose: ", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=("arial", 12, "bold"), text="No Of Tablets: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.NumberofTablets, width=35)
        txtNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=5)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Lot, width=35)
        txtLot.grid(row=4, column=1)

        lblissueDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.Issuedate, width=35)
        txtissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2,pady=6)
        lblExpDate.grid(row=5,column=0,sticky=W)
        txtExpDate = Entry(DataFrameLeft, font=("arial", 13,"bold"), textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataFrameLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataFrameLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect: ", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.sideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.FurtherInformation, width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblDrivingMachine = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)
        txtDrivingMachine = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.DrivingUsingMachine, width=35)
        txtDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(DataFrameLeft, font=("arial", 12,"bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataFrameLeft, font=("arial", 12,"bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedicine = Label(DataFrameLeft, font=("arial", 12,"bold"), text="Medication:", padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataFrameLeft, font=("arial", 12,"bold"), textvariable=self.HowToUseMedication, width=35)
        txtMedicine.grid(row=3, column=3, sticky=W)

        lblPatientId = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Id", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataFrameLeft, font=("arial", 12, "bold"), text="NHS Number", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Name", padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)
        txtPatientname = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.PatientName, width=35)
        txtPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Date Of Birth", padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth = Entry(DataFrameLeft, font=("arial", 12, "bold"), textvariable=self.DateOfBirth, width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataFrameLeft, font=("arial", 12,"bold"), textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

        # =================================== DataframeRight ==============

        self.txtPrescription = Text(DataFrameRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ==================== ButtonFrame =================
        btnPrescription = Button(ButtonFrame, text="Prescription", command=self.iPrescription, font=("arial", 12, "bold"), width=23)
        btnPrescription.grid(row=0, column=0)

        btnReceipt = Button(ButtonFrame, text="Prescription Data", command=self.iPrescriptionData, font=("arial", 12, "bold"))
        btnReceipt.grid(row=0, column=1)

        btnExit = Button(ButtonFrame, text="Update", command=self.update_data, font=("arial", 12, "bold"), width=23, bg="green")
        btnExit.grid(row=0, column=2)

        btnDelete = Button(ButtonFrame, text="Delete", command=self.iDelete, font=("arial", 12, "bold"), width=23, bg="green")
        btnDelete.grid(row=0,column=3)

        btnReset = Button(ButtonFrame, text="Reset", command=self.iReset, font=("arial", 12, "bold"), width=23, bg="green")
        btnReset.grid(row=0,column=4)

        btnExit = Button(ButtonFrame, text="Exit", command=self.iExit, font=("arial", 12, "bold"), width=23, bg="green")
        btnExit.grid(row=0, column=5)






