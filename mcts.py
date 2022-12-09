import random, math
from hex import Board
from helper import Tree, Data

class MCTS():
    """
    A implementation of UCT 
    """ 
    def __init__(self, board: Board):
        # consists of the root for the state of the board
        self.root = Tree(Data(board, 0, 0))
        self.c = 1

    def selection(self, curr):
        """
        Will select the node that maximizes UCB1. If a node has not been
        expanded yet will select that one straight away.
        """
        # If a leaf node has been reached 
        if(curr.num_children == 0):
            return curr

        max_val = 0
        curr = self.root 

        children = curr.get_children()
        
        for i, child in enumerate(children):
            data = child.data
            val = (data.util / data.n) + self.c * math.sqrt(math.log(data.n / data.n))
            if(val > max_val):
                max_i = i
                max_val = val

        return self.selection(children[max_val])

    def expand(self, root: Tree):
        """
        Adds node to tree 
        root: Tree
        """
        
        pass 

    def simulation(self, board: Board):
        """
        Simulate games of hex based on current expansion state.
        """
        # Can not draw so do not have to check if board is full
        while(board.checks_win() == -1):
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
        node = self.selection()
        self.expand()
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
