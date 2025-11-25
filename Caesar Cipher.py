alphabet = [chr(i) for i in range(97, 123)]  # 'a' to 'z'

def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")

wanna_do = False
while not wanna_do:
    condition = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: ")
    message = input("Type your message:\n")
    shift = int(input("Enter the shift number:\n"))

    if condition == 'encrypt':
        encryption(plain_text=message, shift_key=shift)
    elif condition == 'decrypt':
        decryption(cipher_text=message, shift_key=shift)

    play_again = input("Enter yes or no: ")
    if play_again.lower() == 'no':
        wanna_do = True
