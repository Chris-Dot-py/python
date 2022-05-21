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
                        # print(ports)
                        lines = []
                    elif ch == ')':
                        open_brackets -= 1
                        lines.append(ch)
                    elif open_brackets != 0:
                        lines.append(ch)

        if len(generics) != 0:
            list_of_generics = list(generics.split(';'))
            # print(list_of_generics)
            for item in list_of_generics:
                tmp = item.split()
                # print(tmp)
                entity.add_generics(tmp[0],tmp[2])
        """
            each port declaration has 4 items:
                1) port name
                2) semi-colon ':'
                3) port direction
                4) port type
        """
        if len(ports) != 0:
            port_name = ''
            port_dir = ''
            port_type = ''
            port_len = 0
            s = ''

            list_of_ports = list(ports.split(';'))
            # print(list_of_ports)
            for item in list_of_ports:
                tmp = item.split()
                # print(tmp)

                port_name = tmp[0]
                port_dir = tmp[2]
                port_type = ''.join(tmp[3:])

                for x in list(tmp):
                    if x.lower() == 'downto': # if this is true, its a bit vector
                        # print(VGen.get_port_len(port_type))
                        s = f'  {port_name} : {port_dir} std_logic_vector({VGen.get_port_len(port_type) - 1} downto 0);\n'
                        port_type = VGen.get_port_len(port_type)
                        break
                    elif x.lower() == 'std_logic':
                        s = f'  {port_name} : {port_dir} std_logic;\n'
                        port_type = 1
                        break
                    else:
                        s = f'  {port_name} : {port_dir} {port_type};\n'

                print(s)
                entity.add_port(Port(port_name,port_dir,port_type))


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
