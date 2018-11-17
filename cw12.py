'''The programme implements a Binary Search Tree that hoads English words.
The programme reads words from a text file, determinates their frequencies,
prints the tree in pre-order, deleted a node and finds words and prints the 
traversed path as well as indicated if the word exists in the tree.
The programme provides a menu for its users. The code has been created
based on the code provided on the Coventry University Moodle website, and 
changed respectively. The programmehas been created by implementing pseudocodes'''

class BinTreeNode(object):
  def __init__(self, value):
      self.value=value
      self.left=None
      self.right=None
              
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

#Function that returns the words in a string and their occurrences
def occurrences(words):
  frequencies = dict()
  for word in words:
    if word in frequencies.keys():
      frequencies[word] += 1
    else:
      frequencies[word] = 1
  return frequencies
  
def pre_order(tree):
  print(tree.value)
  if(tree.left!=None):
      pre_order(tree.left)
  if(tree.right!=None):
      pre_order(tree.right)
        
#Function tam returns the path traversed while searching for the word along with the information if the word is found
def tree_find(tree, target):
  path = "The path traversed is: "
  tempTree = tree
  while tempTree != None:
    if tempTree.value == target:
      path = path + str(tempTree.value) + " "
      return(path + "\nyes")
    elif tempTree.value > target:  
      path = path + str(tempTree.value) + " "
      tempTree = tempTree.left
    else:
      path = path + str(tempTree.value) + " "
      tempTree = tempTree.right
  return(path + "\nno")

def minValue(tree): 
    while(tree.left is not None): 
        tree = tree.left 
    return tree  
  
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
        temp = tree.right  #storing the right subtree in a temporary variable
        tree = None    #deleting the current node
        return temp    #returning the stored subtree
      elif tree.right is None : 
        temp = tree.left  
        tree = None
        return temp 
      else:
        temp = minValue(tree.right)  #Finding the minimum value in the subtree
        tree.value = temp.value    #Assigning the value to the current value in the tree
        tree.right = delete_node(tree.right , temp.value)      #deleting minimum found value from the subtree
    return tree
    
if __name__ == '__main__':
  
  try:
    f = open("words.txt", "r")
    string = f.read().split()  
    f.close()
    
    t=tree_insert(None,string[0]);    #definig the root of the tree
    for word in range(1,len(string)):
      tree_insert(t,string[word])   
          
  except IndexError: print("The file does not have any values")   
    
  basecase=0
  
  #Implementation of the menu
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
