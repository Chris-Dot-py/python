from VHDL import *
import sys

def main():
    if len(sys.argv) != 2:
        print('\nUsage : .\main.py <directory_name>\n')
    else:
        imported_entities = VGen.vimport_files(sys.argv[1])

        tb_clock = Testbench('top')

        for entity in imported_entities.values():
            tb_clock.add_component(entity)
            tb_clock.instantiate(entity)

        tb_clock.generate_code()


if __name__ == '__main__' :
    main()
