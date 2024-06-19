from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class DetailsRoom:
    def __init__(self,root) :
        self.root=root
        self.root.title("TechDorm")
        self.root.geometry("1295x550+230+220")   # to size the screen
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)



        img2=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\iiitklogo.png")     #r is convert backslash to slash    
        img2 = img2.resize((100, 40), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg2=ImageTk.PhotoImage(img2)   # resized image is stored in this variable pimg2


        lblimg=Label(self.root,image=self.pimg2,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)


        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)


        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)
        
        self.var_RoomNo=StringVar()
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)


        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)
        
        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)



        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)  #400-->420

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)


        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)


        btnDelete=Button(btn_frame,text="Delete",command=self.sDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)


        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)


        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)


        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)


        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        
        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room No")
        self.room_table.heading("roomType",text="Room Type")
        


        self.room_table['show']="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomNo.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)   
    

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2])

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter Floor number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="studentmanagement")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET Floor=%s, RoomType=%s WHERE RoomNo=%s", (
                self.var_floor.get(),
                self.var_RoomType.get(),
                self.var_RoomNo.get()
            ))
            conn.commit()
            conn.close()

            # Clear the table
            for item in self.room_table.get_children():
                self.room_table.delete(item)

            # Fetch and display the updated data
            self.fetch_data()

            messagebox.showinfo("Update", "New Room details have been updated successfully", parent=self.root)


    def sDelete(self):
        sDelete=messagebox.askyesno("Student Management System","Do you want to delete this Room Details",parent=self.root)
        if sDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not sDelete:
                return
            
        conn.commit()
        self.fetch_data()
        conn.close()


    def  reset_data(self):
        self.var_floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set("")
    
    






if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
