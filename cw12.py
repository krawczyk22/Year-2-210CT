'''The programme implements a Binary Search Tree that holds English words.
The programme reads words from a text file, determinates their frequencies,
prints the tree in the pre-order, deletes nodes and finds words and prints the 
traversed path as well as indicates if the word exists in the tree.
The programme provides a menu for its users.'''

#[Source code].http://cumoodle.coventry.ac.uk/
#Task 1
class BinTreeNode(object):
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right=None
              
def tree_insert(tree, item):
  if tree==None:
    tree=BinTreeNode(item)    #definig the roof of the tree
  else:
    if(item < tree.value):
      if(tree.left==None):
        tree.left=BinTreeNode(item)    #adding the node to the left leaf if the leaf is empty
      else:
        tree_insert(tree.left,item)
    else:
      if(tree.right==None):
        tree.right=BinTreeNode(item)    #adding the node to the right leaf if the leaf is empty
      else:
        tree_insert(tree.right,item)
  return tree

#Function that returns the words in a string and their occurrences
def occurrences(words):
  frequencies = dict() 
  for word in words:
    if word in frequencies.keys():
      frequencies[word] += 1    #incrementing the number if a word is found in a tree
    else:
      frequencies[word] = 1
  return frequencies
  
#Function that prints the tree in a pre order
def pre_order(tree):
  print(tree.value)
  if(tree.left!=None):
      pre_order(tree.left)
  if(tree.right!=None):
      pre_order(tree.right)
        
#Function that returns the path traversed while searching for the word along with the information if the word is found
def tree_find(tree, target):
  path = "The path traversed is: "
  tempTree = tree
  while tempTree != None:
    if tempTree.value == target:
      path = path + str(tempTree.value) + " "
      return(path + "\nyes")    #returns the path and indicates that the word is found
    elif tempTree.value > target:  
      path = path + str(tempTree.value) + " "
      tempTree = tempTree.left
    else:
      path = path + str(tempTree.value) + " "
      tempTree = tempTree.right
  return(path + "\nno")    #returns the path and indicates that the word is not found

#Task 2

#Function that finds the minimum value in a tree/subtree
def minValue(tree): 
  while(tree.left is not None): 
    tree = tree.left 
  return tree  
  
#[Source code]. https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
  
def delete_node(tree, value):
  if tree is None: 
        return tree
  else:        #iterating over the tree until the node is found
    if (value < tree.value): 
      tree.left = delete_node(tree.left, value) 
    elif (value > tree.value):
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
        temp = minValue(tree.right)  #finding the minimum value in the subtree
        tree.value = temp.value    #assigning the value to the current value in the tree
        tree.right = delete_node(tree.right , temp.value)      #deleting the minimum found value from the subtree
    return tree
    
if __name__ == '__main__':
  
  try:
    f = open("words.txt", "r")
    string = f.read().split()    #opening the file, taking the values it contains and splitting them into a list
    f.close()
    
    t=tree_insert(None,string[0]);    #definig the root of the tree
    for word in range(1,len(string)):
      tree_insert(t,string[word])   #iterating over the elements and adding them to the tree
          
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
    except ValueError:     #omitting non-integer values
      print("You cannot enter non-integer values")
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
      
#REFERENCES
'''********************************************************************
* Title: Binary Search Tree in Python
* Author: Coventry University
* Date: 2018
* Availability: http://cumoodle.coventry.ac.uk/
***********************************************************************'''

'''********************************************************************
* Title: Binary Search Tree | Set 2 (Delete)
* Author: Geeksforgeeks
* Date: 2018
* Availability: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
***********************************************************************'''
