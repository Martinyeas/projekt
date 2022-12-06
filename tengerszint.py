tengerszintnev  = None
tengerszintmag = None
fajl = open("tenger.txt","w",encoding="utf-8")

tengerszinttabnev = []
tengerszinttab = []

while tengerszintnev != "":
    tengerszintnev = input("Adjon meg egy földrajzi hely nevét: ")
    tengerszinttabnev.append(tengerszintnev)
    if tengerszintnev == "":
        break
    else:
        tengerszintmag = int(input("Adja meg ennek tengerszint feletti magasságát: "))
        tengerszinttab.append(tengerszintmag)

def tengerszintek(magassag):
    if magassag < 200:
        return "alföld"
    elif magassag < 500 and magassag >= 200:
        return "dombság"
    elif magassag < 1500 and magassag >= 500:
        return "kőzéphegység"
    else:
        return "magashegység"

for i in range(0,len(tengerszinttab)):
    fajl.write(f"{tengerszinttab[i]} ")
    fajl.write(f"{tengerszinttabnev[i]} ")
    fajl.write(f"{tengerszintek(tengerszinttab[i])}\n")

fajl.close()