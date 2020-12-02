vstup = open('input2.txt', encoding='utf-8')
radky = [radek.split('\n')[0] for radek in vstup]

radky = [radek.split(' ') for radek in radky]
radky = [[times.split('-') for times in radek] for radek in radky]

times=[radek[0] for radek in radky]
letter=[radek[1][0][0] for radek in radky]
pasw=[radek[2][0] for radek in radky]

delkaMin=[int(time[0]) for time in times]
delkaMax=[int(time[1]) for time in times]

ok=0

# part 1:
# for i in range(0, len(delkaMin)):
#   kolikrat=0
#   for t in range (0,len(pasw[i])):
#       if pasw[i][t]==letter[i]:
#         kolikrat=kolikrat+1
#   # print(kolikrat)
#   if kolikrat >=delkaMin[i] and kolikrat  <=delkaMax[i]:
#     ok=ok+1
# print(ok)

# part2
for i in range(0, len(delkaMin)):
   if ((pasw[i][delkaMin[i]-1]==letter[i]) and (pasw[i][delkaMax[i]-1]!=letter[i])) or \
      ((pasw[i][delkaMin[i]-1]!=letter[i]) and (pasw[i][delkaMax[i]-1]==letter[i])):
    ok=ok+1
print(ok)
