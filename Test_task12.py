import unittest
import cw12
    
"""The programme tests the cw12.py file"""
  
class TestBinTree(unittest.TestCase):
    
  def setUp(self):
    f = open("words.txt", "r")
    self.path = f.read().split()  
    f.close()
    
    self.t=cw12.tree_insert(None,self.path[0]);    #defining the tree and assigning the words into the tree
    for word in range(1,len(self.path)):
      cw12.tree_insert(self.t,self.path[word]) 
    
  def test_find_path(self):
    self.path=str(cw12.tree_find(self.t, "programme"))
    self.assertEqual(self.path, "The path traversed is: This is the simple programme \nyes")
    
  def test_occurrences(self):
    occurrences_function = str(cw12.occurrences(self.path))
    occurrences_manual="OrderedDict([('This', 1), ('is', 1), ('the', 2), ('simple', 1), ('text', 1), ('for', 1), ('programme', 1)])"
    self.assertEqual(occurrences_function, occurrences_manual)
    
  def test_node_delete(self):
    self.t_copy=cw12.tree_insert(None,self.path[0]);
    for word in range(1,len(self.path)-1):
      cw12.tree_insert(self.t_copy,self.path[word])     
    
    self.t=cw12.delete_node(self.t, "programme")
    
    self.assertIs(self.t, self.t_copy)
    
if __name__ == '__main__':
    unittest.main()
