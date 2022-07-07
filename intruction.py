# ===========================================================================================
# ======================================= INSTRUCTION =======================================

from tkinter import *

root = Tk()
root.title("Instruction")
root.geometry("700x620")
root.configure(bg="#EBCEF5")

class Instruction:
    def __init__(self):
        self.head = Label(root, text="Instruction", font=("Arial", 25, "bold"), bg="#EBCEF5")
        self.head.place(x=280, y=120)
        self.text = Label(root, justify=CENTER,font=("Arial", 14,),
                          bg="#EBCEF5", text="Hello, welcome to Chemistry Quiz! This is a quiz about the basic of\n"
                          "chemistry,specifically about chemistry formula. There are a total of 10\n"
                          "questions for you to answer. For half of the question, you will be tested\n"
                          "about name and symbol of different elements in the periodic table. Then\n"
                          "for the other half of the question, you will be tested about the fomula \n"
                          "of different components that are seen everyday. At the end of the quiz,\n"
                          "there will be a message box pop up that summarise the number of your \n"
                          "correct and wrong answer as well as giving you the score")
        self.text.place(x=130, y=170)
        self.text2 = Label(root, justify=CENTER, bg="#EBCEF5", font=("Arial", 14,),
                           text="Once you have read the instruction, you can click 'start':")
        self.text2.place(x=180, y=320)
        self.startB = Button(root, text="Start", width=10, font=("Arial", 14), bg="#EFF0FF")
        self.startB.place(x=300, y=370)
        self.quitB = Button(root, text="Quit", bg="#EFF0FF", width=10, font=("Arial", 14), command=root.destroy)
        self.quitB.place(x=30, y=25)

    #def startButton(self):
        
instruction = Instruction()
root.mainloop()
