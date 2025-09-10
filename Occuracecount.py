s = "Rajaram"
counter = {}
for char in s :
  if char in counter: counter[char] += 1
  else: counter[char] = 1
#print(counter)

for char, val in counter.items():
  print(f"{char}:{val}")
