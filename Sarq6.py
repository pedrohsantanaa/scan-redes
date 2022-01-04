#/usr/bin/python
# -*- coding:utf-8 -*-
#serv_sock.py
import socket
import os 
import time
import sys


def Main():
	
	host = "localhost"
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Aguardando Conexão")
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	s.listen(10)

	cont = 1
	b = 1
	a = 111
	conta = 1

	
	while True:
		conn, addr = s.accept()
		print ("Conectado\n")
		while True:
			print ("Aguardando Mensagem")
			msg = conn.recv(2048)
			maior = 1
			teste = 0
			if msg != '11':
				os.system("iwlist wlan0 scan > a2.txt 2> erro.txt")
				arq = open("erro.txt", "r")
				for i in arq.readlines():
					if "Interface doesn't support scanning" in i:
						teste = 1
					
				arq.close()
				
				if teste == 1:
					os.system("rm erro.txt");
					conn.send("erro")
					break
				else:
					arq = open("a2.txt","r")
					conn.send("\n")
					conn.send("*********************************************************************\n")
					conn.send("*                        %d SCANEAMENTO                             *\n"%conta)
					conn.send("*********************************************************************\n")
					print("\n\n")
					for i in arq.readlines():
						if 'Quality' in i:
							if b > 1:
								conn.send("\n\n")
							conn.send("Qualidade da Rede %d \n"%b)
							conn.send((str(a)+i+'\n'))
							
						elif 'ESSID' in i:
							conn.send("Rede %d \n"%b)
							conn.send((i))
							b = b + 1
							if a > maior:
								maior = a
							a = a + 1

					fp = open("maior.txt","w")
					fp.write(str(a))
					fp.close()				


					print ("%d Scan Completo"%cont)	
					conta = conta + 1
					cont = cont + 1
					b = 1
					a = 111
					arq.close()
					conn.close()
					break
				
				


			

	conn.close()
	s.close()




if __name__ == "__main__":
	Main()
