import tkinter as tk


def printSomething():
    print("Hello World!")

root = tk.Tk()

# ***** Main Menu *****

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

# ***** Toolbar *****

toolbar = tk.Frame(root, bg="blue")

insert = tk.Button(toolbar, text="Insert Image", command=printSomething)
insert.pack(side=tk.LEFT, padx=2, pady=5)
printButton = tk.Button(toolbar, text="Print", command=printSomething)
printButton.pack(side=tk.LEFT, padx=2, pady=5)

toolbar.pack(side=tk.TOP, fill=tk.X)

# ***** Status Bar *****

status = tk.Label(root, text="Preparing to do nothing...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
