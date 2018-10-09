def lorry(N, material, weight, value):
  
materiallist=[]
weightlist=[]
valuelist=[]
ask = "y"

while ask == "y":
  material=str(input("What is the material? "))
  weight=int(input("What is its weight? "))
  value=int(input("What is its value"))
  materiallist.append(material)
  weightlist.append(weight)
  valuelist.append(value)
