from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root) :
        self.root=root
        self.root.title("TechDorm")
        self.root.geometry("1295x550+230+220")   # to size the screen



        self.var_Contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noOfdays=StringVar()
        #self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        




        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)



        img2=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\logo.jpg")     #r is convert backslash to slash    
        img2 = img2.resize((100, 40), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg2=ImageTk.PhotoImage(img2)   # resized image is stored in this variable pimg2


        lblimg=Label(self.root,image=self.pimg2,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        lbl_student_contact=Label(labelframeleft,text="Student Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_student_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_Contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        btnFetchData=Button(labelframeleft,text="Fetch Data",command=self.fetch_contact,font=("arial",8,"bold"),bg="black",fg="gold",width=9)
        btnFetchData.place(x=347,y=4)



        check_in_date=Label(labelframeleft,text="Check_in Date:",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)


        lbl_check_out=Label(labelframeleft,text="Check_Out Date:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_check_out.grid(row=2,column=0,sticky=W)

        txt_check_out=ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkout,font=("arial",13,"bold"))
        txt_check_out.grid(row=2,column=1)


        label_RoomType=Label(labelframeleft,text="Room Type:",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=('arial',12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Triple")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        lblRoomAvailable=Label(labelframeleft,text="Room No:",font=("arial",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=('arial',12,"bold"),width=27,state="readonly")
        combo_RoomNo["value"]=rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)

        lblMeal=Label(labelframeleft,text="Meal:",font=("arial",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        txtMeal=ttk.Entry(labelframeleft,width=29,textvariable=self.var_meal,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)


        lblNoOfDays=Label(labelframeleft,text="No. Of Days:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)

        txtNoOfDays=ttk.Entry(labelframeleft,width=29,textvariable=self.var_noOfdays,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=7,column=1)




        lblTotalcost=Label(labelframeleft,text="Total Cost:",font=("arial",12,"bold"),padx=2,pady=6)
        lblTotalcost.grid(row=8,column=0,sticky=W)

        txtTotalcost=ttk.Entry(labelframeleft,width=29,textvariable=self.var_total,font=("arial",13,"bold"))
        txtTotalcost.grid(row=8,column=1)


        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnBill.grid(row=6,column=0,padx=1,sticky=W)









        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=412,height=40)  #400-->420

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)


        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.sDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)


        btnReset=Button(btn_frame,text="Reset",command=self.reset ,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        img3=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\img13.jpg")     #r is convert backslash to slash    
        img3 = img3.resize((520,300), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg3=ImageTk.PhotoImage(img3)   # resized image is stored in this variable pimg2


        lblimg=Label(self.root,image=self.pimg3,bd=0,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=760,y=55,width=520,height=200)









        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=('arial',12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,width=24,textvariable=self.txt_search,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)


        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)


        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)



        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


        self.room_table=ttk.Treeview(details_table,column=("Mobile","Checkin","Checkout","RoomType","RoomAvailable","Meal","NoOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Mobile",text="Mobile")
        self.room_table.heading("Checkin",text="Check-in")
        self.room_table.heading("Checkout",text="Check-out")
        self.room_table.heading("RoomType",text="Room Type")
        self.room_table.heading("RoomAvailable",text="Room No.")
        self.room_table.heading("Meal",text="Meal")
        self.room_table.heading("NoOfDays",text="NoOfDays")


        self.room_table['show']="headings"

        self.room_table.column("Mobile",width=100)
        self.room_table.column("Checkin",width=100)
        self.room_table.column("Checkout",width=100)
        self.room_table.column("RoomType",width=100)
        self.room_table.column("RoomAvailable",width=100)
        self.room_table.column("Meal",width=100)
        self.room_table.column("NoOfDays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    
    def add_data(self):
        if self.var_Contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root) ############
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                        self.var_Contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noOfdays.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

#fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_Contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6])

#update 
    def update(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set checkin=%s,checkout=%s,roomtype=%s,Room=%s,meal=%s,noOfdays=%s where Mobile=%s",(
                                                        self.var_checkin.get(),
                                                        self.var_checkout.get(),
                                                        self.var_roomtype.get(),
                                                        self.var_roomavailable.get(),
                                                        self.var_meal.get(),
                                                        self.var_noOfdays.get(),
                                                        self.var_Contact.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)

    def sDelete(self):
        sDelete=messagebox.askyesno("Student Management System","Do you want to delete this room",parent=self.root)
        if sDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            my_cursor=conn.cursor()
            query="delete from room where Mobile=%s"
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not sDelete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        self.var_Contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfdays.set("")
        self.var_total.set("")





    def fetch_contact(self):
        if self.var_Contact.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            my_cursor=conn.cursor()  
            query=("select Name from student where Mobile=%s")
            value=(self.var_Contact.get(),)
            my_cursor.execute(query,value) 
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This Number Is Not Found",parent=self.root)
            else:

                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)


                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)


                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()  
                query=("select Gender from student where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)


                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()  
                query=("select Email from student where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()  
                query=("select Nationality from student where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)

                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()  
                query=("select Address from student where Mobile=%s")
                value=(self.var_Contact.get(),)
                my_cursor.execute(query,value) 
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)

        if self.var_meal.get()=="Yes" and self.var_roomtype.get()=="Single":
            q1=float(70)
            q2=float(600)
            q3=float(self.var_noOfdays.get())
            TT=("Rs.",str(q3*(q2+(q1*3))))
            self.var_total.set(TT)


        elif self.var_meal.get()=="No" and self.var_roomtype.get()=="Single":
            q2=float(600)
            q3=float(self.var_noOfdays.get())
            self.var_total.set(q2*q3)    



        elif self.var_meal.get()=="Yes" and self.var_roomtype.get()=="Double":
            q1=float(70)
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            TT=("Rs.",str(q3*(q2+(q1*3))))
            self.var_total.set(TT)


        elif self.var_meal.get()=="No" and self.var_roomtype.get()=="Double":
            q2=float(500)
            q3=float(self.var_noOfdays.get())
            self.var_total.set(q2*q3)    


        elif self.var_meal.get()=="Yes" and self.var_roomtype.get()=="Triple":
            q1=float(70)
            q2=float(350)
            q3=float(self.var_noOfdays.get())
            TT=("Rs.",str(q3*(q2+(q1*3))))
            self.var_total.set(TT)


        elif self.var_meal.get()=="No" and self.var_roomtype.get()=="Triple":
            q2=float(350)
            q3=float(self.var_noOfdays.get())
            self.var_total.set(q2*q3)    

            



            








                





if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
