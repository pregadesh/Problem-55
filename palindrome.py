#palindrome
s = "racecar"
arr = list(s)
l = 0
r = len(arr)-1
is_pal = True
while l < r :
    if s[l] != s[r]:
        is_pal = False
        break
    l += 1
    r -= 1
if is_pal :
    print("Yes its palindrome")
else:
    print("Not palindrome")

#palindrome with number 
s = 123
arr = [s]
#same logic as above
