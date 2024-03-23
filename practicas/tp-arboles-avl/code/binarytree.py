from linkedlist import *

class BinaryTree:
  root = None

class BinaryTreeNode:
  key = None
  value = None
  leftnode = None 
  rightnode = None
  parent = None 

def recursiveSearch(nodo,element):
  if nodo is None:
    return None
  if nodo.value == element:
    return nodo.key
  elif nodo.rightnode is not None:
    result = recursiveSearch(nodo.rightnode,element)
    if result is not None:
      return result
  if nodo.leftnode is not None:
    result = recursiveSearch(nodo.leftnode,element)
    if result is not None:
      return result
  else:
    return None

#SEARCH    
def search(B,element):
  if B.root is None:
    return None
  else:
    result = recursiveSearch(B.root,element)
    if result is None:
      return None
    else:
      return result

#Funcion que dado un arbol binario, busca una cierta key y 
#devuelve el nodo que contiene cierta key, o None si no lo encuentra
def searchForAKey(nodo,key):
  if nodo is None:
    return
  if nodo.key == key:
    return nodo
  elif nodo.rightnode is not None:
    result = searchForAKey(nodo.rightnode,key)
    if result is not None:
      return result
  if nodo.leftnode is not None:
    result = searchForAKey(nodo.leftnode,key)
    if result is not None:
      return result

def recursiveInsert(B,newNode,node):
  if node is None:
    B.root = newNode
    return newNode.key
  if newNode.key > node.key:
    if node.rightnode is None:
      newNode.parent = node
      node.rightnode = newNode
    else:
      recursiveInsert(B,newNode,node.rightnode)
  else:
    if node.leftnode is None:
      newNode.parent = node
      node.leftnode = newNode
    else:
      recursiveInsert(B,newNode,node.leftnode)
  return newNode.key

#INSERT
def insertBT(B,element,key):
  newNode = BinaryTreeNode()
  newNode.key = key 
  newNode.value = element
  if searchForAKey(B.root,key) is not None:
    return None
  else:
    return recursiveInsert(B,newNode,B.root)  


#Esta funcion devuelve un puntero que indica donde esta el nodo
#que tiene el elemento solicitado
def searchNodeForElement(node,element):
  if node.value == element:
    return node
  elif node.rightnode is not None:
    returnValue = searchNodeForElement(node.rightnode,element)
    if returnValue is not None:
      return returnValue
  if node.leftnode is not None:
    returnValue = searchNodeForElement(node.leftnode,element)
    if returnValue is not None:
      return returnValue

def searchSmallestBiggest(node):
  if node.leftnode is not None:
    current = searchSmallestBiggest(node.leftnode)
    if current is not None:
      return current
  else:
    return node

def deleteNode(B,nodeToDelete):
  #El nodo a eliminar es una hoja    
  if nodeToDelete.rightnode is None and nodeToDelete.leftnode is None: 
    if nodeToDelete == B.root:
      B.root = None
    else:
      if nodeToDelete.key > nodeToDelete.parent.key:
        nodeToDelete.parent.rightnode = None
      else:
        nodeToDelete.parent.leftnode= None
  #El nodo a eliminar tiene dos hijos   
  elif nodeToDelete.rightnode is not None and nodeToDelete.leftnode is not None:
    smallest = searchSmallestBiggest(nodeToDelete.rightnode)
    smallest.leftnode = nodeToDelete.leftnode
    if smallest.parent == nodeToDelete:
      smallest.parent = None
      smallest.leftnode.parent = smallest
    else:
      smallest.parent.leftnode = None
      smallest.rightnode = nodeToDelete.rightnode

    if nodeToDelete == B.root:
      B.root = smallest
    else:
      if nodeToDelete.key > nodeToDelete.parent.key:
        nodeToDelete.parent.rightnode = smallest
      else:
        nodeToDelete.parent.leftnode = smallest
    #El nodo a eliminar tiene un hijo  
  else:
    if nodeToDelete.rightnode is None:
      if nodeToDelete.leftnode.key > nodeToDelete.parent.key:
        nodeToDelete.parent.rightnode = nodeToDelete.leftnode
      else:
        nodeToDelete.parent.leftnode = nodeToDelete.leftnode
    else:
      if nodeToDelete.leftnode is None:
        if nodeToDelete.rightnode.key > nodeToDelete.parent.key:
          nodeToDelete.parent.rightnode = nodeToDelete.rightnode
        else:
          nodeToDelete.parent.leftnode = nodeToDelete.rightnode
  return nodeToDelete.key

#DELETE
def deleteBT(B,element):
  if search(B,element) is None:
    return None
  else:
    nodeToDelete = searchNodeForElement(B.root,element)
    return deleteNode(B,nodeToDelete)

#DELETE KEY
def deleteKey(B,key):
  node = searchForAKey(B.root,key)
  if node is None:
    return None
  else:
    return deleteNode(B,node)

#ACCESS
def access(B,key):
  node = searchForAKey(B.root,key)
  if node is None:
    return None
  else:
    return node.value

#UPDATE
def update(B,element,key):
  node = searchForAKey(B.root,key)
  if node is None:
    return None
  else:
    node.value = element
    return key
