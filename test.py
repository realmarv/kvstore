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


if __name__ == '__main__':
    unittest.main()
