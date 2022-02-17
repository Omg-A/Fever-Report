from tkinter import *
from tkinter import messagebox as tkmb

root = Tk()
root.title("Fever Report")
root.geometry("600x600")

question1 = StringVar(value = "0")
label_question1 = Label(root, text="Do you have headache and sour throat?")
label_question1.pack()
question1_radio1 = Radiobutton(root, text="Yes", variable=question1, value="yes")
question1_radio1.pack()
question1_radio2 = Radiobutton(root, text="No", variable=question1, value="no")
question1_radio2.pack()


question2 = StringVar(value = "0")
label_question2 = Label(root, text="Is your body temperature high?")
label_question2.pack()
question2_radio1 = Radiobutton(root, text="Yes", variable=question2, value="yes")
question2_radio1.pack()
question2_radio2 = Radiobutton(root, text="No", variable=question2, value="no")
question2_radio2.pack()

question3 = StringVar(value = "0")
label_question3 = Label(root, text="Are there any symptoms of eye redness?")
label_question3.pack()
question3_radio1 = Radiobutton(root, text="Yes", variable=question3, value="yes")
question3_radio1.pack()
question3_radio2 = Radiobutton(root, text="No", variable=question3, value="no")
question3_radio2.pack()

score = 0

def check():
    global score
    
    if question1.get() == "yes":
        score = score + 20
        print(score)
    if question2.get() == "yes":
        score = score + 20
        print(score)
    if question3.get() == "yes":
        score = score + 20
        print(score)
    
    if score <= 20:
        tkmb.showinfo("Report", "You don't need to visit a doctor")
    elif score > 20 and score <= 40:
        tkmb.showinfo("Report", "You might perhaps have to visit a doctor")
    else:
        tkmb.showinfo("Report", "You have to visit a doctor")

btn_check = Button(root, text="Done", command = check)
btn_check.pack()

root.mainloop()