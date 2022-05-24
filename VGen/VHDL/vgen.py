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
                    if ch == '(':
                        if open_brackets == 0:
                            open_brackets += 1
                        else:
                            open_brackets += 1
                            lines.append(ch)
                    elif ch == ')':
                        if open_brackets == 1:
                            open_brackets -= 1
                            generics = ports
                            ports = ''.join(lines)
                            lines = []
                            # print(ports)
                        else:
                            open_brackets -= 1
                            lines.append(ch)
                    elif open_brackets >= 1:
                        lines.append(ch)

        s = f'entity : {entity.get_entity_name()}\n'
        print(s)
        if len(generics) != 0:
            s = f' generics :\n{generics}'
            print(s)

        if len(ports) != 0:
            s = f' ports :\n{ports}'
            print(s)


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
    def get_port_len(s):
        num = []
        nums_found = []
        num_found = False

        for ch in list(s):
            if num_found is False:
                if ch.isdigit():
                    num.append(ch)
                    num_found = True
                    # print(ch)
            else:
                if ch.isdigit():
                    num.append(ch)
                    # print(ch)
                else:
                    nums_found.append(int(''.join(num)))
                    num_found = False
                    num = []
                    # print(nums_found)

        if len(nums_found) != 0:
            return (nums_found[0] + 1) - nums_found[1];
        else:
            return 1;
