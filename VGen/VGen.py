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

    clock.generate_code()
    tb_clock.generate_code()


if __name__ == '__main__' :
    # print(__name__)
    main()
