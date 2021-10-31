def binary_search(list,item):
  low = 0
  high = len(list)-1
  while low <= high:
    mid = int((low + high)/2)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid-1
    else:
      low = mid+1
  return None

list = [2,4,6,8,10]
print(binary_search(list, 6))
print(binary_search(list, 7))