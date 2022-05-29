from VHDL import *
import sys

def main():
    if len(sys.argv) != 2:
        print('\nUsage : .\main.py <directory_name>\n')
    else:
        imported_entities = VGen.vimport_files(r'C:\Users\Christian\Desktop\Python\python\VGen\VHDL_codes')

        tb = Testbench('top')

        # add components
        for entity in imported_entities.values():
            tb.add_component(entity)

        # connect ports
        tb.show_components()
        # tmp_ports['clk'].show_connections()
        # print(tmp_ports['clk'].get_direction())
        # print(imported_entities['clock'].get_port('clk').get_direction())

        entity_a = 'clk_Rst' # ENTITY A
        ##################################################################################
        port_a = 'clk' # PORT A

        # PORT Bs
        entity_b = 'clock'
        port_b = 'clk'
        tmp_ports = imported_entities[entity_a].get_ports()
        tmp_ports[port_a].connect_port(imported_entities[entity_b], imported_entities[entity_b].get_port(port_b))
        imported_entities[entity_b].get_port(port_b).connect_port(imported_entities[entity_a],imported_entities[entity_a].get_port(port_a))

        entity_b = 'counter'
        port_b = 'clk'
        tmp_ports = imported_entities[entity_a].get_ports()
        tmp_ports[port_a].connect_port(imported_entities[entity_b], imported_entities[entity_b].get_port(port_b))
        imported_entities[entity_b].get_port(port_b).connect_port(imported_entities[entity_a],imported_entities[entity_a].get_port(port_a))
        ##################################################################################

        ##################################################################################
        port_a = 'rst_n' # PORT A

        entity_b = 'clock'
        port_b = 'rst_n'
        tmp_ports = imported_entities[entity_a].get_ports()
        tmp_ports[port_a].connect_port(imported_entities[entity_b], imported_entities[entity_b].get_port(port_b))
        imported_entities[entity_b].get_port(port_b).connect_port(imported_entities[entity_a],imported_entities[entity_a].get_port(port_a))

        entity_b = 'counter'
        port_b = 'rst_n'
        tmp_ports = imported_entities[entity_a].get_ports()
        tmp_ports[port_a].connect_port(imported_entities[entity_b], imported_entities[entity_b].get_port(port_b))
        imported_entities[entity_b].get_port(port_b).connect_port(imported_entities[entity_a],imported_entities[entity_a].get_port(port_a))
        ##################################################################################


        # tmp_ports['clk'].show_connections()
        # imported_entities['clock'].get_port('clk').show_connections()

        # instantiate
        for entity in imported_entities.values():
            tb.instantiate(entity)

        tb.generate_code()


if __name__ == '__main__' :
    main()
