import sys
import VHDL

# contants
entity_open = "entity {} is\n"
entity_end = "end entity;\n"

# function definitions
def generate_empty_entity(entity_name):
    fname = entity_name + ".vhd"
    empty_entity = entity_open.format(entity_name) + entity_end
    with open(fname, mode = 'w') as vhdl_file:
        vhdl_file.write(empty_entity)

def is_valid_input(num_of_args):
    if num_of_args != 2:
        print('Arguments required : 2, passed : {}'.format(num_of_args))
        return False

    return True

# Main code
if is_valid_input(len(sys.argv)):
    generate_empty_entity(sys.argv[1])
