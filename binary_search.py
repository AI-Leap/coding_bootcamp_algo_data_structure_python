def binary_search(my_list,item):
  '''
  my_list: the input list
  item: the number to be searched
  Takes in my_list and item as parameters
  If the item is found, returns the index number
  If the item is not found, return None
  '''
  low = 0
  high = len(my_list)-1
  while low <= high:
    mid = round((low + high)/2)
    name = my_list[mid]
    if name == item:
      return mid
    if name > item:
      high = mid-1
    else:
      low = mid+1
  return None

my_list = [2,4,6,8,10]
print(binary_search(my_list, 6))
print(binary_search(my_list, 7))
