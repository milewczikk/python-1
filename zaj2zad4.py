import random

slowa =("python" ,"gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
poprawnie = word
#pomie=""
iloscLiter= len(word)
szansa =0
licznik = 0
#podp = 100

#while word:
	#position = random.randrange(len(word))
	#pomie+=word[position]
	#word =word[:position] + word [(position +1):]
#print(word)



print (
"""
Witaj w grze 'Jaka to melodi... Wróć jakie To Miasto!  
Znając ilość liter zgadnij nazwe miasta , masz 5 szans za zadanie pytania czy jakas litera znajduje sie w slowie
Komputer moze odpowiedziec tylko TAK lub NIE
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print
("Zgadnij, jakie to słowo gdy ilosc liter to: ",iloscLiter)
 
 
while szansa <5: 
	litera = input ("Podaj litere: ")
	if litera in poprawnie:
		print("TAK")
		szansa= szansa+1
	else:
		print("NIE")
		szansa= szansa+1

miasto = input ("podaj miasto: ")
if miasto ==poprawnie:
	print ("brawo TY!!!" )
else:
	print ("niestety nie udalo sie")

		
	


#print("Dziekuje za udzial w grze. Udalo ci sie odpowiedziec w ",licznik, "probach Twoj wynik to: ",podp)

