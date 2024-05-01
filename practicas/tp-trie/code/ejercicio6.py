from trie import *

def reverseWord(T,children,word):
  if children == None:
    return
  returnValue = False
  i = 0
  origWord = word
  origChildren = children
  while i < len(children):
    word = word + children[i].key
    if children[i].isEndOfWord is True:
      reverse = word[::-1]
      print(search(T,reverse))
      if search(T,reverse) is True:
        return True
    returnValue = reverseWord(T,children[i].children,word)
    i += 1
    word = origWord
    children = origChildren
  return returnValue

def searchReversedWords(T):
  if T.root is None:
    return False
  return reverseWord(T,T.root.children,"")


