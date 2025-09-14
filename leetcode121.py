# Best time buy and sell stock :
def esh(arr):
  min_val = arr[0]
  max_val = 0
  for val in arr:
    if val < min_val : min_val = val
    profit = val - min_val
    if profit > max_val : max_val = profit
  return max_val
arr = [7,1,5,3,6,4]
print(esh(arr))
