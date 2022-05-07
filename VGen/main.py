from VHDL import *

def main():

    clock = Entity('clock') # entry

    # button commands
    clock.add_port(Port('clk','in',1))
    clock.add_port(Port('rst_n','in',1))
    clock.add_port(Port('seconds','out',6))
    clock.add_port(Port('minutes','out',6))
    clock.add_port(Port('hours','out',5))
    clock.add_port(Port('dummy_port','out',16))
    clock.generate_code()

    counter = Entity('counter')
    counter.add_port(Port('clk','in',1))
    counter.add_port(Port('rst_n','in',1))
    counter.add_port(Port('count','out',4))
    counter.generate_code()

    tb_clock = Testbench(clock)
    tb_clock.add_component(clock)
    tb_clock.add_component(counter)
    tb_clock.instantiate(clock)
    tb_clock.instantiate(counter)
    tb_clock.generate_code()

if __name__ == '__main__' :
    # print(__name__)
    main()
