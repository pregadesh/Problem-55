# rearrange the numbers in an array in even in ascending order and odd in descending order but in the initial position
def esh(arr):
  n = len(arr)
  eve_arr = [0]*n
  odd_arr = [0]*n
  eve_idx = 0
  odd_idx = 0
  for i in range(n):
    if arr[i] % 2 == 0:
      eve_arr[eve_idx] = arr[i]
      eve_idx += 1
    else:
      odd_arr[odd_idx] = arr[i]
      odd_idx += 1
  def even_looper(arr, length):
    for i in range(n):
      for j in range(0,length-i-1):
        if arr[j] > arr[j+1] : arr[j], arr[j+1] = arr[j+1], arr[j]
  def odd_looper(arr, length):
    for i in range(n):
      for j in range(0,length-i-1):
        if arr[j] < arr[j+1] : arr[j], arr[j+1] = arr[j+1], arr[j]
  even_looper(eve_arr,eve_idx)
  odd_looper(odd_arr,odd_idx)
  eve_pointer = 0
  odd_pointer = 0
  for i in range(n):
    if arr[i] % 2 == 0:
      arr[i] = eve_arr[eve_pointer]
      eve_pointer += 1
    else:
      arr[i] = odd_arr[odd_pointer]
      odd_pointer += 1
  return arr
arr = [3,4,5,1,2]
print(esh(arr))
