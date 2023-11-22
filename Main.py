from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector

class EmployeeDetailsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Details")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="white")

        self.Emp_id=StringVar()
        self.Emp_name=StringVar()
        self.Emp_doj=StringVar()
        self.Emp_dob=StringVar()
        self.City_name=StringVar()
        self.Mobile_no=StringVar()
       
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=60,width=1350,height=350)
        title2=Label(Frame1,text="Employee details",font=("times new roman",20),bg='lightgray',fg="black",anchor="w",padx=10).place(x=550,y=0)

        lbl_id=Label(Frame1,text="Emp_id",font=("times new roman",20),bg='white',fg="black").place(x=10,y=70)
        txt_id=Entry(Frame1,text="Emp_id",textvariable=self.Emp_id,font=("times new roman",15),bg='lightyellow',fg="black").place(x=170,y=70,width=300)
        lbl_city=Label(Frame1,text="City_name",font=("times new roman",20),bg='white',fg="black").place(x=690,y=70)
        txt_city=Entry(Frame1,text="City_name",textvariable=self.City_name,font=("times new roman",15),bg='lightyellow',fg="black").place(x=870,y=70,width=300)
        
        lbl_mobno=Label(Frame1,text="Mobile_no",font=("times new roman",20),bg='white',fg="black").place(x=10,y=119)
        txt_mobno=Entry(Frame1,text="Mobile_no",textvariable=self.Mobile_no,font=("times new roman",15),bg='lightyellow',fg="black").place(x=170,y=119,width=300)
        lbl_dob=Label(Frame1,text="Emp_dob",font=("times new roman",20),bg='white',fg="black").place(x=690,y=119)
        txt_dob=Entry(Frame1,text="Emp_dob",textvariable=self.Emp_dob,font=("times new roman",15),bg='lightyellow',fg="black").place(x=870,y=119,width=300)





        lbl_name=Label(Frame1,text="Emp_name",font=("times new roman",20),bg='white',fg="black").place(x=10,y=160)
        txt_name=Entry(Frame1,text="Emp_name",textvariable=self.Emp_name,font=("times new roman",15),bg='lightyellow',fg="black").place(x=170,y=165,width=300)
        lbl_doj=Label(Frame1,text="Emp_doj",font=("times new roman",20),bg='white',fg="black").place(x=690,y=160)
        txt_doj=Entry(Frame1,text="Emp_doj",textvariable=self.Emp_doj,font=("times new roman",15),bg='lightyellow',fg="black").place(x=870,y=165,width=300)




        btn_update=Button(Frame1,text="Update",command=self.update,font=("times new roman",20),bg='orange',fg="black").place(x=450,y=300,height=30,width=120)
        btn_save=Button(Frame1,text="Save",command=self.add,font=("times new roman",20),bg='green',fg="white").place(x=580,y=300,height=30,width=120) 
        btn_delete=Button(Frame1,text="Delete",command=self.delete,font=("times new roman",20),bg='white',fg="black").place(x=710,y=300,height=30,width=120)
        # Add code for Employee Details window here


    def add(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into employee_details values(%s,%s,%s,%s,%s,%s)",(self.Emp_id.get(),self.City_name.get(),self.Mobile_no.get(),self.Emp_dob.get(),self.Emp_name.get(),self.Emp_doj.get(),))
 #my_cursor.execute("insert into Department values(%s,%s)",(self.Dept_id.get(),self.Dept_name.get(),))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record Added succesfully")
    




    def delete(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="delete from employee_details where ID=%s or City_name=%s or Mobile_no = %s or DOB =%s or Name=%s or DOJ =%s"
        value=(self.Emp_id.get(),self.City_name.get(),self.Mobile_no.get(),self.Emp_dob.get(),self.Emp_name.get(),self.Emp_doj.get(),)
        my_cursor.execute(query,value)

        #query="delete from Company where Company_name=%s or Company_id=%s or Company_mob_no= %s"
        #value=(self.Comapny_name.get(),self.Company_id.get(),self.Comp_mob_no.get(),)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Delete","Info has been deleted succesfully")

    def update(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="update employee_details set City_name=%s  where ID=%s"
        #or Mobile_no=%s or DOJ=%s self.Mobile_no.get(),self.Emp_doj.get(),
        value=(self.City_name.get(),self.Emp_id.get(),)
        my_cursor.execute(query,value)


        #query="update Department set Dept_name=%s where Dept_id=%s"
        #value=(self.Dept_name.get(),self.Dept_id.get(),)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Update","Info has been Updated succesfully")





class CompanyDetailsWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Company Details")


        self.Company_id = StringVar()
        self.Comapny_name=StringVar()
        self.Comp_mob_no = StringVar()
        self.comp_loc=StringVar()



        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=60,width=1500,height=350)
        # 
        title2=Label(Frame1,text="Company details",font=("times new roman",20),bg='lightgray',fg="black",anchor="w",padx=10).place(x=625,y=0)
        lbl_cid=Label(Frame1,text="Company_id",font=("times new roman",20),bg='white',fg="black").place(x=10,y=70)
        txt_cid=Entry(Frame1,text="Company_id",textvariable=self.Company_id,font=("times new roman",15),bg='lightyellow',fg="black").place(x=270,y=70,width=300)
        lbl_cname=Label(Frame1,text="Company_name",font=("times new roman",20),bg='white',fg="black").place(x=840,y=70)
        txt_cname=Entry(Frame1,text="Company_name",font=("times new roman",15),textvariable=self.Comapny_name,bg='lightyellow',fg="black").place(x=1120,y=70,width=300)
        lbl_no=Label(Frame1,text="Company_mob_no",font=("times new roman",20),bg='white',fg="black").place(x=10,y=150)
        txt_no=Entry(Frame1,text="Company_mob_no",font=("times new roman",15),textvariable=self.Comp_mob_no,bg='lightyellow',fg="black").place(x=270,y=150,width=300)
        lbl_location=Label(Frame1,text="Company_location",font=("times new roman",20),bg='white',fg="black").place(x=840,y=150)
        txt_location=Entry(Frame1,text="Company_location",font=("times new roman",15),textvariable=self.comp_loc,bg='lightyellow',fg="black").place(x=1120,y=150,width=300)

        btn_update=Button(Frame1,text="Update",command=self.update,font=("times new roman",20),bg='orange',fg="black").place(x=450,y=300,height=30,width=120)
        btn_save=Button(Frame1,text="Save",command=self.add,font=("times new roman",20),bg='green',fg="white").place(x=580,y=300,height=30,width=120) 
        btn_delete=Button(Frame1,text="Delete",command=self.delete,font=("times new roman",20),bg='white',fg="black").place(x=710,y=300,height=30,width=120)



    def add(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into company values(%s,%s,%s,%s)",(self.Company_id.get(),self.Comapny_name.get(),self.Comp_mob_no.get(),self.comp_loc.get()))



        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record Added succesfully")
    




    def delete(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="delete from Company where Company_name=%s or Company_id=%s or Company_mob_no= %s"
        value=(self.Comapny_name.get(),self.Company_id.get(),self.Comp_mob_no.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Delete","Info has been deleted succesfully")

    def update(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="update company set comp_loc=%s  where Company_id =%s"
        #or Mobile_no=%s or DOJ=%s self.Mobile_no.get(),self.Emp_doj.get(),
        value=(self.comp_loc.get(),self.Company_id.get(),)
        my_cursor.execute(query,value)


        #query="update Department set Dept_name=%s where Dept_id=%s"
        #value=(self.Dept_name.get(),self.Dept_id.get(),)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Update","Info has been Updated succesfully")

class PayrollWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll")

        self.emp_id=StringVar()
        self.salary_month=StringVar()
        self.net_salary=StringVar()
        self.trans_id=StringVar()
        self.salary_year=StringVar()
        self.reinburse_date=StringVar()


        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=60,width=1500,height=500)
        title2=Label(Frame1,text="Payroll",font=("times new roman",20),bg='lightgray',fg="black",anchor="w",padx=10).place(x=650,y=0)
        lbl_cid=Label(Frame1,text="Employee_id",font=("times new roman",20),bg='white',fg="black").place(x=10,y=70)
        txt_cid=Entry(Frame1,text="Employee_id",textvariable=self.emp_id ,font=("times new roman",15),bg='lightyellow',fg="black").place(x=270,y=70,width=300)
        
        lbl_cname=Label(Frame1,text="Transaction_id",font=("times new roman",20),bg='white',fg="black").place(x=840,y=70)
        txt_cname=Entry(Frame1,text="Transaction_id",textvariable=self.trans_id,font=("times new roman",15),bg='lightyellow',fg="black").place(x=1120,y=70,width=300)
        
        lbl_no=Label(Frame1,text="Emp_salary_month",font=("times new roman",20),bg='white',fg="black").place(x=10,y=150)
        txt_no=Entry(Frame1,text="Emp_salary_month",textvariable=self.salary_month,font=("times new roman",15),bg='lightyellow',fg="black").place(x=270,y=150,width=300)
        
        lbl_location=Label(Frame1,text="Emp_salary_year",font=("times new roman",20),bg='white',fg="black").place(x=840,y=150)
        txt_location=Entry(Frame1,text="Emp_salary_year",textvariable=self.salary_year,font=("times new roman",15),bg='lightyellow',fg="black").place(x=1120,y=150,width=300)
        
        lbl_no=Label(Frame1,text="Emp_net_salary",font=("times new roman",20),bg='white',fg="black").place(x=10,y=230)
        txt_no=Entry(Frame1,text="Emp_net_salary",textvariable=self.net_salary,font=("times new roman",15),bg='lightyellow',fg="black").place(x=270,y=230,width=300)
        
        lbl_location=Label(Frame1,text="Reinbursment_date",font=("times new roman",20),bg='white',fg="black").place(x=840,y=230)
        txt_location=Entry(Frame1,text="Reinbursment_date",textvariable=self.reinburse_date,font=("times new roman",15),bg='lightyellow',fg="black").place(x=1120,y=230,width=300)

        btn_update=Button(Frame1,text="Update",font=("times new roman",20),bg='orange',fg="black").place(x=550,y=400,height=30,width=120)
        btn_save=Button(Frame1,text="Save",command=self.add,font=("times new roman",20),bg='green',fg="white").place(x=680,y=400,height=30,width=120) 
        btn_delete=Button(Frame1,text="Delete",command=self.delete,font=("times new roman",20),bg='white',fg="black").place(x=810,y=400,height=30,width=120)


       
    def add(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into payroll values(%s,%s,%s,%s,%s,%s)",(self.emp_id.get(),self.salary_month.get(),self.net_salary.get(),self.trans_id.get(),self.salary_year.get(),self.reinburse_date.get(),))


        #my_cursor.execute("insert into Department values(%s,%s)",(self.Dept_id.get(),self.Dept_name.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record Added succesfully")


    # def delete(self):
    #     import mysql.connector
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
    #     my_cursor=conn.cursor()
    #     query="delete from paygrade where Grade_id =%s or Grade_name=%s or Grade_basic = %s or Grade_bonus =%s or Grade_ta =%s or Grade_da =%s"
    #     value=(self.Grade_id.get(),self.Grade_name.get(),self.Grade_basic.get(),self.Grade_bonus.get(),self.Grade_ta.get(),self.Grade_da.get(),)
    #     my_cursor.execute(query,value)

    #     #query="delete from Company where Company_name=%s or Company_id=%s or Company_mob_no= %s"
    #     #value=(self.Comapny_name.get(),self.Company_id.get(),self.Comp_mob_no.get(),)

    #     conn.commit()
    #     conn.close()
    #     # self.fetch_data()
    #     messagebox.showinfo("Delete","Info has been deleted succesfully")
    




    def delete(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="delete from payroll where emp_id =%s or salary_month =%s or net_salary= %s or trans_id = %s or salary_year =%s or reinburse_date=%s"
        value=(self.emp_id.get(),self.salary_month.get(),self.net_salary.get(),self.trans_id.get(),self.salary_year.get(),self.reinburse_date.get(),)
        my_cursor.execute(query,value)


        #query="delete from Company where Company_name=%s or Company_id=%s or Company_mob_no= %s"
        #value=(self.Comapny_name.get(),self.Company_id.get(),self.Comp_mob_no.get(),)


        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Delete","Info has been deleted succesfully")

class PayGradeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Pay Grade")
        # Add code for Pay Grade window here
        self.root = root
        self.root.title("Employee Details")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="white")


        self.Grade_id=StringVar()
        self.Grade_name=StringVar()
        self.Grade_basic=StringVar()
        self.Grade_bonus=StringVar()
        self.Grade_ta=StringVar()
        self.Grade_da=StringVar()


       
        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=60,width=1350,height=350)
        title2=Label(Frame1,text="Pay grade",font=("times new roman",20),bg='lightgray',fg="black",anchor="w",padx=10).place(x=550,y=0)

        lbl_Grade_id=Label(Frame1,text="Grade_id",font=("times new roman",20),bg='white',fg="black").place(x=10,y=70)
        txt_Grade_id=Entry(Frame1,text="Grade_id",textvariable=self.Grade_id,font=("times new roman",15),bg='lightyellow',fg="black").place(x=170,y=70,width=300)
        lbl_Grade_name=Label(Frame1,text="Grade_name",font=("times new roman",20),bg='white',fg="black").place(x=690,y=70)
        txt_Grade_name=Entry(Frame1,text="Grade_name",textvariable=self.Grade_name,font=("times new roman",15),bg='lightyellow',fg="black").place(x=870,y=70,width=300)
        
        lbl_Grade_basic=Label(Frame1,text="Grade_basic",font=("times new roman",20),bg='white',fg="black").place(x=10,y=119)
        txt_Grade_basic=Entry(Frame1,text="Grade_basic",textvariable=self.Grade_basic,font=("times new roman",15),bg='lightyellow',fg="black").place(x=170,y=119,width=300)
        lbl_Grade_bonus=Label(Frame1,text="Grade_bonus",font=("times new roman",20),bg='white',fg="black").place(x=690,y=119)
        txt_Grade_bonus=Entry(Frame1,text="Grade_bonus",textvariable=self.Grade_bonus,font=("times new roman",15),bg='lightyellow',fg="black").place(x=870,y=119,width=300)





        lbl_Grade_ta=Label(Frame1,text="Grade_ta",font=("times new roman",20),bg='white',fg="black").place(x=10,y=160)
        txt_Grade_ta=Entry(Frame1,text="Grade_ta",textvariable=self.Grade_ta,font=("times new roman",15),bg='lightyellow',fg="black").place(x=170,y=165,width=300)
        lbl_Grade_da=Label(Frame1,text="Grade_da",font=("times new roman",20),bg='white',fg="black").place(x=690,y=160)
        txt_Grade_da=Entry(Frame1,text="Grade_da",textvariable=self.Grade_da,font=("times new roman",15),bg='lightyellow',fg="black").place(x=870,y=165,width=300)

        btn_update=Button(Frame1,text="Update",font=("times new roman",20),bg='orange',fg="black").place(x=450,y=300,height=30,width=120)
        btn_save=Button(Frame1,text="Save",command=self.add,font=("times new roman",20),bg='green',fg="white").place(x=580,y=300,height=30,width=120) 
        btn_delete=Button(Frame1,text="Delete",command=self.delete,font=("times new roman",20),bg='white',fg="black").place(x=710,y=300,height=30,width=120)


    def add(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into paygrade values(%s,%s,%s,%s,%s,%s)",(self.Grade_id.get(),self.Grade_name.get(),self.Grade_basic.get(),self.Grade_bonus.get(),self.Grade_ta.get(),self.Grade_da.get(),))
 #my_cursor.execute("insert into Department values(%s,%s)",(self.Dept_id.get(),self.Dept_name.get(),))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record Added succesfully")
    




    def delete(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="delete from paygrade where Grade_id =%s or Grade_name=%s or Grade_basic = %s or Grade_bonus =%s or Grade_ta =%s or Grade_da =%s"
        value=(self.Grade_id.get(),self.Grade_name.get(),self.Grade_basic.get(),self.Grade_bonus.get(),self.Grade_ta.get(),self.Grade_da.get(),)
        my_cursor.execute(query,value)

        #query="delete from Company where Company_name=%s or Company_id=%s or Company_mob_no= %s"
        #value=(self.Comapny_name.get(),self.Company_id.get(),self.Comp_mob_no.get(),)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Delete","Info has been deleted succesfully")

    # def update(self):
    #     import mysql.connector
    #     conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
    #     my_cursor=conn.cursor()
    #     query="update employee_details set City_name=%s  where ID=%s"
    #     #or Mobile_no=%s or DOJ=%s self.Mobile_no.get(),self.Emp_doj.get(),
    #     value=(self.City_name.get(),self.Emp_id.get(),)
    #     my_cursor.execute(query,value)


    #     #query="update Department set Dept_name=%s where Dept_id=%s"
    #     #value=(self.Dept_name.get(),self.Dept_id.get(),)

    #     conn.commit()
    #     conn.close()
    #     # self.fetch_data()
    #     messagebox.showinfo("Update","Info has been Updated succesfully")


class DepartmentDetailsWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Department Details")

        self.Dept_id = StringVar()
        self.Dept_name=StringVar()



        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=60,width=1500,height=350) 
        title2=Label(Frame1,text="Department_details",font=("times new roman",20),bg='lightgray',fg="black",anchor="w",padx=10).place(x=625,y=0)
        lbl_Dept_id=Label(Frame1,text="Department_id",font=("times new roman",20),bg='white',fg="black").place(x=10,y=70)
        txt_Dept_id=Entry(Frame1,text="Department_id",textvariable=self.Dept_id,font=("times new roman",15),bg='lightyellow',fg="black").place(x=270,y=70,width=300)
        lbl_Dept_name=Label(Frame1,text="Department_name",font=("times new roman",20),bg='white',fg="black").place(x=840,y=70)
        txt_Dept_name=Entry(Frame1,text="Department_name",textvariable=self.Dept_name,font=("times new roman",15),bg='lightyellow',fg="black").place(x=1120,y=70,width=300)

        btn_update=Button(Frame1,text="Update",command=self.update,font=("times new roman",20),bg='orange',fg="black").place(x=550,y=200,height=30,width=120)
        btn_save=Button(Frame1,text="Save",command=self.add,font=("times new roman",20),bg='green',fg="white").place(x=680,y=200,height=30,width=120) 
        btn_delete=Button(Frame1,text="Delete",command=self.delete,font=("times new roman",20),bg='white',fg="black").place(x=810,y=200,height=30,width=120)

    def add(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into Department values(%s,%s)",(self.Dept_id.get(),self.Dept_name.get(),))



        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record Added succesfully")
    




    def delete(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="delete from Department where Dept_name=%s or Dept_id=%s"
        value=(self.Dept_name.get(),self.Dept_id.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Delete","Info has been deleted succesfully")

    def update(self):
        import mysql.connector
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya@9403",database="payroll_management_system")
        my_cursor=conn.cursor()
        query="update Department set Dept_name=%s where Dept_id=%s"
        value=(self.Dept_name.get(),self.Dept_id.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        # self.fetch_data()
        messagebox.showinfo("Update","Info has been Updated succesfully")




class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1370x700+0+0")
        self.root.config(bg="#f0f0f0")  # Background color

        #self.create_menu()
        self.set_background_image()  # Add background image

        self.create_menu()
    
    # def create_menu(self):
    # # Add buttons to open different windows
    #     button_styles = [
    #         {"text": "Employee Details", "command": self.open_employee_window, "bg": "#4CAF50"},  # Green
    #         {"text": "Company Details", "command": self.open_company_window, "bg": "#2196F3"},  # Blue
    #         {"text": "Payroll", "command": self.open_payroll_window, "bg": "#FF9800"},  # Orange
    #         {"text": "Pay Grade", "command": self.open_paygrade_window, "bg": "#9C27B0"},  # Purple
    #         {"text": "Department Details", "command": self.open_department_window, "bg": "#FF5722"},  # Deep Orange
    #     ]

    #     for button_style in button_styles:
    #         button = tk.Button(
    #             self.root,
    #             text=button_style["text"],
    #             command=button_style["command"],
    #             bg=button_style["bg"],
    #             fg="#ffffff",  # Brighter font color (white)
    #             height=3,
    #             width=30,
    #             bd=0,
    #             cursor="hand2",
    #             activebackground="#BDBDBD",c 
    #                                                                                                                                                                                                                       
    # 
    # 
    # 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      #         )
    #         button.pack(side=tk.LEFT, padx=10, pady=10) 
    #  # Place buttons on the left side with some padding

    def create_menu(self):
    # Add buttons to open different windows
        button_styles = [
            {"text": "Employee Details", "command": self.open_employee_window, "bg": "#000000"},  # Black
            {"text": "Company Details", "command": self.open_company_window, "bg": "#2196F3"},  # Blue
            {"text": "Payroll", "command": self.open_payroll_window, "bg": "#000000"},  # Black
            {"text": "Pay Grade", "command": self.open_paygrade_window, "bg": "#2196F3"},  # Blue
            {"text": "Department Details", "command": self.open_department_window, "bg": "#000000"},  # Black
        ]

        for button_style in button_styles:
            button = tk.Button(
                self.root,
                text=button_style["text"],
                command=button_style["command"],
                bg=button_style["bg"],
                fg="#ffffff",  # Brighter font color (white)
                height=3,
                width=30,
                bd=0,
                cursor="hand2",
                activebackground="#BDBDBD",
            )
            button.pack(side=tk.TOP, padx=10, pady=10)  # Place buttons at the top with some padding




    def set_background_image(self):
        try:
            # Load the image
            img = Image.open(r"C:\Users\Pai\Desktop\op.JPG")

            # Resize the image to fit the window size
            img = img.resize((1370, 700), Image.ANTIALIAS)

            # Convert the image to Tkinter PhotoImage
            img = ImageTk.PhotoImage(img)

            # Create a Label to hold the image
            bg_label = tk.Label(self.root, image=img)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            # Ensure the image persists by attaching it to an attribute of the label
            bg_label.image = img

        except Exception as e:
            print("Error loading background image:", e)
    def open_employee_window(self):
        employee_window = tk.Toplevel(self.root)
        employee_details = EmployeeDetailsWindow(employee_window)

    def open_company_window(self):
        company_window = tk.Toplevel(self.root)
        company_details = CompanyDetailsWindow(company_window)

    def open_payroll_window(self):
        payroll_window = tk.Toplevel(self.root)
        payroll = PayrollWindow(payroll_window)

    def open_paygrade_window(self):
        paygrade_window = tk.Toplevel(self.root)
        pay_grade = PayGradeWindow(paygrade_window)

    def open_department_window(self):
        department_window = tk.Toplevel(self.root)
        department_details = DepartmentDetailsWindow(department_window)

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()