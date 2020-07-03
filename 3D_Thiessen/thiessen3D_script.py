"""required input.txt file content:
X Y Z Attribute
Tab eliminated

The 3D matrix points get the closest (in 3D) predefined point's attribute.
"""
import sys

test=0

# input file read
# order to list
f = open ("input.txt",'r')
content = f.readlines()
f.close()
sorok = []
for i in content:
	sorok.extend(i.split())

# order to list  according the type
xbase = []
ybase = []
zbase = []
abase = []

for i in range(0,int((len(sorok)/4))):
	counter = 0
	section = i * 4
	xbase.append(float(sorok[section+counter]))
	counter +=1
	ybase.append(float(sorok[section+counter]))
	counter +=1
	zbase.append(float(sorok[section+counter]))
	counter +=1
	abase.append(sorok[section+counter])
	counter +=1

# define border of the matrix
xmin = min(xbase)
ymin = min(ybase)
zmin = min(zbase)
xmax = max(xbase)
ymax = max(ybase)
zmax = max(zbase)

print("Matrix borders:")
print("X: "+str(xmin)+" - "+str(xmax))
print("Y: "+str(ymin)+" - "+str(ymax))
print("Z: "+str(zmin)+" - "+str(zmax))

# pontkiosztas megadasa
dx = input("\nX direction pieces: ")
dx = int(dx)
dy = input("Y direction pieces: ")
dy = int(dy)
dz = input("Z direction pieces: ")
dz = int(dz)

tipus = input("\nDefine all the elements of the net (1) or just the different attribute object's faces (2)? ")
tipus = int(tipus)

def pontkiosztas():
        # define points
        global x,y,z
        x = []
        y = []
        z = []
        
        print('\nINFO:\n'+str('{0:,.0f}'.format((dx+1)*(dy+1)*(dz+1)))+' point will be processed!')
        print('Counting, please wait...')
        for ix in range(0,dx+1):
                for iy in range(0,dy+1):
                        for iz in range(0,dz+1):
                                x.append(float(xmin+ix*((xmax-xmin)/dx)))
                                y.append(float(ymin+iy*((ymax-ymin)/dy)))
                                z.append(float(zmin+iz*((zmax-zmin)/dz)))


        print(str('{0:,.0f}'.format(len(x)))+' points have created!\n')
        print('Datatable fiilling with attributes...')

pontx = []
ponty = []
pontz = []
ponta = []

if tipus == 1:
        pontkiosztas()
        
        # define the points attribute
        a = []
        counter = 0
        ref_p = 0
        for i in range(0,len(x)):
                tx = x[i]
                ty = y[i]
                tz = z[i]
                d = []
                for i in range(0,len(xbase)):
                        d.append(((tx-xbase[i])**2+(ty-ybase[i])**2+(tz-zbase[i])**2)**(1/2))
                mind = 9999999999999999999999999
                for number in d:
                        if number < mind:
                                mind = number
                        min_index = d.index(mind)
                a.append(abase[min_index])

                pontx.append(tx)
                ponty.append(ty)
                pontz.append(tz)
                ponta.append(abase[min_index])

                # % counter
                counter += 1
                perc = counter/len(x)*100
                if round(perc) > ref_p:
                        sys.stdout.write('\r%d%%' % perc)
                        sys.stdout.flush()
                ref_p = round(perc)
        
                if test == 1:
                        print(str(tx)+'   '+str(ty)+'   '+str(tz)+'   '+str(abase[min_index])+'   '+str(counter/len(x)*100)+'%')
                
# decreasing the number of the elements from the matrix
if tipus == 2:
        pontkiosztas()
        print('... and element number decreasing!\n')
        
        # define the points attribute
        a = []
        counter = 0
        ref_p = 0
        for i in range(0,len(x)):
                mug = []
                tx = x[i]
                ty = y[i]
                tz = z[i]
                difix = [0,(xmax-xmin)/dx,-(xmax-xmin)/dx,0,0,0,0]
                difiy = [0,0,0,(ymax-ymin)/dy,-(ymax-ymin)/dy,0,0]
                difiz = [0,0,0,0,0,(zmax-zmin)/dz,-(zmax-zmin)/dz]
                for p in range(0,7):
                        ttx = tx+difix[p]
                        tty = ty+difiy[p]
                        ttz = tz+difiz[p]
                        d = []
                        for i in range(0,len(xbase)):
                                d.append(((ttx-xbase[i])**2+(tty-ybase[i])**2+(ttz-zbase[i])**2)**(1/2))
                        mind = 9999999999999999999999999
                        for number in d:
                                if number < mind:
                                        mind = number
                                min_index = d.index(mind)
                        mug.append(abase[min_index])
                if mug[0]==mug[1] and mug[1]==mug[2] and mug[2]==mug[3] and mug[3]==mug[4] and mug[4]==mug[5] and mug[5]==mug[6]:
                        True
                else:
                        ponta.append(mug[0])
                        pontx.append(tx)
                        ponty.append(ty)
                        pontz.append(tz)
                        
                # % counter
                counter += 1
                perc = counter/len(x)*100
                if round(perc) > ref_p:
                        sys.stdout.write('\r%d%%' % perc)
                        sys.stdout.flush()
                ref_p = round(perc)
                
                if test == 1:
                        print(str(tx)+'   '+str(ty)+'   '+str(tz)+'   '+str(abase[min_index])+'   '+str(counter/len(x)*100)+'%')

# output txt file creation
if tipus == 1:
        fajlnev = "matrix_full.txt"
if tipus == 2:
        fajlnev = "matrix_reduced.txt"
file = open(str(fajlnev),"w")
for i in range(0,len(ponta)):
        file.write(str(pontx[i])+'    '+str(ponty[i])+'    '+str(pontz[i])+'    '+str(ponta[i])+'\n')
file.close()

print('\n\nA '+fajlnev+' file has been created successfully!')
