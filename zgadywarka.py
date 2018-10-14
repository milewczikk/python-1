#!/user/bin/env python3
#-*- coding: utf-8-*-

import random
liczba = random.randint(1,49)

#odp = input ("jaka liczba od 1 do 49 wylosowano ")
 
for i in range (6):
	odp = int(input(" zgadnij liczbe"))
	if liczba == int (odp):
		print("wll done")
		break
	else:
		print("no nioestety")
		if i== int(5):
			print("poszukiwana liczba to ",liczba)


