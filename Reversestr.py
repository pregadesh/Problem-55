s = "rewolfnus"
s = list(s)
left = 0
right = len(s)-1
while left < right :
  s[left], s[right] = s[right], s[left]
  left += 1
  right -= 1
print("".join(s))

#or
#while left < right :
#temp = s[left]
#s[left] = s[right]
#s[right] = temp
#left += 1
#right -= 1
#print("".join(s))
