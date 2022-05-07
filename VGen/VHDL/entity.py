
"""
    Fixes to make:
        - remove ';' in the last port when building code to avoid VHDL syntax error [_solved_]

    Notes :
        - find a better way to handle python errors or a way to generate custom errors
            (see try-except)
"""
from pathlib import Path
from .port import Port
import os

class Entity:
    # constants : should be saved in VHDL
    library      = {'ieee'  :           'library ieee;\n'}
    use          = {'std_logic_1164' :  'use ieee.std_logic_1164.all;\n'}

    entity       = {'open'  :           'entity {name} is\n',
                    'end'   :           'end entity {name};\n\n'}

    port         = {'open'  :           '  port(\n',
                    'end'   :           '  );\n'}

    component    = {'open'  :           '  component {name} is\n',
                    'end'   :           '  end component {name};\n\n'}

    instance     = {'open'  :           '  {i_name} : {e_name}\n'\
                                        '  port map(\n',
                    'map'   :           '    {i_port} => {connect_to},\n',
                    'end'   :           '  );\n\n'}

    architecture = {'open'  :           'architecture {name}_arch of {name} is\n\n',
                    'begin' :           'begin\n\n',
                    'end'   :           'end architecture;\n'}
    directory    = r"VHDL_codes"

    def __init__(self, entity_name, circuit_type = None):
        self.__entity_name = entity_name
        self.__vhdl_code = []
        self.__port_body = {} # dictionary, associate port name with port lines
        self.__number_of_inputs = 0
        self.__number_of_outputs = 0
        # {"entity_name" : (Entity, instances)}
        self.__components = {} # dictionary of entities
        self.__isPrimitive = True # if True, no need for component declarations or instantiations

    def get_entity_name(self):
        return self.__entity_name

    def get_ports(self):
        return self.__port_body

    def get_code(self):
        if len(self.__vhdl_code) == 0:
            return 'Null'
        else:
            return ''.join([str(item) for item in self.__vhdl_code])

    def add_port(self, port):
        port_name = port.get_port_name()
        self.__port_body[port_name] = port.get_line()
        if port.get_direction() == "in" :
            self.__number_of_inputs += 1;
        elif port.get_direction() == "out":
            self.__number_of_outputs += 1;

    def get_component(self,entity):
        if entity.get_entity_name() in list(self.__components.keys()):
            entity_name = entity.get_entity_name()
            comp,instances = self.__components[entity_name]
            return comp


    # returns a list of tuple pairs entity,instances
    def get_components(self):
        return self.__components.values()

    """
        Can add the import function to this
    """
    def add_ports(self, num_of_inputs = 1, num_of_outputs = 1):
        for i in range(num_of_inputs):
            self.add_port(Port(f'input_{i}','in',1))
            self.__number_of_inputs += 1

        for i in range(num_of_outputs):
            self.add_port(Port(f'output_{i}','out',1))
            self.__number_of_outputs += 1

    def add_component(self, entity):
        entity_name = entity.get_entity_name()
        self.__components[entity_name] = entity,0


    def instantiate(self,entity, num_of_instances = 0):
        if entity.get_entity_name() in list(self.__components.keys()):
            comp, instances = self.__components[entity.get_entity_name()]

            if num_of_instances == 0:
                N = instances + 1
            else:
                N = instances + num_of_instances

            self.__components[entity.get_entity_name()] = comp,N
        #     print("instantiated!")
        else:
            print('component hasn\'t been declared')

    def remove_port(self):
        pass

    def add_line(self, s):
        self.__vhdl_code.append(s)

    def __build_code(self, file_name = None):
        if file_name == None:
            name_placeholder = self.__entity_name
        else:
            name_placeholder = file_name

        self.add_line(Entity.library['ieee'])
        self.add_line(Entity.use['std_logic_1164'])
        self.add_line('\n')
        self.add_line(Entity.entity['open'].format(name = name_placeholder))

        if not (self.__number_of_inputs == 0 and self.__number_of_outputs == 0):
            self.add_line(Entity.port['open'])

            for index,line in enumerate(list(self.__port_body.values())):
                if index == len(self.__port_body) - 1:
                    tmp = line.replace(';','')
                    self.add_line(tmp)
                else:
                    self.add_line(line)

            self.add_line(Entity.port['end'])

        self.add_line(Entity.entity['end'].format(name = self.get_entity_name()))

        self.add_line(Entity.architecture['open'].format(name = name_placeholder))

        if len(self.__components) != 0:
            for comp_name,(comp,instances) in self.__components.items():
                self.add_line(Entity.component['open'].format(name = comp_name))

                tmp_comp = comp.get_ports()
                if len(tmp_comp) != 0:  # skip if no ports
                    self.add_line(Entity.port['open'])

                for index,line in enumerate(list(tmp_comp.values())):
                    if index == len(tmp_comp) - 1:
                        tmp_line = line.replace(';','')
                        self.add_line(tmp_line)
                    else:
                        self.add_line(line)

                if len(tmp_comp) != 0:  # skip if no ports
                    self.add_line(Entity.port['end'].format(name = comp_name))

                self.add_line(Entity.component['end'].format(name = comp_name))

        self.add_line(Entity.architecture['begin'])

        # instantiations
        for comp_name,(component,instances) in list(self.__components.items()):
            tmp_port_body = component.get_ports()
            if len(tmp_port_body) != 0:
                if instances != 0:
                    for i in range(instances):
                        self.add_line(Entity.instance['open'].format(i_name = f'{comp_name}_{i}_i', e_name = comp_name))

                        for index,port_name in enumerate(list(tmp_port_body.keys())):

                            if index == len(tmp_port_body) - 1:
                                tmp = Entity.instance['map'].format(i_port = port_name, connect_to = 'open')
                                self.add_line(tmp.replace(',',''))
                            else:
                                self.add_line(Entity.instance['map'].format(i_port = port_name, connect_to = 'open'))

                        self.add_line(Entity.instance['end'])

                        print(f"{comp_name}_{i}_i instanced!")

        self.add_line(Entity.architecture['end'])

    def show_code(self):
        print(self.get_code())

    def show_components(self):
        print(f"\nDeclared components :\n")
        for component,instances in self.__components.values():
            s = f' {component.get_entity_name()}, {instances} instances'
            print(s)
        print('')

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
