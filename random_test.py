# Checks the percent of the time the board wins against random play at size 7x7
# With random going first to give it the advantage 

# Warning this code can take a while to run at current setting decrease the num
# test, board size or serach itteration. To speed up runtime.

import random
from mcts import MCTS
from hex import Board

total = 0
n = 20
for i in range(n):
    board = Board(size = 9, first=False)
    while(board.checks_win() == -1):
        moves = board.get_moves()
        idx = random.randint(0, len(moves) - 1)
        move = moves[idx]
        board.make_move(*move) 

        mcts = MCTS(board)

        # do n itteration of serach 
        for _ in range(500):
            mcts.search()

        # get best move 
        idx = mcts.get_move()
        moves = board.get_moves()
        move = moves[idx]

        board.make_move(*move)


    print((i + 1)/n * 100, "% done")
    total += board.checks_win()

print("MCTS wins", total / n * 100, "% of the time against random")
