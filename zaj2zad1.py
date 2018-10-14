#!/user/bin/env python3
#-*- coding: utf-8-*-



start =int(input("podaj pierwsza liczbe "))
stop= int(input ("podaj ostatnia liczbe "))
skok= int(input ("podaj odstęp miedzy kolejnymi liczbami "))


for wylistuj in range (start,stop,skok):
	print (wylistuj)
