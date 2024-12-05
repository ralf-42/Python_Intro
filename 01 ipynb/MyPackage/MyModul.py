#
#
def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)
#
# 
def swap_case(s):
    st = ""
    st1 = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(s)): 
        st = str(s[i])
        if st in lowercase: st = st.upper()
        else: st = st.lower() 
        st1 = st1 + st           
    return st1
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