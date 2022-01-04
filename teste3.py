import os

def ler(cont):
	arq = open("nomes2.txt","r")
	for i in arq.readlines():
		cont = cont + 1

	return cont
	arq.close()


def compara(i, cont2):
	v = 0
	dados = open("dados.txt","r")
	qualidade = open("qualidade.txt","a")
	junto = open("junto.txt","a")
	junto.write('\n')
	junto.write(i)
	junto.write('\n')
	for a in dados.readlines():
		p = str(cont2)
		if p in a:
			if 'Quality' in a:
				junto.write(a)
			
def main():
	arq = open("nomes2.txt","r")
	os.system("rm junto.txt ")
	a = 0
	cont2 = 111
	cont = ler(a)
	while cont > 0:
		i = arq.readline()
		compara(i,cont2)
		cont = cont - 1
		cont2 = cont2 + 1
	
	
if __name__ == "__main__":
	main()
	
