import tkinter as tk

root = tk.Tk()

label_1 = tk.Label(root, text="Name")
label_2 = tk.Label(root, text="Password")
entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)
c = tk.Checkbutton(root, text="Keep me logged in")

label_1.grid(row=0, sticky=tk.E)
label_2.grid(row=1, sticky=tk.E)

entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

c.grid(columnspan=2)

root.mainloop()
