# step 1 : import tkinter
from tkinter import *
from tkinter import filedialog
import sys,os
from pathlib import Path

def browse():
    filename = filedialog.askopenfilename(
                                        initialdir =   "/",
                                        title      =   "Select a File",
                                        filetypes  = (("VHDL files","*.vhd*"),
                                                      ("all files" ,"*.*")),
                                        multiple   = True
                                        )




    for fname in filename:
        collected_paths.append(fname)
        if not check_file(fpaths_fname):
            with open(fpaths_fname, mode = 'w') as file:
                file.write(fname)
        else:
            with open(fpaths_fname, mode = 'a+') as file:
                s = '\n' + fname
                file.write(s)

def check_file(path):
    file = Path(path)
    return file.is_file()

def generate():
    for fname in collected_paths:
        print(fname)
        

    if check_file(fpaths_fname):
        os.remove(fpaths_fname)

def save_paths(paths):
    return list(paths)

def organize():
    label_file_explorer.grid(column = 0, row = 1,sticky = 'W')
    browse_button.grid(column = 0, row = 2,sticky = 'W')
    generate_button.grid(column = 0, row = 3,pady=5,sticky = 'W')
    done_button.grid(column = 0, row = 4,pady=5,sticky = 'W')

##########################################################################################

# step 2 : make root window
root = Tk()
root.title("File selection")
root.geometry("300x150")
root.resizable(False,False) # x and y direction of window not resizable

# file paths placeholder
fpaths_fname = 'vhd_files.txt'
collected_paths = []
# step 3: declare/add widgets
label_file_explorer = Label(root,
                            text = "Component selection",
                            fg = "blue")

browse_button = Button(root, text = 'Browse', command = browse)
generate_button = Button(root, text = 'Generate', command = generate)
done_button = Button(root, text = 'Done', command = exit)
# organize widgets
organize()
# execute window
root.mainloop()
