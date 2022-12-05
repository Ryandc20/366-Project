# Object of game is to connect the two sides of the boards with markers
# Once a player has adjacent stones that connect two sides of board together
# they win
class Board:
    # Initlize the board
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
        Get the aviabile moves for the board
        """
        pass

    def make_move(self):
        """
        Changes the board state based on the current player 
        """
        pass

    def checks_win(self):
        """
        Checks If I player has won the game. Will return one if player zero wins
        and will return negative one if player one. 
        """
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
