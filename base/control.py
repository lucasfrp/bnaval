from base.base import GameBaseException
import os

clear_screen = lambda: os.system('clear')
HIT_COMMAND = 1
SHOW_BOARD_COMMAND = 9
QUIT_COMMAND = 10


class ControlException(GameBaseException):
    pass


class InputException(ControlException):
    default_message = 'Entrada inválida'
    handled_exceptions = (ValueError,)


class Game():

    def __init__(self, board, turn_options):
        self.board = board
        self.turn_options = turn_options

    def start(self):
        self.turn()

    @InputException.catch_exception
    def get_input(self):
        return int(input('\n'.join(self.turn_options)+'\n\nYour Choice: ' ))

    @InputException.catch_exception
    def hit(self):
        try:
            x = int(input('Type x cordinate: '))
            y = int(input('Type y cordinate: '))
            self.board.hit(x,y)
        except Exception as e:
            raise InputException(e)

    def turn(self):

        clear_screen()
        print(self.board)

        user_input = self.get_input()

        if user_input == HIT_COMMAND:
            self.hit()

        elif user_input == SHOW_BOARD_COMMAND:
            pass

        elif user_input == QUIT_COMMAND:
            print('Bye!')
            return

        input('Press any key to continue...')
        self.turn()