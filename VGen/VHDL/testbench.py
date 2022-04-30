"""
    To Do:
        - Add generate
"""

from VHDL import *
import os
class Testbench(Entity):
    def __init__(self, entity):
        super().__init__(entity.get_entity_name())
        self.__testbench_name = 'tb_' + entity.get_entity_name()

    def get_entity_name(self):
        return self.__testbench_name

    def generate_code(self):
        super().generate_code(self.__testbench_name)
