'''The programme implements a graph, lets the users print the nodes,
find a path between two nodes, check if the graph is strongly connected,
implement the Deapth First Search, Breadth First Search and Dijkstra
algorithms. The programme provides a menu for its users.'''

#[Source code]. https://gist.github.com/anirudhjayaraman/272e920079fd8cea97f81487ef1e78a3
#Task 3
#definig the class Node with its connections to other nodes and their weights 
class Node(object):
  def __init__(self, node):
    if node > 0:
      self.node = node
      self.connections = []
      self.distance = []
        
#Function that connects the nodes and adds the weights
  def connection_insert(self, connection, distance):
    if isinstance(connection, Node):
      if connection.node not in self.connections:
        self.connections.append(connection.node)
        connection.connections.append(self.node)
        self.distance.append(distance)
        connection.distance.append(distance)
      else: 
        print("The value is not an instance of the class")

#Defining the Graph class
class Graph(object):
  def __init__(self):
    self.nodes = {}
    self.distances = {}

  def add_to_graph(self, nodes):
    for vertex in nodes:
      self.nodes[vertex.node] = vertex.connections    #adding corresponding nodes and distances to the graph      
      self.distances[vertex.node] = vertex.distance
      
  # Function that returns the whole graph (its nodes, connections and corresponding to them distances)
  def adjacencyList(self):
    if len(self.nodes) >= 1:
      string = "Node\tAdjacency List\tCorresponding distances\n"
      for key in self.nodes.keys():
        string = string + str(key) + ":\t" + str(self.nodes[key]) + "\t\t" + str(self.distances[key]) + "\n"
      return string
    else:
      return dict()  
          
 #Function that returns a list of the nodes used in the menu and in the isConnected class function
  def listOfTheNodes(self):
    listOfNodes=[]
    for key in self.nodes.keys():
      listOfNodes.append(key)
    return listOfNodes  
    
  #Function that returns the path traversed between two nodes
  def isPath(self, start, finish, path=None):
    if path == None:
      path=[]
    path.append(start)
    if start==finish:
      return path
    if start not in self.nodes or finish not in self.nodes:
      return("At least one of the nodes is not in the graph")
    for node in self.nodes[start]:    # iterates through the connected nodes
      if node not in path:
        extendPath = self.isPath(node, finish, path)
        if extendPath: return extendPath    # returns the path only if the path is found
    return False    # if the path is not found, it returns False
    
#Task 5
    
#Function that implements the Depth-First Search algorithm
  def depthFirstSearch(self, vertex):
    Stack=[]
    visited=[]
    Stack.append(vertex)
    graph=self.nodes
    while len(Stack) > 0:
      index = Stack[-1]
      Stack.pop()
      if index not in visited:
        visited.append(index)
        for node in graph[index]:
          Stack.append(node)
    return visited
    
#Function that implements the Breadth-First Search algorithm
  def breadthFirstSearch(self, vertex):
    Queue=[]
    visited=[]
    Queue.append(vertex)
    graph=self.nodes
    while len(Queue) > 0:
      index = Queue[0]
      Queue.pop(0)
      if index not in visited:
        visited.append(index)
        for node in graph[index]:
          Queue.append(node)
    return visited 

#Task 4
  
  #Function that indicates if the graph is strongly connected
  def isConnected(self):
    NodesInTheGraph=self.listOfTheNodes()    #assigning the list of all of the nodes from the Graph
    NumberOfVisitedNodes=len(self.breadthFirstSearch(NodesInTheGraph[0]))    #assigning the number of nodes returned from the BFS function
    NumberOfAllNodes=len(NodesInTheGraph)    #assigning the number of all nodes in the graph
    if NumberOfAllNodes == NumberOfVisitedNodes:
      return("Yes")
    else:
      return("No")
    
