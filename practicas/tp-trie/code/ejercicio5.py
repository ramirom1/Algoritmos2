from trie import *

def getWords(children,word,words):
  if children == None:
    return
  i = 0
  origWord = word
  origChildren = children
  while i < len(children):
    word = word + children[i].key
    if children[i].isEndOfWord is True:
      words.append(word)
    getWords(children[i].children,word,words)
    i += 1
    word = origWord
    children = origChildren
  return words

def equalTries(T1,T2):
  if T1.root is None and T2.true is None:
    return True
  words = []
  word = ""
  words = getWords(T1.root.children,word,words)
  for i in range(0,len(words)):
    if search(T2,words[i]) is False:
      return False
  return True


