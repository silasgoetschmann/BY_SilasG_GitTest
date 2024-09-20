hundeAlter = int(input("Bitte gib hier das Alter deines Hundes ein: "))
if hundeAlter == 1:
    print("Dein Hund ist etwa 14 Jahre alt")
elif hundeAlter == 2:
    print("Dein Hund ist etwa 22 Jahre alt")
else:
    hundeAlter = hundeAlter * 5
    print("Dein Hund ist etwa " + str(hundeAlter) + " Jahre alt in Menschenjahren")
