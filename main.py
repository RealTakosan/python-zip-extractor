from tkinter import *
from tkinter import filedialog
from pathlib import Path
import zipfile

def open_file():
    global zip_open
    global file_path
    global file_name
    global file_ext
    zip_open=False
    con_list.delete(0, END)
    file_path=filedialog.askopenfilename()
    file_name=Path(file_path).stem
    file_ext=Path(file_path).suffix
    is_a_zip=zipfile.is_zipfile(file_path)
    file_label.config(text=file_name+file_ext)
    if is_a_zip==True:
        zip_open = True
        zip_file = zipfile.ZipFile(file_path, "r")
        for name in zip_file.namelist():
            con_list.insert(END, f"{name}")
            zip_file.close()

def extract_all():
    if zip_open==True:
        extractall_label.config(text="Success!")
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(file_name)

def extract():
    if zip_open==True:
        extract_label.config(text="Success!")
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extract(con_list.get(ANCHOR), file_name)

root = Tk()

root.resizable(False,False)
root.title("ZIP Extractor")
root.geometry("450x200")

con_list = Listbox(root)
con_list.place(x=15,y=15)

open_btn = Button(root, text="Open ZIP", height=1, width=10, command=open_file)
open_btn.place(x=150,y=15)

extractall_btn = Button(root, text="Extract All", height=1, width=10, command=extract_all)
extractall_btn.place(x=150,y=55)

extract_btn = Button(root, text="Extract", height=1, width=10, command=extract)
extract_btn.place(x=150,y=95)

file_label = Label(root, text="", height=1, width=30, anchor="w", justify=LEFT)
file_label.place(x=230, y=15)

extractall_label = Label(root, text="", height=1, width=10, anchor="w", justify=LEFT)
extractall_label.place(x=230, y=55)

extract_label = Label(root, text="", height=1, width=10, anchor="w", justify=LEFT)
extract_label.place(x=230, y=95)

root.mainloop()
