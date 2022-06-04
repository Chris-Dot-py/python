library ieee;
use ieee.std_logic_1164.all;

Entity clk_Rst is
  generic(
    -- comment here
    clk_prd : integer := 21 -- comment
    -- comment
  );
  port(
    clk : out std_logic;
    rst_n : out std_logic;
    -- comment ---
    -- comment ----
    is_test : out boolean;
    is_test2 : in bsafadfoolean;
    is_test3 : out bsafadfoolean(blabla downto 0);
    input_one : in std_logic;
    input_two : in std_logic;
    -- comments
    bit_Vector_signal : out std_logic_vector(63 downto 0); -- comment her
    custom_signal : out t_tyasdpe; -- comment here
    custom_signal_three : out std_logic_vector((byte_len)-1 DowntO 0);
    custom_signal_four : out unsigned((byte_len)-1 DOWNTO 0);
    custom_signal_five : out signed((((byte_len)*(ASD))/2)-1 downto 0);
    -- comment here
    custom_signal_too : out t_type_no_two; -- comment here
    test : out std_logic
  );
end entity clk_Rst;

architecture clk_rst_arch of clk_rst is

begin
end architecture;
