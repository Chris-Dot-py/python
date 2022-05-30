from tkinter import *

global entity_labels_a, entites, ports

root = Tk()
root.title('test')
root.geometry("600x500")

entity_labels_a = []
entities = ['clk_rst','orologio','display', 'uart','scheduler','adc']
ports = []

### event functions ######################################################################
def pop_up(event, num):
    """ ------------------------------- Golden Code ---------------------------------- """
    for label in entity_labels_a:
        label.pack_forget()
        port_labels_frame.pack_forget()

    if port_labels_frame in entity_labels_a:
        if last_clicked.get() != num:
            entity_labels_a.remove(port_labels_frame)
            entity_labels_a.insert(num+1, port_labels_frame) # change pos
            last_clicked.set(num)
        else:
            entity_labels_a.remove(port_labels_frame)
    else:
        last_clicked.set(num)
        entity_labels_a.insert(num+1, port_labels_frame)

    for index,label in enumerate(entity_labels_a):
        label.pack(side = 'top', anchor = 'nw')
    """ ------------------------------------------------------------------------------ """

### GUI variables ########################################################################
last_clicked = IntVar(root,0)

### Main UI Frames #######################################################################
frame_a_label = Label(root, text = 'OUT PORTS :')
frame_a_label.grid(row = 0, column = 0, padx = 5, pady = (5,0), sticky = 'w')
frame_b_label = Label(root, text = 'IN PORTS : ')
frame_b_label.grid(row = 0, column = 2, padx = 5, pady = (5,0), sticky = 'w')

root.rowconfigure(1, weight = 1)
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 1)

border_a = Frame(root, bg = 'black',width=500,height=300)
# border_a.pack(expand = True, side = 'left', fill = 'both', padx = (5,2.5), pady = 5)
border_a.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, sticky = 'news', padx = (5,2.5), pady = 5)
frame_a = Frame(border_a, bg = 'white',width=100,height=100)
frame_a.pack(expand = True, side = 'left', fill = 'both', padx = 1, pady = 1)

border_b = Frame(root, bg = 'black',width=500,height=300)
# border_b.pack(expand = True, side = 'left', fill = 'both', padx = (2.5,5), pady = 5)
border_b.grid(row = 1, column = 2, rowspan = 4, columnspan = 2, sticky = 'news', padx = (2.5,5), pady = 5)
frame_b = Frame(border_b, bg = 'white',width=100,height=100)
frame_b.pack(expand = True, side = 'left', fill = 'both', padx = 1, pady = 1)

### Entity Labels ########################################################################

""" ---------------------------------- Golden Code ----------------------------------- """
for index,entity in enumerate(entities):
    label = Label(frame_a, text = entity)
    label.pack(side = 'top', anchor = 'nw')
    label.bind('<Button-1>', lambda event, i = index: pop_up(event,i))
    entity_labels_a.append(label)
""" ---------------------------------------------------------------------------------- """


label_b = Label(frame_b, text = 'a label')
label_b.pack(padx = 5, side = 'top', anchor = 'nw')

port_labels_frame = Frame(frame_a)
port_a1 = Label(port_labels_frame, text = '      port 1', fg = 'blue')
ports.append(port_a1)
port_a2 = Label(port_labels_frame, text = '      port 2', fg = 'blue')
ports.append(port_a2)
port_a3 = Label(port_labels_frame, text = '      port 3', fg = 'blue')
ports.append(port_a3)
for port in ports:
    port.pack(side = 'top', anchor = 'nw')

# run window
root.mainloop()
