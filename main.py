import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import tkinter.font as font
  
    
class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    
        # Sign in part
        self.border = tk.LabelFrame(self, text='Please sign in', fg="lime", bg='black', bd = 10, font=('Serif', 20))
        self.border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        self.user_label = tk.Label(self.border, text="Username", font=("Arial" , 15), fg = "lime", bg='black')
        self.user_label.place(x=50, y=20)
        self.user_entry = tk.Entry(self.border, width = 30, bd = 5)
        self.user_entry.place(x=180, y=20)
        
        self.password_label = tk.Label(self.border, text="Password", font=("Arial", 15), fg="lime", bg='black')
        self.password_label.place(x=50, y=80)
        self.password_entry = tk.Entry(self.border, width = 30, show='*', bd = 5)
        self.password_entry.place(x=180, y=80)
        
        def verify():
            try:
                with open("users.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        self.user_name, self.user_password =e.split(",")
                        if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                            controller.show_frame(Second)
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Username and password does not match")
     
         
        self.submitbutton = tk.Button(self.border, text="Submit", font=("Arial", 15), bg = "lime", command=verify)
        self.submitbutton.place(x=320, y=115)
        
        def register():
            register_window = tk.Tk()
            register_window.resizable(0,0)
            register_window.configure(bg="black")
            register_window.title("Sign Up")
            reg_name_label = tk.Label(register_window, text="Username:", font=("Arial",15), bg="black", fg = "lime")
            reg_name_label.place(x=10, y=10)
            reg_name_entry = tk.Entry(register_window, width=30, bd=5)
            reg_name_entry.place(x = 200, y=10)
            
            reg_password_label = tk.Label(register_window, text="Password:", font=("Arial",15), bg="black", fg = "lime")
            reg_password_label.place(x=10, y=60)
            reg_password_entry = tk.Entry(register_window, width=30, show="*", bd=5)
            reg_password_entry.place(x = 200, y=60)
            
            confirm_password_label = tk.Label(register_window, text="Confirm Password:", font=("Arial",15), bg="black", fg = "lime")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = tk.Entry(register_window, width=30, show="*", bd=5)
            confirm_password_entry.place(x = 200, y=110)
            
            def check():
                if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":
                    if reg_password_entry.get()==confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!")
                            register_window.destroy()
                    else:
                        messagebox.showinfo("Error","Your passwords do not match!")
                else:
                    messagebox.showinfo("Error", "Please fill in all the boxes!")
                    
            self.register_button = tk.Button(register_window, text="Sign Up", font=("Arial",15), bg="lime", command=check)
            self.register_button.place(x=170, y=150)
            
            register_window.geometry("470x220")
            register_window.mainloop()
            
        self.register_button = tk.Button(self, text="Sign Up", bg = "dark orange", font=("Arial",15), command=register)
        self.register_button.place(x=650, y=20)
        
class Second(tk.Frame):
    def __init__(self, parent, controller):
        background_color = "black"
        tk.Frame.__init__(self, parent,bg = background_color)
    
        
        self.title_label = tk.Label(self, text="Welcome to my quiz!", font=("Arial Bold", 25), bg = "white" )
        self.title_label.place(x=200, y=20)        
        self.next_button = tk.Button(self, text="Continue", font=("Arial", 15),bg = "black", fg = "lime", command=lambda: controller.show_frame(Third), width=10)
        self.next_button.place(x=400, y=300)
        
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), bg = "black", fg = "lime", command=lambda: controller.show_frame(Start), width=10)
        self.back_button.place(x=200, y=300)
        
#A lambda function is a small anonymous function(usually we dont need to reuse it)
#A lambda function can take any number of arguments, but can only have one expression 

class Third(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.configure(bg='ivory')
        
        self.app_label = tk.Label(self, text="Store some content related to your \n project or what your application made for. \n All the best!!", bg = "ivory", font=("Arial Bold", 25))
        self.app_label.place(x=40, y=150)
        
        self.home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Start))
        self.home_button.place(x=650, y=450)
        
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Second))
        self.back_button.place(x=100, y=450)
        
        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
      
        self.window = tk.Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (Start, Second, Third):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(Start)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Climate Change App") 


#start of program
if __name__ == '__main__':           
    app = Application()
    app.maxsize(800,500)
    app.mainloop()

