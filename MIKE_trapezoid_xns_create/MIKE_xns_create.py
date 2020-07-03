""" elvárt input fájl tartalma:
Branch_name TopoID Szelvény Fenékszél. Rézsű Fenékszint Bp.mag. Jp.mag.
Tab eliminated
"""
# fájl behívása olvasásra
# listába rendezés
f = open("import.txt",'r')
contents = f.readlines()
f.close()
sorok = []
for i in contents:
    sorok.extend(i.split())
# külön listákba rendezés típus szerint
branch = []
topoid = []
chainage = []
fenekszel = []
rezsu = []
fenekszint = []
bpszint = []
jpszint = []
x1 = []
z1 = []
x2 = []
z2 = []
x3 = []
z3 = []
x4 = []
z4 = []
x5 = []
z5 = []

for i in range(0,int((len(sorok)/8))):
    counter = 0
    section = i * 8
    branch.append(sorok[section+counter])
    counter += 1
    topoid.append(sorok[section+counter])
    counter += 1
    chainage.append(sorok[section+counter])
    counter += 1
    fenekszel.append(sorok[section+counter])
    counter += 1
    rezsu.append(sorok[section+counter])
    counter += 1
    fenekszint.append(sorok[section+counter])
    counter += 1
    bpszint.append(sorok[section+counter])
    counter += 1
    jpszint.append(sorok[section+counter])

for i in range(0,len(branch)):
    x1.append(0)
    z1.append(float(jpszint[i]))
    x2.append(float(x1[i])+(float(jpszint[i])-float(fenekszint[i]))*float(rezsu[i]))
    z2.append(float(fenekszint[i]))
    x3.append(float(x2[i])+float(fenekszel[i])/2)
    z3.append(float(fenekszint[i]))
    x4.append(float(x3[i])+float(fenekszel[i])/2)
    z4.append(float(fenekszint[i]))
    x5.append(float(x4[i])+(float(bpszint[i])-float(fenekszint[i]))*float(rezsu[i]))
    z5.append(float(bpszint[i]))

