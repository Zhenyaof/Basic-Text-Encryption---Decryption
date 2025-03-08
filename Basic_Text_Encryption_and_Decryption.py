def encrypt(msg, n):
    encrypted_msg = ""
    for char in msg:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted = chr((ord(char) - base + n) % 26 + base)
            encrypted_msg += shifted
        else:
            encrypted_msg += char
    return encrypted_msg

def decrypt(encrypted_msg, n):
    return encrypt(encrypted_msg, -n)

def encrypt_file(input_file, output_file, n):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            encrypted_content = encrypt(content, n)

        with open(output_file, 'w') as file:
            file.write(encrypted_content)
        
        print(f"Encryption successful! Encrypted content saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    
    except PermissionError:
        print(f"Permission denied for {input_file}!")

def decrypt_file(input_file, output_file, n):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            decrypted_content = decrypt(content, n)

        with open(output_file, 'w') as file:
            file.write(decrypted_content)
        
        print(f"Decryption successful! Decrypted content saved to {output_file}.")
    
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    
    except PermissionError:
        print(f"Permission denied for {input_file}!")

def letter_frequency(encrypted_msg):
    frequency = {}
    for char in encrypted_msg:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

message = input("Enter the message to encrypt: ")
key = int(input("Enter the key (shift value): "))
encrypted_message = encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")

input_file_name_encrypt = input("Enter the full path of the input file to encrypt: ")
output_file_name_encrypt = input("Enter the full path of the output file for encryption: ")
encrypt_file(input_file_name_encrypt, output_file_name_encrypt, key)

input_file_name_decrypt = input("Enter the full path of the input file to decrypt: ")
output_file_name_decrypt = input("Enter the full path of the output file for decryption: ")
decrypt_file(input_file_name_decrypt, output_file_name_decrypt, key)

freq = letter_frequency(encrypted_message)
print("Frequency of each letter in the encrypted message:")
for char, count in freq.items():
    print(f"{char}: {count}")
