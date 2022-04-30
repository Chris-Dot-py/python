library ieee;
use ieee.std_logic_1164.all;

entity clock is
  port(
    clk : in std_logic;
    rsgn : in std_logic;
    seconds : out std_logic_vector(5 downto 0);
    minutes : out std_logic_vector(5 downto 0);
    hours : out std_logic_vector(4 downto 0);
    dummy_port : out std_logic_vector(15 downto 0)
  );
end entity;

architecture clock_arch of clock is
begin
end architecture;