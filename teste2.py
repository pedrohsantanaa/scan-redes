import os
def procurando_esside(contl):
	arq = open("dados.txt","r")
	nome = open("nome.txt", "w")
	
	for i in arq.readlines():
		if 'ESSID' in i:
			nome.write(i)
	nome.close()
	
	nome = open("nome.txt", "r")
	for i in nome.readlines():
		contl = contl + 1
	nome.close()
	arq.close()
	return contl
def escrever_nome(i):
	cont = 0
	contb = 0
	nome = open("nome.txt", "r")
	os.system("touch nomes.txt")
	nomes = open("nomes.txt","r+")

	for a in nome.readlines():
		if a == i:
			cont = cont + 1

	while cont > 0:
		cont  = cont - 1
	
	
	for a in nomes.readlines():
		if i == a:
			contb = contb + 1
	
	
	if contb == 0:
		nomes.write(i)
	
	nome.close()
	nomes.close()

def main():
	a = 0
	contl = procurando_esside(a)
	nome = open("nome.txt", "r")
	while contl>0:
		i = nome.readline()
		escrever_nome(i)
		contl = contl - 1

if __name__ == "__main__":
	main()
	os.system("cat nomes.txt | cut -c 27-70 > nomes2.txt")
   	os.system("cat nomes2.txt | sed 's, ,_,g;' > nomes3.txt")

