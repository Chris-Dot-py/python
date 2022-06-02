# step 1 : import tkinter
from tkinter import *
from tkinter import filedialog
from pathlib import Path
from VHDL import *
import sys,os

### Variables ############################################################################
global collected_paths,present_paths, paths, fpaths_fname, root
# step 2 : make root window
root = Tk()
root.title("VGen")
root.geometry("600x500")
root.resizable(False,False) # x and y direction of window not resizable
# file paths placeholder
fpaths_fname = 'VHDL_files.txt'
added_components = []
collected_paths = []
present_paths = set()
paths = {}

entity_labels_a = [] # OUT
port_labels_a = []
entity_labels_b = [] # IN
port_labels_b = []
entities = ['clk_rst','orologio','display', 'uart','scheduler','adc']
ports_a = ['port_1','port_2','port_3'] # OUT PORTS
ports_b = ['inport_1','inport_2','inport_3'] # IN PORTS

netlist = {} # {'Entity name' : [Port, .., Port]}

selected_out_port = StringVar(root)
selected_in_port = ''
out_port_connections = {}
selected_in_ports = []
is_highlight_on_a = BooleanVar(root, False)
is_highlight_on_b = []
last_clicked_port = IntVar(root,0)
last_clicked_entity = IntVar(root,0)

### Port Mapping related Funcitons #######################################################
def pop_up_a(event, num):
    for entity_label in entity_labels_a:
        entity_label.pack_forget()
    port_labels_frame_a.pack_forget()

    if port_labels_frame_a in entity_labels_a:
        if last_clicked_entity.get() != num:
            entity_labels_a.remove(port_labels_frame_a)
            entity_labels_a.insert(num+1, port_labels_frame_a) # change pos
            last_clicked_entity.set(num)
        else:
            entity_labels_a.remove(port_labels_frame_a)
    else:
        last_clicked_entity.set(num)
        entity_labels_a.insert(num+1, port_labels_frame_a)

    for index,entity_label in enumerate(entity_labels_a):
        entity_label.pack(side = 'top', anchor = 'nw')

def pop_up_b(event, num):
    for entity_label in entity_labels_b:
        entity_label.pack_forget()
        port_labels_frame_b.pack_forget()

    if port_labels_frame_b in entity_labels_b:
        if last_clicked_entity.get() != num:
            entity_labels_b.remove(port_labels_frame_b)
            entity_labels_b.insert(num+1, port_labels_frame_b) # change pos
            last_clicked_entity.set(num)
        else:
            entity_labels_b.remove(port_labels_frame_b)
    else:
        last_clicked_entity.set(num)
        entity_labels_b.insert(num+1, port_labels_frame_b)

    for index,entity_label in enumerate(entity_labels_b):
        entity_label.pack(side = 'top', anchor = 'nw')

def select_out_port(event, num):
    for port_label in port_labels_a:
        port_label.configure(bg = 'white')
        port_label.pack_forget()

    for index,port_label in enumerate(port_labels_a):
        if index == num:
            if is_highlight_on_a.get() is False:
                is_highlight_on_a.set(True)
                port_label.configure(bg = 'cyan')
                port_label.pack(side = 'top', anchor = 'nw')
                selected_out_port.set(port_label['text'].replace(' ',''))
            else:
                # cliking on different port
                if last_clicked_port.get() != num:
                    last_clicked_port.set(num)
                    port_label.configure(bg = 'cyan')
                    port_label.pack(side = 'top', anchor = 'nw')
                    selected_out_port.set(port_label['text'].replace(' ',''))
                    # deselect port labels b
                    for port_label in port_labels_b:
                        is_highlight_on_b[index].set(False)
                        port_label.pack_forget()

                    for port_label in port_labels_b:
                        port_label.configure(bg = 'white')
                        port_label.pack(side = 'top', anchor = 'nw')

                # clicking on the same port
                else:
                    is_highlight_on_a.set(False)
                    port_label.pack(side = 'top', anchor = 'nw')
                    selected_out_port.set('')
                    # deselect port labels b
                    for port_label in port_labels_b:
                        port_label.pack_forget()

                    for port_label in port_labels_b:
                        port_label.configure(bg = 'white')
                        port_label.pack(side = 'top', anchor = 'nw')
        else:
            port_label.pack(side = 'top', anchor = 'nw')

    if len(selected_out_port.get()) != 0:
        print(selected_out_port.get())

