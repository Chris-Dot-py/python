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
    def vimport(vfile):
        found_entity_name = False
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

                if found_entity_name is False:
                    line_list = line.split()
                    for index,item in enumerate(line_list):
                        if item.lower() == 'entity':
                            entity = Entity(line_list[index + 1])
                            found_entity_name = True


                for ch in list(line):
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

        if len(generics) != 0:
            list_of_generics = list(generics.split(';'))
            print(list_of_generics)
            for item in list_of_generics:
                tmp = item.split()
                # print(tmp)
                entity.add_generics(tmp[0],tmp[2])

        if len(ports) != 0:
            is_std_logic_vector = False
            is_std_logic = False
            is_custom_type = False
            port_len = 0

            list_of_ports = list(ports.split(';'))
            print(list_of_ports)
            for item in list_of_ports:
                tmp = item.split()
                print(tmp)
                print(VGen.get_port_len(item))

                port_name = tmp[0]
                port_dir = tmp[2]

                entity.add_port(Port(port_name,port_dir,VGen.get_port_len(item)))

        return entity

    @staticmethod
    def vimport_files(directory_path):
        files = os.listdir(directory_path)
        path = directory_path + '/'
        entities = {}
        for file in files:
            file_path = path + ''.join(file)
            imported_entity = VGen.vimport(file_path)
            entities[imported_entity.get_entity_name()] = imported_entity

        return entities

    @staticmethod
    def get_port_len(line):
        num = []
        numbers_found = []
        canParse = False
        foundANumber = False
        for i,ch in enumerate(list(line)):
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
                        if i == len(line)-1:
                            numbers_found.append(int(''.join(num)))
                    else:
                        numbers_found.append(int(''.join(num)))
                        num = []
                        foundANumber = False

        if len(numbers_found) == 0:
            return 1
        else:
            return (numbers_found[0]+1) - numbers_found[1]
