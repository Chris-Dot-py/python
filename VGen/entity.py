"""
    Fixes to make:
        - remove ';' in the last port when building code to avoid VHDL syntax error 
"""

import os

class Entity:
    # constants : should be saved in VHDL
    library = {'ieee' : 'library ieee;\n'}
    use = {'std_logic_1164' : 'use ieee.std_logic_1164.all;\n'}
    entity = {'open' : 'entity {name} is\n', 'end' : 'end entity;\n\n'}
    port = {'open' : '  port(\n', 'close' :'  );\n'}
    architecture = {'open' : 'architecture {name}_arch of {name} is\n', 'begin' : 'begin\n', 'end' : 'end architecture;'}

    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.vhdl_code = []
        self.port_body = {}
        self.number_of_inputs = 0
        self.number_of_outputs = 0
        self.combined = False

    def get_entity_name(self):
        return self.entity_name

    def get_ports(self):
        return self.port_body

    def add_port(self, port):
        port_name = port.get_port_name()
        self.port_body[port_name] = port.get_line()
        if port.get_direction() == "in" :
            self.number_of_inputs += 1;
        elif port.get_direction() == "out":
            self.number_of_outputs += 1;

    def remove_port(self):
        pass

    def build_code(self):
        self.vhdl_code.append(Entity.library['ieee'])
        self.vhdl_code.append(Entity.use['std_logic_1164'])
        self.vhdl_code.append('\n')
        self.vhdl_code.append(Entity.entity['open'].format(name = self.entity_name))
        if not (self.number_of_inputs == 0 and self.number_of_outputs == 0):
            self.vhdl_code.append(Entity.port['open'])
            for line in list(self.port_body.values()):
                self.vhdl_code.append(line)
            self.vhdl_code.append(Entity.port['close'])
        self.vhdl_code.append(Entity.entity['end'])
        self.vhdl_code.append(Entity.architecture['open'].format(name = self.entity_name))
        self.vhdl_code.append(Entity.architecture['begin'])
        self.vhdl_code.append(Entity.architecture['end'])
        self.combined = True

    def show_code(self):
        preview = self.combine_code()
        print(preview)
        if not self.combined:
            print("\nCombined status : False")
        else:
            print("\nCombined status : True")

    def combine_code(self):
        return ''.join([str(item) for item in self.vhdl_code])

    def clear_code(self):
        self.vhdl_code = []
        self.combined = False

    def generate_code(self,path,entity_name):
        fname = entity_name + '.vhd'
        complete_path = os.path.join(path, fname)
        with open(complete_path, mode = 'w') as file:
            if self.combined:
                file.write(self.combine_code())
            else:
                self.build_code()
                file.write(self.combine_code())

class Port:
    def __init__(self, port_name = 'port', direction = 'in', length = 1):
        self.port_name = port_name
        self.direction = direction
        self.length = length
        if self.length > 1:
            self.line = f"    {self.port_name} : {self.direction} std_logic_vector({length - 1} downto 0);\n"
        else:
            self.line = f"    {self.port_name} : {self.direction} std_logic;\n"

    def get_port_name(self):
        return self.port_name

    def get_direction(self):
        return self.direction

    def get_length(self):
        return self.length

    def get_line(self):
        return self.line

clock = Entity('clock')
clock_ports = Port()
clock.add_port(Port('clk','in',1))
clock.add_port(Port('rsgn','in',1))
clock.add_port(Port('seconds','out',6))
clock.add_port(Port('minutes','out',6))
clock.add_port(Port('hours','out',5))


clock.build_code()
clock.show_code()
directory = r"C:\Users\Christian\Desktop\Python\python\VGen"
clock.generate_code(directory,clock.get_entity_name())
