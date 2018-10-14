import random

slowa =("python" ,"gdansk","dlaczego","gdynia","wsb")
word = random.choice(slowa)
poprawnie = word
pomie=""
licznik = 0
podp = 100

while word:
	position = random.randrange(len(word))
	pomie+=word[position]
	word =word[:position] + word [(position +1):]
	print(pomie)

print (
"""
Witaj w grze 'Wymieszane litery'!  
Uporządkuj litery, aby odtworzyć prawidłowe słowo.
(Aby zakończyć zgadywanie, naciśnij klawisz Enter bez podawania odpowiedzi.)
"""
)
print
("Zgadnij, jakie to słowo:", pomie)
i=0

zgaduj = input ("\nTowaj odpowiedź: ")
while zgaduj != poprawnie and zgaduj != "":
	licznik= licznik +1
	print ("niestety, to nie to slowo.", licznik)
	if licznik > 3:
		print ("Twoja podpowiedz to ", poprawnie[position:i])
		podp = podp -5
		i=i+1
	zgaduj = input("Twoja odpowiedz: ")

		
	
if zgaduj == poprawnie:
	licznik= licznik +1
	print("Zgadza sie ! Zgadles!\n")

print("Dziekuje za udzial w grze. Udalo ci sie odpowiedziec w ",licznik, "probach Twoj wynik to: ",podp)
