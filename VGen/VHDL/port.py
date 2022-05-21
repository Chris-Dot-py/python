class Port:
    def __init__(self, port_name = 'port', direction = 'in', length = 1):
        self.port_name = port_name
        self.direction = direction
        self.length = length

        if type(length) == type(1):
            if self.length > 1:
                self.line = f"    {self.port_name} : {self.direction} std_logic_vector({self.length - 1} downto 0);\n"
            else:
                self.line = f"    {self.port_name} : {self.direction} std_logic;\n"
        else:
            self.line = f"    {self.port_name} : {self.direction} {length};\n"

        self.isConnected = False
        self.number_of_connections = 0
        self.connections = {}

    def connect_port(self, target_port):
        if target_port.get_direction() != self.get_direction(): # in - out | out - in
            self.connections.add(target_port)
            self.number_of_connections += 1

    def disconnect_port(self, target_port):
        self.connections.remove(target_port)
        self.number_of_connections -= 1

    def get_port_name(self):
        return self.port_name

    def get_direction(self):
        return self.direction

    def get_length(self):
        return self.length

    def get_line(self):
        return self.line

# print(__name__)
