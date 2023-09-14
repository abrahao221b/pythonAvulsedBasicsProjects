from caesarCipherAssets import *

key = 0
phrase = ""
encode_phrase = ""


def encode_caeser_cipher(phrase, encode_phrase, key):
    shift = key % 26
    for i in phrase:
        if i == " ":
            encode_phrase += " " 
        else:    
            position = (alphabet.index(i.upper()) + shift) % 26
            if i == i.lower():
                encode_phrase += alphabet[position].lower()
            else:
                encode_phrase += alphabet[position]
    phrase = ""
    key = -99999
    return (encode_phrase, phrase, key)

def decode_caeser_cipher(phrase, encode_phrase, key):
    shift = key % 26
    for i in encode_phrase:
        if i == " ":
            phrase += " "
        else:    
            relative_shift = alphabet.index(i.upper()) - shift
            if relative_shift >= 0:
                position = relative_shift 
            else:
                position = abs(relative_shift % 26)
            if i == i.upper():
                phrase += alphabet[position]
            else:
                phrase += alphabet[position].lower()   
    return phrase


def menu(phrase, encode_phrase, key):
    while True:
        action = input("Type \'encode\' to encrypt, type \'decode\' to decrypt: \n").lower()
        if action == "encode":
            phrase = input("Type your message: \n")
            key = int(input("Type the shift number: \n"))
            encode_phrase, phrase, key = encode_caeser_cipher(phrase, encode_phrase, key)
            print(f"Here's the encoded result: {encode_phrase}")
        elif action == "decode":
            print(encode_phrase)
            if encode_phrase == "":
               phrase = input("Type your message: \n")
               key = int(input("Type the shift number: \n"))
               encode_phrase, phrase, key = encode_caeser_cipher(phrase, encode_phrase, key)
               print(f"Here's the decode result: {encode_phrase}")
            else:
               key = int(input("Type the shift number: "))
               phrase = decode_caeser_cipher(phrase, encode_phrase, key)
               print(f"Here's the decoded result: {phrase}")
               phrase = ""
        else:
            print("Command not found!")
            
        want_continue = input("Type \'yes\' if you want to go again. Otherwise type \'no\'.\n").lower()
        if want_continue == "no":
            break
        
menu(phrase, encode_phrase, key)