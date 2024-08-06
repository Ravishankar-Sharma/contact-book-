from tkinter import *

def save_data():
    nametext = name.get()
    phonetext = phone.get()

    with open("contact.txt", 'a') as file:
            file.write(f"Name: {nametext}\n")
            file.write(f"Phone: {phonetext}\n\n")
            Label(root, text="Contact Saved Successfully", fg="green", font="Helvetica 13").grid(row=4, column=1)
            name.set("")
            phone.set("")

root = Tk()
root.geometry('400x400')

# labels:
Label(root, text="name:").grid(row=0, column=0, padx=10, pady=10)
Label(root, text="phone:").grid(row=1, column=0, padx=10, pady=10)

# Variables defining
name = StringVar()
phone = StringVar()

# Entries
Entry(root, textvariable=name).grid(row=0, column=1, pady=10)
Entry(root, textvariable=phone).grid(row=1, column=1, pady=10)

# button
Button(root, text="Submit", command=save_data).grid(row=3, column=1)

root.mainloop()
