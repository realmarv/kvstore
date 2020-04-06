import unittest
import kvstore


class TestInsert(unittest.TestCase):

    def testinsert(self):
        trie = kvstore.Trie()
        trie.insert('zhra', 'tehrani')
        value = trie.root.children['z'].children['h'].children['r'].children['a'].value
        self.assertEqual('tehrani', value)

    def testoverride(self):
        trie = kvstore.Trie()
        trie.insert('zhra', 'tehrani')
        trie.insert('zhra', 'musavi')
        value = trie.root.children['z'].children['h'].children['r'].children['a'].value
        self.assertEqual('musavi', value)

    def testmiddle(self):
        trie = kvstore.Trie()
        trie.insert('abcd', 'first')
        trie.insert('abe', 'second')
        
        value1 = trie.root.children['a'].children['b'].children['c'].children['d'].value
        self.assertEqual(value1, 'first')
        
        value2 = trie.root.children['a'].children['b'].children['e'].value
        self.assertEqual(value2, 'second')


class Search(unittest.TestCase):
    
    def testsearch(self):
        trie = kvstore.Trie()
        trie.insert('zahra', 'tehrani')
        value = trie.search('zahra')
        self.assertEqual(value, 'tehrani')


if __name__ == '__main__':
    unittest.main()
