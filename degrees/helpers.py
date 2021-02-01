class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action



class StackFrontier():

    def __init__ (self):
        self.frontier = []

    def push(self, node):
        self.frontier.append(node)
    
    def contains(self, item):
        return any(node.state == item for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            return None
        else:
            ele = self.frontier[-1]
            self.frontier.pop()
            return ele


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            return None
        else:
            ele = self.frontier[0]        
            self.frontier = self.frontier[1:]
            return ele
        