Name = input("Wie heisst du: ")
Alter = int(input("Wie alt bist du: "))
if Alter < 6:
    print(Name + ", kannst du schon lesen?")
if Alter > 15 and Alter < 18:
    print(Name + ", du darfst den Mofaführerschein machen")
if Alter >= 18:
    print(Name + ", du bis volljährig")
else:
    for i in range(0, 10):
        print("Krass")
