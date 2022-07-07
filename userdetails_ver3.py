# ================================== USER DETAILS ==================================
# ==================================== VERSION 3 ===================================

from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("User details")
root.geometry("700x500")
root.configure(bg="#EBCEF5")

class UserDetails:
    def __init__(self):
        #Welcome statement
        #nameL = label name
        #nameE = entry name
        #submitB = submit button
        self.head = Label(root, text="Welcome to Chemistry Quiz!", font=("Arial", 25), bg="#EBCEF5")
        self.head.place(x=190, y=110)

        self.text = Label(root, text="Let's start by filling in your details!", font=("Arial", 16), bg="#EBCEF5")
        self.text.place(x=215, y=150)

        self.nameL = Label(root, text="Name", width=20, font=("Arial", 14), bg="#EBCEF5")
        self.nameL.place(x=130, y=190)

        self.nameE = Entry(root, width=30, font=("Arial", 14))
        self.nameE.place(x=260, y=190)
        self.nameE.insert(0, "Enter here...")
        self.nameE.bind("<FocusIn>", self.name_on_click)
        self.nameE.bind("<FocusOut>", self.name_out_click)
        self.nameE.config(fg="grey")

        self.ageL = Label(root, text="Age", width=20, font=("Arial", 14), bg="#EBCEF5")
        self.ageL.place(x=130, y=230)

        self.ageE = Entry(root, width=30, font=("Arial", 14))
        self.ageE.place(x=260, y=230)
        self.ageE.insert(0, "Enter here...")
        self.ageE.bind("<FocusIn>", self.age_on_click)
        self.ageE.bind("<FocusOut>", self.age_out_click)
        self.ageE.config(fg="grey")

        self.year_levelL = Label(root, text="Year level", width=20, font=("Arial", 14), bg="#EBCEF5")
        self.year_levelL.place(x=130, y=270)

        self.year_levelE = Entry(root, width=30, font=("Arial", 14))
        self.year_levelE.place(x=260, y=270)
        self.year_levelE.insert(0, "Enter here...")
        self.year_levelE.bind("<FocusIn>", self.year_level_on_click)
        self.year_levelE.bind("<FocusOut>", self.year_level_out_click)
        self.year_levelE.config(fg="grey")

        self.submitB = Button(root, highlightbackground="#EFF0FF", text="Submit", width=15, font=("Arial", 14), command=self.submitButton)
        self.submitB.place(x=280, y=320)

        self.quitB = Button(root, text="Quit", highlightbackground="#EFF0FF", width=10, font=("Arial", 14), command=root.destroy)
        self.quitB.place(x=30, y=450)

    #FocusIn and FocusOut
    def name_on_click(self, nameE):
        if self.nameE.get() == "Enter here...":
            self.nameE.delete(0, "end")
            self.nameE.insert(0, "")
            self.nameE.config(fg="black")

    def name_out_click(self, nameE):
        if self.nameE.get() == "":
            self.nameE.insert(0, "Enter here...")
            self.nameE.config(fg="grey")

    def age_on_click(self, ageE):
        if self.ageE.get() == "Enter here...":
            self.ageE.delete(0, "end")
            self.ageE.insert(0, "")
            self.ageE.config(fg="black")

    def age_out_click(self, ageE):
        if self.ageE.get() == "":
            self.ageE.insert(0, "Enter here...")
            self.ageE.config(fg="grey")

    def year_level_on_click(self, year_levelE):
        if self.year_levelE.get() == "Enter here...":
            self.year_levelE.delete(0, "end")
            self.year_levelE.insert(0, "")
            self.year_levelE.config(fg="black")

    def year_level_out_click(self, year_levelE):
        if self.year_levelE.get() == "":
            self.year_levelE.insert(0, "Enter here...")
            self.year_levelE.config(fg="grey")

    #Name check
    def nameCheck(self, name):
        name = self.nameE.get()
        if len(name) == 13:
            mb.showerror("Error", "Name can't be empty. Please try again.")
        elif all(letter.isalpha() or letter.isspace() for letter in name):
            passL = Label(root, text="Sucess", width=10, font=("Arial", 14), bg="#EBCEF5")
            passL.place(x=520, y=190)
        else:
            mb.showerror("Error", "The name you entered is invalid. Please try again.")
        return

    #Age check
    def ageCheck(self, age):
        while True:
            try:
                age = int(self.ageE.get())
                if age >= 12 and age <= 18:
                    passL = Label(root, text="Sucess", width=10, font=("Arial", 14), bg="#EBCEF5")
                    passL.place(x=520, y=230)
                    break
                else:
                    mb.showerror("Error", "The age you entered is invalid. Age should be between 12 and 18. Please try again.")
                    return False
                    break
            except ValueError:
                mb.showerror("Error", "Age should be entered as number.")
                return False
                break
        return

    #Year level check
    def year_levelCheck(self, year_level):
        while True:
            try:
                year_level = int(self.year_levelE.get())
                if year_level >= 9 and year_level <= 12:
                    passL = Label(root, text="Sucess", width=10, font=("Arial", 14), bg="#EBCEF5")
                    passL.place(x=520, y=270)
                    break
                else:
                    mb.showerror("Error", "The year level you entered is invalid. Year level should be between 9 and 12. Please try again.")
                    return False
                    break
            except ValueError:
                mb.showerror("Error", "Year level should be entered as number.")
                return False
                break
        return

    #Submit button calling name, agecheck and year level check functions
    def submitButton(self):
        self.nameCheck(self)
        self.ageCheck(self)
        self.year_levelCheck(self)
        
        
user_details = UserDetails()
root.mainloop()

