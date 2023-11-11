#CAESAR CIPHER PROJECT
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#required variables declaration
direction = input("type encode to encrypt or type decode to decrypt\n")
text = input("Enter the text: ")
shift = int(input("Enter the shift amount: "))

def caesar(input_text,shift_amount,user_direction):
    output_text=""
    for letter in input_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            output_text += alphabet[new_position]
        elif direction == "decode":
            new_position = position - shift_amount
            output_text += alphabet[new_position]
        else:
            print("Wrong input")
            break
    print(f"Your desired answer is {output_text}")

caesar(input_text=text,shift_amount=shift,user_direction=direction)