# A Collection of helper functions and classes. 

# Union Find Data Structure implement to unify to states of the hex board
class Union:
    def __init__(self, numel):
        """
        parameters:
            numel(int): number elements
        """
        self.numel = numel
        
        # Keeps track of a nodes parent node
        self.ids = []

        # Keeps track of the size of each set 
        self.size = [1] * numel

        # Make sure all nodes start by pointing at themselves
        for i in range(numel):
            self.ids.append(i)


    def root(self, item):
        """
        Find the root of item
        """

        while(self.ids[item] != item):
            item = self.ids[item]

        # TODO Add path collapse

        return item

    # Add a position of the board to the union structure
    def union(self, a, b):
        """
        Unions two sets together.
        """
        if(self.joint(a,b)): return

        # Get the roots of the nodes         
        root_a = self.root(a)
        root_b = self.root(b)

        # Unify the smaller set into the larget set 
        if(self.size[root_a] < self.size[root_b]):
            # Increase the size of root_b 
            self.size[root_b] += self.size[root_a]
            self.size[root_a] = 0
            self.ids[root_a] = root_b
        else:
            self.size[root_a] += self.size[root_b]
            self.size[root_b] = 0
            self.ids[root_b] = root_a

    def joint(self, a, b):
        """
        Check if two elements are within the same sets returns true if so 
        """
        return self.root(a) == self.root(b)

    def copy(self):
        union = Union(self.numel)
        union.ids = self.ids.copy()
        union.size = self.size.copy()
        return union




class Tree:
    """
    Simple implementation of tree data structure for mcts.
    With the ability to backtrack for backpropagation.
    """
    def __init__(self, data):
        """
        data: contains data for root node 
        """
        self.data = data
        self.parent = None
        self.children = []

    def get_data(self):
        return self.data

    def add_child(self, data):
        node = Tree(data)
        node.parent = self
        self.children.append(node)

    def get_children(self):
        return self.children

    def num_children(self):
        return len(self.children)

    def get_parent(self):
        return self.parent

class Data:
    """
    A node that contains the data needed for each expanded node.
    """
    def __init__(self, board, num, utility):
        self.board = board
        self.n = num
        self.util = utility
