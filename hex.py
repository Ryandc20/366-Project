from helper import Union

class Board:
    """
    Represents a hex board
    """
    def __init__(self, size=11):
        self.board = [['_'] * size for _ in range(size)]
        self.size = 11

        # Create union which tracks what pieces are together
        self.uni_0 = Union(size * size + 2)
        self.uni_1 = Union(size * size + 2)

        # Side position for player 0 will be left and right side of the board
        for i in range(self.size):
            # Left side
            idx = self.hash(i, 0)
            self.uni_0.union(0, idx) 

            # Right side
            idx = self.hash(i, self.size-1)
            self.uni_0.union(1, idx)
            
        # Side position for player will be top and bottom part of the board.
        for j in range(self.size):
            # Left side 
            idx = self.hash(0, j)
            self.uni_1.union(0,idx)

            # Right side 
            idx = self.hash(self.size-1, j)
            self.uni_1.union(1, idx)

        # False represents player zero and true represents player one
        self.player = False
        pass
    
    def get_moves(self):
        """
        Get the aviabile moves for the board. Which is all empty spaces. Will
        returns this as a list of i, j tuples.
        """

        moves = []
        for i, row in enumerate(self.board):
            for j, unit in enumerate(row):
                if(unit == '_'):
                    moves.append((i,j))

        return moves

    def make_move(self, i, j):
        """
        Changes the board state based on the current player 

        Returns false if the move is a faliure and true if successful 
        """
        # If the board state is empty change it to current player
        if(self.board[i][j] != '_'):
            return False

        # If player zero
        if not self.player:
            self.board[i][j] = '0'
            uni = self.uni_0
            # Swap the player
            self.player = True
        else:
            self.board[i][j] = '1'
            uni = self.uni_1
            # Swap the player
            self.player = False

        # unify with all neighbors
        idx = self.hash(i, j)

        # The neighbors of a non edge piece will be left right j - 1, j + 1
        if(j != 0 and self.board[i][j] == self.board[i][j-1]):
            idx1 = self.hash(i, j - 1)
            uni.union(idx, idx1)

        if(j != self.size-1 and self.board[i][j] == self.board[i][j+1]):
            idx1 = self.hash(i, j + 1)
            uni.union(idx, idx1)

        if(i != 0 and self.board[i][j] == self.board[i-1][j]):
            idx1 = self.hash(i - 1, j)
            uni.union(idx, idx1)

        if(i != self.size-1 and self.board[i][j] == self.board[i+1][j]):
            idx1 = self.hash(i + 1, j)
            uni.union(idx, idx1)

        if(i != 0 and j != self.size-1 and self.board[i][j] == self.board[i-1][j+1]):
            idx1 = self.hash(i-1,j+1)
            uni.union(idx, idx1)
        
        if(i != self.size-1 and j != 0 and self.board[i][j] == self.board[i + 1][j - 1]):
            idx1 = self.hash(i + 1, j - 1)
            uni.union(idx, idx1)
        

        return True

    def checks_win(self):
        """
        Checks If I player has won the game. Will return one if player zero wins
        and will return negative one if player one. 
        """

        # Checks win if both sides are connected by seing if they are in the
        # same set within the union data structure
        if(self.uni_0.joint(0,1)):
            return 1
        if(self.uni_1.joint(0,1)):
            return 0

        # No one has one the game in this state
        return 0

    def copy(self): 
        """
        Returns a deep copy of the board 
        """
        board = Board(self.size)
        board.board = [row.copy() for row in self.board]
        board.player = self.player
        board.uni_0 = self.uni_0.copy()
        board.uni_0 = self.uni_1.copy()
        return board
    
    def hash(self, x, y):
        """
        Maps each item of the board to a unique integer. 
        As it is a perfect hashing function. Will add two to leave space for both
        sides of the board for each player.
        """
        return x * self.size + y + 2


    # TODO if have time make it print diagonally 
    def __str__(self):
        """
        Overwrite the print functionality to display the board.
        """
        string = ""
        for i, row in enumerate(self.board):
            for cell in row:
                string += cell + "   "
            string += "\n"
            string += "  " * (i + 1)

        return string

# TODO remove just to check if the game is working properly
def main():
    board = Board()
    print(board)
    for i in range(11):
        board.make_move(i,i//2)
    print(board)
    print(board.checks_win())

    board=Board()

if __name__ == "__main__":
    main()
