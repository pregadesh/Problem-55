def eshtya(arr):
  m = max(arr)
  sec_lag = float('-inf')
  for num in arr:
    if num < m and num > sec_lag:
      sec_lag = num
  return sec_lag
arr = [7,11,2,3]
print(eshtya(arr))
