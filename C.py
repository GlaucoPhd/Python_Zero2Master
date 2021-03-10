from tkinter import *

root = Tk()

def myClick():
    my_label = Label(root, text='Clicked a Button.')
    my_label.pack()

my_button = Button(root, text='Click', padx=100, pady=50)
my_button.pack()

root.mainloop()
