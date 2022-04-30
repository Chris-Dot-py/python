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

# print(__name__)
