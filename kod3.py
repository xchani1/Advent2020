vstup = open('input3.txt', encoding='utf-8')
radky = [radek.split('\n') for radek in vstup]

radky=[(len(radky)//(len(radek)))*radek[0] for radek in radky]

stromu_celk=[]
nasobek=1

for (a,b) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
  stromu=0
  x=0
  y=0
  for i in range (0,len(radky)//b):
    m=radky[y][x]
    if m=='#':
      stromu+=1
    x+=a
    y+=b
  stromu_celk.append(stromu)

for strom in stromu_celk:
  nasobek*=strom
print("Nasobek je",nasobek)

