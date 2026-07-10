from tkinter import *
from time import strftime
root=Tk()
root.title("Digital Clock")
root.geometry("500x200")
root.configure(bg="black")

def time():
    string=strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(100,time)

label = Label(
    root,
    font=("arial", 50, "bold"),
    background="black",
    foreground="red"
)
label.pack(anchor="center", pady=40)

time()
root.mainloop()
