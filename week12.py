def amstrong(number):
  s=0
  numberlist=list(str(number))
  for n in numberlist:
    m=int(n)
    s=s+(m**3)
  if s == number:
    print("Yes")
  else: print("No")

amstrong(int(input("What is the number? ")))
