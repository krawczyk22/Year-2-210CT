#defining the binary tree class
class BinTreeNode(object):
  def __init__(self, value):
      self.value=value
      self.left=None
      self.right=None

#Inserting a node to the tree              
def tree_insert(tree, item):
  if tree==None:
      tree=BinTreeNode(item)
  else:
      if(item < tree.value):
          if(tree.left==None):
              tree.left=BinTreeNode(item)
          else:
              tree_insert(tree.left,item)
      else:
          if(tree.right==None):
              tree.right=BinTreeNode(item)
          else:
              tree_insert(tree.right,item)
  return tree

def occurrences(words):
  frequencies = dict()
  for word in words:
    if word in frequencies.keys():
      frequencies[word] += 1
    else:
      frequencies[word] = 1
  return frequencies
  
#Function that prints the tree in pre-order
def pre_order(tree):
  print(tree.value)
  if(tree.left!=None):
      pre_order(tree.left)
  if(tree.right!=None):
      pre_order(tree.right)
        
#Function showing the path traversed while searching a node and indicating if the node is found
def tree_find(tree, target):
  path = "The path traversed is: "
  r = tree
  while r != None:
    if r.value == target:
      path = path + str(r.value) + " "
      return(path + "\nyes")
    elif r.value > target:  
      path = path + str(r.value) + " "
      r = r.left
    else:
      path = path + str(r.value) + " "
      r = r.right
  return(path + "\nno")

def minValue(tree): 
    node = tree
    while(node.left is not None): 
        node = node.left 
    return node  
  
#Function that deletes a node from the binary tree
def delete_node(tree, value):
  if tree is None: 
        return tree
  else:
    if (value < tree.value): 
          tree.left = delete_node(tree.left, value) 
    elif(value > tree.value): 
          tree.right = delete_node(tree.right, value) 
    else:
      if tree.left is None : 
        temp = tree.right  
        tree = None 
        return temp  
      elif tree.right is None : 
        temp = tree.left  
        tree = None
        return temp 
      else:
        temp = minValue(tree.right) 
        tree.value = temp.value
        tree.right = delete_node(tree.right , temp.value) 
    return tree
  
    
if __name__ == '__main__':
  
  try:
    f = open("words.txt", "r")
    string = f.read().split()  #opening the file, reading the string and splitting it into a list
    f.close()
    
    t=tree_insert(None,string[0]);  #defining the tree (assigning the root)

    for word in range(1,len(string)):
      tree_insert(t,string[word])   #iterating through the list of words and assigning them to the list
          
  except IndexError: print("The file does not have any values")   #throwing an error while the text file is empty
  
  basecase=0
  while basecase == 0:
    print("What do you want to do?")
    print("1. Print the list of words with their occurrences")
    print("2. Print the list in pre_order")
    print("3. Find a word")
    print("4. Delete a node")
    print("5. Exit")
    
    try:
      answer=int(input(""))
    except ValueError: 
      print("You cannot enter no-integer values")
      answer=6

    if answer == 1:
      print(str(occurrences(string)))
    elif answer == 2:
      pre_order(t)
    elif answer == 3:
      answerFind=str(input("What is the word you want to find? \n"))
      print(tree_find(t, answerFind))
    elif answer == 4:
      answerDelete=str(input("What is the word you want to delete? \n"))
      if answerDelete not in string:
        print("There is no such word in the tree")
      else: t=delete_node(t, answerDelete)
    elif answer == 5:
      basecase=1
    else: print("There is no such option")
