def archivo():
	archi=open('libro.txt','r')
	linea=archi.readline()
	b=len(linea)
	a=round(b,0)
	archi.close()
	print (a)
	return a

tex=archivo()

def dividir_archi(tex):
	c=tex/3
	res=round(c,0)
	print(res)
	return res

total = dividir_archi(tex)

def grabaTxt(tot):
	 primero=linea[:tot]
	 segundo=linea[:tot+tot]
	 tecero= linea[:tot+tot+tot]

def creartxt():
	archi=open('primera_parte.txt','w')
	archi.write()
	archi.close()
def creartxt2():
	archi=open('segunda_parte.txt','w')
	archi.close()
def creartxt3():
	archi=open('tercera_parte.txt','w')
	archi.close()


def crear_archi(tot,tex):
	for i in range (0,tex):
		if i==tot:
			creartxt()
			print (i)
		if i==tot+tot:
			creartxt2()
			print (i)
		if i==tot+tot+tot:
			creartxt3()
			print (i)
		
resultado=crear_archi(total,tex)
	
print("hola mundo")
print("manejar source tree es dificil")