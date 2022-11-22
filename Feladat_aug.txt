aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]
augtxt = open("./11.22/aug.txt","w",1,"utf-8")

if len(aug) == 12:
    print(f"ez egy augusztusi hőmérséklet adatsora")
else:
    print(f"ez nem egy augusztusi hőmérséklet adatsora")

legnagyobb = aug[0]
for i in range(0,len(aug)):
    if aug[i] > legnagyobb:
        legnagyobb = aug[i]
print(f"Legnagyobb: {legnagyobb}")

legkisebb = aug[0]
for i in range(0,len(aug)):
    if aug[i] < legkisebb:
        legkisebb = aug[i]
print(f"Legkisebb: {legkisebb}")

ossz = 0
for i in range(0,len(aug)):
    ossz +=1
print(ossz)
print(len(aug))

felett = 0
szam = 31
for i in range(0,len(aug)):
    if aug[i] > szam:
        felett += 1
print(felett)

hanyadikan = 20
for i in range(0,len(aug)):
    if i == hanyadikan+1:
        hanyadikan_eredmeny = aug[i]

atlag = 0
for i in range(0,len(aug)):
    if i == hanyadikan+1:
        atlag += aug[i]
atlag = atlag/len(aug)
        

augtxt.write(f"Legnagyobb : {legnagyobb}\n")
augtxt.write(f"Legkisebb : {legkisebb}\n")
augtxt.write(f"Összesen : {ossz}\n")
augtxt.write(f"{szam} alatt : {felett}\n")
augtxt.write(f"átlag : {atlag}\n")
augtxt.write(f"{hanyadikan}. : {hanyadikan_eredmeny}\n")
augtxt.write(f"hőingadozás: {legnagyobb-legkisebb}\n")

augtxt.close()