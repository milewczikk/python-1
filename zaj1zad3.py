#!/user/bin/env python3
#-*- coding: utf-8-*-


cenaPodstawowa= float(input("podaj cena samochodu"))
podatek = float(cenaPodstawowa/100*19)
oplataRejestracyjna = float(cenaPodstawowa /100*5)
prowizja = int(1000)
dostarczenie = int(500)

cenaFinalna = print("do zaplaty: " ,cenaPodstawowa+oplataRejestracyjna+prowizja+dostarczenie)
