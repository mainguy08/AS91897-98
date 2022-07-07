# =============================== CHEMISTRY QUIZ ==================================
# ================================= VERSION 1 ===================================

#Subscript: \u208

from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.title("Chemistry quiz")
root.geometry("700x500")

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
    ["HCO\u2086", "CO\u2082", "C\u2086H\u2081\u2082O\u2086", "C\u2081\u2082O\u2081\u2082H\u2086"],
    ["Carbon", "Carbon Dioxide", "Oxygen", "Water"],
    ["Oxygen", "Hydroxide", "Hydroxide", "Hydrogen"],
    ]

answer = [3,1,2,1,4,3,1,3,2,4]

class Quiz:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn): #display the title and the question
        t = Label(root, text="Chemistry Quiz", width=50, fg="black")
        t.place(x=0, y=2)
        qn = Label(root, text=questions[qn], width=60, anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self): #code for 4 option buttons
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1)
            b.append(btn)
            btn.place(x=100, y=yp)
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
    
    def buttons(self): #this code is for next and quit button
        nbutton = Button(root, text="Next", command=self.nextbtn, width=10)
        nbutton.place(x=200, y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy, width=10)
        quitbutton.place(x=380, y=380)

    def checkans(self, qn): #check if the user chose a correct answer
        if self.opt_selected.get() == answer[qn]:
            return True

    def nextbtn(self):  #check if the user has reached 10 questions or not
                        #otherwise it will keep moving to the next question
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(questions):
            self.display_result()
        else:
            self.display_options(self.qn)

    def display_result(self): #calculate and display the result
        score = int(self.correct / len(questions) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(questions) - self.correct
        correct = "No, of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))

quiz = Quiz()
#######################################################################
root.mainloop()
