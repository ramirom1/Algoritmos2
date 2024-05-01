from trie import * 

def findWords(children,prefix,n,currLen,word):
  if currLen > n:
    return
  i = 0
  origWord = word
  origChildren = children
  while i < len(children):
    word = word + children[i].key
    if children[i].isEndOfWord is True and n == currLen:
      print(word)
    else:
      children = children[i].children
      findWords(children,prefix,n,currLen+1,word)
    i += 1
    word = origWord
    children = origChildren
  return 

def printWords(T,prefix,n):
  if T.root is None:
    return 
  node = searchLastNode(T,prefix)
  children = node.children
  findWords(children,prefix,n,len(prefix)+1,prefix)
  return 