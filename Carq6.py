#/usr/bin/python
#-*- coding:utf-8 -*-
#client_sock.py
import socket
import os
import time
import sys


def menu():
	print "		**************************"
	print "		*   Escolha uma Opção    *"
	print "		**************************"
	print "		* 1 - Escanear Rede      *"
	print "		* 0 - Para Escaneamento  *"
	print "		**************************"

def menu2():
	print "\n"
	print "		***********************************"
	print "		*   Escolha uma Opção             *"
	print "		***********************************"
	print "		* 1 - Continuar Escaneamento      *"
	print "		* 0 - Para Escaneamento           *"
	print "		***********************************"


def cria_socket():
	host = 'localhost'
	port = 5000
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))

def media():
	os.system("python teste2.py")
	os.system("python teste3.py")
	os.system("rm -f media.txt")
	os.system("./separa.sh")


def Main():
	menu()
	soma = 0
	while True:
		entrada = int(input("Opção:"))
		if entrada == 0:
			os.system("rm -f dados.txt;rm -f contador.txt; rm -f junto.txt; rm -f maior.txt ; rm -f nomes2.txt; rm -f nomes.txt;")
			os.system("rm -f nome.txt; rm -f qualidade.txt; rm -f soma1.txt; rm -f soma2.txt;rm -f a2.txt; rm -f nomes3.txt ")
			sys.exit()
		elif entrada != 1:
			print("Oção invalida")		
		
		elif entrada == 1:
			soma = soma + 10
			fp = open("contador.txt","w")
			fp.write(str(soma))
			fp.close()
			cont = 1
			while cont <= 10:
				cria_socket()
				s.send(str(cont))
				arq = open("dados.txt", "a")
				while True:
					dados = s.recv(1024)
				#	if "erro" in dados:
				#		print ("Problema com o servidor. Tente se conectar novamente")
				#		sys.exit()
					if not dados:
						break
					arq.write(dados)
				print(" %d Scan Completo"%cont)
				arq.close()
				s.close()
				cont = cont + 1	

			print ("\n Calculando a Media\n")
			media()
			os.system("clear")
			os.system("cat media.txt")
			os.system("sleep 1")
#			os.system("rm -f dados.txt")
			menu2()
		

if __name__ == "__main__":
	Main()