# raw data txt fájl elkészítése
file = open("rawdata_XNS.txt","w")
for i in range(0,len(branch)):
    file.write(str(topoid[i])+'\n')
    file.write(str(branch[i])+'\n')
    chainage[i] = format(float(chainage[i]), '.3f')
    if float(chainage[i]) < 10:
        file.write('               '+str(chainage[i])+'\n')
    if float(chainage[i]) >= 10 and float(chainage[i]) < 100:
        file.write('              '+str(chainage[i])+'\n')
    if float(chainage[i]) >= 100 and float(chainage[i]) < 1000:
        file.write('             '+str(chainage[i])+'\n')
    if float(chainage[i]) >= 1000 and float(chainage[i]) < 10000:
        file.write('            '+str(chainage[i])+'\n')
    if float(chainage[i]) >= 10000 and float(chainage[i]) < 100000:
        file.write('           '+str(chainage[i])+'\n')
    if float(chainage[i]) >= 100000 and float(chainage[i]) < 1000000:
        file.write('          '+str(chainage[i])+'\n')
    file.write('COORDINATES\n    0\nFLOW DIRECTION\n    0\nPROTECT DATA\n    0\n')
    file.write('DATUM\n      0.00\nRADIUS TYPE\n    0\nDIVIDE X-Section\n0\nSECTION ID\n')
    file.write('     \nINTERPOLATED\n    0\nANGLE\n    0.00   0\nRESISTANCE NUMBERS\n')
    file.write('   0  0     1.000     1.000     1.000    1.000    1.000\nPROFILE        5\n')

    x1[i] = format(float(x1[i]), '.3f')
    if float(x1[i]) < 10:
        file.write('     '+str(x1[i]))
    if float(x1[i]) < 100 and float(x1[i]) >= 10:
        file.write('    '+str(x1[i]))
    if float(x1[i]) < 1000 and float(x1[i]) >= 100:
        file.write('   '+str(x1[i]))
    z1[i] = format(float(z1[i]), '.3f')
    if float(z1[i]) < 10:
        file.write('     '+str(z1[i]))
    if float(z1[i]) < 100 and float(z1[i]) >= 10:
        file.write('    '+str(z1[i]))
    if float(z1[i]) < 1000 and float(z1[i]) >= 100:
        file.write('   '+str(z1[i]))
    file.write('     1.000     <#1>     0     0.000     0\n')

    x2[i] = format(float(x2[i]), '.3f')
    if float(x2[i]) < 10:
        file.write('     '+str(x2[i]))
    if float(x2[i]) < 100 and float(x2[i]) >= 10:
        file.write('    '+str(x2[i]))
    if float(x2[i]) < 1000 and float(x2[i]) >= 100:
        file.write('   '+str(x2[i]))
    z2[i] = format(float(z2[i]), '.3f')
    if float(z2[i]) < 10:
        file.write('     '+str(z2[i]))
    if float(z2[i]) < 100 and float(z2[i]) >= 10:
        file.write('    '+str(z2[i]))
    if float(z2[i]) < 1000 and float(z2[i]) >= 100:
        file.write('   '+str(z2[i]))
    file.write('     1.000     <#0>     0     0.000     0\n')

    x3[i] = format(float(x3[i]), '.3f')
    if float(x3[i]) < 10:
        file.write('     '+str(x3[i]))
    if float(x3[i]) < 100 and float(x3[i]) >= 10:
        file.write('    '+str(x3[i]))
    if float(x3[i]) < 1000 and float(x3[i]) >= 100:
        file.write('   '+str(x3[i]))
    z3[i] = format(float(z3[i]), '.3f')
    if float(z3[i]) < 10:
        file.write('     '+str(z3[i]))
    if float(z3[i]) < 100 and float(z3[i]) >= 10:
        file.write('    '+str(z3[i]))
    if float(z3[i]) < 1000 and float(z3[i]) >= 100:
        file.write('   '+str(z3[i]))
    file.write('     1.000     <#2>     0     0.000     0\n')
    
    x4[i] = format(float(x4[i]), '.3f')
    if float(x4[i]) < 10:
        file.write('     '+str(x4[i]))
    if float(x4[i]) < 100 and float(x4[i]) >= 10:
        file.write('    '+str(x4[i]))
    if float(x4[i]) < 1000 and float(x4[i]) >= 100:
        file.write('   '+str(x4[i]))
    z4[i] = format(float(z4[i]), '.3f')
    if float(z4[i]) < 10:
        file.write('     '+str(z4[i]))
    if float(z4[i]) < 100 and float(z4[i]) >= 10:
        file.write('    '+str(z4[i]))
    if float(z4[i]) < 1000 and float(z4[i]) >= 100:
        file.write('   '+str(z4[i]))
    file.write('     1.000     <#0>     0     0.000     0\n')

    x5[i] = format(float(x5[i]), '.3f')
    if float(x5[i]) < 10:
        file.write('     '+str(x5[i]))
    if float(x5[i]) < 100 and float(x5[i]) >= 10:
        file.write('    '+str(x5[i]))
    if float(x5[i]) < 1000 and float(x5[i]) >= 100:
        file.write('   '+str(x5[i]))
    z5[i] = format(float(z5[i]), '.3f')
    if float(z5[i]) < 10:
        file.write('     '+str(z5[i]))
    if float(z5[i]) < 100 and float(z5[i]) >= 10:
        file.write('    '+str(z5[i]))
    if float(z5[i]) < 1000 and float(z5[i]) >= 100:
        file.write('   '+str(z5[i]))
    file.write('     1.000     <#4>     0     0.000     0\n')

    file.write('LEVEL PARAMS\n   0  0    0.000  0    0.000  50\n')
    file.write('*******************************\n')
        
file.close()
