from VHDL import *

class VGen:
    def __init__(self):
        pass

    """
        scans 1 vhd file, and saves it as an Entity object
    """
    @staticmethod
    def v_import(vfile):
        match_open = ('entity','is')
        match_end = ('end','entity')
        with open(vfile, mode = 'r') as rfile:
            done = False
            while done is not True:
                line = rfile.readline()
                if all([word in line for word in match_open]):
                    open_line = line.split()
                    entity = Entity(open_line[1])
                elif ':' in line:
                    port = line.split()
                    entity.add_port(Port(port[0],port[2],VGen.get_port_len(line)))

                elif all([word in line for word in match_end]):
                    done = True

        return entity

    @staticmethod
    def get_port_len(line):
        num = []
        numbers_found = []
        canParse = False
        foundANumber = False
        for ch in list(line):
            if ch == ':':
                canParse = True
            elif canParse is True:
                if foundANumber is not True:
                    if ch.isdigit():
                        num.append(ch)
                        foundANumber = True
                else:
                    if ch.isdigit():
                        num.append(ch)
                    else:
                        numbers_found.append(int(''.join(num)))
                        num = []
                        foundANumber = False

        if len(numbers_found) == 0:
            return 1
        else:
            return (numbers_found[0]+1) - numbers_found[1]

    def quick_test(self, clk_freq, DUT):
        pass
        # generates tb_top file with indicated clock frequency and reset
        # with a declared component and port mapped black_box clocked entity
        # if file is imported (indicated path file), declares imported file and
        # port maps it.

file = r'VHDL_codes\clock.vhd'

entity = VGen.v_import(file)
print(entity.get_entity_name())
ports = entity.get_ports()
for port_name, port in list(ports.items()):
    print(port_name)
    print(port.get_line())
