import sys
import VHDL

# constants : should be saved in VHDL
library = {'ieee' : 'library ieee;\n'}
use = {'std_logic_1164' : 'use ieee.std_logic_1164.all;\n'}
entity = {'open' : 'entity {name} is\n', 'end' : 'end entity;\n'}
architecture = {'open' : 'architecture {name}_arch of {name} is\n', 'begin' : 'begin\n', 'end' : 'end architecture;'}

# function definitions
def generate_code(entity_name, vhdl_code):
    fname = entity_name + ".vhd"
    with open(fname, mode = 'w') as vhdl_file:
        vhdl_file.write(vhdl_code)

def empty_code(entity_name):
    entity_code = entity['open'].format(name = entity_name) + entity['end'] + '\n'
    architecture_code = architecture['open'].format(name = entity_name) + architecture['begin'] + architecture['end']
    vhdl_code = library['ieee'] + use['std_logic_1164'] + '\n' + entity_code + architecture_code
    return vhdl_code

def is_valid_input(num_of_args):
    if num_of_args != 3:
        print('# Invalid Arguments\n   Arguments required : 3, passed : {}'.format(num_of_args))
        return False

    return True

# Main code
if is_valid_input(len(sys.argv)):
    entity_name = sys.argv[1]
    vhdl_code = ''
    if sys.argv[2] == 'e':
        vhdl_code = empty_code(entity_name)

        generate_code(entity_name, vhdl_code) # temporary

    elif sys.argv[2] == 'tb':
        tb_name = 'tb_' + entity_name
        entity_name = tb_name
        vhdl_code = empty_code(entity_name)

        generate_code(entity_name, vhdl_code) # temporary

    elif sys.argv[2] == 'io':
        print('Function unavailable...')
    elif sys.argv[2] == 'ii':
        print('Function unavailable...')
    elif sys.argv[2] == 'oo':
        print('Function unavailable...')
    else:
        print('Usage : \n'\
                + '  ' + sys.argv[0] + ' <entity_name> <code_type>\n\nCode types :\n'\
                + '  e - empty\n'\
                + '  tb - testbench\n'\
                + '  io - in and out\n'\
                + '  ii - input only\n'\
                + '  oo - output only\n')
