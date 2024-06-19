from tkinter import*
from PIL import Image,ImageTk   #pip install pillow
from student import student_window
from room import Roombooking
from details import DetailsRoom
import tkinter as tk
import webbrowser



class managementSystem:
    def __init__(self,root) :
        self.root=root
        self.root.title("TechDorm")
        self.root.geometry("5500x2500+0+0")   # to size the screen


        img1=Image.open(r"C:\Users\sdgid\Desktop\Python Project\img11.jpg")            
        img1 = img1.resize((1920, 140), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg1=ImageTk.PhotoImage(img1)   # resized image is stored in this variable pimg1


        lblimg=Label(self.root,image=self.pimg1,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=0,width=1920,height=140)



        img2=Image.open(r"C:\Users\sdgid\Desktop\Python Project\logo.jpg")            
        img2 = img2.resize((220, 140), Image.LANCZOS) #high level image is converted to low level image using Antialias/lanczos
        self.pimg2=ImageTk.PhotoImage(img2)   # resized image is stored in this variable pimg2


        lblimg=Label(self.root,image=self.pimg2,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=0,width=230,height=140)

        
        lbl_title=Label(self.root,text="Tech Dorm",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)     #Stay,Learn,Grow
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




        img3=Image.open(r"C:\Users\sdgid\Desktop\Python Project\img10.png")            
        img3 = img3.resize((1673, 799), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg3=ImageTk.PhotoImage(img3)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg3,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=225,y=0,width=1690,height=815)





        img4=Image.open(r"C:\Users\sdgid\Desktop\Python Project\img8.jpg")            
        img4 = img4.resize((230, 210), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg4=ImageTk.PhotoImage(img4)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg4,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=225,width=228,height=210)


        img5=Image.open(r"C:\Users\sdgid\Desktop\Python Project\img9.jpg")            
        img5 = img5.resize((230, 190), Image.LANCZOS) #high level image is converted to low level image using Antialias
        self.pimg5=ImageTk.PhotoImage(img5)   # resized image is stored in this variable pimg2


        lblimg=Label(main_frame,image=self.pimg5,bd=4,relief=RIDGE)  #bd means border relief means style
        lblimg.place(x=0,y=420,width=228,height=190)



        img6=Image.open(r"C:\Users\sdgid\Desktop\Python Project\img12.jpg")            
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
    
    def open_link(self):
        url = "https://docs.google.com/forms/d/e/1FAIpQLSd2FnEvuZPA7MF_1IKq1LaTEAKvMy1HiI0ogHNmg325VFwcyw/viewform?usp=pp_url"  # Replace with the URL you want to open
        webbrowser.open(url)

    def ask_password1(self):
        password_window = tk.Toplevel(root)
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
        password_window = tk.Toplevel(root)
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
        password_window = tk.Toplevel(root)
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

    def logout(self):
        self.root.destroy()







if __name__=="__main__":  #to call main function 
    root=Tk()   #tool kit
    obj=managementSystem(root)
    root.mainloop()   # to close the main loop