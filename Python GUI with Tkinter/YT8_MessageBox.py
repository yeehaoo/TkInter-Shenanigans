import tkinter as tk
import tkinter.messagebox

root = tk.Tk()

tk.messagebox.showinfo('Window Title', 'Hello World!')

answer = tk.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print('Get a life')

root.mainloop()
