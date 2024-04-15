import subprocess
import tkinter as tk

def open_program1():
    subprocess.run(["python", "Special_Calc.py"])

def open_program2():
    subprocess.run(["python", "assignment_1.py"])

def open_program3():
    subprocess.run(["python", "program3.py"])

def open_program4():
    subprocess.run(["python", "program4.py"])

root = tk.Tk()

button1 = tk.Button(root, text="Open Special Relativity Calculator", command=open_program1)
button1.pack()

button2 = tk.Button(root, text="Open Profit Estimator", command=open_program2)
button2.pack()

button3 = tk.Button(root, text="Open Program 3", command=open_program3)
button3.pack()

button4 = tk.Button(root, text="Open Program 4", command=open_program4)
button4.pack()

root.mainloop()