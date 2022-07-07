# ===================================== USER DETAILS =====================================
# ======================================= VERSION 2 ======================================

from tkinter import *

root = Tk()
root.title("User details")
root.geometry("700x500")

class UserDetails:
    def __init__(self):
        #Welcome statement
        #nameL = label name
        #nameE = entry name
        #submitB = submit button
        self.head = Label(root, text="Welcome to Chemistry Quiz!", font=("Arial", 25))
        self.head.place(x=190, y=100)

        self.text = Label(root, text="Let's start by filling in your details!", font=("Arial", 16))
        self.text.place(x=215, y=140)

        self.nameL = Label(root, text="Name", width=20, font=("Arial", 14))
        self.nameL.place(x=130, y=180)

        self.nameE = Entry(root, width=30, text="", font=("Arial", 14))
        self.nameE.place(x=260, y=180)

        self.ageL = Label(root, text="Age", width=20, font=("Arial", 14))
        self.ageL.place(x=130, y=215)

        self.ageE = Entry(root, text="", width=30, font=("Arial", 14))
        self.ageE.place(x=260, y=215)

        self.year_levelL = Label(root, text="Year level", width=20, font=("Arial", 14))
        self.year_levelL.place(x=130, y=250)

        self.year_levelE = Entry(root, text="", width=30, font=("Arial", 14))
        self.year_levelE.place(x=260, y=250)

        self.submitB = Button(root, text="Submit", width=20, font=("Arial", 14), command=self.submitButton)
        self.submitB.place(x=250, y=300)

    #Name check
    def nameCheck(self, name):
        name = self.nameE.get()
        if len(name) == 0:
            emptyL = Label(root, text="Name can't be empty", width=20, font=("Arial", 14))
            emptyL.place(x=250, y=340)
        elif all(letter.isalpha() or letter.isspace() or letter == "-" for letter in name):
            passL = Label(root, text="Success", width=20, font=("Arial", 14))
            passL.place(x=250, y=340)
        else:
            failL = Label(root, text="The name you entered is invalid.", width=30, font=("Arial", 14))
            failL.place(x=250, y=340)
        return

    #Age check
    def ageCheck(self, age):
        while True:
            try:
                age = int(self.ageE.get())
                if age >= 12 and age <= 18:
                    passL = Label(root, text="Success", width=20, font=("Arial", 14))
                    passL.place(x=250, y=380)
                else:
                    failL = Label(root, text="Age should be between 12 and 18.", width=20, font=("Arial", 14))
                    failL.place(x=250, y=380)
            except ValueError:
                numberL = Label(root, text="Age should be entered as number.", width=30, font=("Arial", 14))
                numberL.place(x=250, y=380)
            return False
        return

    #Year level check
    def year_levelCheck(self, year_level):
        while True:
            try:
                year_level = int(self.year_levelE.get())
                if year_level >= 9 and year_level <= 13:
                    passL = Label(root, text="Success", width=20, font=("Arial", 14))
                    passL.place(x=250, y=420)
                else:
                    failL = Label(root, text="Year level should be between 9 and 12.", width=30, font=("Arial", 14))
                    failL.place(x=250, y=420)
            except ValueError:
                numberL = Label(root, text="Year level should be entered as number.", width=30, font=("Arial", 14))
                numberL.place(x=250, y=420)
            return False
        return

    def submitButton(self):
        self.nameCheck(self)
        self.ageCheck(self)
        self.year_levelCheck(self)
        return
        
    
user_details = UserDetails()
root.mainloop()


