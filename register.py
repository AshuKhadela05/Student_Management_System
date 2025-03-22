# from tkinter import *
# from tkinter import ttk,messagebox
# from PIL import Image, ImageTk  # pip install pillow
# # import pymysql # pip install pymysql
# import mysql.connector
# from login import Login


# class Register:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Registration Form")
#         self.root.geometry("1520x785+0+0")
#         self.root.config(bg="white")
        
#         # Bg Image
        
#         # Load and resize the background image
#         bg_image = Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/b2.jpg")
#         bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
#         self.bg = ImageTk.PhotoImage(bg_image)

#         # Set the image as the background
#         bg = Label(self.root, image=self.bg)
#         bg.place(x=0, y=0, relwidth=1, relheight=1)

#         # Load and resize the left image
#         left_image = Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/r.jpg")
#         left_image = left_image.resize((400, 500), Image.Resampling.LANCZOS)  # Resize to 400x500 pixels
#         self.left = ImageTk.PhotoImage(left_image)

#         # Set the left image inside a label
#         left = Label(self.root, image=self.left)
#         left.place(x=220, y=130, width=400, height=500)  # Correctly setting width & height

#         # Register Frame
#         Frame1=Frame(self.root,bg="white")
#         Frame1.place(x=600,y=130,width=670,height=500)

#         title=Label(Frame1,text="REGISTER HERE",font=("montserrat",20,"bold"),bg="white",fg="#17A2B8").place(x=50,y=30)

#         # self.var_fname=StringVar()

#         #-----------
#         f_name=Label(Frame1,text="First Name:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=50,y=80)
#         self.txt_fname=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_fname.place(x=50,y=120,width=250)

#         l_name=Label(Frame1,text="Last Name:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=370,y=80)
#         self.txt_lname=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_lname.place(x=370,y=120,width=250)
        
#         # ----------
#         contact=Label(Frame1,text="Contact No:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=50,y=150)
#         self.txt_contact=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_contact.place(x=50,y=190,width=250)
        
#         email=Label(Frame1,text="Email:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=370,y=150)
#         self.txt_email=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_email.place(x=370,y=190,width=250)
        
#         # ----------
#         question=Label(Frame1,text="Security question:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=50,y=220)
#         self.cmd_quest=ttk.Combobox(Frame1,font=("montserrat",13),state='readonly',justify=CENTER)
#         self.cmd_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
#         self.cmd_quest.place(x=50,y=260,width=250)
#         self.cmd_quest.current(0)

#         answer=Label(Frame1,text="Answer:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=370,y=220)
#         self.txt_answer=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_answer.place(x=370,y=260,width=250)
        
#         # ----------
#         password=Label(Frame1,text="Password:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=50,y=290)
#         self.txt_pasword=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_pasword.place(x=50,y=330,width=250)

#         cpassword=Label(Frame1,text="Confirm Password:",font=("montserrat",15,"bold"),bg="white",fg="black").place(x=370,y=290)
#         self.txt_cpassword=Entry(Frame1,font=("montserrat",15),bg="lightgray")
#         self.txt_cpassword.place(x=370,y=330,width=250)
        
#         # Terms
#         self.var_chk=IntVar()
#         chk=Checkbutton(Frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("montserrat,",12,'bold')).place(x=50,y=370)

#         self.btn_img=ImageTk.PhotoImage(file="D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/register.png")
#         btn_register=Button(Frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        
#         btn_login = Button(self.root, text="Sign In", font=("montserrat", 12), bd=0, cursor="hand2",command=self.login_window,bg="#17A2B8", fg="black", activebackground="#138496", activeforeground="white")
#         btn_login.place(x=300, y=550, width=150)

#     def login_window(self):
#         from login import Login  # Import only inside the function
#         self.new_window = Toplevel(self.root)
#         Login(self.new_window)

#     def open_login(self):
#         self.root.destroy()  # Close the register window
#         import login
#         login.Login(Tk())  # Open login window


#     def clear(self):
#         self.txt_fname.delete(0,END)
#         self.txt_lname.delete(0,END)
#         self.txt_contact.delete(0,END)
#         self.txt_email.delete(0,END)
#         self.txt_answer.delete(0,END)
#         self.txt_pasword.delete(0,END)
#         self.txt_cpassword.delete(0,END)
#         self.cmd_quest.current(0)
        
        
#     def register_data(self):
#         if (self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmd_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_pasword.get() == "" or self.txt_cpassword.get() == ""):
#             messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        
#         elif self.txt_pasword.get() != self.txt_cpassword.get():
#             messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=self.root)
        
#         elif self.var_chk.get() == 0:
#             messagebox.showerror("Error", "Please Agree to Our Terms & Conditions", parent=self.root)
        
#         else:
#             try:
#                 # Connect to MySQL database
#                 con = mysql.connector.connect(
#                     host="localhost",
#                     user="root",
#                     password="Ashish@0629",
#                     database="sms"
#                 )
#                 cur = con.cursor()

