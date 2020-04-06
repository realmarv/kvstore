
class Node:
    
    def __init__(self, value=None):
        self.value = value
        self.children = dict()


class Trie:
    
    def __init__(self):
        self.root = Node()

    def insert(self, key, value):
        '''
        Insert a key value to the trie data structure
        Key must be string.
        '''
        if not isinstance(key, str):
            raise NotStringException()

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
        '''
        Search a value in dictionary by it's key
        Returns None if the key doesn't exist in the dictionary.
        '''
        node = self.root
        for i in range(len(key)):
            try:
                keynode = node.children[key[i]]
                if i != len(key) - 1:
                    node = keynode
                else:
                    return keynode.value
            except:
                return None


class NotStringException(Exception): pass
    

