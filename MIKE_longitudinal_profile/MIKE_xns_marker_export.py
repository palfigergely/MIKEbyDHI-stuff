# fájl behívása olvasásra
# soronként változóba másolás
f = open("export.txt",'r')
contents = f.readlines()
f.close()

# szükséges infomrációk kinyerése
# folyónév,TopoID,szelvény,M1-Z,M2-Z,M3-Z
cache = []
counter = 0
for line in contents:
    if counter == 0 or counter == 1 or counter == 2:
        cache.append(line.rstrip())
    if '<#1>' in line or '<#2>' in line or '<#4>' in line:
        cache.append(line.rstrip())
    if '******************************' in line:
        counter = -1
    counter += 1

# szükséges információk kiprintelése
print(*cache, sep='\n')
print('\n*************************************************************\n')

# kiszedi a keresztszelvény adatok közül a fölösleges szóközt és
# egyenként egy listaelem lesz minden bejegyzés
cache2 = []
for item in cache:
    cache2.extend(item.split())

# sorba rendezni az egy szelvényhez tartozó adatokat
# külön listába rendezni az adatokat típus szerint,
# a sorszám biztosítja az egymáshoz tartozást
topo = []
folyo = []
szelveny = []
marker1 = []
marker2 = []
marker3 = []

for i in range(0,int((len(cache2)/24))):
    counter = 0
    section = i * 24
    topo.append(cache2[section+counter])
    counter = 1
    folyo.append(cache2[section+counter])
    counter = 2
    szelveny.append(cache2[section+counter])
    counter = 4
    marker1.append(cache2[section+counter])
    counter = 11
    marker2.append(cache2[section+counter])
    counter = 18
    marker3.append(cache2[section+counter])
    
# egyes listák összefésülése egy tab eliminated txt fájlba

file = open("longprof.txt","w")
file.write("RIVER\tTOPOID\tCHAINAGE\tMARKER1\tMARKER2\tMARKER3\n")
for i in range(0,int((len(cache2)/24))):
    file.write(folyo[i]+"\t"+topo[i]+"\t"+szelveny[i]+"\t"+marker1[i]+"\t"+marker2[i]+"\t"+marker3[i]+"\n")
file.close()

"""
elvárt output:
FOLYONEV    TOPOID    CHAINAGE    MARKER1-Z    MARKER2-Z    MARKER3-Z
"""
