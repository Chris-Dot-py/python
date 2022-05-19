from VHDL import *
import os

class VGen:
    """
    line formats:
        entity < entity name > is
          port(
            < port name > : < direction > std_logic;
            < port name > : < direction > std_logic_vector( N - 1 downto 0 );
          );
        end entity < entity name >;
    """
    default_path = r'VHDL_codes'

    """
        step 1 : search for entity name
        step 2 : check if has generics
            step 2.1 : if has generics, parse generics
        step 3 : check if has ports
            step 3.1 : if has ports, parse ports, else do not import
        step 4 : search for "end entity"
    """
    @staticmethod
    def v_import(vfile):
        open_brackets = 0
        step_one_done = False
        hasGenerics = False
        isComment = False
        generics = ''
        ports = ''
        line = ''
        lines = []
        with open(vfile, mode = 'r') as read_file:
            while ('end' not in line):
                line = read_file.readline()
                # print(line)
                if 'entity' in line and 'is' in line:
                    # print(line)
                    tmp = line.split()
                    entity = Entity(tmp[1])
                    # print(entity.get_entity_name())

                for ch in list(line):
                    # print(ch)
                    if isComment is True:
                        if ch == '\n':
                            isComment = False
                    elif ch == '-':
                        isComment = True # needed to filter out comments
                    elif ch == '(':
                        open_brackets += 1
                        if open_brackets > 1:
                            lines.append(ch)
                    elif (ch == ';') and (open_brackets == 0):
                        step_one_done = True
                    elif (ch == ')') and (open_brackets == 1):
                        open_brackets -= 1
                        generics = ports
                        ports = ''.join(lines)
                        print(ports)
                        lines = []
                    elif ch == ')':
                        open_brackets -= 1
                        lines.append(ch)
                    elif open_brackets != 0:
                        lines.append(ch)


        # print(ports.split(';'))
        #
        # if hasGenerics is True:
        #     pass
        if len(generics) != 0:
            list_of_generics = list(generics.split(';'))
            for item in list_of_generics:
                tmp = item.split()
                entity.add_generics(tmp[0],tmp[2])

        # print(entity.get_generics())

        if len(ports) != 0:
            list_of_ports = list(ports.split(';'))
            for item in list_of_ports:
                tmp = item.split()
                entity.add_port(Port(tmp[0],tmp[2],VGen.get_port_len(item)))

        # ports_gotten = entity.get_ports()
        # for item_name,item in ports_gotten.items():
        #     s = f'port name : {item_name}\nport line : {item.get_line()}\n'
        #     print(s)
        return entity

    @staticmethod
    def v_import_files(directory_path):
        files = os.listdir(directory_path)
        path = directory_path + '/'
        entities = {}
        for file in files:
            file_path = path + ''.join(file)
            imported_entity = VGen.v_import(file_path)
            entities[imported_entity.get_entity_name()] = imported_entity

        return entities

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
#
# file = r'VHDL_codes\clock.vhd'
#
# entity = VGen.v_import(file)
# print(entity.get_entity_name())
# ports = entity.get_ports()
# for port_name, port in list(ports.items()):
#     print(port_name)
#     print(port.get_line())

# imported_entities = VGen.v_import_files(VGen.default_path)
#
# for name,enti in imported_entities.items():
#     print(enti.get_entity_name())
