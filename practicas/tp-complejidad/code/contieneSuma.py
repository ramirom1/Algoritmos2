def contieneSuma(A,n):
  j = 0
  izq = A[j]
  i = len(A)-1
  der = A[i]
  while izq != der:
    if izq + der > n:
      i -= 1
      der = A[i]
    elif izq + der < n:
      j += 1
      izq = A[j]
    else:
      return True
  return False
  