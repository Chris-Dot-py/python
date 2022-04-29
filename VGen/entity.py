class Entity:
    # constants : should be saved in VHDL
    library = {'ieee' : 'library ieee;\n'}
    use = {'std_logic_1164' : 'use ieee.std_logic_1164.all;\n'}
    entity = {'open' : 'entity {name} is\n', 'end' : 'end entity;\n\n'}
    port = {'open' : '  port(\n  ', 'close' :'  );\n'}
    architecture = {'open' : 'architecture {name}_arch of {name} is\n', 'begin' : 'begin\n', 'end' : 'end architecture;'}

    def __init__(self, entity_name):
        self.entity_name = entity_name
        self.vhdl_code = []
        self.port_body = []
        self.number_of_inputs = 0
        self.number_of_outputs = 0

    def set_number_of_inputs(self):
        pass

    def set_number_of_outputs(self):
        pass

    def build(self):
        pass

    def add_port(self, port):
        self.port_body.append(port)
        if port.get_direction() == "in" :
            self.number_of_inputs += 1;
        elif port.get_direction() == "out":
            self.number_of_outputs += 1;

    def remove_port(self):
        pass

    def get_ports(self):
        return self.port_body

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



clk = Port('clk', 'in',1)
print(clk.get_line())

byte_in = Port('byte_in','in',8)
print(byte_in.get_line())

clock = Entity('clock')
clock.add_port(clk)
mylist = clock.get_ports()
print(mylist[0].get_line())
