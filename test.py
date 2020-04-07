import unittest
import kvstore


class InsertTest(unittest.TestCase):

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

        value3 = trie.root.children['a'].children['b'].children['c'].children['d'].children['e'].value
        self.assertEqual(value3, 'third')

    def testnotstringkey(self):
        '''
        insert method should throw a NotStringException if key is not a string
        '''
        trie = kvstore.Trie()
        self.assertRaises(kvstore.NotStringException, trie.insert, 2, 'foo')
        self.assertRaises(kvstore.NotStringException, trie.insert, None, 'foo')

    def testemptystringkey(self):
        '''
        Trying to insert a key, value with  an empty string key should
        raise an EmptyStringException.
        '''
        trie = kvstore.Trie()
        self.assertRaises(kvstore.EmptyStringException, trie.insert, '', 'bar')


class SearchTest(unittest.TestCase):
    
    def testsearch(self):
        '''
        search method should work properly when we search an existing key.
        ''' 
        trie = kvstore.Trie()
        trie.insert('zahra', 'tehrani')
        value = trie.search('zahra')
        self.assertEqual(value, 'tehrani')    

    def testprefix(self):
        '''
        searching a key that is prefix of some other key should work properly.
        '''
        trie = kvstore.Trie()
        trie.insert('foo', 'baz')
        trie.insert('fooz', 'bar')
        self.assertEqual(trie.search('foo'), 'baz')

    def testsuffix(self):
        '''
        searching a key that is suffix of some other key should work properly.
        '''
        trie = kvstore.Trie()
        trie.insert('foo', 'baz')
        trie.insert('fooz', 'bar')
        self.assertEqual(trie.search('fooz'), 'bar')

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
        self.assertRaises(kvstore.EmptyStringException, trie.search, '')

    def testnotstringkey(self):
        '''
        search method should raise NotStringException if defined key is not
        a string.
        '''
        trie = kvstore.Trie()
        self.assertRaises(kvstore.NotStringException, trie.search, None)
        self.assertRaises(kvstore.NotStringException, trie.search, 2)

class DeleteTest(unittest.TestCase):

    def testdeletenode(self):
        '''
        Delete a key, value by an existing key 
        when removig trie nodes is needed should work properly.
        '''
        trie = kvstore.Trie()
        trie.insert('foo', 'bar')
        trie.delete('foo')
        self.assertFalse('f' in trie.root.children)

        trie.insert('foo', 'bar')
        trie.insert('fo', 'baz')
        trie.delete('foo')
        self.assertFalse('o' in trie.root.children['f'].children['o'].children)

        trie.insert('foo', 'bar')
        trie.insert('foz', 'bar')
        trie.delete('foz')
        self.assertFalse('z' in trie.root.children['f'].children['o'].children)
        self.assertTrue('o' in trie.root.children['f'].children['o'].children)

        trie.insert('longword', 'quu')
        trie.delete('longword')
        self.assertFalse('l' in trie.root.children)


    def testremovevalue(self):
        '''
        Delete a value by it's key
        when just value of the node should become None should work properly.
        '''
        trie = kvstore.Trie()
        trie.insert('foo', 'bar')
        trie.insert('fo', 'baz')
        trie.delete('fo')
        self.assertEqual(None, trie.root.children['f'].children['o'].value)

        trie.insert('foz', 'qux')
        trie.insert('fo', 'baz')
        trie.delete('fo')
        self.assertEqual(None, trie.root.children['f'].children['o'].value)

    def testemptystring(self):
        '''
        Trying to delete an empty string should raise an 
        EmptyStringException.
        '''
        trie = kvstore.Trie()
        self.assertRaises(kvstore.EmptyStringException, trie.delete, '')

class DictTest(unittest.TestCase):
    
    def testdict(self):
        '''
        Pass a Trie object to python dict built-in function should return a dictionary.
        '''
        trie = kvstore.Trie()
        self.assertEqual({}, dict(trie))

        trie.insert('foo', 'bar')
        trie.insert('baz', 'qux')
        mydict = dict(trie)
        self.assertEqual({'foo':'bar', 'baz':'qux'}, mydict)

class UpdateTest(unittest.TestCase):

    def testkwarg(self):
        '''
        Pass kwargs to update method should insert all key.values to the trie.
        '''
        trie = kvstore.Trie()
        trie.update(foo='bar', qux='quu')
        value1 = trie.root.children['f'].children['o'].children['o'].value
        value2 = trie.root.children['q'].children['u'].children['x'].value
        self.assertEqual('bar', value1)
        self.assertEqual('quu', value2)


if __name__ == '__main__':
    unittest.main()
