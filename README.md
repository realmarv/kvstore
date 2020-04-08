# kvstore

key, value store (kvstore) is a library to store key values in a dictionary.
the data structure that is used in this library is trie or prefix tree.

### Usage

* Create  
use kvstore.Trie() to create a new trie.
```
trie = kvstore.Trie()
```
  
* Insert  
use insert method to insert a key, value to the trie.
```
trie.insert(key, value)
```
  
* Update  
use update method to insert arbitrary number of key, values to the trie.
```
trie.update(key1=value1, key2=value2, key3=value3)
  
trie.update(udict={'foo':'bar', 'qux':'quu'})
  
trie.update(uiter=[('foo', 'bar'), ('qux', 'quu')])
```
  
* Search  
use search method to get a value in trie by it's key.
```
value = trie.search(key)
```
  
* Delete  
use delete method to delete a value by it's key from the trie.
```
trie.delete(key)
```
  
* Save  
use saveinfo to save trie key, values in a file in json format.
```
trie.saveinfo('filename.txt')
```
  
* Load  
use loadinfo to load key, values from a file in json format and add them to
the trie.
```
trie.loadinfo('filename.txt')
```
* Iterate over a Trie object
you can pass a Trie object to python built-in dict function and get a dictionary of key, values. or simply iterate over a trie in a loop.
```
kvdict = dict(trie)

for key, value in trie:
  do something
```
