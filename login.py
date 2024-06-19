from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector
import random
from student import student_window
from room import Roombooking
from details import DetailsRoom
import webbrowser

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("TECHDORM")
        self.root.geometry("1550x800+0+0")


        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\logo.jpg")  # Replace with your image path/image name
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Labels
        username = Label(frame, text="Enter Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Enter Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

    

        # Icon Images
        img2 = Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\user.jpg")  
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\password.jpg")  
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=393, width=25, height=25)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"), borderwidth=0,
                             fg="white", bg="black", activeforeground="white", activebackground="red")
        registerbtn.place(x=15, y=350, width=160)

        # Forget Password Button
        forget_password_btn = Button(frame, text="Forgot Password",command=self.forgot_password_window,font=("times new roman", 10, "bold"),
                                     borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="red")
        forget_password_btn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "ALL FIELDS ARE REQUIRED TO BE FILLED")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            cur=conn.cursor()
            cur.execute("select * from register where email=%s and password=%s",(
                                                                             self.txtuser.get(),
                                                                             self.txtpass.get()
                                                                      ))

        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid Username and Password")
        else:
               self.new_window=Toplevel(self.root)
               self.app=managementSystem(self.new_window)
        conn.commit()
        conn.close()   
    

    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpswd.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="studentmanagement")
            cur=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_securiy_Q.get(),self.txt_security.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpswd.get(),self.txtuser.get())
                cur.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with the new password",parent=self.root2)
                self.root2.destroy()
            
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset the password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="studentmanagement")
            cur=conn.cursor()
            query=("select * from register where email=%s")  
            value=(self.txtuser.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter a valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman", 10, "bold"),fg="red", bg="white")
                l.place(x=0,y=10,relwidth=1)


                security_Q=Label(self.root2,text="Select Security Questions", font=("times new roman",15,"bold"), bg="white", fg="black")
                security_Q.place (x=50, y=80)

                self.combo_securiy_Q=ttk.Combobox (self.root2,font=("times new roman", 15, "bold"),state="readonly")

                self.combo_securiy_Q["values"]=("Select", "Your Birth Place", "Your Nick Name", "Your Pet Name")

                self.combo_securiy_Q.place(x=50,y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A=Label(self.root2, text="Security Answer", font=("times new roman",15,"bold"), bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))

                self.txt_security.place(x=50,y=180, width=250)

                pswd=Label(self.root2, text="New Password",font=("times new roman", 15, "bold"), bg="white", fg="black")
                pswd.place(x=50,y=220)

                self.txt_newpswd=ttk.Entry(self.root2,font=("times new roman",15,"bold")) 

                self.txt_newpswd.place(x=50,y=250,width=250)


                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="green", fg="white")
                btn.place(x=100,y=290)



