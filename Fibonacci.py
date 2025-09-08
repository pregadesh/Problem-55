#Fibonacci number :
def esh(n):
  if n == 0 : return 0
  if n == 1 : return 1
  return esh(n-1)+ esh(n-2)
n = 5
print(f"fib num : {esh(n)}")

#Fibonacci seq :
def tya(n):
  if n==0 :return 0
  if n == 1 : return 1
  return tya(n-1) + tya(n-2)
seq = [tya(i) for i in range(n)]
print(f"fib seq :{seq}")
