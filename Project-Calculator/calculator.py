from tkinter import *
from tkinter import ttk

colour1 = "#fcba03" #yellow
colour2 = "#161715" #black
colour3 = "#fca2f2" #pink
colour4= "#8a8484" #gray

calculator = Tk()
calculator.title("Simple Calculator")
calculator.geometry("297x343")
calculator.config(bg=colour2)
values = ''

text_value = StringVar()

frame_screen = Frame(calculator, width=300, height=50, bg=colour3)
frame_screen.grid(row=0, column=0)
calculator_label = Label(frame_screen, textvariable=text_value, width=32, anchor="e", height=3,padx=7, relief=FLAT, justify=RIGHT, font=('Arial'), bg=colour3)
calculator_label.place(x=0,y=0)

def calculate(button_click):
    global values
    values = values + str(button_click)    
    text_value.set(values)
    
def calculating():
    global values
    result = eval (values)
    text_value.set(result)
    
def frame_clean():
    global values
    values = ''
    text_value.set('')

frame_keys = Frame(calculator, width=300, height=350, bg=colour2)
frame_keys.grid(row=1, column=0)

button1 = Button(frame_keys, text="C", width=11, height=2, font=('Arial'), relief=RAISED, overrelief=RIDGE, command = frame_clean)
button1.place(x=0,y=0)
button2 = Button(frame_keys, text="%", width=11 , height=2, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('%'))
button2.place(x=100,y=0)
button3 = Button(frame_keys, text="/",width=11, height=2, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('/'))
button3.place(x=200,y=0)

button4 = Button(frame_keys, text="7", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('7'))
button4.place(x=0,y=48)
button5 = Button(frame_keys, text="8", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('8'))
button5.place(x=75,y=48)
button6 = Button(frame_keys, text="9", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('9'))
button6.place(x=150,y=48)
button7 = Button(frame_keys, text="x", width=8, height=3, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('*'))
button7.place(x=225,y=48)

button8 = Button(frame_keys, text="4", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('4'))
button8.place(x=0,y=114)
button9 = Button(frame_keys, text="5", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('5'))
button9.place(x=75,y=114)
button10 = Button(frame_keys, text="6", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('6'))
button10.place(x=150,y=114)
button11 = Button(frame_keys, text="-", width=8, height=3, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('-'))
button11.place(x=225,y=114)

button12 = Button(frame_keys, text="1", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('1'))
button12.place(x=0,y=176)
button13 = Button(frame_keys, text="2", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('2'))
button13.place(x=75,y=176)
button14 = Button(frame_keys, text="3", width=8, height=3, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('3'))
button14.place(x=150,y=176)
button15 = Button(frame_keys, text="+", width=8, height=3, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('+'))
button15.place(x=225,y=176)

button16 = Button(frame_keys, text="0", width=16, height=2, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('0'))
button16.place(x=0,y=240)
button17 = Button(frame_keys, text=".", width=8, height=2, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command=lambda: calculate('.'))
button17.place(x=150,y=240)
button18 = Button(frame_keys, text="=", width=8, height=2, bg=colour1, font=('Arial'), relief=RAISED, overrelief=RIDGE, command = calculating)
button18.place(x=225,y=240)

calculator.mainloop()  