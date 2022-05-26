# step 1 : import tkinter
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from VHDL import *
import sys,os

### Global variables #####################################################################
global collected_paths,present_paths, fpaths_fname, root
# step 2 : make root window
root = Tk()
root.title("VGen")
root.geometry("480x300")
root.resizable(False,False) # x and y direction of window not resizable
# file paths placeholder
fpaths_fname = 'VHDL_files.txt'
collected_paths = []
present_paths = set()

### Button commands ######################################################################
# browse button command
def browse():
    filename = filedialog.askopenfilename(
        initialdir =   "/",
        title      =   "Select a File",
        filetypes  = (("VHDL files","*.vhd*"),
                      ("all files" ,"*.*")),
        multiple   = True
    )

    if len(filename) != 0:
        for fname in filename:
            # only consider the new files added
            if fname not in present_paths:
                # all unique files are added
                present_paths.add(fname)
                collected_paths.append(fname)
                if not check_file(fpaths_fname):
                    with open(fpaths_fname, mode = 'w') as file:
                        file.write(fname)
                else:
                    with open(fpaths_fname, mode = 'a+') as file:
                        s = '\n' + fname
                        file.write(s)

                file_list.insert(len(present_paths),fname)
            else:
                print(f'------------------------------')
                print(f'{fname} has already been added')

        print(f'-------------')
        print('added files :')
        for files in collected_paths:
            s = '  ' + files
            print(s)
    else:
        print('No selected files')

# generate button command
def generate():
    imported_entities = VGen.vimport_files(collected_paths)
    # declare top level
    parent_entity = Entity(parent_entity_name_entry.get())

    # add and instantiate selected components
    for entity in imported_entities.values():
        parent_entity.add_component(entity)
        parent_entity.instantiate(entity)

    if len(collected_paths):
        parent_entity.generate_code()
    else:
        print(f'-----------------')
        print('No files selected')

    print(f'------------------------------')
    for fname in collected_paths:
        print(fname)

    collected_paths.clear()
    present_paths.clear()
    file_list.delete(0,END)

    if check_file(fpaths_fname):
        os.remove(fpaths_fname)

# done button command
def done():
    if check_file(fpaths_fname):
        os.remove(fpaths_fname)
    exit()

### Misc functions #######################################################################
def check_file(path):
    file = Path(path)
    return file.is_file()

def organize():
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)

    name_input_frame.grid(column = 0, row = 0, columnspan = 1, sticky = 'W')
    parent_entity_name.pack(side = LEFT)
    parent_entity_name_entry.pack(side = LEFT)
    label_file_explorer.grid(column = 0, row = 1,sticky = 'W')
    file_list.grid(column = 0, row = 2, columnspan = 4, padx = 5, pady = 5, sticky = 'nesw')
    browse_button.grid(column = 0, row = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'nesw')
    generate_button.grid(column = 2, row = 3, columnspan = 2, padx = 5, pady = 5, sticky = 'wsen')
    done_button.grid(column = 0, row = 4, columnspan = 4, padx = 5, pady = 5,sticky = 'nesw')

### MAIN #################################################################################
# step 3: declare/add widgets
label_file_explorer = Label(root, text = "Added components : ")
browse_button = Button(root, text = 'Browse', width = 20,command = browse)
generate_button = Button(root, text = 'Generate', width = 20,command = generate)
done_button = Button(root, text = 'Done', command = done)
file_list = Listbox(root)
name_input_frame = Frame(root)
parent_entity_name = Label(name_input_frame, text = 'Entity : ')
parent_entity_name_entry = Entry(name_input_frame)
# organize widgets
organize()
# execute window
root.mainloop()
