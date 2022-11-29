import random

fajl = open("fa.txt","w",encoding="utf-8")

kitermeles = []

for i in range(0,31):
    kitermeles.append(random.randint(50,100))

legnagyobb = 0
for i in range(0,len(kitermeles)):
    if kitermeles[i] > legnagyobb:
        legnagyobb = kitermeles[i]
print(legnagyobb)
fajl.write(f"{legnagyobb}\n")

legkisebb = 0
for i in range(0,len(kitermeles)):
    if kitermeles[i] < legkisebb:
        legkisebb = kitermeles[i]
print(legkisebb)
fajl.write(f"{legkisebb}\n")

alkalom = 0
for i in range(0,len(kitermeles)):
    if kitermeles[i] > 82:
        alkalom+=1
print(alkalom)
fajl.write(f"{alkalom}\n")

hanyadikan = 20
print(f"{hanyadikan}.-án : {kitermeles[hanyadikan+1]}")
fajl.write(f"{hanyadikan}.-án : {kitermeles[hanyadikan+1]}\n")

atlag = 0
for i in range(0,len(kitermeles)):
    atlag = atlag+kitermeles[i]
atlag = atlag/len(kitermeles)
fajl.write(f"{atlag}\n")

fajl.close()