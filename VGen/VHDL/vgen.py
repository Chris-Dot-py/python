from VHDL import *
import os

class VGen:
    """
    Accpetable formats :
        entity < entity name > is
        generic(
            < val name > : < val type >;
            < val name > : < val type >
        );
          port(
            < port name > : < direction > < type >;
            < port name > : < direction > < custom type >;
            < port name > : < direction > < vector >( < expression > downto 0 )
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

        comment = []
        comments = {}

        generics_tmp = {}
        isComment = False
        maybeComment = False

        gen_comments = []
        port_comments = []

        gen_nls = 0
        port_nls = 0
        num_of_newlines = 0

        code_order = {}
        code_line = []
        print('----------------------------------')
        with open(vfile, mode = 'r') as read_file:
            while ('end' not in line):
                line = read_file.readline()
                # print(line)

                if found_entity_name is False:
                    line_list = line.split()
                    for index,item in enumerate(line_list):
                        if item.lower() == 'entity':
                            entity = Entity(line_list[index + 1])
                            found_entity_name = True
                else:
                    for ch in list(line):
                        # newline counter
                        if ch == '\n':
                            if open_brackets >= 1:
                                num_of_newlines += 1
                                code_order[str(num_of_newlines-1)] = ''.join(code_line)
                                code_line = []

                        # comment parser
                        if isComment is True:
                            if ch == '\n':
                                isComment = False
                                maybeComment = False
                                comments[str(num_of_newlines-1)] = ''.join(comment)
                                comment = []
                            else:
                                comment.append(ch)
                                code_line.append(ch)

                        elif maybeComment is True:
                            if ch == '-':
                                isComment = True
                                code_line.append(ch)
                            else:
                                maybeComment = False
                                lines.append(ch_tmp)
                                lines.append(ch)
                                code_line.append(ch_tmp)
                                code_line.append(ch)

                        elif ch == '-' and open_brackets >= 1:
                            maybeComment = True
                            ch_tmp = ch
                            code_line.append(ch)

                        # port parser
                        elif ch == '(':
                            if open_brackets == 0:
                                open_brackets += 1
                            else:
                                open_brackets += 1
                                lines.append(ch)
                                code_line.append(ch)
                        elif ch == ')':
                            if open_brackets == 1:
                                open_brackets -= 1
                                generics = ports
                                ports = ''.join(lines)
                                print(generics)
                                print(ports)

                                gen_comments = port_comments
                                port_comments = comments

                                gen_nls = port_nls
                                port_nls = num_of_newlines


                                for i,x in code_order.items():
                                    s = f'line {i} : {x}'
                                    print(s)

                                code_order = {}
                                lines = []
                                comments = {}
                                num_of_newlines = 0
                            else:
                                open_brackets -= 1
                                lines.append(ch)
                                code_line.append(ch)
                        elif open_brackets >= 1:
                            if ch != '\n':
                                lines.append(ch)
                                code_line.append(ch)



        s = f'\nentity : {entity.get_entity_name()}\n'
        print(s)
        # generics
        if len(generics) != 0:
            s = f' generics :\n{generics}'
            # print(s)
            # print(gen_comments)
            tmp = generics.split(';')
            for i,x in enumerate(tmp):
                # sss = f'{i} : {x}'
                # print(sss)
                tmp_2 = x.split()
                # print(tmp_2)
                entity.add_generics(tmp_2[0],tmp_2[2])


        # ports
        isvector = False
        vec_len = ''
        if len(ports) != 0:
            s = f' ports :\n{ports}'
            # print(s)
            # print(port_comments)

            tmp = ports.split(';')
            for i,x in enumerate(tmp):
                # sss = f'{i} : {x}'
                # print(sss)

                tmp_2 = x.split()

                port_name = tmp_2[0]
                port_dir = tmp_2[2]

                for i,y in enumerate(tmp_2):
                    if y.lower() == 'downto':
                        tmp_2[i] = y.lower()
                        isvector = True

                if isvector is True:
                    port_type = VGen.get_type(x)
                    vec_len = VGen.get_len(x)
                    if vec_len.isdigit():
                        port_len = int(vec_len) + 1
                        # print(f'length is fixed : length = {int(vec_len) + 1}')
                        s = f'{port_name} : {port_dir} {port_type}({port_len-1} downto 0)'
                    else:
                        port_len = vec_len
                        # print(f'has an expression : length_exp = {vec_len}')
                        s = f'{port_name} : {port_dir} {port_type}({port_len} downto 0)'
                    isvector = False
                    entity.add_port(Port(port_len,port_name,port_dir,port_type))


                else:
                    port_type = tmp_2[3]
                    entity.add_port(Port(1,port_name,port_dir,port_type))

                    s = f'{port_name} : {port_dir} {port_type}'

                print(s)


        return entity

    # ### Gui testing ######################################################################
    @staticmethod
    def vimport_files(list_of_files):
        entities = {}
        for file in list_of_files:
            imported_entity = VGen.vimport(file)
            entities[imported_entity.get_entity_name()] = imported_entity

        return entities

    ### Cmd prompt testing ###############################################################
    # @staticmethod
    # def vimport_files(directory_path):
    #     files = os.listdir(directory_path)
    #     path = directory_path + '/'
    #     entities = {}
    #     for file in files:
    #         file_path = path + ''.join(file)
    #         imported_entity = VGen.vimport(file_path)
    #         entities[imported_entity.get_entity_name()] = imported_entity
    #
    #     return entities


    @staticmethod
    def get_type(s):
        tmp = s.split('(')
        tmp_2 = tmp[0].split()
        return tmp_2[-1]

    @staticmethod
    def get_len(s):
        s_tmp = s
        new_string = ''
        for x in s.split():
            if x.lower() == 'downto':
                new_string = s_tmp.replace(x,x.lower())

        tmp = new_string.split('downto')
        index = tmp[0].find('(')
        tmp_list = list(tmp[0])
        tmp_list[index] = ' '
        final_string = ''.join(tmp_list)
        return_val = final_string.split()
        return return_val[-1]
