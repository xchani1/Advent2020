vstup = open('input5.txt', encoding='utf-8')
radky = [radek.split('\n')[0] for radek in vstup]

hodnoty=[]

for radek in radky:
  rada=0
  sloupec=0
  for i in range(0,7):
    if radek[i]=='B':
      rada+=2**(6-i)
  for j in range(7,10):
    if radek[j]=='R':
      sloupec+=2**(9-j)
  hodnoty.append(rada*8+sloupec)
print(max(hodnoty))
hodnoty.sort()

for a in range(min(hodnoty),max(hodnoty)):
  if a not in hodnoty:
    print(a)
