
komunikat = input ("podaj tresc komunikatu ktory magicznie zostanie odwrocony   ")

komunikatLen = len(komunikat)

print (komunikat[:: - 1])

for i in range(komunikatLen, 0, -1):
	print (komunikat[i - 1])


