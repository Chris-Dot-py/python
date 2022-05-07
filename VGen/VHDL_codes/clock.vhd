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
end entity clock;

architecture clock_arch of clock is

  component test_block is
  port(
    input_0 : in std_logic;
    input_1 : in std_logic;
    input_2 : in std_logic;
    input_3 : in std_logic;
    input_4 : in std_logic;
    input_5 : in std_logic;
    input_6 : in std_logic;
    input_7 : in std_logic;
    input_8 : in std_logic;
    input_9 : in std_logic;
    input_10 : in std_logic;
    input_11 : in std_logic;
    input_12 : in std_logic;
    input_13 : in std_logic;
    output_0 : out std_logic;
    output_1 : out std_logic;
    output_2 : out std_logic;
    output_3 : out std_logic;
    output_4 : out std_logic;
    output_5 : out std_logic;
    output_6 : out std_logic;
    output_7 : out std_logic;
    output_8 : out std_logic;
    output_9 : out std_logic
  );
  end component test_block;

  component tb_clock is
  end component tb_clock;

  component dummy_block is
  port(
    input_0 : in std_logic;
    input_1 : in std_logic;
    output_0 : out std_logic;
    output_1 : out std_logic;
    output_2 : out std_logic;
    output_3 : out std_logic
  );
  end component dummy_block;

begin

  test_block_0_i : test_block
  port map(
    input_0 => open,
    input_1 => open,
    input_2 => open,
    input_3 => open,
    input_4 => open,
    input_5 => open,
    input_6 => open,
    input_7 => open,
    input_8 => open,
    input_9 => open,
    input_10 => open,
    input_11 => open,
    input_12 => open,
    input_13 => open,
    output_0 => open,
    output_1 => open,
    output_2 => open,
    output_3 => open,
    output_4 => open,
    output_5 => open,
    output_6 => open,
    output_7 => open,
    output_8 => open,
    output_9 => open
  );

  dummy_block_0_i : dummy_block
  port map(
    input_0 => open,
    input_1 => open,
    output_0 => open,
    output_1 => open,
    output_2 => open,
    output_3 => open
  );

  dummy_block_1_i : dummy_block
  port map(
    input_0 => open,
    input_1 => open,
    output_0 => open,
    output_1 => open,
    output_2 => open,
    output_3 => open
  );

  dummy_block_2_i : dummy_block
  port map(
    input_0 => open,
    input_1 => open,
    output_0 => open,
    output_1 => open,
    output_2 => open,
    output_3 => open
  );

end architecture;
