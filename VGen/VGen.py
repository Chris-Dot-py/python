from VHDL import *

def main():

    clock = Entity('clock')
    clock.add_port(Port('clk','in',1))
    clock.add_port(Port('rsgn','in',1))
    clock.add_port(Port('seconds','out',6))
    clock.add_port(Port('minutes','out',6))
    clock.add_port(Port('hours','out',5))
    clock.add_port(Port('dummy_port','out',16))

    tb_clock = Testbench(clock)
    clk_gen = Testbench('master_clk')

    clock.generate_code()
    tb_clock.generate_code()
    clk_gen.generate_code()

    tb_clock.quick_test()
    clk_gen.quick_test()

    # # idea number 1 : generates a tb file and a clocked entity
    # DUT = Entity('insert_vhd_file_path')
    # black_box.generate_code()
    #
    # black_box.quick_test() # should be a VGen object

if __name__ == '__main__' :
    # print(__name__)
    main()

# # temporary
# class VGen(): # should go study generators, might help
#     def __init__(self):
#         pass
#
#     def quick_test(self, clk_freq, DUT):
#         pass
#         # generates tb_top file with indicated clock frequency and reset
#         # with a declared component and port mapped black_box clocked entity
#         # if file is imported (indicated path file), declares imported file and
#         # port maps it.
