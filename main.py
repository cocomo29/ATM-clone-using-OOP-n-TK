#imports
from tkinter import *
import os
from PIL import ImageTk, Image
import random

class BankModel:
    try:
        def __init__(self,master,img):
            self.master = master
            self.master.title("Banking App")
            self.master.geometry('650x500')
            self.master.config(bg='black')
            self.master.resizable(width=False,height=False)

            self.photo = PhotoImage(file = f"{os.getcwd()}/512x512.png")
            self.master.iconphoto(False, self.photo)

            # self.master.geometry("500x500")

            #Labels
            Label(self.master, text="Uit Cash",fg='white',bg='black', font=("ubuntu mono",40)).pack(pady=15)
            Label(self.master, text="fluent  in  finance.",fg='white',bg='black', font="ubuntu").pack(pady=12)
            Label(self.master, image=img).pack(pady=30)

            Button(self.master, text="Register",fg='white',bg='black', font=("Calibri", 12), width=20, command=self.register).pack()
            Button(self.master, text="Login",fg='white',bg='black', font=("Calibri", 12), width=20, command=self.login).pack()

            Label(self.master, text="made by @cocomo and @Rayyan",fg='green',bg='black', font=("ubuntu mono",10)).pack(pady=15)

            self.tempName = None
            self.tempAge = None
            self.tempGender = None
            self.tempPassword = None
            self.notif = None
            self.loginName = None
            self.amount = None
            self.depositNotif = None
            self.currentBalanceL = None
            self.tempLoginName = None
            self.tempLoginPassword = None
            self.loginNotif = None
            self.loginScreen = None
            self.withdrawAmount = None
            self.withdrawNotif = None
            self.currentBalanceL = None

            self.allAccounts = os.listdir()

    except FileNotFoundError as f:
        print("""due to directory diffrentiations, file may not run on your device, if so: try executing "main.py" directly from file explorer""", f)

    

