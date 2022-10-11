import cipher_art
print(cipher_art.logo)
i=1
while(i==1):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    """def encrypt(plain_text,shift):
        cipher_text=""
        for letter in plain_text:
            position=alphabet.index(letter)
            new_position=position+shift
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        print(f"Encrypted text is {cipher_text}")
    def decrypt(plain_text,shift):
        cipher_text=""
        for letter in plain_text:
            position=alphabet.index(letter)
            new_position=position-shift
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        print(f"Decrypted text is {cipher_text}")"""
    def ceaser(plain_text,shift,direction): #Combine the encrypt() and decrypt() functions into a single function called caesar().
        cipher_text = ""
        if direction == "decode":
            shift *= -1
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:                               #if the user enters a number/symbol/space
                cipher_text+=char
        print(f"{direction}d text is {cipher_text}")
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    plain_text=input("Enter your message\n")
    shift=int(input("Type shift number:\n"))
    shift=shift%26 #if the user enters a shift that is greater than the number of letters in the alphabet
    ceaser(plain_text,shift,direction)
    """if direction=="encode":
        encrypt(plain_text,shift)
    else:
        decrypt(plain_text,shift)"""
    i=int(input("Do you want to encrypt or decrypt another text for yes type '1' for no type '0' "))
    if i==0:
        print("Psst Goodbye!")