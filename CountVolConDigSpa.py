#Count vowels, consonants, digits, spaces in a string
vol = ["a","e","i","o","u"]
dig = [str(i) for i in range(0,10)]
s = "Hello World 123"
s = s.lower()
v_count = 0
con_count = 0
dig_count = 0
space_count = 0
for char in s :
    if char in vol :
        v_count += 1
    elif char in dig :
        dig_count += 1
    elif char == " ":
        space_count += 1
    else:
        con_count += 1
print("vol_count :",v_count)
print("con_count :",con_count)
print("dig_count :",dig_count)
print("space_count :",space_count)