def multi_select_in_port(event, num):
    if is_highlight_on_a.get() is True:
        for port_label in port_labels_b:
            port_label.pack_forget()

        for index,port_label in enumerate(port_labels_b):
            if index == num:
                if is_highlight_on_b[index].get() is False:
                    is_highlight_on_b[index].set(True)
                    port_label.configure(bg = 'cyan')
                    port_label.pack(side = 'top', anchor = 'nw')
                    if len(selected_out_port.get()) != 0:
                        out_port_connections[selected_out_port.get()].append(port_label['text'])
                else:
                    is_highlight_on_b[index].set(False)
                    port_label.configure(bg = 'white')
                    port_label.pack(side = 'top', anchor = 'nw')
                    if len(selected_out_port.get()) != 0:
                        out_port_connections[selected_out_port.get()].remove(port_label['text'])
            else:
                port_label.pack(side = 'top', anchor = 'nw')

        print(out_port_connections[selected_out_port.get()])
    else:
        for port_label in port_labels_b:
            port_label.pack_forget()

        for port_label in port_labels_b:
            port_label.configure(bg = 'white')
            port_label.pack(side = 'top', anchor = 'nw')
        Label(root,text = 'no selected out ports', fg = 'red').grid()


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
                added_components.append(VGen.vimport(fname))
                if not check_file(fpaths_fname):
                    with open(fpaths_fname, mode = 'w') as file:
                        file.write(fname)
                else:
                    with open(fpaths_fname, mode = 'a+') as file:
                        s = '\n' + fname
                        file.write(s)

                component_name = fname.split('/')
                file_list.insert(len(present_paths),component_name[-1].replace('.vhd',''))
                # file_list.insert(len(present_paths),fname)

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
    if len(parent_entity_name_entry.get()) != 0:
        imported_entities = VGen.vimport_files(collected_paths)
        # declare top level
        parent_entity = Entity(parent_entity_name_entry.get())

        # add and instantiate selected components
        for entity in imported_entities.values():
            parent_entity.add_component(entity)
            parent_entity.instantiate(entity)

        if len(collected_paths) != 0:
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

        message('','black')
    else:
        s = 'Please Enter Entity Name...'
        message(s,'red')

# done button command
def done():
    if check_file(fpaths_fname):
        os.remove(fpaths_fname)
    exit()

### Misc functions #######################################################################
def check_file(path):
    file = Path(path)
    return file.is_file()

def message(s,c):
    GUI_message.pack_forget()
    GUI_message.configure(text = s, fg = c)
    GUI_message.pack(side = 'top', anchor = 'w')

def instantiate():
    print(file_list.get(ANCHOR))
    # for index,component in enumerate(added_components):
    entity_label_a = Label(frame_a, text = file_list.get(ANCHOR), bg = 'white')
    entity_label_a.pack(side = 'top', anchor = 'nw')
    # entity_label_a.bind('<Button-1>', lambda event, i = index: pop_up_a(event,i))
    entity_label_a.pack_propagate(False)
    entity_labels_a.append(entity_label_a)

    entity_label_b = Label(frame_b, text = file_list.get(ANCHOR), bg = 'white')
    entity_label_b.pack(side = 'top', anchor = 'nw')
    entity_label_b.pack_propagate(False)
    entity_labels_b.append(entity_label_b)

def organize():
    # root.columnconfigure(0, weight=0)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    # root.rowconfigure(0, weight=0)
    # root.rowconfigure(1, weight=0)
    root.rowconfigure(2, weight=1)
    # root.rowconfigure(3, weight=0)
    # root.rowconfigure(4, weight=0)

    # Entity name input
    name_input_frame.grid( row = 0, column = 0, sticky = 'W')
    parent_entity_name.pack( side = LEFT) # Label
    parent_entity_name_entry.pack( side = LEFT)
    # Selected Components viewer
    label_file_explorer.grid( row = 1, column = 0, sticky = 'W') # Label
    file_list.grid( row = 2, column = 0, padx = 5, pady = 5, sticky = 'nesw')
    # Browse and Instantiate Buttons
    browse_inst_button_frame.grid( row = 3, column = 0, padx = 5, pady = 5)
    browse_button.pack( side = 'left', anchor = 'nw', padx = (5,2.5))
    instantiate_button.pack( side = 'left', anchor = 'nw', padx = (2.5,5))
    # Out Ports Frame
    frame_a_label.grid( row = 1, column = 1, padx = 5, pady = (5,0), sticky = 'w') # Label
    border_a.grid( row = 2, column = 1, rowspan = 2, sticky = 'nws', padx = (5,2.5), pady = 5)
    border_a.grid_propagate(False)
    frame_a.pack( expand = True, side = 'left', fill = 'both', padx = 1, pady = 1)
    frame_a.pack_propagate(False)
    # In Ports Frame
    frame_b_label.grid( row = 1, column = 2, padx = 5, pady = (5,0), sticky = 'w') # Label
    border_b.grid( row = 2, column = 2, rowspan = 2, sticky = 'nws', padx = (2.5,5), pady = 5)
    border_b.grid_propagate(False)
    frame_b.pack( expand = True, side = 'left', fill = 'both', padx = 1, pady = 1)
    frame_b.pack_propagate(False)
    # Generate And Done Buttons
    gen_done_button_frame.grid( row = 4, column = 2, padx = 5, pady = 5, sticky = 'e')
    generate_button.pack( side = 'left', anchor = 'nw', padx = (5,2.5))
    done_button.pack( side = 'left', anchor = 'nw', padx = (2.5,5))
    # GUI messages
    GUI_message_wrapper.grid(row=4, column = 0, columnspan = 2, padx = 5, sticky = 'we')
    GUI_message.pack( side = 'left', anchor = 'nw')


