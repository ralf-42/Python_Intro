
# MyModul.py - Allgemeine und wiederverwendbare Modulfunktionen

def fibonacci(n: int) -> int:
    """Berechnet die N-te Fibonacci-Zahl."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def caesar_cipher(text: str, shift: int) -> str:
    """Verschlüsselt einen Text mittels Caesar-Chiffre."""
    result = []
    for char in text:
        if 'a' <= char.lower() <= 'z':
            shift = shift % 26
            # Bestimmt, ob Groß- oder Kleinbuchstabe ist
            start = ord('a') if char.islower() else ord('A')
            # Berechnet den verschlüsselten Code
            shifted_ord = (ord(char) - start + shift) % 26 + start
            result.append(chr(shifted_ord))
        else:
            result.append(char)
    return "".join(result)

def ist_primzahl(n: int) -> bool:
    """
    Prüft, ob eine gegebene Zahl n eine Primzahl ist.
    Eine Primzahl ist eine natürliche Zahl größer als 1, die nur durch 1 und sich selbst teilbar ist.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 und 3 sind Primzahlen
    # Prüfe, ob teilbar durch 2 oder 3 ist
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Optimierte Prüfung (nur Zahlen der Form 6k ± 1)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

