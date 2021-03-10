from tkinter import *

root = Tk()

# my_label1 = Label(root, Text="Olá tudo Bem?")
# my_label1.pack()
# # my_label2 = Label()
#
# root.mainloop()

my_label1 = Label(root, text="Olá")
my_label2 = Label(root, text='OLA MEU NOME É ROBOT 👽 ')

my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=1)

root.mainloop()
