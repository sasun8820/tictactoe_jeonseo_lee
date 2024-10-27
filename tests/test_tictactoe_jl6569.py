import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from tictactoe_jl6569.tictactoe_jl6569 import initialize_board, make_move, check_winner, reset_game

def test_initialize_board():
    board = initialize_board()
    assert board == [[' ' for _ in range(3)] for _ in range(3)], "Board should be empty 3x3 grid."

def test_make_move_valid():
    board = initialize_board()
    
    # Player 'X' makes a valid move at (1, 1)
    result_x = make_move(board, 1, 1, 'X')
    assert result_x is True, "Move should be valid for player 'X'"
    assert board[1][1] == 'X', "Board should reflect player 'X''s move"
    
    # Player 'O' makes a valid move at (0, 0)
    result_o = make_move(board, 0, 0, 'O')
    assert result_o is True, "Move should be valid for player 'O'"
    assert board[0][0] == 'O', "Board should reflect player 'O''s move"
    
    # Check the final board configuration
    expected_board = [['O', ' ', ' '],
                      [' ', 'X', ' '],
                      [' ', ' ', ' ']]
    assert board == expected_board, "Board should have 'O' at (0, 0) and 'X' at (1, 1)"

def test_make_move_invalid():
    board = initialize_board()
    make_move(board, 0, 0, 'X')  # Player 'X' makes a move at (0, 0)
    
    # Try to make a move for player 'O' in the same cell (0, 0)
    result = make_move(board, 0, 0, 'O')
    
    # Check that the move is not allowed
    assert result is False, "Move should be invalid because the cell is already occupied"
    assert board[0][0] == 'X', "The board should not allow overwriting an occupied cell"

def test_game_integration():
    board = initialize_board()
    assert board == [[' ' for _ in range(3)] for _ in range(3)], "The board should be initialized to an empty 3x3 grid."
    
    # Series of valid moves
    assert make_move(board, 0, 0, 'X') is True
    assert make_move(board, 0, 1, 'O') is True
    assert make_move(board, 1, 1, 'X') is True
    assert make_move(board, 0, 2, 'O') is True
    assert make_move(board, 2, 2, 'X') is True
    
    # Check for a winner
    winner = check_winner(board)
    assert winner == 'X', "Player 'X' should win with a diagonal."
    
    # Verify the board state before resetting
    expected_board = [['X', 'O', 'O'],
                      [' ', 'X', ' '],
                      [' ', ' ', 'X']]
    assert board == expected_board, "The board should reflect the moves made."
    
    # Reset the game
    board = reset_game()
    assert board == [[' ' for _ in range(3)] for _ in range(3)], "The board should be reset to an empty 3x3 grid."