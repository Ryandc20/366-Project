# Test to see how much MCTS improves with an doubling in serach depth of 500 to
# 1000 on a 9 x 9 board. By playing against it self. Half games will be played
# with one search playing first and half will be played with the
# other one playing first 
from mcts import MCTS
from hex import Board

# Define hyperparmets 
n = 20

# Make sure depth 2 is greater than depth 1
iteration_1 = 500 
iteration_2 = 1000 

total = 0 

for i in range(n // 2):
    pass 


for j in range(n // 2):
    pass 

print("MCTS with iteration", iteration_1, "beat MCTS with iteration",iteration_2, total / n * 100 "% of the time")
