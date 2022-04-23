import sys
import VHDL

# constants : should be saved in VHDL
library = {'ieee' : 'library ieee;\n'}
use = {'std_logic_1164' : 'use ieee.std_logic_1164.all;\n'}
entity = {'open' : 'entity {name} is\n', 'end' : 'end entity;\n'}
architecture = {'open' : 'architecture {name}_arch of {name} is\n', 'begin' : 'begin\n', 'end' : 'end architecture;'}

# function definitions
def generate_empty_entity(entity_name):
    fname = entity_name + ".vhd"
    entity_code = entity['open'].format(name = entity_name) + entity['end'] + '\n'
    architecture_code = architecture['open'].format(name = entity_name) + architecture['begin'] + architecture['end']

    vhdl_code = library['ieee'] + use['std_logic_1164'] + '\n' + entity_code + architecture_code
    with open(fname, mode = 'w') as vhdl_file:
        vhdl_file.write(vhdl_code)

def is_valid_input(num_of_args):
    if num_of_args != 2:
        print('Arguments required : 2, passed : {}'.format(num_of_args))
        return False

    return True

# Main code
if is_valid_input(len(sys.argv)):
   generate_empty_entity(sys.argv[1])
