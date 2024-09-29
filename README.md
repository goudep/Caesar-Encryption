# Caesar Cipher Encryption and Decryption Program in Python 

This program implements the Caesar cipher algorithm for encrypting and decrypting text messages. 
The Caesar cipher is a simple encryption technique where each letter in the plaintext is shifted 
by a fixed number of positions down the alphabet.

## How the Program Works
1. User Input

The program prompts the user to select encryption or decryption.
It then asks for the text to process and the shift value.

2. Processing the Text

Depending on the user's choice, the program either encrypts or decrypts the text using the Caesar cipher algorithm.
The shift value determines how many positions each letter is moved in the alphabet.

3. Displaying the Result

The program outputs the encrypted or decrypted text.
Non-alphabetic characters remain unchanged in the output.

## Examples 

### Encryption Example 

`Enter 'e' to encrypt or 'd' to decrypt: e`
`Enter your text: Attack at dawn!`
`Enter shift value (0-25): 3`
`Encrypted text: DWWDFN DW GDZQ!`

### Decryption Example
`Enter 'e' to encrypt or 'd' to decrypt: d`
`Enter your text: DWWDFN DW GDZQ!`
`Enter shift value (0-25): 3`
`Decrypted text: ATTACK AT DAWN!`
