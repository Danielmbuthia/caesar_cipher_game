from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if shift > 25:
    shift = shift%26
    
start_of_game =True

def caesar(text,shift,direction):
    start_of_game = False
    word = ""
    for letter in text:
        try:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
                if new_position > 25: # index start from 0
                    new_position -= 26 # position is 26 len of list         
            elif direction == "decode":
                new_position = position - shift
                if new_position < 0: # index start from 0
                    new_position += 26 # position is 26 len of list          
            new_letter = alphabet[new_position]
            word += new_letter 
        except ValueError:
            word+=letter
    print(f"The {direction}d text is: {word}")

# continue_play = input(print("Type 'Yes' to proceed playing and 'No' to quit the game"))
 
caesar(text,shift,direction)
