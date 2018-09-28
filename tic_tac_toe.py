# -*- coding: utf-8 -*-
#
# Tic-Tac-Toe game implemetation

# Copyright 2017 Al Sweigart

# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided
# that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce
# the above copyright notice, this list of conditions
# and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
# OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#
# A derivative module for the avtTicTacToeBot project was created by:
# @authors: A.V.T. Software (Andrei Tostikov, Vita Tolstikova)
#

import random


class TicTacToe():
    """ Tic-Tac-Toe game implementation
    """

    # class variables

    # The game board for playing Tic-Tac-Toe (size 3 x 3 cells).
    # A list of 10 strings representing the board (ignore index 0)
    board = list()

    # A list with the user's letter as the first item
    # and the bot's letter as the second.
    game_letters = list()

    # Player who performs the current move ('user' or 'bot')
    turn = ''

    # Player who performs the next move ('user' or 'bot')
    next_player = ''

    # class methods

    def init_board(self):
        """Initialization a list representing
            the game board with initial values
        """
        self.board = ['  '] * 10

    def get_board(self):
        """Get the game board for Tic-Tac-Toe

        Returns:
            list -- A list representing the game board
        """

        return self.board

    def get_drawn_board(self, board):
        """Representing a filled game board as a string

        Arguments:
            board {list} -- A list representing the game board

        Returns:
            string -- A filled game board
        """

        row_0 = '✎\n'
        row_1 = self.board[7] + '|' + self.board[8] + '|' + \
            self.board[9] + '\n'
        row_2 = '--+--+--\n'
        row_3 = self.board[4] + '|' + self.board[5] + '|' + \
            self.board[6] + '\n'
        row_4 = '--+--+--\n'
        row_5 = self.board[1] + '|' + self.board[2] + '|' + \
            self.board[3] + '\n'

        drawn_board = row_0 + row_1 + row_2 + row_3 + row_4 + row_5

        return drawn_board

    def set_game_letters(self, user_game_letter):
        """Initialization a list in which the first element is
            the user's letter; the second is the bot's letter

        Arguments:
            user_game_letter {string} -- Game letter selected by the user
        """

        if user_game_letter == 'X':
            self.game_letters = ['X', 'O']
        else:
            self.game_letters = ['O', 'X']

    def get_user_game_letter(self):
        """Returns the user's letter

        Returns:
            string -- The user's letter
        """

        return self.game_letters[0]

    def get_bot_game_letter(self):
        """Returns the bot's letter

        Returns:
            string -- The bot's letter
        """

        return self.game_letters[1]

    def set_turn(self):
        """Randomly choose which player goes first.
        """

        if random.randint(0, 1) == 0:
            self.turn = 'bot'
        else:
            self.turn = 'user'

    def get_turn(self):
        """Returns the player whose turn to make the current move

        Returns:
            string -- The player whose turn to make the current move
        """

        return self.turn

    def set_next_turn(self, current_turn):
        """Sets the player whose turn to make the next move

        Arguments:
            current_turn {string} -- The player whose turn to make
                                        the current move
        """

        if current_turn == 'bot':
            self.turn = 'user'
        else:
            self.turn = 'bot'

    def make_move(self, board, game_letter, move):
        """Placing a Mark on the Board.

        Arguments:
            board {list} -- A list of 10 strings representing
                            the board (ignore index 0)

            game_letter {string} -- is the player’s letter
                                        (either 'X' or 'O')

            move {integer} -- is the place on the board
                                where that player wants to go
                                (which is an integer from 1 to 9)

        """

        board[move] = game_letter

    def is_winner(self, board, game_letter):
        """Given a board and a player's letter,
            this function returns True if that player has won.

        Arguments:
            board {list} -- A list of 10 strings representing
                            the board (ignore index 0)

            game_letter {string} -- is the player’s letter
                                        (either 'X' or 'O')

        Returns:
            [boolean] -- Returns True if player has won
        """

        # -1- check the top row
        top_row_check = board[7] == game_letter and \
            board[8] == game_letter and board[9] == game_letter

        # -2- check the middle row
        middle_row_check = board[4] == game_letter and \
            board[5] == game_letter and board[6] == game_letter

        # -3- check the bottom row
        bottom_row_check = board[1] == game_letter and \
            board[2] == game_letter and board[3] == game_letter

        # -4- check the left column
        left_column_check = board[7] == game_letter and \
            board[4] == game_letter and board[1] == game_letter

        # -5- check the middle column
        middle_column_check = board[8] == game_letter and \
            board[5] == game_letter and board[2] == game_letter

        # -6- check the right column
        right_column_check = board[9] == game_letter and \
            board[6] == game_letter and board[3] == game_letter

        # -7- check the main diagonal
        main_diagonal_check = board[7] == game_letter and \
            board[5] == game_letter and board[3] == game_letter

        # -8- check the secondary diagonal
        secondary_diagonal_check = board[9] == game_letter and \
            board[5] == game_letter and board[1] == game_letter

        # check all winner combinations
        is_winner_check = top_row_check or middle_row_check or \
            bottom_row_check or left_column_check or \
            middle_column_check or right_column_check or \
            main_diagonal_check or secondary_diagonal_check

        return is_winner_check

    def get_board_copy(self, board):
        """Make a copy of the board list

        Arguments:
            board {list} -- A list of 10 strings representing
                            the board (ignore index 0)

        Returns:
            list -- A copy of the board list
        """

        board_copy = []

        for i in board:
            board_copy.append(i)

        return board_copy

    def is_space_free(self, board, move):
        """Check if the passed move is free on the passed board

        Arguments:
            board {list} -- A list of 10 strings representing
                            the board (ignore index 0)

            move {integer} -- is the place on the board
                                where that player wants to go
                                (which is an integer from 1 to 9)

        Returns:
            boolean -- Return True if the passed move
                        is free on the passed board
        """

        return board[move] == '  '

    def choose_random_move_from_list(self, board, moves_list):
        """Returns a valid move from the passed list on the passed board.
        Returns None if there is no valid move.

        Arguments:
            board {list} -- A list of 10 strings representing
                            the board (ignore index 0)

            moves_list {list} -- The passed list on the passed board

        Returns:
            [integer] -- A valid move from the passed list on the passed board
            or
            [None] --   Returns None if there is no valid move
        """

        possible_moves = []

        for i in moves_list:
            if self.is_space_free(board, i):
                possible_moves.append(i)

        if len(possible_moves) != 0:
            return random.choice(possible_moves)
        else:
            return None

    def get_bot_move(self, board, bot_game_letter):
        """Given a board and the bot's game letter,
            determine where to move and return that move.

        Arguments:
            board {list} -- A list of 10 strings representing
                                the board (ignore index 0)

            bot_game_letter {string} -- is the bot’s letter
                                        (either 'X' or 'O')

        Returns:
            integer -- is the place on the board where bot to go
                            (which is an integer from 1 to 9)
        """

        if bot_game_letter == 'X':
            player_game_letter = 'O'
        else:
            player_game_letter = 'X'

        # Here is our algorithms for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            board_copy = self.get_board_copy(board)
            if self.is_space_free(board_copy, i):
                self.make_move(board_copy, bot_game_letter, i)
                if self.is_winner(board_copy, bot_game_letter):
                    return i

        # Check if the player could win on his next move and block them
        for i in range(1, 10):
            board_copy = self.get_board_copy(board)
            if self.is_space_free(board_copy, i):
                self.make_move(board_copy, player_game_letter, i)
                if self.is_winner(board_copy, player_game_letter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.choose_random_move_from_list(board, [1, 3, 7, 9])
        if move is not None:
            return move

        # Try to take the center, if it is free.
        if self.is_space_free(board, 5):
            return 5

        # Move on one of the sides.
        return self.choose_random_move_from_list(board, [2, 4, 6, 8])

    def is_board_full(self, board):
        """Return True if every space on the board has been taken.
            Otherwise return False.

        Arguments:
            board {list} -- A list of 10 strings representing
                            the board (ignore index 0)

        Returns:
            boolean -- Return True if every space on the board has been taken.
                        Otherwise return False.
        """

        for i in range(1, 10):
            if self.is_space_free(board, i):
                return False
        return True
