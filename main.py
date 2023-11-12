#CAESAR CIPHER PROJECT
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
#required variables declaration

def caesar(input_text,shift_amount,user_direction):
    output_text=""
    if user_direction == "decode":
        shift_amount *= -1
    for char in input_text:
        if char not in alphabet:
            output_text += char
        else:
            position = alphabet.index(char)
            new_position =  position + shift_amount
            output_text += alphabet[new_position]
    print(f"Your {direction}d answer is {output_text}")

should_continue = "yes"
while should_continue == "yes":
    direction = input("type encode to encrypt or type decode to decrypt\n")
    text = input("Enter the text: ")
    shift = int(input("Enter the shift amount: "))
    shift = shift % 26
    caesar(input_text=text,shift_amount=shift,user_direction=direction)
    should_continue = int("Type yes to go again and no to exit: ").lower()
