"""
Write a Python function named morse_translator that translates a given string into Morse code.

Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
The Morse code for each character should be separated by a space.
Each word in the string should be separated by a forward slash (/).
The function should handle both uppercase and lowercase alphabetic characters.
The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
Non-alphabetic characters (like numbers or symbols) should not be translated.

https://en.wikipedia.org/wiki/Morse_code
"""


def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Your code goes here
    text = text.upper()
    morse_result = []

    for every_al in text:
        if every_al in morse_code_dict:
            morse_result.append(morse_code_dict[every_al])
        else:
            if every_al == " ":
                morse_result.append("/")
            else:
                pass
    return " ".join(morse_result)


# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
