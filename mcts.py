import random, math
from hex import Board
from helper import Tree, Data

class MCTS():
    """
    A implementation of UCT 
    """ 
    def __init__(self, board: Board):
        # Data of the root 
        self.data = Data(board, 0, 0)
        # Root of the mcts search tree 
        self.root = Tree(self.data)
        # Tuneable parameters 
        self.c = 1


    def selection(self, curr: Tree):
        """
        Will select the node that maximizes UCB1. If a node has not been
        expanded yet will select that one straight away.
        """

        # Gets the moves of the current root 
        moves = curr.data.board.get_moves()

        # If node has not been expaned more than the number of possible moves
        if(curr.num_children() < len(moves) or curr.num_children() == 0):
            return curr

        best_val = 0
        best = 0
        children = curr.get_children()
        
        for i, child in enumerate(children):
            data = child.data

            val = (data.util / data.n) + self.c * math.sqrt(math.log(self.data.n) / data.n)

            if(val > best_val):
                best = i
                best_val = val


        return self.selection(children[best])

    def expand(self, root: Tree):
        """
        Adds node to tree the root will not be fully expanded 
        """

        board = root.data.board.copy()

        # Make sure that all nodes have not been expanded 
        if(root.num_children() == len(board.get_moves())):
            return root

        # Get a copy of the board
        n = root.num_children()
        moves = board.get_moves() 
        move = moves[n]
        board.make_move(*move)
        data = Data(board, 0, 0)
        root.add_child(data)

        return root.get_children()[-1]

    def simulation(self, data: Data):
        """
        Simulate games of hex based on current expansion state.
        """

        # Copy the board to not make changes to it 
        board = data.board.copy()

        # Can not draw so do not have to check if board is full
        while(board.checks_win() == -1):
            # Get avaliable moves
            moves = board.get_moves()

            # Get selection for random move
            idx = random.randint(0, len(moves) - 1)
            move = moves[idx]

            # Makes the move
            board.make_move(*move)


        return board.checks_win()

    def backpropagation(self, node: Tree, val):
        """
        Update utility. By path back to root 
        """
        curr = node
        while(curr != None): 
            data = curr.data 
            # Update the values 
            data.n += 1 
            data.util += val

            curr = curr.parent

    def search(self):
        """
        Perform one iteration of the mcts algorithm
        """
        node = self.selection(self.root)
        node = self.expand(node)
        val = self.simulation(node.data)
        self.backpropagation(node,val)

    def get_move(self):
        """
        Will return optimal move based on current tree values.
        """
        best_util = 0.
        best_move = 0
        for i, child in enumerate(self.root.get_children()):
            data = child.data
            util = data.util / data.n
            if(util > best_util):
                best_util = util 
                best_move = i

        return best_move

def main():
    """
    Play a game against mcts.
    """
    board = Board()
    while(board.checks_win() == -1):
        mcts = MCTS(board)
        for _ in range(500):
            mcts.search()

        # Get the move mcts selects 
        idx = mcts.get_move()
        moves = board.get_moves()
        move = moves[idx]
        
        board.make_move(*move)

        if(board.checks_win() != -1):
            break

        moves = board.get_moves()

        # Get selection for random move
        idx = random.randint(0, len(moves) - 1)
        move = moves[idx]
        board.make_move(*move)

        print(board)

    print(board)
    print(board.checks_win())

if __name__ == "__main__":
    main()
