
class Node:
    
    def __init__(self, key=None, value=None, isend=False):
        self.key = key
        self.value = value
        self.children = []
        self.isend = isend

    def insert(self, key, value):
        childnode = children[key[0]]


class Trie:
    root

    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        node = root
        for i in range(len(key)):
            keynode = [x for x in node.children if x == key[i]][0]
            if keynode and i != len(keynode.key):
                node = keynode
            else if keynode and i == len(keynode.key):
                return keynode
            else:
                n = None
                if i == len(keynode):
                    n = Node(key=key, value=value, isend=true)
                else:
                    n = Node()
                node.children.add(n)
                node = n




    
    def 
