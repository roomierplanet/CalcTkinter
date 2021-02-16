from tkinter import *

class Calculator(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.CalcEntry()
        self.CalcButtons()
        self.numStack = []
        self.operationStack = []

    def CalcEntry(self):
        self.field = Entry(self, width=45, borderwidth=5)
        self.field.grid(row=0, column=0, columnspan = 3)

    def SetButton(self, num):
        current = str(self.field.get())
        self.field.delete(0, END)
        self.field.insert(0, current + str(num))

    def OpButton(self, op):
        self.numStack.append(float(self.field.get()))
        self.operationStack.append(op)
        self.field.delete(0, END)

    def EqualsButton(self):
        last_num = int(self.field.get())
        self.field.delete(0, END)
        res = self.numStack[0]
        print(self.numStack)
        print(self.operationStack)
        print(last_num)
        for i in range(1, len(self.numStack)):
            if self.operationStack[i] == '+':
                res += self.numStack[i]
                print(res)
            if self.operationStack[i] == '-':
                res -= self.numStack[i]
                print(res)
            elif self.operationStack[i] == '*':
                res *= self.numStack[i]
                print(res)
            elif self.operationStack[i] == '/':
                if self.numStack[i] == 0:
                    self.field.delete(0, END)
                else:
                    res /= self.numStack[i]
            else:
                res = pow(self.numStack[i], self.numStack[i+1])
        length = len(self.operationStack)
        top = self.operationStack[length-1]
        print(res)
        print(top)
        if top == '+':
            self.field.insert(0, res+last_num)
        elif top == '-':
            self.field.insert(0, res-last_num)
        elif top == '*':
            self.field.insert(0, res*last_num)
        elif top == '/':
            self.field.insert(0, res/last_num)
        elif top == '^':
            self.field.insert(0, pow(res, last_num))
        self.operationStack = []
        self.numStack = []


    def CalcButtons(self):
        button1 = Button(self, text="1", padx=40, pady=20, command=lambda:self.SetButton(1)).grid(row=3, column=0)
        button2 = Button(self, text="2", padx=40, pady=20, command=lambda:self.SetButton(2)).grid(row=3, column=1)
        button3 = Button(self, text="3", padx=40, pady=20, command=lambda:self.SetButton(3)).grid(row=3, column=2)
        button4 = Button(self, text="4", padx=40, pady=20, command=lambda:self.SetButton(4)).grid(row=2, column=0)
        button5 = Button(self, text="5", padx=40, pady=20, command=lambda:self.SetButton(5)).grid(row=2, column=1)
        button6 = Button(self, text="6", padx=40, pady=20, command=lambda:self.SetButton(6)).grid(row=2, column=2)
        button7 = Button(self, text="7", padx=40, pady=20, command=lambda:self.SetButton(7)).grid(row=1, column=0)
        button8 = Button(self, text="8", padx=40, pady=20, command=lambda:self.SetButton(8)).grid(row=1, column=1)
        button9 = Button(self, text="9", padx=40, pady=20, command=lambda:self.SetButton(9)).grid(row=1, column=2)
        button0 = Button(self, text="0", padx=40, pady=20, command=lambda:self.SetButton(0)).grid(row=4, column=0)
        buttonClear = Button(self, text="Clear", padx=30, pady=20,
                             command = lambda: self.field.delete(0, END)).grid(row=4, column=1)
        buttonEqual = Button(self, text = "=", padx=40, pady=20,
                             command = self.EqualsButton).grid(row = 4, column = 2)
        buttonAdd = Button(self, text="+", padx=20, pady=20,
                           command = lambda: self.OpButton('+')).grid(row=0, column=3)
        buttonSub = Button(self, text="-", padx=22, pady=20,
                           command = lambda: self.OpButton('-')).grid(row=1, column=3)
        buttonMult = Button(self, text="*", padx=22, pady=20,
                            command = lambda: self.OpButton('*')).grid(row=2, column=3)
        buttonDiv = Button(self, text="/", padx=22, pady=20,
                           command = lambda: self.OpButton('/')).grid(row=3, column=3)
        buttonExp = Button(self, text="^", padx=20, pady=20,
                           command = lambda: self.OpButton('^')).grid(row=4, column=3)
root = Tk()
root.title("Arnav Nagpal - Calculator")
app = Calculator(master = root)
app.mainloop()
