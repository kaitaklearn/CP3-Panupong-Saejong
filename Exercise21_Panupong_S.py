from tkinter import *
import math

def leftClickButton(event):
    labelresult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    result = float(textBoxWeight.get()) / math.pow(float(textBoxHeight.get()) / 100, 2)
    if result >= 30:
        labelresult2.configure(text="อ้วนมาก")
    elif 25 <= result <= 29.9:
        labelresult2.configure(text="อ้วน")
    elif 23 <= result <= 24.9:
        labelresult2.configure(text="น้ำหนักเกิน")
    elif 18.6 <= result <= 22.9:
        labelresult2.configure(text="น้ำหนักปกติ เหมาะสม")
    else :
        labelresult2.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow,text = "Height : ",width=15)
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow,width=30)
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text = "Weight : ",width=15)
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow,width=30)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "Calculate")
calculateButton.bind("<Button-1>",leftClickButton)
calculateButton.grid(row=2)
labelresult = Label(MainWindow,text = "Result")
labelresult.grid(row=2,column=1)
labelresult2 = Label(MainWindow,text = "")
labelresult2.grid(row=3,column=1)
MainWindow.mainloop()