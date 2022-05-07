from VHDL import *

def main():

    clock = Entity('clock') # entry

    # button commands
    clock.add_port(Port('clk','in',1))
    clock.add_port(Port('rsgn','in',1))
    clock.add_port(Port('seconds','out',6))
    clock.add_port(Port('minutes','out',6))
    clock.add_port(Port('hours','out',5))
    clock.add_port(Port('dummy_port','out',16))

    tb_clock = Testbench(clock)
    tb_clock.generate_code()
    clk_gen = Testbench('master_clk')

    test_block = Entity('test_block')
    test_block.add_ports(14,10)
    test_block.generate_code()

    dummy_block = Entity('dummy_block')
    dummy_block.add_ports(2,4)
    dummy_block.generate_code()

    clock.add_component(test_block)
    clock.add_component(tb_clock)
    clock.add_component(dummy_block)
    # button generate command
    clk_gen.generate_code()

    tb_clock.quick_test()
    clk_gen.quick_test()

    clock.show_components()
    clock.instantiate(tb_clock)
    clock.show_components()
    clock.instantiate(tb_clock,3)
    clock.instantiate(dummy_block,3)
    clock.show_components()


    clock.generate_code()

    # # idea number 1 : generates a tb file and a clocked entity
    # DUT = Entity('insert_vhd_file_path')
    # black_box.generate_code()
    #
    # black_box.quick_test() # should be a VGen object

if __name__ == '__main__' :
    # print(__name__)
    main()
