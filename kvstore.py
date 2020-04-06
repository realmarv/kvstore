
class Node:
    
    def __init__(self, value=None):
        self.value = value
        self.children = dict()

    def insert(self, key, value):
        childnode = children[key[0]]


class Trie:
    
    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        node = self.root
        for i in range(len(key)):
            try:
                keynode = node.children[key[i]]
                if i != len(key)-1:
                    node = keynode
                    continue
                else:
                    keynode.value = value
                    return keynode
            except:
                if i != len(key) - 1:
                    n = Node()
                    node.children[key[i]] = n
                    node = n
                
                else:
                    n = Node(value)
                    node.children[key[i]] = n
                    return n
              

    def search(self, key):
        node = self.root
        for i in range(len(key)):
            keynode = node.children[key[i]]
            try:
                keynode = node.children[key[i]]
                if i != len(key) - 1:
                    node = keynode
                else:
                    return keynode.value
            except:
                return Node


    

