class DictionaryNode:
  key = None
  value = None


dictionary = [[]] * 2

def insert(D, key, value):
  node = DictionaryNode()
  node.key = key
  node.value = value
  position = key % 9
  D[position].append(node)
  return D

def search(D,key):
  position = key % 9 
  list = D[position]
  for node in list:
    if node.key == key:
      return node.value
  return None  

def delete(D,key):
  position = key % 9 
  list = D[position]
  for node in list:
    if node.key == key:
      list.remove(node)
  return D