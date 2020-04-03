from base.base import GameBaseException

EMPTY_KEY = 0
SHIP_KEY = 1
HIT_KEY = 2
MISS_KEY = 3

class BoardException(GameBaseException):
    default_message = 'Erro no tabuleiro'


class Board:

    def __init__(self, dimension, *args, **kwargs):
        self.dimension = dimension
        self.key_values = kwargs['key_values']
        self.float_spaces = ' ' * kwargs.get('float_spaces', 3)
        self.ships = []
        self.reset_board()

    def reset_board(self):
        self.board = []
        for _ in range(self.dimension):
            self.board.append([EMPTY_KEY for _ in range(self.dimension)])

    def print_position(self, value):
            return '%s' % self.key_values[value] + self.float_spaces

    def set_position(self, x, y, key):
        if key == HIT_KEY:
            print('\nAcertou')
        elif key == MISS_KEY:
            print('\nErrou')

        self.board[x][y] = key

    @BoardException.catch_exception
    def add_ship(self, x, y, size, orientation):
        ship = Ship(x, y, size, orientation, self)

        for position in ship.cordinates:
            self.board[position[0]][position[1]] = SHIP_KEY

        self.ships.append(ship)

    @BoardException.catch_exception
    def hit(self, x, y):
        position = self.board[x][y]

        if position == EMPTY_KEY:
            self.set_position(x, y, MISS_KEY)
        elif position == MISS_KEY or position == HIT_KEY:
            raise BoardException('Posicao ja escolhida')
        elif position == SHIP_KEY:
            self.set_position(x, y, HIT_KEY)

    def __str__(self):
        board = []
        first_line = ' %s%s\n' % (self.float_spaces, self.float_spaces.join([str(i) for i in range(self.dimension)]) )

        for y in range(self.dimension):
            line = '%s' % y + self.float_spaces
            for x in range(self.dimension):
                line += self.print_position(self.board[x][y])

            board.append(line)

        return first_line + '\n'.join(board)


class Ship():

    def __init__(self, x, y, size, orientation, board, *args, **kwargs):
        self.cordinates = []
        self.board = board

        for i in range(size):
            pos_x = x+i if orientation == 'h' else x
            pos_y = y+i if orientation == 'v' else y

            self.validate(pos_x, pos_y)
            
            self.cordinates.append((pos_x, pos_y))

    def validate(self, x, y):
        try:
            if self.board.board[x][y] != EMPTY_KEY:
                raise BoardException('Coordenada não vazia: %s, %s' % (x, y))
        except IndexError:
                raise BoardException('Coordenada fora do limite do tabuleiro: %s, %s' % (x, y))