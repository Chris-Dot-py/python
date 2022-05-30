from tkinter import *

global entity_labels_a

root = Tk()
root.title('test')
root.geometry("600x500")

entity_labels_a = []

### event functions ######################################################################
def pop_up(event, num):
    for label in entity_labels_a:
        label.pack_forget()

    if pop_label_a in entity_labels_a:
        if last_clicked.get() != num:
            entity_labels_a.remove(pop_label_a)
            entity_labels_a.insert(num+1, pop_label_a) # change pos
            last_clicked.set(num)
        else:
            entity_labels_a.remove(pop_label_a)
    else:
        last_clicked.set(num)
        entity_labels_a.insert(num+1, pop_label_a)

    for label in entity_labels_a:
        label.pack(side = 'top', anchor = 'nw')

### GUI variables ########################################################################
clicked = BooleanVar(root, False)
click_event = BooleanVar(root, False)
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
label_a1 = Label(frame_a, text = 'a label')
entity_labels_a.append(label_a1)
label_a1.bind('<Button-1>', lambda x : pop_up('<Button-1>',0))

label_a2 = Label(frame_a, text = 'also label')
entity_labels_a.append(label_a2)
label_a2.bind('<Button-1>', lambda x : pop_up('<Button-1>',1))
#
for label in entity_labels_a:
    label.pack(side = 'top', anchor = 'nw')

label_b = Label(frame_b, text = 'a label')
label_b.pack(padx = 5, side = 'top', anchor = 'nw')

pop_label_a = Label(frame_a, text = '      popped text', fg = 'blue')

# run window
root.mainloop()
