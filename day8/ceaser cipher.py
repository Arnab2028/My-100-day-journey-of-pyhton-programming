# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for character in original_text:
        if character not in alphabet:
            output_text += character
        else:


            shifted_position = alphabet.index(character) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n=> ").lower()
    if direction == "encode" or direction == "decode":
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
        restart = input("\nDo you want to use the program again?\n"
                        "a) Type 'Yes' to continue.\n"
                        "b) Type 'No' to exit the program.\n=> ").lower()

        if restart == "no":
            should_continue = False
            print("---Good Bye---")
        elif restart == "yes":
            should_continue = True
        else:
            print("---Invalid Input---\n"
                  "---Program terminated---")
            exit()

    else:
        print("---Invalid Direction---")




