from tkinter import*
class Qr_Generator:

    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200")
        self.root.title("QR Generator | Developed by ABDOU_ DZB 🍆")
        self.root.resizable(False,False)

        title=Label(self.root,text="   Qr Code Generator",font=("times new roman",40),bg='#053246',fg='white' ,anchor='w').place(x=0,y=0,relwidth=1)

        #====Employee Details window=========
        emp_Frame+Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title=Label(emp_Frame=Label(self.root,text="Employee Details",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1,text="   Qr Code Generator",font=("times new roman",40),bg='#053246',fg'white' ,anchor='w').place(x=0,y=0,relwidth=1)

        lbl_emp_code=Label(emp_Frame=Label(self.root,text="Employee ID",font=("times new roman",15,'bold'),bg='white').place(20=0,y=60)
        lbl_emp_name=Label(emp_Frame=Label(self.root,text="NAME",font=("times new roman",15,'bold'),bg='white').place(20=0,y=100)
        lbl_emp_department=Label(emp_Frame=Label(self.root,text="Department",font=("times new roman",15,'bold'),bg='white').place(20=0,y=140)
        lbl_designation=Label(emp_Frame=Label(self.root,text="Designation",font=("times new roman",15,'bold'),bg='white').place(20=0,y=180)

        txt_emp_code=Entry(emp_Frame,font=("times new roman",15,'bold'),bg='lightyellow').place(20=0,y=60)
        txt_emp_name=Entry(emp_Frame,font=("times new roman",15,'bold'),bg='lightyellow').place(20=0,y=100)
        txt_emp_department=Entry(emp_Frame,font=("times new roman",15,'bold'),bg='lightyellow').place(20=0,y=140)
        txt_designation=Entry(emp_Frame,font=("times new roman",15,'bold'),bg='lightyellow').place(20=0,y=180)


        btn_gemerate=Button(emp_Frame,text='QR Generate',font=("times new roman",18, 'bold'),bg='#2196f3',fg='white').place(x=90,Y=250,width=200,height=30)
        btn_clear=Button(emp_Frame,text='Clear',font=("times new roman",18, 'bold'),bg='607d8b',fg='white').place(x=282,Y=250,width=200,height=30)
        
        self.msg='Qr Generator Successfully!!!'
        self.lbl_msg=Label(emp_Frame=Label(self.root,text=self.msg,font=("times new roman",20,),bg='white',fg='green').place(x=0,y=320,relwidth=1)

        #====Employee QR Code window=========
        qr_Frame+Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Erame=Label(self.root,text="Employee QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1,text="   Qr Code Generator",font=("times new roman",40),bg='#053246',fg'white' ,anchor='w').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,Text='No Qr\nAvailable',font=('times new roman',15),bg='3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.Place(x=35,y=100,width=180,height=180)

root=Tk()
obj =Qr_Generator
root.mainloop()    