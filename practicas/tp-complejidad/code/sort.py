def sort(list):
#Primero lo que hacemos es ordenar la lista, lo que tiene una complejidad de n log n
  list.sort()
  if len(list) % 2 == 0:
    mid = list[(len(list)-1) // 2]
    list[(len(list)-1) // 2] = list[len(list)-2]
    list[len(list)-2] = mid
  else:
    mid = list[len(list) // 2]
    list[len(list)//2] = list[len(list)-1]
    list[len(list)-1] = mid
  return list  
