from tkinter import *
from tkinter import colorchooser

win = Tk()
win.title('hello world')
win.geometry('400x400')
win.resizable(False, False)
#mylable1 = Label(win, text='1 label hhh')
#mylable1.pack()
#mylable2 = Label(win, text='2 lable kkk')
#mylable3 = Label(win, text='3 lable jjj')
#mylable1.grid(row=0, column=0)
#mylable2.grid(row=1, column=1)
#mylable3.grid(row=0, column=2)

#colour = colorchooser.askcolor()
#print(colour)

#def onclick():
#    mylable = Label(win, text=f'hello {input_field.get()}')
#    mylable.pack()


def get_squares(number):
    input_field.delete(0, END)
    input_field.insert(0, int(number ** 2))

input_field = Entry(win, width=50, fg='red', bg='blue', borderwidth=5)
input_field.pack()


myButton = Button(win, text='click me', padx=50, pady=50, fg='#FF0000', bg='#00ff00',
                  command=lambda: get_squares(input_field.get()))
myButton.pack()

win.mainloop()