# Binary Search
def binary_search(array,target):
  left=0
  right=len(array-1)
  while (left<=right):
    mid = (left+right)//2
    if (array[mid]==target):
      return mid
    elif (array[mid]>target):
      right = mid-1
    else:
      left = mid+1
  return -1

array = [10,20,32,123,1241]
target=20

result = binary_search(array,target)
if result == -1:
  print("not found")
else:
  print('we found the index of the target is %d'%result)
