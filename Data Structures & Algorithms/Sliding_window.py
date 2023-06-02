# Sliding window
def maxSum(arr, windowSize):
  array_size = len(arr)

  if array_size < windowSize:
    print('invalid operation')
    return -1
  
  window_sum = sum([arr[i] for i in range(windowSize)])
  max_sum = 0
  for i in range(array_size - windowSize):
    window_sum = window_sum + arr[i+windowSize] - arr[i]
    max_sum = max(max_sum, window_sum)
  return max_sum 

# Brute force of sliding window
# Brute force
def maxSum(arr, windowSize):
  array_size = len(arr)

  if array_size < windowSize:
    print('invalid operation')
    return -1
  
  window_sum = 0
  max_sum = 0
  for i in range(array_size-windowSize+1):
    for j in range(windowSize):
      window_sum = window_sum + arr[j]
    max_sum = max(max_sum, window_sum)
  return max_sum


maxSum([10,213,1241,1239,12,14139123,231,123429,3],9)
