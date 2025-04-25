# Question Number 1

'''
This Python program performs:
* Encryption and decryption on the contents of a text file 'raw_text.txt' using Caesar-style cipher
* Writes encrypted output to encrypted_text.txt file
* Writes decrypted output to decrypted_text.txt file
* Then, verifies its correctness by comparing decrypted content with the original content.
'''
# Step 1: Define file paths
original_file_path = r"raw_text.txt"
encrypt_file_path = r"encrypted_text.txt"
decrypt_file_path = r"decrypted_text.txt"

# Step 2: Open and read the original file text
with open(original_file_path, 'r') as file:
    file_text = file.read()

# Step 3: Take the integer values for n and m from the user
while True:
    try:
        n = int(input("Enter the integer value for n: "))
        m = int(input("Enter the integer value for m: "))
        # Exit loop when both inputs are valid integers
        break
    except ValueError:
        # Handle the case if the inputs are not an integer
        print("Invalid input! Please enter integers value for both n and m.")
print("Encryption keys received: n = ", n, ", m = ", m)

# Step 4: Define the function for the data encryption
def encrypt(text, n, m):
    encrypt_result = ""
    for char in text:
        if char.isalpha():
            # Check the uppercase condition and encrypt
            # First half uppercase letters shifted backward by n
            if char.isupper() and 'A' <= char <= 'M':
                encrypt_result += chr((ord(char) - n - 65) % 13 + 65)
            # Second half uppercase letters shifted forward by m^2
            elif char.isupper() and 'N' <= char <= 'Z':
                encrypt_result += chr((ord(char) + (m**2) - 78) % 13 + 78)

            # Check the lowercase condition and encrypt
            # First half lowercase shifted forward by n * m
            elif char.islower() and 'a' <= char <= 'm':
                encrypt_result += chr((ord(char) + (n * m) - 97) % 13 + 97)
            # Second half lowercase shifted backward by n + m
            else:
                encrypt_result += chr((ord(char) - (n + m) - 110) % 13 + 110)
        else:
            # Handle space, special characters and numbers
            encrypt_result += char
    return encrypt_result

# Step 5: Encrypt the original text and save content to the new encrypted_text.txt file
encrypted_text = encrypt(file_text, n, m)
with open(encrypt_file_path, "w") as f:
    f.write(encrypted_text)

# Step 5: Define the function for decryption process
def decrypt(text, n, m):
    decrypt_result = ""
    for char in text:
        if char.isalpha():
            # Check the uppercase condition and decrypt
            if char.isupper() and 'A' <= char <= 'M':
            # Reverse the backward shift of n for first half
               decrypt_result += chr((ord(char) + n - 65) % 13 + 65)
            elif char.isupper() and 'N' <= char <= 'Z':
                # Reverse the forward shift of m^2 for second half
                decrypt_result += chr((ord(char) - (m**2) - 78) % 13 + 78)

            # Check the lowercase condition and decrypt
            elif char.islower() and 'a' <= char <= 'm':
                # Reverse the forward shift of n*m
                decrypt_result += chr((ord(char) - (n * m) - 97) % 13 + 97)
            else:
                # Reverse the backward shift of n+m
                decrypt_result += chr((ord(char) + (n + m) - 110) % 13 + 110)
        else:
            # Handle space, special characters and numbers
            decrypt_result += char
    return decrypt_result

# Step 6: Read the encrypted text 
with open(encrypt_file_path, 'r') as file:
    encrypted_file_text = file.read()

# Step 7: Decrypt the encrypted content
decrypted_text = decrypt(encrypted_file_text, n, m)
with open(decrypt_file_path, "w") as f:
    f.write(decrypted_text)

# Step 8: Display both encrypted and decrypted results 
print("\nOriginal Text:\n", file_text)
print("\nEncrypted Text:\n", encrypted_text)
print("\nDecrypted Text:\n", decrypted_text)

# Step 9: Verify the content of decrypted text with the original one
with open(original_file_path, "r") as f1, open(decrypt_file_path, "r") as f2:
    original_content = f1.read().rstrip() #removing unnecessary whitespaces using rstrip()
    decrypted_content = f2.read().rstrip() 

if original_content == decrypted_content:
    print("\n Decryption verified successfully! ✅✅")
else:
    print("\n Decryption failed! ❌❌")