### widgets ######################################################################
frame_a_label = Label(root, text = 'Out Ports :')
frame_b_label = Label(root, text = 'In Ports : ')
border_a = Frame(root, bg = 'black', width = 200)
frame_a = Frame(border_a, bg = 'white', width = 200)
border_b = Frame(root, bg = 'black', width = 200)
frame_b = Frame(border_b, bg = 'white', width = 200)

label_file_explorer = Label(root, text = "Added components : ")

browse_inst_button_frame = Frame(root)
browse_button = Button(browse_inst_button_frame, text = 'Browse', width = 10,command = browse)
instantiate_button = Button(browse_inst_button_frame, text = 'Instantiate', width = 10, command = instantiate)

gen_done_button_frame = Frame(root)
generate_button = Button(gen_done_button_frame, text = 'Generate', width = 10,command = generate)
done_button = Button(gen_done_button_frame, text = 'Done', width = 10, command = done)

file_list = Listbox(root)
name_input_frame = Frame(root)
parent_entity_name = Label(name_input_frame, text = 'Entity : ')
parent_entity_name_entry = Entry(name_input_frame)

GUI_message_wrapper = Frame(root)
GUI_message = Label(GUI_message_wrapper)

### Instanced Labels manager #############################################################
# entities A
# for index,entity in enumerate(added_components):
#     netlist[entity] = {}
#     entity_label = Label(frame_a, text = entity, bg = 'white')
#     entity_label.pack(side = 'top', anchor = 'nw')
#     entity_label.pack_propagate(False)
#     entity_label.bind('<Button-1>', lambda event, i = index: pop_up_a(event,i))
#     entity_labels_a.append(entity_label)

# # pop up port labels OUT
# # port selection are just one at a time
# port_labels_frame_a = Frame(frame_a, bg = 'white')
# for index, port in enumerate(ports_a):
#     out_port_connections[port] = []
#     port_name = '    ' + port
#     port_label = Label(port_labels_frame_a, text = port_name, fg = 'blue', bg = 'white')
#     port_label.pack(side = 'top', anchor = 'nw')
#     port_label.pack_propagate(False)
#     port_label.bind('<Button-1>', lambda event, i = index: select_out_port(event,i))
#     port_labels_a.append(port_label)
#
# # entities B
# for index,entity in enumerate(entities):
#     label = Label(frame_b, text = entity, bg = 'white')
#     label.pack(side = 'top', anchor = 'nw')
#     label.pack_propagate(False)
#     label.bind('<Button-1>', lambda event, i = index: pop_up_b(event,i))
#     entity_labels_b.append(label)
#
# # pop up port labels IN
# # NOTE: this section of the GUI has multiple selection
# port_labels_frame_b = Frame(frame_b, bg = 'white')
# for index, port in enumerate(ports_b):
#     selected_in_ports = []
#     port_name = '    ' + port
#     port_label = Label(port_labels_frame_b, text = port_name, fg = 'blue', bg = 'white')
#     port_label.pack(side = 'top', anchor = 'nw')
#     port_label.pack_propagate(False)
#     port_label.bind('<Button-1>', lambda event, i = index: multi_select_in_port(event,i))
#     port_labels_b.append(port_label)
#     isHiglightOn = BooleanVar(root,False)
#     is_highlight_on_b.append(isHiglightOn)


# organize widgets
organize()
# execute window
root.mainloop()
