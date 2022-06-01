from tkinter import *

root = Tk()
root.title('test')
root.geometry("600x500")

entities = ['clk_rst','orologio','display', 'uart','scheduler','adc']
ports_a = ['port_1','port_2','port_3'] # OUT PORTS
ports_b = ['inport_1','inport_2','inport_3'] # IN PORTS

### GUI variables ########################################################################
entity_labels_a = [] # OUT
port_labels_a = []
entity_labels_b = [] # IN
port_labels_b = []
"""
    netlist = {
        # entity
        'entity_name' : [
            Port_1,
            Port_2,
            ...
            Port_N
        ]

    }

 """
netlist = {} # {'Entity name' : [Port, .., Port]}

selected_out_port = StringVar(root)
selected_in_port = ''
out_port_connections = {}
selected_in_ports = []
is_highlight_on_a = BooleanVar(root, False)
is_highlight_on_b = []
last_clicked_port = IntVar(root,0)
last_clicked_entity = IntVar(root,0)

### event functions ######################################################################
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
# entities A
for index,entity in enumerate(entities):
    netlist[entity] = {}
    entity_label = Label(frame_a, text = entity, bg = 'white')
    entity_label.pack(side = 'top', anchor = 'nw')
    entity_label.bind('<Button-1>', lambda event, i = index: pop_up_a(event,i))
    entity_labels_a.append(entity_label)

# pop up port labels OUT
# port selection are just one at a time
port_labels_frame_a = Frame(frame_a, bg = 'white')
for index, port in enumerate(ports_a):
    out_port_connections[port] = []
    port_name = '    ' + port
    port_label = Label(port_labels_frame_a, text = port_name, fg = 'blue', bg = 'white')
    port_label.pack(side = 'top', anchor = 'nw')
    port_label.bind('<Button-1>', lambda event, i = index: select_out_port(event,i))
    port_labels_a.append(port_label)

# entities B
for index,entity in enumerate(entities):
    label = Label(frame_b, text = entity, bg = 'white')
    label.pack(side = 'top', anchor = 'nw')
    label.bind('<Button-1>', lambda event, i = index: pop_up_b(event,i))
    entity_labels_b.append(label)

# pop up port labels IN
# NOTE: this section of the GUI has multiple selection
port_labels_frame_b = Frame(frame_b, bg = 'white')
for index, port in enumerate(ports_b):
    selected_in_ports = []
    port_name = '    ' + port
    port_label = Label(port_labels_frame_b, text = port_name, fg = 'blue', bg = 'white')
    port_label.pack(side = 'top', anchor = 'nw')
    port_label.bind('<Button-1>', lambda event, i = index: multi_select_in_port(event,i))
    port_labels_b.append(port_label)
    isHiglightOn = BooleanVar(root,False)
    is_highlight_on_b.append(isHiglightOn)

# run window
root.mainloop()
