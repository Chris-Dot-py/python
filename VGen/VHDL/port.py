class Port:
    def __init__(self, port_len, port_name = 'port', direction = 'in', port_type = 'std_logic' ):
        self.__port_name = port_name
        self.__direction = direction
        self.__port_type = port_type
        self.__port_len = port_len
        self.__isConnected = False
        self.__connections = {} # {'entity_name' : Port}

        if type(self.__port_len) == type('string'): # length defined by an expression
            self.__line = f"    {self.__port_name} : {self.__direction} {self.__port_type}({port_len} downto 0);\n"
        else: # defined integer
            if port_len > 1:
                self.__line = f"    {self.__port_name} : {self.__direction} {self.__port_type}({port_len - 1} downto 0);\n"
            else:
                self.__line = f"    {self.__port_name} : {self.__direction} {self.__port_type};\n"

    def connect_port(self, target_entity, target_port):
        if target_port.get_direction() != self.get_direction(): # in - out | out - in
            self.__connections[target_entity.get_entity_name()] = target_port
        else:
            print('invalid connection')

    def disconnect_port(self,target_entity, target_port):
        self.__connections.clear()

    ### Get Methods ######################################################################
    def get_port_name(self): return self.__port_name
    def get_direction(self): return self.__direction
    def get_type(self): return self.__port_type
    def get_length(self): return self.__port_len
    def get_line(self): return self.__line
    def get_connections(self): return self.__connections

    ### functional methods ###############################################################
    def show_connections(self):
        if len(self.__connections) != 0:
            if self.__direction == 'in':
                if len(self.__connections) > 1:
                    print('CONFLICT! More than one port is connected into this input.')
                else:
                    for entity,port in self.__connections.items():
                        print(f'entity : \'{entity}\' : port : \'{port.get_port_name()}\'')
            elif self.__direction == 'out':
                for entity,port in self.__connections.items():
                    print(f'entity : \'{entity}\' : port : \'{port.get_port_name()}\'')
        else:
            print('no connections')

# print(__name__)
