-- -=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=- --
--     Code generated by VGen by Christian Manuel    --
-- -=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=-=#=- --
library ieee;
use ieee.std_logic_1164.all;

entity top_level is
end entity top_level;

architecture top_level_arch of top_level is

  component clk_rst is
  port(
    clk : out std_logic;
    rst : out std_logic
  );
  end component clk_rst;

  component clk_Rst is
  generic(
    clk_prd : integer
  );
  port(
    clk : out std_logic;
    rst_n : out std_logic;
    is_test : out boolean;
    is_test2 : in bsafadfoolean;
    is_test3 : out bsafadfoolean(blabla downto 0);
    input_one : in std_logic;
    input_two : in std_logic;
    bit_Vector_signal : out std_logic_vector(63 downto 0);
    custom_signal : out t_tyasdpe;
    custom_signal_three : out std_logic_vector((byte_len)-1 downto 0);
    custom_signal_four : out unsigned((byte_len)-1 downto 0);
    custom_signal_five : out signed((((byte_len)*(ASD))/2)-1 downto 0);
    custom_signal_too : out t_type_no_two;
    test : out std_logic
  );
  end component clk_Rst;

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
  port(
    clk : out std_logic;
    rst_n : out std_logic
  );
  end component counter;

  -- clk_rst
  signal clk : std_logic;
  signal rst : std_logic;
  -- clk_Rst
  signal rst_n : std_logic;
  signal is_test : boolean;
  signal is_test3 : bsafadfoolean(blabla downto 0);
  signal bit_Vector_signal : std_logic_vector(63 downto 0);
  signal custom_signal : t_tyasdpe;
  signal custom_signal_three : std_logic_vector((byte_len)-1 downto 0);
  signal custom_signal_four : unsigned((byte_len)-1 downto 0);
  signal custom_signal_five : signed((((byte_len)*(ASD))/2)-1 downto 0);
  signal custom_signal_too : t_type_no_two;
  signal test : std_logic;
  -- clock
  signal seconds : std_logic_vector(5 downto 0);
  signal minutes : std_logic_vector(5 downto 0);
  signal hours : std_logic_vector(4 downto 0);
  signal dummy_port : std_logic_vector(15 downto 0);
  -- counter

begin

  clk_rst_0_i : clk_rst
  port map(
    clk => clk,
    rst => rst
  );

  clk_Rst_0_i : clk_Rst
  generic map(
    clk_prd => open
  );
  port map(
    clk => clk,
    rst_n => rst_n,
    is_test => is_test,
    is_test2 => open,
    is_test3 => is_test3,
    input_one => open,
    input_two => open,
    bit_Vector_signal => bit_Vector_signal,
    custom_signal => custom_signal,
    custom_signal_three => custom_signal_three,
    custom_signal_four => custom_signal_four,
    custom_signal_five => custom_signal_five,
    custom_signal_too => custom_signal_too,
    test => test
  );

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
  port map(
    clk => clk,
    rst_n => rst_n
  );

end architecture;
