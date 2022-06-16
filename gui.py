import tkinter as tk
from tkinter import LEFT, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import same_level_check as main
import os

filepath_1 = ""
filepath_2 = ""

# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
#root.resizable(False, False)
root.geometry('350x500')
root.configure(bg='#57caff')
root.title('Same level student checker - Made by Sean')
root.resizable(True, True)

number_of_months = tk.IntVar()
number_of_months.set(9)

def run_application():
    month_limit = number_of_months.get()

    if(filepath_1 == ""):
        error = "Please choose a contract file."
        tk.messagebox.showerror(title="Error", message=error)
        return
    
    if(filepath_2 == ""):
        error = "Please choose an attendance file."
        tk.messagebox.showerror(title="Error", message=error)
        return

    if(month_limit <= 0 or month_limit == ""):
        error = "Please enter an integer for month limit (eg '9') that is higher than 0."
        tk.messagebox.showerror(title="Error", message=error)
        return
    
    month_limit = int(month_limit)

    print("Send the following:")
    print("Contract filepath: ", filepath_1)
    print("Attendance filepath: ", filepath_2)
    print("Month limit: ", month_limit)

    main.main(filepath_1, filepath_2, month_limit)

def select_file_1():

    global filepath_1

    filetypes = (
        ('csv files', '*.csv'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    label_1['text'] = filename 
    filepath_1 = filename
    print(filename)

def select_file_2():

    global filepath_2

    filetypes = (
        ('csv files', '*.csv'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir=os.getcwd(),
        filetypes=filetypes)

    label_2['text'] = filename 
    filepath_2 = filename

title = tk.Label(root, height=2, text="same level student checker")
title.pack()
title.configure(font=("Times New Roman", 20))
title.configure(bg='#57caff')

sub_title_1 = tk.Label(root, text="      1. Choose the contract file")
sub_title_1.pack(pady=2, anchor="w")
sub_title_1.configure(bg='#57caff')

# open button - contract file
open_button_1 = ttk.Button(
    root,
    text='Select contract csv',
    command=select_file_1
)

open_button_1.pack(pady=5)

label_1 = tk.Label(root, text="No file selected")
label_1.pack(pady=5)
label_1.configure(bg='#57caff')

spacer = tk.Label(root, text="")
spacer.pack(pady=5)
spacer.configure(bg='#57caff')

sub_title_2 = tk.Label(root, text="      2. Choose the attendance file")
sub_title_2.pack(pady=2, anchor="w")
sub_title_2.configure(bg='#57caff')

# open button - attendance file
open_button_2 = ttk.Button(
    root,
    text='Select attendance csv',
    command=select_file_2,
)

open_button_2.pack(pady=5)

label_2 = tk.Label(root, text="No file selected")
label_2.pack(pady=10)
label_2.configure(bg='#57caff')

sub_title_3 = tk.Label(root, text="      3. Input number of months at same level (eg: 9)")
sub_title_3.pack(pady=12, anchor="w")
sub_title_3.configure(bg='#57caff')

month_entry = ttk.Entry(root, textvariable=number_of_months, width=5)
month_entry.pack(pady=5)

sub_title_4 = tk.Label(root, text="      4. Once 1-3 complete, click Run")
sub_title_4.pack(pady=15, anchor="w")
sub_title_4.configure(bg='#57caff')

# open button - attendance file
run_button = ttk.Button(
    root,
    text='Run',
    command=run_application,
)

run_button.pack(pady=5)

# run the application
root.mainloop()