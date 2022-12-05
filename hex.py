class Board:
    def __init__(self, size=11):
        """
        Intilizes a hex board
        """
        self.board = [['_'] * size] * size 

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
        else:
            self.board[i][j] = '1'

        # Add the move to the union find data structure
        
        return True

    def checks_win(self):
        """
        Checks If I player has won the game. Will return one if player zero wins
        and will return negative one if player one. 
        """

        # Check if there exists a path for player zero between the two sides of
        # the board. There will be the top and bottom. 
        pass

    def read_state(self):
        """
        Reads the game state from a file.
        """
        pass

    def save_state(self):
        """
        Saves the state of the game to a file
        """
        pass

    def __str__(self):
        """
        Overwrite the print functionality to display the board diagonally.
        """
        return ""
