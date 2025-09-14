#Product of Array Except Self
def esh(arr):
  n = len(arr)
  res = [1] * n
  pre = 1
  suf = 1
  for i in range(n):
    res[i] = pre
    pre *= arr[i]
  for i in range(n-1,-1,-1):
    res[i] *= suf
    suf *= arr[i]
  return res
arr = [1,2,3,4]
print(esh(arr))
