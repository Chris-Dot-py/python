from VHDL import *
import sys

def main():
    if len(sys.argv) != 2:
        print('\nUsage : .\main.py <directory_name>\n')
    else:
        imported_entities = VGen.vimport_files(sys.argv[1])

        tb = Testbench('top')

        for entity in imported_entities.values():
            tb.add_component(entity)
            tb.instantiate(entity)

        tb.generate_code()


if __name__ == '__main__' :
    main()
