from tkinter import *

root = Tk()
myLabel = Label(root, text='Welcome.')
myLabel.pack()
mainloop()

from tkinter import *

root = Tk()
root.title('CI TECH IBM')
root.iconbitmap('ibm.ico')
root.geometry("600x890")

# Add image
bell = PhotoImage(file="Panda.png")

# Add image to Label
bell_label = Label(root, image=bell)
bell_label.pack(pady=20)

# Create Ring function


def ring():
    root.bell()
# # Add Button
    my_button = Button(root, text="Ring", command=ring, font=("Arial", 14), fg="#4d4d4d")
    my_button.pack(pady=20)

root.bell()
root.mainloop()
