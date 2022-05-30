from tkinter import *

global entity_labels_a, entites, ports_a, ports_b

root = Tk()
root.title('test')
root.geometry("600x500")

entities = ['clk_rst','orologio','display', 'uart','scheduler','adc']
ports_a = ['port_1','port_2','port_3'] # OUT PORTS
ports_b = ['port_1','port_2','port_3'] # IN PORTS
entity_labels_a = [] # OUT
port_labels_a = []
entity_labels_b = [] # IN
port_labels_b = []

### event functions ######################################################################
def pop_up_a(event, num):
    """ ------------------------------- Golden Code ---------------------------------- """
    for label in entity_labels_a:
        label.pack_forget()
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

    for index,label in enumerate(entity_labels_a):
        label.pack(side = 'top', anchor = 'nw')
    """ ------------------------------------------------------------------------------ """

def pop_up_b(event, num):
    """ ------------------------------- Golden Code ---------------------------------- """
    for label in entity_labels_b:
        label.pack_forget()
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

    for index,label in enumerate(entity_labels_b):
        label.pack(side = 'top', anchor = 'nw')
    """ ------------------------------------------------------------------------------ """


### GUI variables ########################################################################
clicked_port = BooleanVar(root, False)
last_clicked_port = IntVar(root,0)
last_clicked_entity = IntVar(root,0)

### Main UI widgets ######################################################################
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
border_a.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, sticky = 'news', padx = (5,2.5), pady = 5)
frame_a = Frame(border_a, bg = 'white',width=100,height=100)
frame_a.pack(expand = True, side = 'left', fill = 'both', padx = 1, pady = 1)

border_b = Frame(root, bg = 'black',width=500,height=300)
border_b.grid(row = 1, column = 2, rowspan = 4, columnspan = 2, sticky = 'news', padx = (2.5,5), pady = 5)
frame_b = Frame(border_b, bg = 'white',width=100,height=100)
frame_b.pack(expand = True, side = 'left', fill = 'both', padx = 1, pady = 1)

# buttons
generate_button = Button(root, text = 'Generate')
generate_button.grid(row = 5, column = 0, columnspan = 2, padx = (5,2.5), pady = 5, sticky = 'news')
done_button = Button(root, text = 'Done', command = quit)
done_button.grid(row = 5, column = 2, columnspan = 2, padx = (2.5,5), pady = 5, sticky = 'news')

### Entity Labels ########################################################################
""" ---------------------------------- Golden Code ----------------------------------- """
# entities A
for index,entity in enumerate(entities):
    label = Label(frame_a, text = entity, bg = 'white')
    label.pack(side = 'top', anchor = 'nw')
    label.bind('<Button-1>', lambda event, i = index: pop_up_a(event,i))
    entity_labels_a.append(label)

# pop up port labels OUT
port_labels_frame_a = Frame(frame_a, bg = 'white')
for index, port in enumerate(ports_a):
    port_name = '    ' + port
    port_label = Label(port_labels_frame_a, text = port_name, fg = 'blue', bg = 'white')
    port_label.pack(side = 'top', anchor = 'nw')
    # port_label.bind('<Button-1>', lambda event, i = index: highlight_a(event,i))
    port_labels_a.append(label)

# entities B
for index,entity in enumerate(entities):
    label = Label(frame_b, text = entity, bg = 'white')
    label.pack(side = 'top', anchor = 'nw')
    label.bind('<Button-1>', lambda event, i = index: pop_up_b(event,i))
    entity_labels_b.append(label)

# pop up port labels IN
port_labels_frame_b = Frame(frame_b, bg = 'white')
for index, port in enumerate(ports_b):
    port_name = '    ' + port
    label = Label(port_labels_frame_b, text = port_name, fg = 'blue', bg = 'white')
    label.pack(side = 'top', anchor = 'nw')
""" ---------------------------------------------------------------------------------- """

# run window
root.mainloop()
