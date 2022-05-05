"""
    ttk must be used to create this button and NOT tk!

    grid(row = __ , column = __) defines where the content is placed in a grid style layout

    sticky locks a content into a side:
    - W (west) = left
    - N (North) = up
    - E (East) = right
    - S (soouth) = down

    Label : prints normal text
    Entry : text input box
    button : a button that can be associated with a function
    bind : print a value
"""
from tkinter import *
from tkinter import ttk
from VHDL import *

def printEntity():
    message = ttk.Label(root, text = entity_name.get())
    message.grid(row = 1, column = 1)

root  = Tk() # root window instantiation
root.title("VGen") # window title
root.geometry("300x150") # window size
# root.resizable(False,False) # x and y direction of window not resizable
# root.configure(background = "blue") # set background
entity_name_label = ttk.Label(root, text = "Entity name : ")
entity_name_label.grid(row = 0, column = 0 )

entity_name = StringVar()
entity_name_entry = Entry(root, width = 12, textvariable = printEntity)
entity_name_entry.grid(row = 0, column = 1)


add_port_button = ttk.Button(text = "app port", command = printEntity) # create a button
add_port_button.grid(row = 2 , column = 0) # place a row 0 column 0

generate_button = ttk.Button(text = "generate", command = printEntity) # create a button
generate_button.grid(row = 2, column = 1, pady = 20) # place a row 0 column 0


if __name__ == '__main__':
    root.mainloop()
