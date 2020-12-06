vstup = open('input6.txt', encoding='utf-8')
radky = [radek.split('\n')[0] for radek in vstup]

odpovedi=[]
pocty=0

# part 1:
# for radek in radky:
#   if radek!='':
#     for pismeno in radek:
#       if pismeno not in odpovedi:
#         odpovedi.append(pismeno)
#     print(odpovedi)
#   else:
#     pocty=pocty+len(odpovedi)
#     odpovedi=[]
#     print(pocty)
# pocty+=len(odpovedi)
# print(pocty)

# part 2 - nefunkcni :(
i=0
for radek in radky:
  i=i+1
  if radek!='':
    if i==1:
      for pismeno in radek:
        if pismeno not in odpovedi:
          odpovedi.append(pismeno)
      print(odpovedi)
    else:
      for p in odpovedi:
        if p not in radek:
          odpovedi.remove(p)
      print(odpovedi)
  else:
    pocty=pocty+len(odpovedi)
    odpovedi=[]
    print(pocty)
    i=0
pocty+=len(odpovedi)
print(pocty)
