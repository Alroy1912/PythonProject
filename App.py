from tkinter import *
from tkinter import ttk 
import datetime as dt
from tkinter import messagebox

Tasks=[]
Timer={}
TotalTime={}

def homePage():
    AddTasks.grid_forget()
    Task.grid_forget()
    dashBoard.grid_forget()
    Home.pack()

def AddTasksPage():
    Home.pack_forget() 
    Task.grid_forget()
    dashBoard.grid_forget()
    AddTasks.grid()

def taskPage():
    for widget in Task.winfo_children():
        widget.destroy()
    AddTasks.grid_forget()
    Home.pack_forget()
    dashBoard.grid_forget()
    Task.grid()
    taskLabel = Label(Task, text="Tasks",bg="white",padx=10).grid(row=0, column=0)
    for i,(task,date,time) in enumerate(Tasks):
        x1 = Label(Task,width=10, text=task, bg="white").grid(row=i+1, column=0)
        x2 = Label(Task,width=10, text=date, bg="white").grid(row=i+1, column=1)
        # x3 = Label(Task,width=10, text=time, bg="white").grid(row=i+1, column=2)
        x4 = Button(Task,text="Start Task",command=lambda t=task: start(t)).grid(row=i+1, column=3)
    homeButton = Button(Task, text="Exit", command=homePage).grid(row =len(Tasks)+2, column=1,pady=20,padx=20)
    AddTasksButton = Button(Task, text="Add Tasks", command=AddTasksPage).grid(row =len(Tasks)+2, column=2,pady=20,padx=20)
    dashBoardButton = Button(Task, text="DashBoard", command=dashBoardPage).grid(row =len(Tasks)+2, column=3,pady=20,padx=20)

def dashBoardPage():
    for widget in dashBoard.winfo_children():
        widget.destroy()
    AddTasks.grid_forget()
    Task.grid_forget()
    Home.pack_forget()
    dashBoard.grid()
    taskLabel = Label(dashBoard, text="DashBoard",bg="white",padx=10).grid(row=0, column=0)
    for i,(task,duration) in enumerate(TotalTime.items()):
        x1 = Label(dashBoard,width=10, text=task, bg="white").grid(row=i, column=0)
        x2 = Label(dashBoard,width=10, text=str(duration), bg="white").grid(row=i, column=1)
    homeButton = Button(dashBoard, text="Exit", command=homePage).grid(row =len(TotalTime)+1, column=0,pady=20,padx=20)
    AddTasksButton = Button(dashBoard, text="AddTasks", command=AddTasksPage).grid(row =len(TotalTime)+1, column=1,pady=20,padx=20)
    taskButton = Button(dashBoard, text="Tasks", command=taskPage).grid(row =len(TotalTime)+1, column=2,pady=20,padx=20)

def addTask():
    task = createTask.get()
    createTask.delete(0, END) 
    if not task:
        print("Please enter a task.")
    elif any(task == t[0] for t in Tasks):
        print(f"Task '{task}' exists.")
    else:
        print(f"Task '{task}' added.")
        TotalTime[task] = dt.timedelta(0)
        date = dt.date.today()
        time = dt.datetime.now().strftime("%H:%M:%S")
        Tasks.append((task,date,time))

def start(task):
    timerStart(task)
    doTask=Toplevel(root,bg="white")
    doTask.title(task)
    doTask.geometry("300x200")
    startLabel = Label(doTask, text="Focus on your task", bg="white").pack(pady=100)
    doTask.protocol("WM_DELETE_WINDOW", lambda: onTaskClose(doTask, task))

def timerStart(task):
    start = dt.datetime.now()
    Timer[task] = start

def timerStop(task):
    end = dt.datetime.now()
    duration = end - Timer[task]
    TotalTime[task] += duration
    messagebox.showinfo("Task Duration", f"Task '{task}' completed in {duration}")

def onTaskClose(doTask, task):
    timerStop(task)
    doTask.destroy()

root = Tk()
root.configure(bg="white")
root.resizable(False, False)
root.title("Focus Tracker")
root.geometry("500x300")

Home = Frame(root,bg="white")
Home.pack()
homeLabel = Label(Home, height=18, width=50, text="FOCUS TRACKER", bg="white").pack()
homeButton = Button(Home, text="Login", command=AddTasksPage).pack()


AddTasks = Frame(root,bg="white")
AddTasksLabel = Label(AddTasks, height=6, width=10, text="Add Tasks",bg="white").grid(row=0, column=0)
createLabel = Label(AddTasks, height=6, width=20, text="Create Task",bg="white").grid(row=1, column=0)
createTask = Entry(AddTasks, width=20)
createTask.grid(row=1, column=1, padx=50)
createButton = Button(AddTasks, text="Add", command=addTask).grid(row=1, column=2)
HomeButton = Button(AddTasks, text="Exit", command=homePage).grid(row=2, column=0)
TaskButton = Button(AddTasks, text="Tasks", command=taskPage).grid(row=2, column=1)
dashBoardButton = Button(AddTasks, text="DashBoard", command=dashBoardPage).grid(row=2, column=2)

Task = Frame(root,bg="white")

dashBoard = Frame(root,bg="white")
dashBoardLabel = Label(dashBoard, height=6, width=10, text="Dashboard",bg="white").grid(row=0, column=0)

root.mainloop() 