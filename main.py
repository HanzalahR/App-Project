import tkinter as tk

window = tk.Tk()
window.title("Climate Change App")  #Change later
window.geometry("500x500")
window.mainloop()
hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()

class Appstarter:
   def __init__(self, parent):
        background_color = "Black" # The background colour
        primary_color = "#FEE715" #font colour for the starting page
        self.app_frame = Frame(parent, bg = background_color, padx = 100, pady = 100)
        self.app_frame.grid()

        self.heading_label = Label(self.app_frame, text = "Health and Fitness quiz", font = ("Myriad", "20", "italic", "bold"), fg = primary_color, bg=background_color)
        self.heading_label.grid(row = 0, padx = 20)

        self.user_label = Label(self.app_frame, text = "Enter username please:", font = ("Myriad", "16"), fg = primary_color, bg = background_color)
        self.user_label.grid(row = 1, padx = 20, pady = 20)

        self.entry_box = Entry(self.app_frame)
        self.entry_box.grid(row = 2, padx = 20, pady = 20)

        self.continue_button = Button(self.app_frame, text = "Start", font = ("Myriad", "13"), bg = primary_color, command=self.name_collection)
        self.continue_button.grid(row = 3, padx = 20, pady = 10)











