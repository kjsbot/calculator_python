from tkinter import *
import operator

root = Tk()
root.title("calculator")

ops = {"+": operator.add, "-": operator.sub, "x": operator.mul, "/": operator.truediv}
n = 0

def numPad(num):
    n = np.get()
    np.delete(0, END)
    np.insert(0, str(n) + str(num))

def clickOp(t):
    global op
    op = t
    global num1
    num1 = int(np.get())
    np.delete(0, END)

def getAns():
    global num2
    num2 = int(np.get())
    np.delete(0, END)
    np.insert(0, str(ops[op](num1, num2)))

def clrScrn():
    np.delete(0, END)
    num1=0
    num2=0
    op=""

def delNum():
    np.delete(0)
    
np = Entry(root, width=35, borderwidth=5)
np.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

equals = Button(root, bg= "#a5b1c2", text="=", padx=20, pady=20, command=getAns)
equals.grid(row=6, column=2)
clear = Button(root, bg= "#a5b1c2", text="CL", padx=20, pady=20, command=clrScrn)
clear.grid(row=6, column=0)

plus = Button(root, bg= "#FFC312", text="+", padx=20, pady=20, command=lambda:clickOp("+"))
plus.grid(row=3, column=3)
minus = Button(root, bg= "#c7ecee", text="-", padx=20, pady=20, command=lambda:clickOp("-"))
minus.grid(row=4, column=3)
multi = Button(root, bg= "#C4E538", text="x", padx=20, pady=20, command=lambda:clickOp("x"))
multi.grid(row=5, column=3)
divi = Button(root, bg= "#FDA7DF", text="/", padx=20, pady=20, command=lambda:clickOp("/"))
divi.grid(row=6, column=3)
#maybe use an array?
b1 = Button(root, text="1", padx=20, pady=20, command=lambda: numPad(1))
b2 = Button(root, text="2", padx=20, pady=20, command=lambda: numPad(2))
b3 = Button(root, text="3", padx=20, pady=20, command=lambda: numPad(3))
b4 = Button(root, text="4", padx=20, pady=20, command=lambda: numPad(4))
b5 = Button(root, text="5", padx=20, pady=20, command=lambda: numPad(5))
b6 = Button(root, text="6", padx=20, pady=20, command=lambda: numPad(6))
b7 = Button(root, text="7", padx=20, pady=20, command=lambda: numPad(7))
b8 = Button(root, text="8", padx=20, pady=20, command=lambda: numPad(8))
b9 = Button(root, text="9", padx=20, pady=20, command=lambda: numPad(9))
b0 = Button(root, text="0", padx=20, pady=20, command=lambda: numPad(0))
#figure out how to use a for loop
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=4, column=0)
b5.grid(row=4, column=1)
b6.grid(row=4, column=2)
b7.grid(row=5, column=0)
b8.grid(row=5, column=1)
b9.grid(row=5, column=2)
b0.grid(row=6, column=1)

root.mainloop()
