# =================================== FINAL ====================================
# =========================== PUTTING PAGES TOGETHER ===========================

from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image

root = Tk()
root.rowconfigure(0, weight=1) 
root.columnconfigure(0, weight=1) 
root.state('zoomed')

root.title("Chemistry quiz")
root.geometry("700x620")

page1 = Frame(root, bg="#EBCEF5")
page2 = Frame(root, bg="#C9BDFC")
page3 = Frame(root, bg="#EBCEF5")
 

for frame in (page1, page2, page3): 
    frame.grid(row=0, column=0, sticky='nsew') 
 

def show_frame(frame): 
    frame.tkraise() 
 

show_frame(page1)

# ======================================== USER DETAILS ========================================
# =========================================== PAGE 1 ===========================================

class UserDetails:
    def __init__(self):
        #Welcome statement
        #nameL = label name
        #nameE = entry name
        #submitB = submit button
        self.head = Label(page1, text="Welcome to Chemistry Quiz!", font=("Arial", 25, "bold"), bg="#EBCEF5")
        self.head.place(x=170, y=140)

        self.text = Label(page1, text="Let's start by filling in your details!", font=("Arial", 16), bg="#EBCEF5")
        self.text.place(x=220, y=180)

        self.nameL = Label(page1, text="Name", width=20, font=("Arial", 14), bg="#EBCEF5")
        self.nameL.place(x=130, y=230)

        self.nameE = Entry(page1, width=30, font=("Arial", 14))
        self.nameE.place(x=260, y=230)
        self.nameE.insert(0, "Enter here...")
        self.nameE.bind("<FocusIn>", self.name_on_click)
        self.nameE.bind("<FocusOut>", self.name_out_click)
        self.nameE.config(fg="grey")

        self.ageL = Label(page1, text="Age", width=20, font=("Arial", 14), bg="#EBCEF5")
        self.ageL.place(x=130, y=270)

        self.ageE = Entry(page1, width=30, font=("Arial", 14))
        self.ageE.place(x=260, y=270)
        self.ageE.insert(0, "Enter here...")
        self.ageE.bind("<FocusIn>", self.age_on_click)
        self.ageE.bind("<FocusOut>", self.age_out_click)
        self.ageE.config(fg="grey")

        self.year_levelL = Label(page1, text="Year level", width=20, font=("Arial", 14), bg="#EBCEF5")
        self.year_levelL.place(x=130, y=310)

        self.year_levelE = Entry(page1, width=30, font=("Arial", 14))
        self.year_levelE.place(x=260, y=310)
        self.year_levelE.insert(0, "Enter here...")
        self.year_levelE.bind("<FocusIn>", self.year_level_on_click)
        self.year_levelE.bind("<FocusOut>", self.year_level_out_click)
        self.year_levelE.config(fg="grey")

        self.submitB = Button(page1, highlightbackground="#EFF0FF", text="Submit", width=15, font=("Arial", 14), command=self.submitButton)
        self.submitB.place(x=280, y=370)

        self.quitB = Button(page1, text="Quit", highlightbackground="#EFF0FF", width=10, font=("Arial", 14), command=root.destroy)
        self.quitB.place(x=30, y=25)

        self.yesBtn = self.yesButton
        self.noBtn = self.noButton

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
            return False
        elif all(letter.isalpha() or letter.isspace() for letter in name):
            return True
        else:
            mb.showerror("Error", "The name you entered is invalid. Please try again.")
            return False
        return

    #Age check
    def ageCheck(self, age):
        while True:
            try:
                age = int(self.ageE.get())
                if age >= 12 and age <= 18:
                    return True
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
                    return True
                    break
                else:
                    mb.showerror("Error", "The year level you entered is invalid. Year level should be between 9 and 12. Please try again.")
                    return False
                    break
            except ValueError:
                mb.showerror("Error", "Please enter a number in year level.")
                return False
                break
        return

    #Submit button calling name, agecheck and year level check functions
    def submitButton(self):
        while True:
            nameC = self.nameCheck(self)
            ageC = self.ageCheck(self)
            yearC = self.year_levelCheck(self)

            if nameC == True and ageC == True and yearC == True:
                self.text1 = Label(page1, text="Would you like to see the instruction?",
                                   bg="#EBCEF5", font=("Arial", 14))
                self.text1.place(x=230, y=430)
                self.yesB = Button(page1, text="Yes", width=10, bg="#EBCEF5", font=("Arial", 14), command=self.yesBtn)
                self.yesB.place(x=245, y=470)
                self.noB = Button(page1, text="No", width=10, bg="#EBCEF5", font=("Arial", 14), command=self.noBtn)
                self.noB.place(x=355, y=470)
                break
            else:
                break

    #Yes button that lead the users to page3 - instruction page
    def yesButton(self):
        show_frame(page3)

    #No button that lead the users to page2 - quiz page
    def noButton(self):
        show_frame(page2)
        
user_details = UserDetails()

# =============================== CHEMISTRY QUIZ ==================================
# ================================== PAGE 2 =======================================

#Subscript: \u208

