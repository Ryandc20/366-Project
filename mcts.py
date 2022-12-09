import random
from hex import Board

class MCTS():
    """
    A implementation of UCT 
    """ 
    def __init__(self, board: Board):
        # consists of the states of the board
        self.board = board
        pass

    def selection(self):
        """
        Will select the node that maximizes UCB1
        """
        pass

    def expansion(self):
        """

        """
        pass 

    def simulation(self, board: Board):
        """
        Simulate games of hex based on current expansion state.
        """
        # Can not draw so do not have to check if board is full
        while(board.checks_win() == 0):
            # Get avaliable moves
            moves = board.get_moves()

            # Get selection for random move
            idx = random.randint(0, len(moves) - 1)
            move = moves[idx]

            # Makes the move
            board.make_move(*move)
        print(board)
            
        return board.checks_win()

    def backpropagation(self):
        """
        Updates probabilities
        """
        pass

    def mcts(self):
        """

        """
        self.selection()
        self.expansion()
        self.simulation(self.board)
        self.backpropagation()
        pass


def main():
    """
    Play a game against user to test code.
    """
    board = Board()
    mcts = MCTS(board)
    print(mcts.simulation(board))

if __name__ == "__main__":
    main()
