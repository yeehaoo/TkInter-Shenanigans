import tkinter as tk

root = tk.Tk()

'''
def printName():
    print("Hello World!")

button_1 = tk.Button(root, text="Print my name", command=printName)
button_1.pack()
'''

def printName(event):
    print("Hello World!")

button_1 = tk.Button(root, text="Print my name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()
