def feistel_round(left,right,subkey):

    f_output = round_function(right,subkey)

    new_left = right
    new_right = left ^ f_output

    return new_left , new_right

def round_function(data,key):
    return data ^ key

def feistel_encrypt(plaintext , subkey ,rounds):

    left = plaintext >> 8 
    right = plaintext & 0xFF

    for i in range(rounds):
        left,right = feistel_round(left,right,subkey[i])

    cipherText = (left << 8) | right
    return cipherText

def feistel_decrypt(ciphertext , subkeys, rounds):
    left = ciphertext >> 8
    right = ciphertext & 0xFF

    for i in range(rounds - 1, -1, -1):
        right,left = feistel_round(right,left,subkeys[i])

    plainText = (left << 8) | right
    return plainText



if __name__ == "__main__":

    plainText = 0xABCD

    subkeys = [0x3A,0x78,0x59,0xC2]

    rounds = 4

    print(f"plainText : {hex(plainText)}")

    cipherText = feistel_encrypt(plainText,subkeys,rounds)

    print(f"cipherText : {hex(cipherText)}")

    decryptText = feistel_decrypt(cipherText,subkeys,rounds)

    print(f"Decrypted plainText : {hex(decryptText)}")
