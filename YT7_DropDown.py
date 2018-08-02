import tkinter as tk


def printSomething():
    print("Hello World!")

root = tk.Tk()

menuBar = tk.Menu(root)
root.config(menu=menuBar)

ddl_1 = tk.Menu(menuBar)
menuBar.add_cascade(label="File", menu=ddl_1)
ddl_1.add_command(label="New Project...", command=printSomething)
ddl_1.add_command(label="New", command=printSomething)
ddl_1.add_separator()
ddl_1.add_command(label="Exit", command=printSomething)

ddl_2 = tk.Menu(menuBar)
menuBar.add_cascade(label="Edit", menu=ddl_2)
ddl_2.add_command(label="Redo", command=printSomething)

root.mainloop()
