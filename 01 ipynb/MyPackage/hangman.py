ges_wort = "Python".lower()
ger_wort = "?" * len(ges_wort)
max_versuche = 7
versuche = 0

while versuche < max_versuche and ger_wort != ges_wort:
  buchstabe = input("Bitte einen Buchstaben raten: ").lower()
  versuche += 1
  if buchstabe in ges_wort:
      i = ges_wort.index(buchstabe)
      liste = list(ger_wort)
      liste[i] = buchstabe
      ger_wort = "".join(liste)
      print(f"Gut geraten, aktueller Stand: {ger_wort}")
      versuche -= 1

if ger_wort == ges_wort:
  print("Klasse, Wort gefunden! 😊")
else:
   print("Maximale Anzahl der Versuche erreicht, vielleicht klappt es beim nächste mal 😐")

input("Für Ende, bitte Return")