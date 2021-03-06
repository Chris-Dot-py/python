-- -=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=- --
--     Code generated by VGen by Christian Manuel    --
-- -=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=- --
library ieee;
use ieee.std_logic_1164.all;

ENTITY clock is
  port(
    clk : in std_logic;
    rst_n : in std_logic;
    seconds : out std_logic_vector(5 downto 0);
    minutes : out std_logic_vector(5 downto 0);
    hours : out std_logic_vector(4 downto 0);
    dummy_port : out std_logic_vector(15 downto 0) -- comment
  );
end entity clock;

architecture clock_arch of clock is


begin

end architecture;
