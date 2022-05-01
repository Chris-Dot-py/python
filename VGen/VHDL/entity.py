
"""
    Fixes to make:
        - remove ';' in the last port when building code to avoid VHDL syntax error [_solved_]

    Notes :
        - find a better way to handle python errors or a way to generate custom errors
"""
from pathlib import Path
import os

class Entity:
    # constants : should be saved in VHDL
    library = {'ieee' : 'library ieee;\n'}
    use = {'std_logic_1164' : 'use ieee.std_logic_1164.all;\n'}
    entity = {'open' : 'entity {name} is\n', 'end' : 'end entity;\n\n'}
    port = {'open' : '  port(\n', 'close' :'  );\n'}
    architecture = {'open' : 'architecture {name}_arch of {name} is\n', 'begin' : 'begin\n', 'end' : 'end architecture;'}
    directory = r"VHDL_codes"

    def __init__(self, entity_name, circuit_type = None):
        self.__entity_name = entity_name
        self.__vhdl_code = []
        self.__port_body = {}
        self.__number_of_inputs = 0
        self.__number_of_outputs = 0

    def get_entity_name(self):
        return self.__entity_name

    def get_ports(self):
        return self.__port_body

    def add_port(self, port):
        port_name = port.get_port_name()
        self.__port_body[port_name] = port.get_line()
        if port.get_direction() == "in" :
            self.__number_of_inputs += 1;
        elif port.get_direction() == "out":
            self.__number_of_outputs += 1;

    def remove_port(self):
        pass

    def __build_code(self, file_name = None):
        if file_name == None:
            name_placeholder = self.__entity_name
        else:
            name_placeholder = file_name

        self.__vhdl_code.append(Entity.library['ieee'])
        self.__vhdl_code.append(Entity.use['std_logic_1164'])
        self.__vhdl_code.append('\n')
        self.__vhdl_code.append(Entity.entity['open'].format(name = name_placeholder))

        if not (self.__number_of_inputs == 0 and self.__number_of_outputs == 0):
            self.__vhdl_code.append(Entity.port['open'])

            for index,line in enumerate(list(self.__port_body.values())):
                if index == len(self.__port_body) - 1:
                    tmp = line.replace(';','')
                    self.__vhdl_code.append(tmp)
                else:
                    self.__vhdl_code.append(line)

            self.__vhdl_code.append(Entity.port['close'])

        self.__vhdl_code.append(Entity.entity['end'])
        self.__vhdl_code.append(Entity.architecture['open'].format(name = name_placeholder))
        self.__vhdl_code.append(Entity.architecture['begin'])
        self.__vhdl_code.append(Entity.architecture['end'])

    def show_code(self):
        print(self.get_code())

    def get_code(self):
        if len(self.__vhdl_code) == 0:
            return 'Null'
        else:
            return ''.join([str(item) for item in self.__vhdl_code])

    def clear_code(self):
        self.__vhdl_code = []

    def generate_code(self, name = None):
        if name == None:
            fname = self.__entity_name + '.vhd'
        else:
            fname = name + '.vhd'

        complete_path = os.path.join(Entity.directory, fname)
        self.__build_code(name)

        if not self.__check_file(complete_path):
            with open(complete_path, mode = 'w') as file:
                file.write(self.get_code())
        else:
            print(f'Failed to generate code : file \'{fname}\' already exists...')

    def __check_file(self,path):
        file = Path(path)
        return file.is_file()

# print(__name__)
