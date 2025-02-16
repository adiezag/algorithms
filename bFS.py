class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        
        # Initialize a queue
        # using a list that mimics a queue
        queue = [self]

        # using a while loop, the graph is traversed level by level
        # the nodes in the queue will be popped them from the queue
        # the name ("letter") added to the ouput array
        # if nodes have children, add them to the queue

        while len(queue) > 0: # while q is not empty
            current = queue.pop(0) # popping first element from the queue
            array.append(current.name) # adding the name to the output array
            for child in current.children: 
                queue.append(child) # appending children or nodes to the queue

        return array