questions = ["Question 1: What is the symbol of Aluminium?",
            "Question 2: What is the symbol of Iron?",
            "Question 3: What is the symbol of Boron?",
            "Question 4: What element has the symbol Cl?",
            "Question 5: What element has the symbol S?",
            "Question 6: What element has the symbol Be?",
            "Question 7: What is the formula for water?",
            "Question 8: What is the formula for glucose?",
            "Question 9: What is the formula CO\u2082 represent?",
            "Question 10: What is the formula H\u2082 represent?"]

options = [
    ["A", "Alu", "Al", "Lu"],
    ["Fe", "Ir", "In", "Fn"],
    ["Br", "B", "Bn", "Bo"],
    ["Chlorine", "Clo", "Chloride", "Calcium"],
    ["Phosphorus", "Sodium", "Strontium", "Sulfur"],
    ["Bohrium", "Boron", "Berylium", "Bismuth"],
    ["H\u2082O", "HO\u2082", "H\u2082O\u2082", "HO"],
    ["HCO\u2086", "CO\u2082", "C\u2086H\u20812O\u2086", "C\u20812O\u20812H\u2086"],
    ["Carbon", "Carbon Dioxide", "Oxygen", "Water"],
    ["Oxygen", "Hydroxide", "Hydroxide", "Hydrogen"],
    ]

answer = [3,1,2,1,4,3,1,3,2,4]

images = ["question1.jpg", "question2.jpg", "question3.jpg", "question4.jpg",
          "question5.jpg", "question6.jpg", "question7.jpg", "question8.jpg", "question9.jpg", "question10.jpg"]

class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0
        self.images = images
        self.display_image(self.qn)

    def question(self, qn): #display the title and the question
        title = Label(page2, text="Chemistry Quiz", width=20, font=("Arial", 25, "bold"), bg="#C9BDFC")
        title.place(x=222, y=60)
        qn = Label(page2, justify=CENTER, text=questions[qn], width=40, anchor="w", font=("Arial", 18), bg="#C9BDFC")
        qn.place(x=162, y=100)
        return qn

    def radiobtns(self): #code for 4 option buttons
        val = 0
        b = []
        yp = 370
        while val < 4:
            btn = Radiobutton(page2, text=" ", variable=self.opt_selected, value=val + 1, font=("Arial", 14), bg="#C9BDFC")
            b.append(btn)
            btn.place(x=200, y=yp)
            val += 1
            yp += 48
        return b

    def display_options(self, qn): #this code display the options
        val = 0
        self.opt_selected.set(0)
        self.ques["text"] = questions[qn]
        for op in options[qn]:
            self.opts[val]["text"] = op
            val += 1

    def display_image(self, qn): #position the image
                                 #take the image corresponding to the question number
        pic = ImageTk.PhotoImage(Image.open(images[qn]))
        label = Label(page2, bg="#C9BDFC")
        label.place(x=175, y=145)
        label.config(image=pic)
        label.image = pic
    
    def buttons(self): #this code is for next and quit button
        nbutton = Button(page2, text="Next", command=self.nextbtn, width=10, font=("Arial", 14), bg="#EFF0FF")
        nbutton.place(x=305, y=560)
        quitbutton = Button(page2, text="Quit", command=root.destroy, width=10, font=("Arial", 14), bg="#EFF0FF")
        quitbutton.place(x=30, y=25)

    def checkans(self, qn):
        if self.opt_selected.get() == answer[qn]:
            return True

    def nextbtn(self): #check if the user chose a correct answer
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(questions):
            self.display_result()
        else:
            self.display_options(self.qn)
            self.display_image(self.qn)

    def display_result(self): #check if the user has reached 10 questions or not
                              #otherwise it will keep moving to the next question
        score = int(self.correct / len(questions) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(questions) - self.correct
        correct = "No, of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

quiz = Quiz()

# ================================== INSTRUCTION ========================================
# ==================================== PAGE 3 ===========================================

class Instruction:
    def __init__(self):
        self.head = Label(page3, text="Instruction", font=("Arial", 25, "bold"), bg="#EBCEF5")
        self.head.place(x=280, y=120)
        
        self.text = Label(page3, justify=CENTER,font=("Arial", 14,),
                          bg="#EBCEF5", text="Hello, welcome to Chemistry Quiz! This is a quiz about the basic of\n"
                          "chemistry,specifically about chemistry formula. There are a total of 10\n"
                          "questions for you to answer. For half of the question, you will be tested\n"
                          "about name and symbol of different elements in the periodic table. Then\n"
                          "for the other half of the question, you will be tested about the fomula \n"
                          "of different components that are seen everyday. At the end of the quiz,\n"
                          "there will be a message box pop up that summarise the number of your \n"
                          "correct and wrong answer as well as giving you the score")
        self.text.place(x=130, y=170)
        
        self.text2 = Label(page3, justify=CENTER, bg="#EBCEF5", font=("Arial", 14,),
                           text="Once you have read the instruction, you can click 'start':")
        self.text2.place(x=180, y=320)

        self.startBtn = self.startButton
        
        self.startB = Button(page3, text="Start", width=10, font=("Arial", 14), bg="#EFF0FF", command=self.startBtn)
        self.startB.place(x=300, y=370)
        self.quitB = Button(page3, text="Quit", bg="#EFF0FF", width=10, font=("Arial", 14), command=root.destroy)
        self.quitB.place(x=30, y=25)
        
    def startButton(self):
        show_frame(page2)

instruction = Instruction()

#######################################################################
root.mainloop()


