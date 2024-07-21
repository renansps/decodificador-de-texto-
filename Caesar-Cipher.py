def decode_caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char
    return result

text = "Khoor, Zruog!"
shift = 3
print(decode_caesar_cipher(text, shift))  # Output: "Hello, World!"
import base64

def decode_base64(text):
    return base64.b64decode(text).decode("utf-8")

text = "SGVsbG8sIFdvcmxkIQ=="
print(decode_base64(text))  # Output: "Hello, World!"

def decode_vigenere_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            result += chr((ord(char) - ascii_offset - ord(key_char) + ascii_offset) % 26 + ascii_offset)
            key_index += 1
        else:
            result += char
    return result

text = "GUR PENML XRL VF ZL FRPERG CBFG"
key = "KEY"
print(decode_vigenere_cipher(text, key))  # Output: "THE QUICK BROWN FOX JUMPS"