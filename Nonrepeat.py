s = "Rajaram"
s = s.lower()
counter = {}
res = []
for char in s : 
  if char in counter : counter[char] += 1
  else: counter[char] = 1
for char, val in counter.items():
  if val == 1: res.append(char)
print("".join(res))
