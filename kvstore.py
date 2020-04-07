
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
        Raises EmptyStringException if key is an empty string.
        Raises NotStringException if key is not an string.
        '''
        if not isinstance(key, str):
            raise NotStringException()
        elif not key:
            raise EmptyStringException()

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
        Returns None if key doesn't exist in dictionary
        Raises EmptyString exception if key is an empty string.
        Raises NotStringException if key is not an string.
        '''
        if not isinstance(key, str):
            raise NotStringException()
        elif not key:
            raise EmptyStringException()

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

    def delete(self, key):
        '''
        Delete a key, value pair by the key from the trie
        Raises a KeyError if the key doesn't exist in the trie.
        '''
        if not isinstance(key, str):
            raise NotStringException()
        elif not key:
            raise EmptyStringException()

        removeinfo = (self.root, key[0]) 
        node = self.root
        for i in range(len(key)):
            if len(node.children) > 1 or node.value:
                removeinfo = (node, key[i])
           
            node = node.children[key[i]]

        if node.children:
            node.value = None
        else:
            father = removeinfo[0]
            char = removeinfo[1]

            del father.children[char]
                
                
class NotStringException(Exception): pass
class EmptyStringException(Exception): pass

