def strings(string1, string2):
  l=[]
  maximum=max(len(string1), len(string2))
  for x in range(0, maximum):
    try:
      l.append(string1[x])
    except IndexError: pass
    try:
      l.append(string2[x])
    except IndexError: pass
  print(l)
  
string1=str(input("What is the 1st string? "))
string2=str(input("What is the 2nd string? "))
strings(string1, string2)
