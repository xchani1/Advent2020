vstup = open('input1.txt', encoding='utf-8')
radky = [int(radek.split('\n')[0]) for radek in vstup]

for num1 in radky:
  for num2 in radky: 
    if radky.index(num2)>radky.index(num1) and (num1+num2)<=2020:
      for num3 in radky:
        if radky.index(num3)>radky.index(num2):
          if num1+num2+num3==2020:
            print('Soucin cisel je',num1*num2*num3,"a cisla jsou:", num1,"a", num2,"a", num3)
