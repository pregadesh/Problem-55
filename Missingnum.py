#Find the Missing Number
arr = [7,5,6,4,2,1]
n = len(arr)+1
total = sum(arr)
expected_sum = n*(n+1)//2
print(expected_sum - total)
