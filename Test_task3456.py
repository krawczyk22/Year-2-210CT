import unittest
import cw3456

"""The programme tests the cw3456.py file"""

class TestGraph(unittest.TestCase):
  
  def setUp(self):
    self.a = cw3456.Node(1)   #defining the nodes
    self.b = cw3456.Node(2)
    self.c = cw3456.Node(3)
    self.d = cw3456.Node(4)
    self.e = cw3456.Node(5)
    self.f = cw3456.Node(6)
    self.h = cw3456.Node(7)
    self.i = cw3456.Node(8)
    
    self.a.connection_insert(self.b, 8)    #connecting the nodes and assigning the weights
    self.c.connection_insert(self.a, 1)
    self.d.connection_insert(self.e, 2)
    self.d.connection_insert(self.a, 6)
    self.e.connection_insert(self.f, 3)
    self.c.connection_insert(self.h, 3)
    self.d.connection_insert(self.h, 3)
    self.i.connection_insert(self.b, 4)
    self.i.connection_insert(self.h, 6)
    self.i.connection_insert(self.f, 3)
    
    self.g = cw3456.Graph()    #defining the graph
    self.g.add_to_graph([self.a,self.b,self.c,self.d,self.e,self.f,self.h,self.i])
  
  def test_list_of_nodes(self):
    list_nodes_result = self.g.listOfTheNodes()
    self.assertEqual(list_nodes_result, [1, 2, 3, 4, 5, 6, 7, 8])
  
  def test_path(self):
    pathFunction = self.g.isPath(2, 4)
    self.assertEqual(pathFunction, [2, 1, 3, 7, 4])
    
  def test_is_strongly_connected(self):
    connected = self.g.isConnected()
    self.assertEqual(connected, "Yes")
    
  def test_DFS(self):
    DFS_result = self.g.depthFirstSearch(1)
    self.assertEqual(DFS_result, [1, 4, 7, 8, 6, 5, 2, 3])
    
  def test_BFS(self):
    BFS_result = self.g.breadthFirstSearch(1)
    self.assertEqual(BFS_result, [1, 2, 3, 4, 8, 7, 5, 6])
    
  def test_dijkstra(self):
    dijkstra_result = self.g.dijkstra(2,4)
    self.assertEqual(dijkstra_result, "The smallest weight is: 12\nThe path traversed is: [2, 8, 6, 5, 4]")
    
  def test_path_file(self):
    f = open("path.txt","r")
    path_file = f.read()
    f.close
    self.assertEqual(path_file, "[2, 1, 3, 7, 4]")
    
  def test_DTS_and_BFS_4(self):
    f = open("DTSBFS.txt","r")
    first_line = f.readline()
    second_line = f.readline()
    f.close
    self.assertEqual(first_line, "DFS: [4, 7, 8, 6, 5, 2, 1, 3]\n")
    self.assertEqual(second_line, "BFS: [4, 5, 1, 7, 6, 2, 3, 8]")
    
if __name__ == '__main__':
    unittest.main()
    
