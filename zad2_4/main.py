def spelnione(x,y):
  while x<y:
    y//=2
  if x==y:
    return True
  return False    

with open ("pary.txt",'r') as file:
  lines=file.read().split('\n')
  # print(lines)
  for el in lines:
    zest=el.split()    
    x=int(zest[0])
    y=int(zest[1])
    if spelnione(x,y):
      print(x,y)
  file.close();