#Task 6
    
  def dijkstra(self, source, destination):
    current = source
    dictionary = {}
    previousNodes = {}
    for key in self.nodes.keys():
      dictionary[key] = float("inf")  # defining the traversal weight of the nodes as infinity
      previousNodes[key] = []
    dictionary[source] = 0     # the traversal weight of the starting node is 0
    visited=[] 
    
    while current != destination:
      index = 0
      for vertex in self.nodes[current]: 
        if dictionary[current] + self.distances[current][index] < dictionary[vertex]:
          dictionary[vertex] = dictionary[current] + self.distances[current][index]    #updating the traversal values
          previousNodes[vertex] = previousNodes[current] + [current]     #keeping track on the previous node
          index+=1
        else: index+=1
      visited.append(current)
      minimum = float("inf")
      for node in dictionary:
        if (node not in visited) and (dictionary[node] < minimum):
          current = node
          minimum = dictionary[node]
    previousNodes[destination] += [destination]
    
    print("The smallest weight is: " + str(dictionary[destination]) + 
          "\nThe path traversed is: " + str(previousNodes[destination]))   #returning the weight of the path traversed
      
# Executing the class functions
def graph(g):
  print(str(g.adjacencyList()))

def path(g, start, finish):
  f = open("path.txt", "w+")
  f.write(str(g.isPath(start, finish)))
  f.close
  
def connected(g):
  print(str(g.isConnected()))
  
def dfs(g,v):
  f = open("DTSBFS.txt", "w+")
  f.write("DFS: " + str(g.depthFirstSearch(v)) + "\n")
  f.close()
  
def bfs(g,v):
  f = open("DTSBFS.txt", "a")
  f.write("BFS: " + str(g.breadthFirstSearch(v)))
  f.close
  
def dijkstra(source, destination):
  g.dijkstra(source, destination)
  
if __name__ == '__main__':  
  
  # Defining the nodes
  a = Node(1)
  b = Node(2)
  c = Node(3)
  d = Node(4)
  e = Node(5)
  f = Node(6)
  h = Node(7)
  i = Node(8)

  # Defining the edges and assigning their weights
  a.connection_insert(b, 8)
  c.connection_insert(a, 1)
  d.connection_insert(e, 2)
  d.connection_insert(a, 6)
  e.connection_insert(f, 3)
  c.connection_insert(h, 3)
  d.connection_insert(h, 3)
  i.connection_insert(b, 4)
  i.connection_insert(h, 6)
  i.connection_insert(f, 3)

  #Defining the Graph
  g = Graph()
  g.add_to_graph([a,b,c,d,e,f,h,i])

  basecase=0

  #Implementation of the menu
  while basecase ==0:
    print("What do you want to do?")
    print("1. Print the graph")
    print("2. Find a path between two nodes")
    print("3. Check if the graph is strongly connected")
    print("4. Do the BFS and DFS")
    print("5. Do the Dijkstra algorithm")
    print("6. Exit")

    try:
      answer=int(input(""))
    except ValueError: 
      print("You cannot enter no-integer values")
      answer=7

    if answer == 1:
      graph(g)

    elif answer == 2:
      try:
        firstVetex=int(input("What is the starting node? "))
        secondVetex=int(input("What is the finishing node? "))
        path(g, firstVetex, secondVetex)
      except ValueError: print("The value has to be an integer")

    elif answer == 3:
      connected(g)

    elif answer == 4:
      try:
        startVertex=int(input("What is the first vertex? "))
        if startVertex in g.listOfTheNodes():
          dfs(g, startVertex)
          bfs(g, startVertex)
        else: print("Such value does not exist in the graph")
      except ValueError: print("The value has to be an integer")

    elif answer == 5:
      try:
        sourceDijkstra=int(input("What is the source node? "))
        destinationDijkstra=int(input("What is the destination node? "))
        dijkstra(sourceDijkstra, destinationDijkstra)
      except ValueError: print("The value has to be an integer")

    elif answer == 6:
      basecase=1

    else: print("There is no such option")
      
'''********************************************************************
* Title: Implementing Undirected Graphs in Python
* Author: anirudhjayaraman
* Date: 2016
* Availability: https://gist.github.com/anirudhjayaraman/272e920079fd8cea97f81487ef1e78a3
***********************************************************************'''

'''********************************************************************
* Title: Week 7 - More Graphs
* Author: Diana Hintea
* Date: 2018
* Availability: http://cumoodle.coventry.ac.uk/
***********************************************************************''' 
