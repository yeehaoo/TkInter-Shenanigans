import tkinter as tk

class Todo(tk.Tk):
    def __init__(self, tasks=None):
        super().__init__()

        #initialisation of "tasks" attribute.
        #if "tasks" argument is empty, initialise tasks.
        #else, use "tasks" argument as tasks.
        if not tasks:
            self.tasks = []
        else:
            self.tasks = tasks

        self.title("To-Do App v1")
        self.geometry("300x400")

        #add "title" as a task, to appear at the top
        todo1 = tk.Label(self, text="--- Add Items Here ---", bg="lightgrey", fg="black", pady=10)
        self.tasks.append(todo1)

        #pack tasks
        for task in self.tasks:
            task.pack(side=tk.TOP, fill=tk.X)

        #textbox to enter new tasks
        self.task_create = tk.Text(self, height=3, bg="white", fg="black")

        #pack textbox, set focus to type
        self.task_create.pack(side=tk.BOTTOM, fill=tk.X)
        self.task_create.focus_set()

        #bind ENTER key to add_task, so user can add a task by pressing enter
        self.bind("<Return>", self.add_task)

        self.colour_schemes = [{"bg": "lightgrey", "fg": "black"}, {"bg": "grey", "fg": "white"}]

    def add_task(self, event=None):
        #get text of textbox
        task_text = self.task_create.get(1.0,tk.END).strip()

        #add task if user has typed any text
        if len(task_text) > 0:
            new_task = tk.Label(self, text=task_text, pady=10)
#background colour of task
            _, task_style_choice = divmod(len(self.tasks), 2)

            my_scheme_choice = self.colour_schemes[task_style_choice]

            new_task.configure(bg=my_scheme_choice["bg"])
            new_task.configure(fg=my_scheme_choice["fg"])
#pack new task
            new_task.pack(side=tk.TOP, fill=tk.X)
#add the task to tasklist
            self.tasks.append(new_task)
#clear textbox
        self.task_create.delete(1.0, tk.END)

if __name__ == "__main__":
    todo = Todo()
todo.mainloop()
