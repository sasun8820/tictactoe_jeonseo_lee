# read version from installed package
from importlib.metadata import version
__version__ = version("tictactoe_jl6569")

from tictactoe_jl6569.tictactoe_jl6569 import initialize_board, make_move, check_winner, reset_game
