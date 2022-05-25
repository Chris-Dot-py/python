class Port:
    def __init__(self, port_len, port_name = 'port', direction = 'in', port_type = 'std_logic' ):
        self.__port_name = port_name
        self.__direction = direction
        self.__port_type = port_type
        self.__port_len = port_len

        if type(self.__port_len) == type('string'): # length defined by an expression
            self.__line = f"    {self.__port_name} : {self.__direction} {self.__port_type}({port_len} downto 0);\n"
        else: # defined integer
            if port_len > 1:
                self.__line = f"    {self.__port_name} : {self.__direction} {self.__port_type}({port_len - 1} downto 0);\n"
            else:
                self.__line = f"    {self.__port_name} : {self.__direction} {self.__port_type};\n"

        self.__isConnected = False
        self.__number_of_connections = 0
        self.__connections = {}

    def connect_port(self, target_port):
        if target_port.get_direction() != self.get_direction(): # in - out | out - in
            self.__connections.add(target_port)
            self.__number_of_connections += 1

    def disconnect_port(self, target_port):
        self.__connections.remove(target_port)
        self.__number_of_connections -= 1

    def get_port_name(self):
        return self.__port_name

    def get_direction(self):
        return self.__direction

    def get_type(self):
        return self.__port_type

    def get_length(self):
        return self.__port_len

    def get_line(self):
        return self.__line

# print(__name__)
