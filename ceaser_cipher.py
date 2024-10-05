def encrypt( text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift -65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97)%26 + 97)
        else:
            result += char

    return result


def decrypt(ciphertext , shift):
    result = ""

    for char in ciphertext:

        if char.isupper():
            result += chr((ord(char) - shift -65)%26 + 65)
        elif char.islower():
            result += chr((ord(char) -shift - 97)%26+97)

        else:
            result += char

    return result
    



if __name__ == "__main__":
    text = input("Enter the message: ")
    shift = int(input("Enter the shift number:"))


    encrypted_text = encrypt(text,shift)
    print(f"Encrypted Text : {encrypted_text}")


    decrypted_text = decrypt(encrypted_text,shift)
    print(f"Decrypted Text: {decrypted_text}")
