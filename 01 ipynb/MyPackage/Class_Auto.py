class Auto:
  def __init__(self, x, y, z): #  Methode zur Erstellung des Blaupause / Bauplan der Klasse
    self.hersteller = x
    self.modell = y
    self.leistung = z
  def __str__(self):
    return f"{self.hersteller} {self.modell} {self.leistung}"