# Basic Text Encryption / Decryption
This code provides a simple and effective implementation of the Caesar cipher with support for both text and file encryption/decryption, as well as a frequency analysis function to examine the encrypted content.

```markdown
# Line-by-Line Explanation of the Caesar Cipher Code

This section provides a detailed explanation of the code for the Caesar cipher implementation, file encryption, decryption, and frequency analysis.

## Code Breakdown

### 1. `encrypt(msg, n)`
This function encrypts a given message using a Caesar cipher with a shift value `n`.

```python
def encrypt(msg, n):
    encrypted_msg = ""
```
- Initializes an empty string `encrypted_msg` to store the resulting encrypted message.

```python
    for char in msg:
```
- Loops through each character in the input message (`msg`).

```python
        if char.isalpha():
```
- Checks if the character is an alphabetical letter (either uppercase or lowercase).

```python
            base = ord('a') if char.islower() else ord('A')
```
- If the character is lowercase (`char.islower()`), it assigns the ASCII value of 'a' to `base`. If the character is uppercase, it assigns the ASCII value of 'A'. This ensures that the shift respects the case of the letter.

```python
            shifted = chr((ord(char) - base + n) % 26 + base)
```
- Converts the character `char` to its corresponding ASCII value using `ord(char)`, then subtracts the ASCII value of the base (`ord('a')` or `ord('A')`).
- Adds the shift value `n` to this result, applies modulo 26 (`% 26`) to wrap around if it goes past 'z' or 'Z', and then adds the base value back to ensure the result is within the correct ASCII range.
- Converts the new shifted value back to a character using `chr()`.

```python
            encrypted_msg += shifted
```
- Adds the shifted character to the `encrypted_msg`.

```python
        else:
            encrypted_msg += char
```
- If the character is not an alphabetic letter (e.g., punctuation, spaces), it is added to `encrypted_msg` without modification.

```python
    return encrypted_msg
```
- Returns the fully encrypted message after processing all characters.

---

### 2. `decrypt(encrypted_msg, n)`
This function decrypts the message by reversing the encryption process.

```python
def decrypt(encrypted_msg, n):
    return encrypt(encrypted_msg, -n)
```
- The decryption process is identical to encryption but with a negative shift (`-n`). It simply calls the `encrypt()` function with `-n` to reverse the encryption.

---

### 3. `encrypt_file(input_file, output_file, n)`
This function encrypts the content of a file and saves the result to another file.

```python
def encrypt_file(input_file, output_file, n):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
```
- Tries to open the input file in read mode (`'r'`). If the file is found, it reads its content into the variable `content`.

```python
            encrypted_content = encrypt(content, n)
```
- Encrypts the file content using the `encrypt()` function with the provided shift value `n`.

```python
        with open(output_file, 'w') as file:
            file.write(encrypted_content)
```
- Opens the output file in write mode (`'w'`) and writes the encrypted content into it.

```python
        print(f"Encryption successful! Encrypted content saved to {output_file}.")
```
- Prints a success message indicating that the encryption was successful and saved to the output file.

```python
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    except PermissionError:
        print(f"Permission denied for {input_file}!")
```
- Catches and handles two potential errors:
  - `FileNotFoundError`: If the input file does not exist.
  - `PermissionError`: If there are insufficient permissions to read the file.

---

### 4. `decrypt_file(input_file, output_file, n)`
This function decrypts the content of a file and saves the result to another file.

```python
def decrypt_file(input_file, output_file, n):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
```
- Tries to open the input file in read mode (`'r'`). If the file is found, it reads its content into the variable `content`.

```python
            decrypted_content = decrypt(content, n)
```
- Decrypts the file content using the `decrypt()` function with the provided shift value `n`.

```python
        with open(output_file, 'w') as file:
            file.write(decrypted_content)
```
- Opens the output file in write mode (`'w'`) and writes the decrypted content into it.

```python
        print(f"Decryption successful! Decrypted content saved to {output_file}.")
```
- Prints a success message indicating that the decryption was successful and saved to the output file.

```python
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    except PermissionError:
        print(f"Permission denied for {input_file}!")
```
- Catches and handles two potential errors:
  - `FileNotFoundError`: If the input file does not exist.
  - `PermissionError`: If there are insufficient permissions to read the file.

---

### 5. `letter_frequency(encrypted_msg)`
This function analyzes the frequency of each alphabetic character in the encrypted message.

```python
def letter_frequency(encrypted_msg):
    frequency = {}
```
- Initializes an empty dictionary `frequency` to store the frequency of each character.

```python
    for char in encrypted_msg:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
```
- Loops through each character in the encrypted message.
- If the character is alphabetic, it adds it to the `frequency` dictionary, incrementing the count for that character. If the character does not exist in the dictionary, it starts with a count of 0.

```python
    return frequency
```
- Returns the `frequency` dictionary containing the counts of each alphabetic character.

---

### 6. Example Execution
```python
message = input("Enter the message to encrypt: ")
key = int(input("Enter the key (shift value): "))
encrypted_message = encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
```
- Prompts the user to input a message and a shift value (`key`).
- Encrypts the message with the specified key and prints the encrypted message.
- Decrypts the encrypted message using the same key and prints the decrypted message.

---

### 7. File Encryption and Decryption
```python
input_file_name_encrypt = input("Enter the full path of the input file to encrypt: ")
output_file_name_encrypt = input("Enter the full path of the output file for encryption: ")
encrypt_file(input_file_name_encrypt, output_file_name_encrypt, key)

input_file_name_decrypt = input("Enter the full path of the input file to decrypt: ")
output_file_name_decrypt = input("Enter the full path of the output file for decryption: ")
decrypt_file(input_file_name_decrypt, output_file_name_decrypt, key)
```
- Prompts the user to provide the paths for the input and output files for both encryption and decryption.
- Calls the `encrypt_file` and `decrypt_file` functions to process the files.

---

### 8. Frequency Analysis of Encrypted Message
```python
freq = letter_frequency(encrypted_message)
print("Frequency of each letter in the encrypted message:")
for char, count in freq.items():
    print(f"{char}: {count}")
```
- Calls the `letter_frequency()` function to analyze the frequency of each letter in the encrypted message.
- Prints the frequency of each alphabetic character in the encrypted message.

---
