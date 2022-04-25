import sys
import VHDL
from pathlib import Path

# constants : should be saved in VHDL
library = {'ieee' : 'library ieee;\n'}
use = {'std_logic_1164' : 'use ieee.std_logic_1164.all;\n'}
entity = {'open' : 'entity {name} is\n', 'end' : 'end entity;\n\n'}
port = {'open' : '  port(\n  ', 'close' :'  );\n'}
architecture = {'open' : 'architecture {name}_arch of {name} is\n', 'begin' : 'begin\n', 'end' : 'end architecture;'}

# function definitions
def generate_code(entity_name, vhdl_code):
    fname = entity_name + ".vhd"
    with open(fname, mode = 'w') as vhdl_file:
        vhdl_file.write(vhdl_code)

def empty_code(entity_name):
    entity_code = entity['open'].format(name = entity_name) + entity['end']
    architecture_code = architecture['open'].format(name = entity_name) + architecture['begin'] + architecture['end']
    vhdl_code = library['ieee'] + use['std_logic_1164'] + '\n' + entity_code + architecture_code
    return vhdl_code

def in_and_out_code(entity_name, num_of_inputs = 1, num_of_outputs = 1):
    # using list because strings are immutable
    in_port = []
    out_port = []
    entity_code = [entity['open'].format(name = entity_name) + port['open']]

    for i in range(num_of_inputs):
        if i == 0:
            in_port = (f'  input_{i} : in std_logic;\n')
        else:
            in_port = (f'    input_{i} : in std_logic;\n')

        entity_code.append(''.join(in_port))

    for i in range(num_of_outputs):
        if i == (num_of_outputs-1):
            out_port = (f'    output_{i} : out std_logic\n')
        else:
            out_port = (f'    output_{i} : out std_logic;\n')

        entity_code.append(''.join(out_port))

    entity_code.append(port['close'])
    entity_code.append(entity['end'])
    final_entity_code = ''.join(str(item) for item in entity_code)
    architecture_code = architecture['open'].format(name = entity_name) + architecture['begin'] + architecture['end']
    vhdl_code = library['ieee'] + use['std_logic_1164'] + '\n' + final_entity_code + architecture_code
    return vhdl_code

def is_valid_input(num_of_args):
    if num_of_args != 3:
        print('# Invalid Arguments\n   Arguments required : 3, passed : {}'.format(num_of_args))
        return False
    return True

# returns true if file exists, otherwise returns false
def check_file(entity_name):
    fname = entity_name + '.vhd'

    if sys.argv[2] == 'tb':
        tb_fname = 'tb_' + fname
        tb_file = Path(tb_fname)
        return (tb_file.is_file())
    else:
        file = Path(fname)
        return (file.is_file())

# MAIN CODE
if is_valid_input(len(sys.argv)):
    entity_name = sys.argv[1]
    vhdl_code = '' # empty file

    if not check_file(entity_name): # check if file exist
        if sys.argv[2] == 'e':
            vhdl_code = empty_code(entity_name)

            generate_code(entity_name, vhdl_code) # temporary

        elif sys.argv[2] == 'tb':
            tb_name = 'tb_' + entity_name
            entity_name = tb_name
            vhdl_code = empty_code(entity_name)

            generate_code(entity_name, vhdl_code) # temporary

        elif sys.argv[2] == 'io':
            num_of_inputs = int(input('Number of inputs : '))
            num_of_outputs = int(input('Number of outputs : '))
            vhdl_code = in_and_out_code(entity_name,num_of_inputs,num_of_outputs)
            generate_code(entity_name, vhdl_code) # temporary

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
    else:
        if sys.argv[2] == 'tb':
            print('The file \'' + 'tb_' + sys.argv[1] + '.vhd\'' + ' already exists...')
        else:
            print('The file \'' + sys.argv[1] + '.vhd\'' + ' already exists...')