class Backend(BankModel):
    def __init__(self,master,img):
        super().__init__(master,img)

    def finishRegistration(self):
            name = self.tempName.get()
            age = self.tempAge.get()
            gender = self.tempGender.get()
            password = self.tempPassword.get()
            

            condition=[name == "", age == "", gender == "",password == ""]
            if any(condition):
                self.notif.config(fg="red", text="FIll All Fields *")
                return
            
            for i in self.allAccounts:
                if i == name:
                    self.notif.config(fg="red", text="name already taken, try {}{}".format(name,random.randint(1,100)))
                    return
                else:
                    newFile=open(name,"w")
                    newFile.write(name+"\n")
                    newFile.write(password+"\n")
                    newFile.write(age+"\n")
                    newFile.write(gender+"\n")
                    newFile.write("0")
                    newFile.close()
                    self.notif.config(fg="green", text="account has successfully been created!")

    def register(self):
        #Var initialisation
        

        self.tempName = StringVar()
        self.tempAge = StringVar()
        self.tempGender = StringVar()
        self.tempPassword = StringVar()

        ########################################################  register screen
        registerScreen =Toplevel(self.master)
        registerScreen.title("Register")
        registerScreen.geometry('370x280')
        registerScreen.resizable(width=False,height=False)
        registerScreen.config(bg='black')
        registerScreen.iconphoto(False, self.photo)
        
        
        #labels
        Label(registerScreen, text="Please enter your details below to register",fg='white',bg='black', font=("calibri", 15)).grid(row=0, sticky=N, pady=20)
        Label(registerScreen, text="Name", fg='white',bg='black',font=("calibri", 12)).grid(row=1, sticky=W)
        Label(registerScreen, text="Age",fg='white',bg='black', font=("calibri", 12)).grid(row=2, sticky=W)
        Label(registerScreen, text="Gender", fg='white',bg='black',font=("calibri", 12)).grid(row=3, sticky=W)
        Label(registerScreen, text="Password",fg='white',bg='black', font=("calibri", 12)).grid(row=4, sticky=W)
        self.notif = Label(registerScreen,fg='white',bg='black',  font=("calibri", 12))
        self.notif.grid(row=6,sticky=N,pady=10)
        

        #Enteries
        Entry(registerScreen, textvariable=self.tempName).grid(row=1, column=0)
        Entry(registerScreen, textvariable=self.tempAge).grid(row=2, column=0)
        Entry(registerScreen, textvariable=self.tempGender).grid(row=3, column=0)
        Entry(registerScreen, textvariable=self.tempPassword, show="*").grid(row=4, column=0)

        #Buttons
        Button(registerScreen, text="Register!", command=self.finishRegistration,fg='white',bg='black', font=("calibri",12)).grid(row=5, sticky=N,pady=10)



    def loginSession(self):
        #yahan se login name shaat mara h
        

        self.loginName= self.tempLoginName.get()
        self.loginPassword= self.tempLoginPassword.get()

        for name in self.allAccounts:
            if name == self.loginName:
                file = open(name,"r")
                fileData=file.read()
                fileData=fileData.split("\n")
                passwordfromList=fileData[1]

                #########################################################Account Dashboard
                if self.loginPassword==passwordfromList:
                    self.master.withdraw()
                    self.loginScreen.destroy()
                    accountDashboard=Toplevel(self.master)
                    accountDashboard.title("Account Dashboard")
                    accountDashboard.iconphoto(False, self.photo)
                    accountDashboard.geometry('650x500')
                    accountDashboard.config(bg='black')
                    accountDashboard.resizable(width=False,height=False)
                    #Labels
                    Label(accountDashboard,text="Uit Cash - Dashboard",fg='white',bg='black',font=("calibri",25)).pack(pady=25)
                    Label(accountDashboard,text="welcome "+ '@'+name,bg='black',fg='green',font=("calibri",15)).pack()
                    #withdraw se shart hogai thi or ab wapsi agai deconify se
                    Button(accountDashboard,text="logout",bg='black',fg='red',command=lambda:[self.master.deiconify(),accountDashboard.destroy()]).pack(pady=5)
                    
                    #Buttons
                    Button(accountDashboard,text="Personal Details",fg='white',bg='black',font=("calibri",12),width=30,command=self.personalDetails).place(relx=0.37,rely=0.4, relwidth=0.25,relheight=0.1)
                    Button(accountDashboard,text="Deposit",fg='white',bg='black',font=("calibri",12),width=30,command=self.deposit).place(relx=0.37,rely=0.5, relwidth=0.25,relheight=0.1)
                    Button(accountDashboard,text="Withdraw",fg='white',bg='black',font=("calibri",12),width=30,command=self.withdraw).place(relx=0.37,rely=0.6, relwidth=0.25,relheight=0.1)
                    try:
                        Label(accountDashboard).grid(row=5, sticky=N,pady=10)
                    except BaseException as be:
                        print("")
                     #XD
                    return
                else:
                    self.loginNotif.config(fg="red", text="incorrect password")
                    return
            else:
                self.loginNotif.config(fg="red", text="no such account")


    def login(self):
        #Var initialisation
        

        self.tempLoginName=StringVar()
        self.tempLoginPassword=StringVar()

        ######################################################## login screen
        self.loginScreen=Toplevel(self.master)
        self.loginScreen.title("Login")
        self.loginScreen.config(bg='black')
        self.loginScreen.geometry('270x200')
        self.loginScreen.iconphoto(False, self.photo)

        #labels
        Label(self.loginScreen, text="Login", font=("calibri, 25"),fg='white',bg='black').grid(row=0,column=1,sticky=N,pady=10)
        Label(self.loginScreen, text="Username", font=("calibri, 12"),fg='white',bg='black').grid(row=1,column=0,sticky=W)
        Label(self.loginScreen, text="Password", font=("calibri, 12"),fg='white',bg='black').grid(row=2,column=0,sticky=W)
        self.loginNotif=Label(self.loginScreen, font=("calbri, 12"),fg='white',bg='black')
        self.loginNotif.grid(row=4,column=1,sticky=N)

        #Enteries
        Entry(self.loginScreen,textvariable=self.tempLoginName).grid(row=1,column=1,padx=5)
        Entry(self.loginScreen,textvariable=self.tempLoginPassword, show="*").grid(row=2,column=1,padx=5)

        #Buttons
        Button(self.loginScreen, text="Login",command=self.loginSession, width=15, font=("calibri"),fg='white',bg='black').grid(row=3, column=1,sticky=W,pady=10)


        
    def personalDetails(self):
        #variables
        file=open(f"{os.getcwd()}/{self.loginName}","r")
        fileData=file.read()
        details=fileData.split("\n")
        
        detailsName=details[0]
        detailsAge=details[2]
        detailsGender=details[3]
        detailsBalance=details[4]


    ########################################################  Personal Details Screen
        personalScreen=Toplevel(self.master)
        personalScreen.title("Personal Details")
        personalScreen.config(bg='black')
        personalScreen.geometry('400x400')
        personalScreen.iconphoto(False, self.photo)
        personalScreen.resizable(width=False,height=False)

        Label(personalScreen,text='--Personal Details--',bg='black',fg='white',font='ariel 25').pack(pady=20)


        listbox = Listbox(personalScreen,bg='black',fg='green',font= 'hack 15')
        listbox.pack()

        listbox.insert('end',f"Name : {detailsName}")
        listbox.insert('end',f"Age : {detailsAge}")
        listbox.insert('end',f"Gender : {detailsGender}")
        listbox.insert('end',f"Balance : {detailsBalance}")
        



    def finalizeDeposit(self):
        if self.amount.get() == "":
            self.depositNotif.config(fg="red",text="cannot be blank")
            return
        if float(self.amount.get()) <= 0:
            self.depositNotif.config(fg="red",text="please enter a valid amount")
            return
        
        file = open(f"{os.getcwd()}/{self.loginName}", "r+")
        fileData=file.read()
        details=fileData.split("\n")
        currentBalance=details[4]
        updatedBalance=currentBalance
        updatedBalance=float(updatedBalance) + float(self.amount.get())

        fileData = fileData.replace(currentBalance, str(updatedBalance))
        file.seek(0)
        file.truncate(0)
        file.write(fileData)
        file.close()

        self.currentBalanceL.config(text=f"{updatedBalance}")
        self.depositNotif.config(fg="green", text="Balance Successfully Updated!")

    def deposit(self):
        #variables
        #innit me shaat kiye h

        self.amount=StringVar()

        file=open(f"{os.getcwd()}/{self.loginName}", "r")
        fileData=file.read()
        details=fileData.split("\n")
        detailsBalance=details[4]
        ########################################################  Deposit Screen
        depositScreen=Toplevel(self.master)
        depositScreen.title("Deposit Cash")
        depositScreen.geometry('350x200')
        depositScreen.config(bg='black')
        depositScreen.iconphoto(False, self.photo)
        depositScreen.resizable(width=False,height=False)


        #labels
        Label(depositScreen, text="Deposit",bg='black',fg='white', font=("calibri",25)).grid(row=0,column=1,sticky=N,pady=10)
        Label(depositScreen, fg='white',bg='black',text="Current Balance: ", font=("calibri")).grid(row=1,column=0,sticky=W)
        self.currentBalanceL=Label(depositScreen,fg='white',bg='black',text=f"{detailsBalance}")
        self.currentBalanceL.grid(row=1,column=1,sticky=W)
        Label(depositScreen, text="Amount", fg='white',bg='black', font=("calibri",12)).grid(row=2,column=0,sticky=W)
        self.depositNotif=Label(depositScreen,  fg='white',bg='black',font=("calibri",12))
        self.depositNotif.grid(row=4, column=1,sticky=N,pady=5)
        
        #Entry
        Entry(depositScreen, textvariable=self.amount).grid(row=2, column=1)

        #buttons
        Button(depositScreen, text="Deposit", fg='white',bg='black', font=("calibri", 12),command=self.finalizeDeposit).grid(row=3,column=1,sticky=W,pady=7)



    def finalizewithdraw(self):
        if self.withdrawAmount.get() == "":
            self.withdrawNotif.config(fg="red",text="please enter amount u want to withdraw")
            return
        if float(self.withdrawAmount.get()) <= 0:
            self.withdrawNotif.config(fg="red",text="please enter a valid amount")
            return
        
        file = open(f"{os.getcwd()}/{self.loginName}", "r+")
        fileData=file.read()
        details=fileData.split("\n")
        currentBalance=details[4]

        if float(self.withdrawAmount.get())> float(currentBalance):
            self.withdrawNotif.config(fg="red", text="you dont have this much money in ur account")
            return

        updatedBalance=currentBalance
        updatedBalance=float(updatedBalance) - float(self.withdrawAmount.get())

        fileData = fileData.replace(currentBalance, str(updatedBalance))
        file.seek(0)
        file.truncate(0)
        file.write(fileData)
        file.close

        self.currentBalanceL.config(fg="green",text=f"{updatedBalance}")
        self.withdrawNotif.config(fg="green", text="Balance Successfully Updated!")

    def withdraw(self):
        #variables
        

        self.withdrawAmount=StringVar()

        file=open(f"{os.getcwd()}/{self.loginName}", "r")
        fileData=file.read()
        details=fileData.split("\n")
        detailsBalance=details[4]
        ########################################################  withdraw Screen
        withdrawScreen=Toplevel(self.master)
        withdrawScreen.title("Withdraw Cash")
        withdrawScreen.geometry('350x200')
        withdrawScreen.config(bg='black')
        withdrawScreen.iconphoto(False, self.photo)
        withdrawScreen.resizable(width=False,height=False)


        #labels
        Label(withdrawScreen, text="Withdraw",bg='black',fg='white', font=("calibri",25)).grid(row=0,column=1,sticky=N,pady=10)
        Label(withdrawScreen, fg='white',bg='black',text="Current Balance: ", font=("calibri")).grid(row=1,column=0,sticky=W)
        self.currentBalanceL=Label(withdrawScreen,fg='white',bg='black',text=f"{detailsBalance}")
        self.currentBalanceL.grid(row=1,column=1,sticky=W)
        Label(withdrawScreen, text="Amount", fg='white',bg='black', font=("calibri",12)).grid(row=2,column=0,sticky=W)
        self.withdrawNotif=Label(withdrawScreen,  fg='white',bg='black',font=("calibri",12))
        self.withdrawNotif.grid(row=4, column=1,sticky=N,pady=5)
        
        #Entry
        Entry(withdrawScreen, textvariable=self.withdrawAmount).grid(row=2, column=1)

        #buttons
        Button(withdrawScreen, text="Withdraw", fg='white',bg='black', font=("calibri", 12),command=self.finalizewithdraw).grid(row=3,column=1,sticky=W,pady=7)

try:
    master = Tk()
    img =  Image.open(f"{os.getcwd()}/uit.jpg")
    img = img.resize((200,180))
    img = ImageTk.PhotoImage(img)
    bank = Backend(master,img)
    master.mainloop()
except FileNotFoundError as f:
         print("""due to directory diffrentiations, file may not run on your device, if so: try executing "main.py" or "main.exe" directly from file explorer""", f)






