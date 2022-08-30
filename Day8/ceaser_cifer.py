import string
encode_or_decode = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")

message = input("Type Your Message: \n").lower()

shift = input("Type shift Number: \n")

lower_case_letter = string.ascii_lowercase



def encrypt(message, shift):
    encrypted_message = []
    for i in range(len(message)):
        char_in_message = message[i]
        for i in range(len(lower_case_letter)):
            if char_in_message == lower_case_letter[i]:
                position = i
        # encrypted_message[i] = lower_case_letter[position + int(shift)]
        encrypted_message.append(lower_case_letter[position + int(shift)])

    return encrypted_message


def decrypt(message, shift):
    decrypted_message = []

    for i in range(len(message)):
        char_in_message = message[i]

        for i in range(len(lower_case_letter)):
            if char_in_message == lower_case_letter[i]:
                position = i

        decrypted_message.append(lower_case_letter[position - shift])

    return decrypted_message


if encode_or_decode == "encode":
    enc = encrypt(message= message, shift=shift)
    enc_message = ''.join(enc)
    print(f" Here is Your encoded result: {enc_message}")
    command = input("Type 'Yes' if you want to continue and 'No' if you want to quite: ").lower()

    if command == 'yes':
        encode_or_decode = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
        message = input("Type Your Message: \n").lower()

        shift = input("Type shift Number: \n")

    else:
        exit()


if encode_or_decode == "decode":
    dec = decrypt(message=message, shift=int(shift))
    dec_message = ''.join(dec)

    print(dec_message)