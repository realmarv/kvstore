import json


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

    def update(self, udict={}, uiter=[], **kwargs):
        '''
        Insert all key, values to the trie.
        udict : a dictionary of key, values
        uiter : an iterable of key, values
        kwargs : arbitrary number of key, values
        '''
        for key, value in kwargs.items():
            self.insert(key, value)

        for key, value in udict.items():
            self.insert(key, value)

        for key, value in uiter:
            self.insert(key, value)


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
                
    def __iter__(self):
        '''
        Returns an iterator so that user can iterate over trie key, values.
        '''
        return iter(self.__getitems())

    def __getitems(self):
        '''
        Returns a list of all (key, value) items in the trie.
        '''
        items = []
        self.__dfs(self.root, '', items)
        return items
        
    def __dfs(self, node, tonowstring, items):
        '''
        Travers the trie and put (key, value) items in items list
        '''
        if node.value:
            items.append((tonowstring, node.value))
        
        for char, childnode in node.children.items():
            self.__dfs(childnode, (tonowstring + char), items)

            
    def saveinfo(self, path, override=False):
        '''
        Save dict of key, valus in json format in a file.
        path : path of the file for saving trie.
        override : a boolean defines existing file should be overridden or not
        
        raises an error if override is False and the file exists.
        '''
        tag = 'x'
        if override:
            tag = 'w'

        with open(path, tag) as f:
            data = json.dumps(dict(self))
            f.write(data)
            


class NotStringException(Exception): pass
class EmptyStringException(Exception): pass

