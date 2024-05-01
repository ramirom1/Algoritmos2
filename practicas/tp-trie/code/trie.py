class Trie:
  root = None

class TrieNode:
  parent = None
  children = None
  key = None
  isEndOfWord = False

#Funcion que busca el caracter en una lista y devuelve el indice donde lo encontró
def compare(list,char):
  for i in range(0,len(list)):
    if list[i].key == char:
      return i
  return None

def addChilds(node,element,charIndex):
  while charIndex != len(element):
    newNode = TrieNode()
    newNode.parent = node
    newNode.key = element[charIndex]
    newNode.children = []
    node.children.append(newNode)
    charIndex += 1
    node = newNode
  node.isEndOfWord = True
  return

def insertR(node,element,charIndex):
  #Reviso que el indice de caracter no se haya pasado del limite
  if charIndex == len(element):
    return
  #Busco el caracter en los hijos del nodo  
  index = compare(node.children,element[charIndex])

  #Divido en dos partes, si el caracter no pertenece a los hijos, o si pertenece
  if index == None:
    addChilds(node,element,charIndex)
  else:
    nextNode = node.children[index]
    if charIndex == len(element) - 1:
      nextNode.isEndOfWord = True
    insertR(nextNode,element,charIndex + 1)
  return

def insert(T,element):
  if T.root == None:
    a = TrieNode()
    a.children = []
    a.key = ""
    T.root = a
  if element is None:
    return
  return insertR(T.root,element,0)

def search(T,element):
  if element is None:
    return False
  node = T.root
  charIndex = 0
  while charIndex != len(element):
    index = compare(node.children,element[charIndex])
    if index is None:
      return False
    node = node.children[index]
    charIndex += 1
  return node.isEndOfWord

def print_nary_tree(root, depth=0):
  if root is None:
    return
  print("  " * depth + str(root.key) + (" → end" if root.isEndOfWord else ""))
  if root.children:
    for child in root.children:
      print_nary_tree(child, depth + 1)

#Funcion search aux para delete que devuelve el ultimo nodo de la palabra solicitada 

def searchLastNode(T,element):
  if element is None:
    return False
  node = T.root
  charIndex = 0
  while charIndex != len(element):
    index = compare(node.children,element[charIndex])
    if index is None:
      return False
    node = node.children[index]
    charIndex += 1
  return node

def deleteChild(father, element):
  i = 0
  while i < len(father.children):
    node = father.children[i]
    if node.key == element:
      father.children.remove(node)
    i += 1   

def delete(T,element):
  info = searchLastNode(T,element)
  #La palabra no se encuentra
  if info is False:
    return False
  #La palabra se encontró
  lastNode = info
  #La palabra esta incluida en otra
  if len(lastNode.children) != 0:
    lastNode.isEndOfWord = False
    return True
  #Hay otras palabras incluidas en el o la palabra es unica
  else:
    father = lastNode.parent
    index = len(element) - 1
    #Me fijo si la palabra insertada es la unica en el arbol
    if father == T.root:
        deleteChild(father,element[index])
    else:
      while father.isEndOfWord != True and len(father.children) == 1:
        deleteChild(father,element[index])
        index -= 1
        father = father.parent
      deleteChild(father,element[index])  
      return True   

def autoCompletar(Trie,cadena):
  node = searchLastNode(Trie,cadena)
  string = ""
  while len(node.children) == 1 and node.isEndOfWord is False:
    string = string + node.children[0].key
    node = node.children[0]
  return string
