import random
Ergebnis = random.randint(1,6)
Counter = 1
while Ergebnis != 6:
    print(str(Ergebnis))
    Ergebnis = random.randint(1,6)
    Counter += 1
if Counter == 1:
    print(str(Ergebnis) + "! Das war eine Sechs, es hat nur einen Wurf gebraucht.")
else:
    print(str(Ergebnis) + "! Das war eine Sechs, es hat " + str(Counter) + " Würfe gebraucht.")
