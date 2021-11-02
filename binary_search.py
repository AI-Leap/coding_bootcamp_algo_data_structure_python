def binary_search(my_list,item):
  '''
  Search item in the sorted list.
  INPUT:
  my_list : list of items
  item: item to be searched
  OUTPUT:
  mid : index of search item
  '''
  my_list.sort()
  low = 0
  high = len(my_list)-1
  while low <= high:
    mid = round((low + high)/2)
    guess = my_list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid-1
    else:
      low = mid+1
  return None

my_list = [5,9,1,7,4]
print(binary_search.__doc__)

if __name__ == '__main__':
  print(binary_search(my_list,9))


