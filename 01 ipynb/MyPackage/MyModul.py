#
#
def shuffle(input_string: str) -> str:
    """
    Konvertiert einen String in Kleinbuchstaben, mischt die Buchstaben zufällig und gibt das Ergebnis zurück.

    Args:
        input_string: Der Eingabe-String.

    Returns:
        Ein String mit den in Kleinbuchstaben konvertierten und gemischten Buchstaben.
    """
    import random
    # Konvertiere in Kleinbuchstaben
    lowercase_string = input_string.lower()

    # Konvertiere den String in eine Liste von Zeichen
    char_list = list(lowercase_string)

    # Mische die Liste zufällig
    random.shuffle(char_list)

    # Füge die gemischten Zeichen wieder zu einem String zusammen
    shuffled_string = "".join(char_list)

    return shuffled_string

#
#
def caesar(text, verschiebung):
    """
    Verschlüsselt einen gegebenen Text mittels einer einfachen Caesar-Verschlüsselung.

    Args:
        text (str): Der zu verschlüsselnde Text.
        verschiebung (int): Die Anzahl der Stellen, um die jeder Buchstabe im Alphabet verschoben wird.

    Returns:
        str: Der verschlüsselte Text.
    """

    verschluesselter_text = ""

    for char in text:
        index = ord(char) + verschiebung
        verschluesselter_text += chr(index)

    return verschluesselter_text