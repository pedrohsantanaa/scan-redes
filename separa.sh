#!/bin/bash

contador=111
final=$(cat maior.txt)
conta=$(cat contador.txt)
cont=1

echo "                            Media Das Redes Escaneadas " > media.txt;
echo "    " >> media.txt;
for  linha in $(cat nomes3.txt);
do
	echo $linha >> media.txt;
	cat junto.txt | grep $contador | grep Quality | cut -c  32-33 > soma1.txt;
	paste -sd'+' soma1.txt|bc >soma2.txt;echo $conta >> soma2.txt;
	paste -sd'/' soma2.txt|bc >> media.txt 
	((contador=$contador+1))
        ((cont=$cont+1))

done

