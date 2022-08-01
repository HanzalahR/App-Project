import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import tkinter.font as font
import random

asked = []
score = 0
  
    
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
        # This is when verifying the username and password. Checking the correct input
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
                    if i==0: # this is shown if the username and passoword does not match
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Username and password does not match") 
     
         # Submit button for sign in page
        self.submitbutton = tk.Button(self.border, text="Submit", font=("Arial", 15), bg = "lime", command=verify)
        self.submitbutton.place(x=320, y=115)
        # This is for the register/sign up page to register new users 
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
            # This is for checking if the user has filled in all the boxes to successfully register or not
            def check():
                if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":
                    if reg_password_entry.get()==confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome","You are registered successfully!!") # Message shown after successfully being registered
                            register_window.destroy()
                    else:
                        messagebox.showinfo("Error","Your passwords do not match!") # shown when the passwords do not match when registering
                else:
                    messagebox.showinfo("Error", "Please fill in all the boxes!") # shown when there is box/es not filled
                    
            self.register_button = tk.Button(register_window, text="Sign Up", font=("Arial",15), bg="lime", command=check)
            self.register_button.place(x=170, y=150)
            
            register_window.geometry("470x220")
            register_window.mainloop()
            
        self.register_button = tk.Button(self, text="Sign Up", bg = "dark orange", font=("Arial",15), command=register)
        self.register_button.place(x=650, y=20)

    # The Second class is for the second frame which is when the user is given the choice to go back or contine with the program. This frame is shown when the user has successfully logged in. If the user presses the back button it will send them back to the sign in page
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

# Also, using .place instead of .grid
  

questions_answers = {
  1: ["Which one is the biggest cause of global warming?", # item 1, index 0 is the question 
      'Pollution from wildfires', # first option 
      'Burning oil and gas', # second option
      'Natural variation', # third option 
      'Decomposing plants', # fourth option
      'Burning oil and gas' # correct answer, index 5
      ,2], # close the list as it is the end of the first key value
  2: ["What is the greenhouse effect?",
      'impact trees have on global temperature',
      'gases from the atmosphere stop heat from escaping',
      'measurement of plant growth',
      'When climate change affects ecosystems',
      'gases from the atmosphere stop heat from escaping'
      ,2],
  3: ["What is responsible for 75% of the warming effect from greenhouse gases",
      'Nitrous oxide',
      'fluorinated gases',
      'Carbon dioxide',
      'Methane',
      'Carbon dioxide'
      ,3],
  4: ["Percentage of species at risk of extinction if global temperature rises?",
      '100%',
      '30-50%',
      '10-15%',
      '15-20%',
      '15-20%'
      ,4],
  5: ["How much have sea levels risen in the past 100 years?",
      '160-210mm',
      '100-150mm',
      '220-250mm',
      'More than 250mm',
      '160-210mm'
      ,1],
}
      
     # This is for randomising the questions so they are not in a specific order. 
def randomise (): #questions will be randomised
  global qnum
  qnum = random.randint(1,5) # 5 questions in total
  if qnum not in asked:
    asked.append (qnum)
  elif qnum in asked: # If the question has already been asked
    randomise()
    
 # This class is for all the 5 quiz questions. This frame is shown when the user presses continue in the second frame
