import unittest
import kvstore


class TestInsert(unittest.TestCase):

    def testinsert(self):
        '''
        insert should add any  key, value properly to the trie.
        '''
        trie = kvstore.Trie()
        trie.insert('zhra', 'tehrani')
        value = trie.root.children['z'].children['h'].children['r'].children['a'].value
        self.assertEqual('tehrani', value)

    def testoverride(self):
        '''
        Inserting a key, value with existing key should override 
        the value of that key with new value
        '''
        trie = kvstore.Trie()
        trie.insert('zhra', 'tehrani')
        trie.insert('zhra', 'musavi')
        value = trie.root.children['z'].children['h'].children['r'].children['a'].value
        self.assertEqual('musavi', value)

    def testprefix(self):
        '''
        insert method should work properly when we add a key, value and
        key has a prefix in the tree
        '''
        trie = kvstore.Trie()
        trie.insert('abcd', 'first')
        trie.insert('abe', 'second')
        trie.insert('abcde', 'third')

        value1 = trie.root.children['a'].children['b'].children['c'].children['d'].value
        self.assertEqual(value1, 'first')
        
        value2 = trie.root.children['a'].children['b'].children['e'].value
        self.assertEqual(value2, 'second')

        value3 = trie.root.children['a'].children['b'].children['c'].children['d'].children['e']
        self.assertEqual(value3, 'third')

    def testnotstringkey(self):
        '''
        insert method should throw a NotStringException if key is not a string
        '''
        trie = kvstore.Trie()
        self.assertRaises(kvstore.NotStringException, trie.insert, 2, 'foo')
        self.assertRaises(kvstore.NotStringException, trie.insert, None, 'foo')
    

class Search(unittest.TestCase):
    
    def testsearch(self):
        '''
        search method should work properly when we search an existing key.
        '''
        
        trie = kvstore.Trie()
        trie.insert('zahra', 'tehrani')
        value = trie.search('zahra')
        self.assertEqual(value, 'tehrani')
    

    def testnotexist(self):
        '''
        search method should return None if searching key doesn't exist.
        '''
        
        trie = kvstore.Trie()
        self.assertEqual(trie.search('zahra'), None)
        
        trie.insert('foo', 'bar')
        self.assertEqual(trie.search('zahra'), None)
        
        self.assertEqual(trie.search('f'), None)

        self.assertEqual(trie.search('fo'), None)

        self.assertEqual(trie.search('fooz'), None)

    def testemptystring(self):
        '''
        search method should return None if we search an empty string
        '''
        
        trie = kvstore.Trie()
        self.assertEqual(trie.search(''), None)


if __name__ == '__main__':
    unittest.main()
