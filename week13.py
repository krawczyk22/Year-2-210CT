def factorial(n):
  if n==0:
    return 1
  elif n>0:
    n=n*(factorial(n-1))
    return n
  else: print("The number must be equal or nigher than 0 ")
    
nlist=[]
mlist=[]
ask = "y"
while ask == "y":
  n=int(input("The 1st number "))
  m=int(input("The 2nd number "))
  nlist.append(n)
  mlist.append(m)
  ask=str(input("More numbers? Press y to type more numbers "))

for x in range(0, len(nlist)):
  if nlist[x] or mlist[x] < 2**31:
    if factorial(nlist[x])%mlist[x] == 0:
      print(str(mlist[x]) + " divides " + str(nlist[x]) +"!")
    else: print(str(mlist[x]) + " does not divide " + str(nlist[x]) +"!")