#                 # Check if email already exists
#                 cur.execute("SELECT * FROM register WHERE email=%s", (self.txt_email.get(),))
#                 row = cur.fetchone()

#                 if row!=None:
#                     messagebox.showerror("Error", "Email already registered! Try with another email.", parent=self.root)
#                 else:
#                     # Insert new user data
#                     cur.execute("""
#                         INSERT INTO register (f_name, l_name, contact, email, question, answer, password)
#                         VALUES (%s, %s, %s, %s, %s, %s, %s)
#                     """, (
#                         self.txt_fname.get(),
#                         self.txt_lname.get(),
#                         self.txt_contact.get(),
#                         self.txt_email.get(),
#                         self.cmd_quest.get(),
#                         self.txt_answer.get(),
#                         self.txt_pasword.get()
#                     ))

#                     con.commit()
#                     messagebox.showinfo("Success", "Registration Successful!", parent=self.root)
#                     self.clear()
#                     self.login_window()
#                 # Close connection
#                 cur.close()
#                 con.close()

#             except mysql.connector.Error as err:
#                 messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)



    
# if __name__ == "__main__":
#     root = Tk()
#     obj = Register(root)
#     root.mainloop()

from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1520x785+0+0")
        self.root.config(bg="white")

        # Bg Image
        bg_image = Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/b2.jpg")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        bg = Label(self.root, image=self.bg)
        bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Left Image
        left_image = Image.open("D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/r.jpg")
        left_image = left_image.resize((400, 500), Image.Resampling.LANCZOS)
        self.left = ImageTk.PhotoImage(left_image)
        left = Label(self.root, image=self.left)
        left.place(x=220, y=130, width=400, height=500)

        # Register Frame
        Frame1 = Frame(self.root, bg="white")
        Frame1.place(x=600, y=130, width=670, height=500)

        title = Label(Frame1, text="REGISTER HERE", font=("montserrat", 20, "bold"), bg="white", fg="#17A2B8").place(x=50, y=30)

        # Form Fields
        f_name = Label(Frame1, text="First Name:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=50, y=80)
        self.txt_fname = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=120, width=250)

        l_name = Label(Frame1, text="Last Name:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=370, y=80)
        self.txt_lname = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=120, width=250)

        contact = Label(Frame1, text="Contact No:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=50, y=150)
        self.txt_contact = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=190, width=250)

        email = Label(Frame1, text="Email:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=370, y=150)
        self.txt_email = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_email.place(x=370, y=190, width=250)

        question = Label(Frame1, text="Security question:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=50, y=220)
        self.cmd_quest = ttk.Combobox(Frame1, font=("montserrat", 13), state='readonly', justify=CENTER)
        self.cmd_quest['values'] = ("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmd_quest.place(x=50, y=260, width=250)
        self.cmd_quest.current(0)

        answer = Label(Frame1, text="Answer:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=370, y=220)
        self.txt_answer = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_answer.place(x=370, y=260, width=250)

        password = Label(Frame1, text="Password:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=50, y=290)
        self.txt_pasword = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_pasword.place(x=50, y=330, width=250)

        cpassword = Label(Frame1, text="Confirm Password:", font=("montserrat", 15, "bold"), bg="white", fg="black").place(x=370, y=290)
        self.txt_cpassword = Entry(Frame1, font=("montserrat", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=330, width=250)

        self.var_chk = IntVar()
        chk = Checkbutton(Frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("montserrat", 12, 'bold')).place(x=50, y=370)

        self.btn_img = ImageTk.PhotoImage(file="D:/Ashish khadela/Master/SEM_2/PYTHON/Mini_Project/SMS/Code/img/register.png")
        btn_register = Button(Frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420)

        btn_login = Button(self.root, text="Sign In", font=("montserrat", 12), bd=0, cursor="hand2", command=self.login_window, bg="#17A2B8", fg="black", activebackground="#138496", activeforeground="white")
        btn_login.place(x=300, y=550, width=150)

    def login_window(self):
        self.root.destroy()  # Close the register window
        from login import Login  # Import the Login class
        login_root = Tk()  # Create a new Tkinter root window
        Login(login_root)  # Initialize the Login window
        login_root.mainloop()  # Start the Tkinter event loop for the Login window

    def register_data(self):
        if (self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmd_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_pasword.get() == "" or self.txt_cpassword.get() == ""):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.txt_pasword.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree to Our Terms & Conditions", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Ashish@0629",
                    database="sms"
                )
                cur = con.cursor()
                cur.execute("SELECT * FROM register WHERE email=%s", (self.txt_email.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Email already registered! Try with another email.", parent=self.root)
                else:
                    cur.execute("""
                        INSERT INTO register (f_name, l_name, contact, email, question, answer, password)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.cmd_quest.get(),
                        self.txt_answer.get(),
                        self.txt_pasword.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Registration Successful!", parent=self.root)
                    self.clear()
                    self.login_window()
                cur.close()
                con.close()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error due to: {str(err)}", parent=self.root)

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pasword.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmd_quest.current(0)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()


