from base.board import Board
from base.control import Game
import yaml

def main():
    config = yaml.safe_load(open('config.yaml', 'r'))
    board = Board(**config['board'])

    for ship in config['board']['ships']:
        board.add_ship(**ship)

    game = Game(board, **config['control'])
    game.start()

if __name__ == "__main__":
    main()