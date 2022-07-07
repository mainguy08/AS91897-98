# ===================================== CHEMISTRY QUIZ ==================================
# ======================================== VERSION 2 ====================================

#Subscript: \u208

from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk, Image

root = Tk()
root.title("Chemistry quiz")
root.geometry("700x620")
root.configure(bg="#C9BDFC")

questions = ["Question 1/10: What is the symbol of Aluminium?",
            "Question 2/10: What is the symbol of Iron?",
            "Question 3/10: What is the symbol of Boron?",
            "Question 4/10: What element has the symbol Cl?",
            "Question 5/10: What element has the symbol S?",
            "Question 6/10: What element has the symbol Be?",
            "Question 7/10: What is the formula for water?",
            "Question 8/10: What is the formula for glucose?",
            "Question 9/10: What is the formula CO\u2082 represent?",
            "Question 10/10: What is the formula H\u2082 represent?"]

options = [
    ["A", "Alu", "Al", "Lu"],
    ["Fe", "Ir", "In", "Fn"],
    ["Br", "B", "Bn", "Bo"],
    ["Chlorine", "Clo", "Chloride", "Calcium"],
    ["Phosphorus", "Sodium", "Strontium", "Sulfur"],
    ["Bohrium", "Boron", "Berylium", "Bismuth"],
    ["H\u2082O", "HO\u2082", "H\u2082O\u2082", "HO"],
    ["HCO\u2086", "CO\u2082", "C\u2086H\u2081\u2082O\u2086", "C\u2081\u2082O\u2081\u2082H\u2086"],
    ["Carbon", "Carbon Dioxide", "Oxygen", "Water"],
    ["Oxygen", "Hydroxide", "Hydroxide", "Hydrogen"],
    ]

answer = [3,1,2,1,4,3,1,3,2,4]

images = ["question1.jpg", "question2.jpg", "question3.jpg", "question4.jpg", "question5.jpg",
          "question6.jpg", "question7.jpg", "question8.jpg", "question9.jpg", "question10.jpg"]

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
        title = Label(root, text="Chemistry Quiz", width=20, font=("Arial", 25, "bold"), bg="#C9BDFC")
        title.place(x=222, y=60)
        qn = Label(root, justify=CENTER, text=questions[qn], width=40, anchor="w", font=("Arial", 18), bg="#C9BDFC")
        qn.place(x=162, y=100)
        return qn

    def radiobtns(self): #code for 4 option buttons
        val = 0
        b = []
        yp = 370
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("Arial", 14), bg="#C9BDFC")
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
        label = Label(root, bg="#C9BDFC")
        label.place(x=175, y=145)
        label.config(image=pic)
        label.image = pic
    
    def buttons(self): #this code is for next and quit button
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10, font=("Arial", 14), bg="#EFF0FF")
        nbutton.place(x=305, y=560)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10, font=("Arial", 14), bg="#EFF0FF")
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
#######################################################################
root.mainloop()

