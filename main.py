alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    if direction == "encode":
        encrypted_word =""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > 25: # index start from 0
                new_position -= 26 # position is 26 len of list 
            new_letter = alphabet[new_position]
            encrypted_word += new_letter
        print(f"The encoded text is {encrypted_word}") 
    elif direction == "decrypt":
        decrypted_word =""
        for letter in text:
            position = alphabet.index(letter) - shift
            if position < 0: # index start from 0
                position += 26 # position is 26 len of list 
            new_letter = alphabet[position]
            decrypted_word += new_letter
        print(f"The decoded text is {decrypted_word}")

caesar(text,shift,direction)
