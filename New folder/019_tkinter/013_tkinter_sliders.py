from tkinter import *

root = Tk()
root.title('This is sample app made by tkinter')
root.geometry('400x400')

vertical = Scale(root, from_=0, to=100)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()


slide_var = StringVar()
def slide():
    slide_var.set(horizontal.get())

my_label = Label(root, textvariable=slide_var)
my_label.pack()


my_button = Button(root, text='Click me', command=slide).pack()
root.mainloop()
