"""
date = '24/04/2021'
modified_date = '24/04/2021'
author = 'Mahesh Naik'
description = Stop watch problem"""
import logging
import random

from logicallog import logger
"""Corners, Center and Others, respectively
    Winner combinations
"""


board = [i for i in range(0, 9)]
player, computer = '', ''

# Corners, Center and Others, respectively
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
# Winner combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
# Table
tab = range(1, 10)


def print_board():
    """board logic
    assign blocks using for loop


"""
    logger.setLevel(logging.INFO)
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1:
                end += '---------\n'
        char = ' '
        if i in ('X', 'O'):
            char = i
        x += 1
        print(char, end=end)


def select_char():
    """Select X or O randomly
    use random function"""
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, player, move):
    """Checking for the Move
    use conditional statement """
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


def can_win(brd, player, move):
    """check block and place empty block
    using append method"""
    places = []
    x = 0
    for i in brd:
        if i == player: places.append(x);
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win:
            break
    return win


def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


def computer_move():
    """Checking for the winning Condition
    Blocking Player
    Trying to win
    move=mv
    ."""
    move = -1

    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            move = i
            break
    if move == -1:
        # Blocking Player
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                move = i
                break
    if move == -1:
        # Trying to win
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move = mv
                    break
    return make_move(board, computer, move)


def space_exist():
    """check board  if board is full than try to another block else game is tie
    using conditional statement use and check print valid sign or not"""
    return board.count('X') + board.count('O') != 9
try:
    player, computer = select_char()
    logger.info('Player is [%s] and computer is [%s]' % (player, computer))
    result = '-----! Drawn, game tie'
    while space_exist():
        print_board()
        print(end='')
        logger.info('Make your move ! [1-9] : ')\

        move = int(input())
        moved, won = make_move(board, player, move)
        if not moved:
            logger.info('  Invalid number, Please Try again ')
            continue
        if won:
            result = ' Congratulations ! You won '
            break
        elif computer_move()[1]:
            result = 'You lose ! '
            break

    print_board()
    logger.info(result)
except Exception:
    logger.exception("Exception occured")