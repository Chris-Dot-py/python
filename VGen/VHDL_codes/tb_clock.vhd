-- -=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=- --
--     Code generated by VGen by Christian Manuel    --
-- -=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=- --
library ieee;
use ieee.std_logic_1164.all;

entity tb_clock is
end entity tb_clock;

architecture tb_clock_arch of tb_clock is

  component clock is
  port(
    clk : in std_logic;
    rst_n : in std_logic;
    seconds : out std_logic_vector(5 downto 0);
    minutes : out std_logic_vector(5 downto 0);
    hours : out std_logic_vector(4 downto 0);
    dummy_port : out std_logic_vector(15 downto 0)
  );
  end component clock;

  component counter is
  generic(
    term_cnt : integer;
    inverted : boolean
  );
  port(
    clk : in std_logic;
    rst_n : in std_logic;
    count : out std_logic_vector(3 downto 0)
  );
  end component counter;

  component clk_rst is
  generic(
    len : integer;
    inverted : boolean
  );
  port(
    clk : in std_logic;
    rst_n : out std_logic;
    display_out : out std_logic_vector(7 downto 0)
  );
  end component clk_rst;

  -- clock
  signal clk : std_logic;
  signal rst_n : std_logic;
  signal seconds : std_logic_vector(5 downto 0);
  signal minutes : std_logic_vector(5 downto 0);
  signal hours : std_logic_vector(4 downto 0);
  signal dummy_port : std_logic_vector(15 downto 0);
  -- counter
  signal count : std_logic_vector(3 downto 0);
  -- clk_rst
  signal display_out : std_logic_vector(7 downto 0);

begin

  clock_0_i : clock
  port map(
    clk => open,
    rst_n => open,
    seconds => seconds,
    minutes => minutes,
    hours => hours,
    dummy_port => dummy_port
  );

  counter_0_i : counter
  generic map(
    term_cnt => open,
    inverted => open
  );
  port map(
    clk => open,
    rst_n => open,
    count => count
  );

  clk_rst_0_i : clk_rst
  generic map(
    len => open,
    inverted => open
  );
  port map(
    clk => open,
    rst_n => rst_n,
    display_out => display_out
  );

end architecture;
