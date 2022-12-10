# Test to see how much MCTS improves with an doubling in serach depth of 500 to
# 1000 on a 7 x 7 board. By playing against it self. Half games will be played
# with one search playing first and half will be played with the
# other one playing first 
from mcts import MCTS
from hex import Board

# Define hyperparmets 
n = 500
iteration_1 = 500 
iteration_2 = 250 

total = 0 

for i in range(n // 2):
    board = Board(size=7)
    while(board.checks_win() == -1):
        mcts = MCTS(board)
        for _ in range(iteration_1):
            mcts.search()
        idx = mcts.get_move()
        moves = board.get_moves()
        move = moves[idx]

        board.make_move(*move)

        mcts = MCTS(board, maximize=False)
        for _ in range(iteration_2):
            mcts.search()
        idx = mcts.get_move()
        moves = board.get_moves()
        move = moves[idx]

        board.make_move(*move)

    total += board.checks_win()
    print((i + 1) / n * 100, "% done")

for j in range(n // 2):
    board = Board(size=7)
    while(board.checks_win() == -1):
        mcts = MCTS(board)
        for _ in range(iteration_2):
            mcts.search()
        idx = mcts.get_move()
        moves = board.get_moves()
        move = moves[idx]

        board.make_move(*move)

        mcts = MCTS(board, maximize=False)
        for _ in range(iteration_1):
            mcts.search()
        idx = mcts.get_move()
        moves = board.get_moves()
        move = moves[idx]

        board.make_move(*move)

    win = board.checks_win()
    if(win == 1):
        win = 0
    else: 
        win = 1

    total += win
    print(((j + 1) / n +  1 / 2) * 100, "% done")


print("MCTS with iteration", iteration_1, "beat MCTS with iteration",iteration_2, total / n * 100, "% of the time")
