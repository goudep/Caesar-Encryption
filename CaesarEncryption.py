# Caesar Encryption 
# Input : msg in letters 
# Output : msg encrypted by Caesar encryption 
# Date : 2024-09-29 

def caesarEncrypt(plaintext, shift):
    result = ''
    for char in plaintext:
        if char.isalpha():
            # Convert lowercase to uppercase 
            if char.islower(): char = char.upper()
            # Determine the base ASCII code depending on uppercase or lowercase
            shiftBase = ord('A') 
            # Perform the shift
            shifted = (ord(char) - shiftBase + shift) % 26 + shiftBase
            result += chr(shifted)
        else:
            # Non-alphabetic characters are added unchanged
            result += char
    return result

def caesarDecrypt(ciphertext, shift):
    # Decryption is just encryption with a negative shift
    return caesarEncrypt(ciphertext, -shift)

def main():
    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    if choice not in ('e', 'd'):
        print("Invalid choice! Please enter 'e' or 'd'.")
        return

    text = input("Enter your text: ")
    try:
        shift = int(input("Enter shift value (0-25): "))
        if not 0 <= shift <= 25:
            print("Shift value must be between 0 and 25.")
            return
    except ValueError:
        print("Invalid shift value! Please enter an integer between 0 and 25.")
        return

    if choice == 'e':
        encryptedText = caesarEncrypt(text, shift)
        print("Encrypted text:", encryptedText)
    else:
        decryptedText = caesarDecrypt(text, shift)
        print("Decrypted text:", decryptedText)

if __name__ == '__main__':
    main()