class Third(tk.Frame):
  def __init__(self, parent, controller):

    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.configure(bg = "black")
    background_color = "black"
    
    
    self.quiz_frame = tk.Frame(parent, bg = background_color, padx = 100, pady = 100)
    self.quiz_frame.grid()
    
    self.question_label = tk.Label(self, text=questions_answers[qnum][0], font=("Arial", 15), fg = "lime", bg = "black" )
    self.question_label.place(x=50, y=20)

    #holds the value of radio buttons
    self.var1=tk.IntVar()

    # Radio Button 1
    self.radiob1 = tk.Radiobutton(self, text=questions_answers[qnum][1], font=("Arial","12"), bg = "lime", value = 1, padx=10, pady=10, variable=self.var1)
    self.radiob1.place(x=50, y=60)

     # Radio Button 2
    self.radiob2 = tk.Radiobutton(self, text=questions_answers[qnum][2], font=("Arial","12"), bg = "lime", value = 2, padx=10, pady=10, variable=self.var1)
    self.radiob2.place(x=50, y=120)

     # Radio Button 3
    self.radiob3 = tk.Radiobutton(self, text=questions_answers[qnum][3], font=("Arial","12"), bg = "lime", value = 3, padx=10, pady=10, variable=self.var1)
    self.radiob3.place(x=50, y=180)

     # Radio Button 4
    self.radiob4 = tk.Radiobutton(self, text=questions_answers[qnum][4], font=("Arial","12"), bg = "lime", value = 4, padx=10, pady=10, variable=self.var1)
    self.radiob4.place(x=50, y=240)

    # Confirm button
    self.quiz_instance=tk.Button(self,text="Confirm", font=("Arial","13"), bg = "lime", command=self.quiz_advancement)
    self.quiz_instance.place(x=350, y=300)

    # Home Button. If the home button is pressed at any stage it will take you back to the sign in page (the beginning) 
    self.home_button = tk.Button(self, text="Home", font=("Arial", "13"),bg = "red", command=lambda: controller.show_frame(Start))
    self.home_button.place(x=650, y=300)

    #score 
    self.score_label = tk.Label(self, text = "SCORE:", font = ("arial", "12"), fg = "lime", bg = background_color,)
    self.score_label.place (x=50, y=310)

 # editing question label to new question and possible answers as new radio button choices
  def question_arrangement(self):
    randomise()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.radiob1.config(text=questions_answers[qnum][1])
    self.radiob2.config(text=questions_answers[qnum][2])
    self.radiob3.config(text=questions_answers[qnum][3])
    self.radiob4.config(text=questions_answers[qnum][4])
    
  #command for confirm button
  def quiz_advancement(self):
    global score
    scr_label=self.score_label
    choice=self.var1.get()
    if len(asked)>4: #determining if its the last question, end quiz after
      if choice == questions_answers[qnum][6]: #checking if the user has chosen the correct answer (stored in index 6 of the value array)
        score +=1 #adds one point to score
        scr_label.configure(text=score)
        self.quiz_instance.config(text="Confirm")
        self.controller.show_frame(End)
      else:
        print(choice)
        score-=0 #score will stay the same. Will not be subtracted
        scr_label.configure(text="The correct answer was:" + questions_answers[qnum][5])
        self.quiz_instance.config(text="Confirm")
        self.controller.show_frame(End)
    else:
      if choice == 0:
        self.quiz_instance.config(text="You did not select an option")
        choice = self.var1.get()
      else:
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.quiz_instance.config(text="Confirm")
          self.question_arrangement()
        else:
          print(choice)
          score -= 0
          scr_label.configure(text="the correct answer was:" + questions_answers[qnum][5]) # show the correct answer if incorrect answer was chosen
          self.quiz_instance.config(text="Confirm")
          self.question_arrangement()

# This class is the last page of the program. This page comes after all the questions of the quiz have been asked 
class End(tk.Frame):
  def __init__(self, parent, controller):

    tk.Frame.__init__(self, parent)
    self.configure(bg = "black")
    background_color = "black"

    



    self.end_heading = tk.Label (self, text = "Good effort, thanks for playing my quiz!", font = ("arial", "20"), bg = background_color, fg = "lime")
    self.end_heading.place(x=50, y=20)

   # self.end_heading2 = tk.Label(self, text = f'your score was {score}', font = ("arial", "20"), bg = background_color, fg = "lime")
   # self.end_heading2.place(x=50, y=50)
      
    
    
    



     
randomise()
      


# The application class controls all the Frames        

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
      
        self.window = tk.Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (Start, Second, Third, End): #Start is the first frame that will start the program
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(Start)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Climate Change Quiz") # Title


if __name__ == '__main__':           
    app = Application()
    app.maxsize(800,500)
    app.mainloop()