class Register:

    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")




        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\sdgid\OneDrive\Desktop\Python Project\iiitklogo.png")# Replace with your image path
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        fname = Label(frame, text="First Name", font=("times new roman",15, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)
        l_name=Label(frame, text="Last Name", font=("times new noman", 15, "bold"), bg="white",fg="black")
        l_name.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman", 15))
        self.txt_lname.place(x=370,y=130, width=250)
        #--row2
        contact=Label(frame, text="Contact No", font=("times new roman", 15, "bold"),bg="white",fg="black") 
        contact.place(x=50,y=170)
        self.txt_contact=ttk. Entry (frame,textvariable=self.var_contact, font=("times new roman",15))
        self.txt_contact.place (x=50,y=200, width=250)
        email=Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200, width=250)

        #-----row3

        security_Q=Label(frame,text="Select Security Questions", font=("times new roman",15,"bold"), bg="white", fg="black")
        security_Q.place (x=50, y=240)

        self.combo_securiy_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman", 15, "bold"),state="readonly")

        self.combo_securiy_Q["values"]=("Select", "Your Birth Place", "Your Nick Name", "Your Pet Name")

        self.combo_securiy_Q.place(x=50,y=270, width=250)
        self.combo_securiy_Q.current(0)

        security_A=Label (frame, text="Security Answer", font=("times new roman",15,"bold"), bg="white",fg="black")
        security_A.place(x=370,y=240)


        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))

        self.txt_security.place(x=370,y=270, width=250)
        #r============4
        pswd=Label(frame, text="Password",font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50,y=310)

        self.txt_newpswd=ttk. Entry (frame,textvariable=self.var_pass,font=("times new roman",15))

        self.txt_newpswd.place(x=50,y=340,width=250)

        confirm_pswd=Label (frame,text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry (frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340, width=250)
      


        img=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\registerbutton.jpg")
        img=img.resize((200,55), Image.LANCZOS)
        self.photoimage=ImageTk. PhotoImage(img)
        b1=Button(frame, image=self.photoimage,command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white")
        b1.place(x=10,y=420, width=200)

        img1=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\loginbutton.jpg")
        img1=img1.resize((200,45), Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,command=self.return_login,image=self.photoimage1,borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"), fg="white") 
        b1.place(x=330, y=420, width=200)



    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required")
        
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Passwords are not matching")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="studentmanagement")  ##########
            cur=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            cur.execute(query,value)
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User/Administrator already exists")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                       self.var_fname.get(),
                                                                       self.var_lname.get(),
                                                                       self.var_contact.get(),
                                                                       self.var_email.get(),
                                                                       self.var_securityQ.get(),
                                                                       self.var_securityA.get(),
                                                                       self.var_pass.get()
                                                                               
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()



class managementSystem:
    def __init__(self,root) :
        self.root=root
        self.root.title("TechDorm")
        self.root.geometry("5500x2500+0+0")   # to size the screen


        img1=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\img11.jpg")            
        img1 = img1.resize((1920, 140), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg1=ImageTk.PhotoImage(img1)   # resized image is stored in this variable pimg1


        lblimg=Label(self.root,image=self.pimg1,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=0,width=1920,height=140)



        img2=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\logo.jpg")            
        img2 = img2.resize((220, 140), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg2=ImageTk.PhotoImage(img2)   # resized image is stored in this variable pimg2


        lblimg=Label(self.root,image=self.pimg2,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=0,width=230,height=140)

        lbl_title=Label(self.root,text="Tech Dorm",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1920,height=50)



        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1920,height=890)


        lb1_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_menu.place(x=0,y=0,width=230)

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)


        stu_btn=Button(btn_frame,text="STUDENT",command=self.ask_password1,font=("times new roman",14,"bold"),width=22,bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        stu_btn.grid(row=0,column=0,pady=1)


        room_btn=Button(btn_frame,text="ROOM",command=self.ask_password2,font=("times new roman",14,"bold"),width=22,bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)


        details_btn=Button(btn_frame,text="DETAILS",command=self.ask_password3,font=("times new roman",14,"bold"),width=22,bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="ONLINE FORM",command=self.open_link,font=("times new roman",14,"bold"),width=22,bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,font=("times new roman",14,"bold"),width=22,bg="black",fg="gold",bd=0,relief=RIDGE,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)




        img3=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\img10.png")            
        img3 = img3.resize((1673, 799), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg3=ImageTk.PhotoImage(img3)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg3,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=225,y=0,width=1690,height=815)





        img4=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\img8.jpg")            
        img4 = img4.resize((230, 210), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg4=ImageTk.PhotoImage(img4)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg4,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=225,width=228,height=210)


        img5=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\img9.jpg")            
        img5 = img5.resize((230, 190), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg5=ImageTk.PhotoImage(img5)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg5,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=420,width=228,height=190)



        img6=Image.open(r"C:\Users\sdgid\OneDrive\Desktop\Python Project\img12.jpg")            
        img6 = img6.resize((243, 193), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg6=ImageTk.PhotoImage(img6)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg6,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=610,width=228,height=197)
    

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student_window(self.new_window)   #to open student window


    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)   #to open student window

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)   #to open student window


    def logout(self):
        self.root.destroy()

    def open_link(self):
        url = "https://docs.google.com/forms/d/e/1FAIpQLSd2FnEvuZPA7MF_1IKq1LaTEAKvMy1HiI0ogHNmg325VFwcyw/viewform?usp=pp_url"  # Replace with the URL you want to open
        webbrowser.open(url)

    def ask_password1(self):
        password_window = Toplevel()
        password_window.title("Password Entry")
        # Create a Label to instruct the user
        label = Label(password_window, text="Enter the password:")
        label.pack()

        # Create an Entry widget for password input
        password_entry = Entry(password_window, show="*")  # Set show="*" to hide the entered characters
        password_entry.pack()

        # Create a function to check the entered password
        def check_password():
            entered_password = password_entry.get()
            if entered_password == "214":
                print("Password is correct. Access granted.")
                self.student_details()
                password_window.destroy()
            else:
                print("Incorrect password. Try again.")


        submit_button = Button(password_window, text="Submit", command=check_password)
        submit_button.pack()


    def ask_password2(self):
        password_window = Toplevel()
        password_window.title("Password Entry")
        # Create a Label to instruct the user
        label = Label(password_window, text="Enter the password:")
        label.pack()

        # Create an Entry widget for password input
        password_entry = Entry(password_window, show="*")  # Set show="*" to hide the entered characters
        password_entry.pack()

        # Create a function to check the entered password
        def check_password():
            entered_password = password_entry.get()
            if entered_password == "214":
                print("Password is correct. Access granted.")
                self.roombooking()
                password_window.destroy()
            else:
                print("Incorrect password. Try again.")

        submit_button = Button(password_window, text="Submit", command=check_password)
        submit_button.pack()


    def ask_password3(self):
        password_window = Toplevel()
        password_window.title("Password Entry")
        # Create a Label to instruct the user
        label = Label(password_window, text="Enter the password:")
        label.pack()

        # Create an Entry widget for password input
        password_entry = Entry(password_window, show="*")  # Set show="*" to hide the entered characters
        password_entry.pack()

        # Create a function to check the entered password
        def check_password():
            entered_password = password_entry.get()
            if entered_password == "214":
                print("Password is correct. Access granted.")
                self.details_room()
                password_window.destroy()
            else:
                print("Incorrect password. Try again.")

        

        # Create a button to submit the entered password
        submit_button = Button(password_window, text="Submit", command=check_password)
        submit_button.pack()




if __name__ == "__main__":
    main()
