from binarytree import *

class AVLTree:
  root = None

class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None

def rotateLeft(Tree,avlnode):
  newRoot = avlnode.rightnode

  if newRoot.leftnode is not None:
    avlnode.rightnode = newRoot.leftnode
    newRoot.leftnode.parent = avlnode

  newRoot.parent = avlnode.parent

  if avlnode.parent is None:
    Tree.root = newRoot
  else:
    if avlnode.parent.rightnode == avlnode:
      avlnode.parent.rightnode = newRoot
    else:
      avlnode.parent.leftnode = newRoot
  avlnode.parent = newRoot
  newRoot.leftnode = avlnode
  return newRoot

def rotateRight(Tree,avlnode):
  newRoot = avlnode.leftnode

  if newRoot.rightnode is not None:
    avlnode.leftnode = newRoot.rightnode
    newRoot.rightnode.parent = avlnode

  newRoot.parent = avlnode.parent

  if avlnode.parent is None:
    Tree.root = newRoot
  else:
    if avlnode.parent.leftnode == avlnode:
      avlnode.parent.leftnode = newRoot
    else:
      avlnode.parent.rightnode = newRoot
  avlnode.parent = newRoot
  newRoot.righttnode = avlnode
  return newRoot

def getHeight(node):
  if node is None:
    return
  left = getHeight(node.leftnode)
  right = getHeight(node.rightnode)
  if left > right:
    return left + 1
  else:
    return right + 1

def calculateBalanceR(node):
  if node is None:
    return
  leftHeight = getHeight(node.leftnode)
  rightHeight = getHeight(node.rightnode)
  node.bf = leftHeight - rightHeight
  calculateBalanceR(node.leftnode)
  calculateBalanceR(node.rightnode)
  return 

def updateBf(node):
  if node is None:
    return
  leftHeight = getHeight(node.leftnode)
  rightHeight = getHeight(node.rightnode)
  node.bf = leftHeight - rightHeight
  return
  
def calculateBalance(AVLTree):
  if AVLTree.root is None:
    return
  else:
    return calculateBalanceR(AVLTree.root)
  

def reBalance(AVLTree,node):
  if node.bf < 0:
    if node.rightnode.bf > 0:
      rotateRight(AVLTree, node.rightnode)
      rotateLeft(AVLTree, node)
    else:
      rotateLeft(AVLTree, node)
  elif node.bf > 0:
    if node.leftnode.bf < 0:
      rotateLeft(AVLTree, node.leftnode)
      rotateRight(AVLTree, node)
    else:
      rotateRight(AVLTree, node)
  return


def insert(AVLTree, element, key):
  insertBT(AVLTree, element, key)
  node = searchForAKey(key)
  while node: # Recorro desde el nodo insertado hasta la raiz
    updateBf(node) #Actualizo el valor del bf de cada nodo
    if node.bf < -1: #Si esta desbalanceado hacia la izquierda 
      reBalance(AVLTree, node)
    elif node.bf > 1: # Si esta desbalanceado hacia la derecha
      reBalance(AVLTree, node)
    node = node.parent 

  return 

def delete(AVLTree, element):
  node = searchNodeForElement(element)
  node = node.parent
  deleteBT(AVLTree, element)
  while node: # Recorro desde el padre del nodo insertado hasta la raiz
    updateBf(node) #Actualizo el valor del bf de cada nodo
    if node.bf < -1: #Si esta desbalanceado hacia la izquierda 
      reBalance(AVLTree, node)
    elif node.bf > 1: # Si esta desbalanceado hacia la derecha
      reBalance(AVLTree, node)
    node = node.parent
    
  return 

  
          
  