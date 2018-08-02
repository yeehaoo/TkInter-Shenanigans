import tkinter as tk

root = tk.Tk()

photo = tk.PhotoImage(file="image.png")
label_1 = tk.Label(root, image=photo)
label_1.pack()

root.mainloop()
