# Introduction to Information Security
# Assignment 1
# Name:- Mansi Dinesh
# CWID:- A20556560
# Function for encrypting a text using a Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Check if the character is alphabetic
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            # Shift the character and handle wrap-around
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            # Append the shifted character to the encrypted text
            encrypted_text += shifted_char
        else:
            # If the character is not alphabetic, leave it unchanged
            encrypted_text += char
    # Return the final encrypted text
    return encrypted_text

# Function for decrypting a text using a Caesar Cipher
def decrypt(encrypted_text, shift):
    # Decryption is the same as encryption with a negative shift
    return encrypt(encrypted_text, -shift)

# Function for conducting a brute force attack on a Caesar Cipher encrypted text
def brute_force_attack(encrypted_text):
    # Try all possible shifts and print the decrypted text for each shift
    for shift in range(26):
        decrypted_text = decrypt(encrypted_text, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Main program loop
while True:
    # Display the menu options
    print("\nMenu:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force Attack")
    print("4. Exit")

    # Get the user's choice for the menu option
    choice = input("Enter the option number: ")

    # Option 1: Encryption
    if choice == "1":
        # Get the plaintext input from the user
        plaintext = input("Enter the text to encrypt: ")
        # Check if the plaintext is empty and prompt the user for valid input
        if not plaintext:
            print("Invalid input. Please enter a valid text.")
            continue
        # Get the shift value for encryption
        shift_value = int(input("Enter the shift value: "))
        # Encrypt the plaintext and display the result
        encrypted_result = encrypt(plaintext, shift_value)
        print(f"Encrypted: {encrypted_result}")

    # Option 2: Decryption
    elif choice == "2":
        # Get the encrypted text input from the user
        encrypted_text = input("Enter the text to decrypt: ")
        # Check if the encrypted text is empty and prompt the user for valid input
        if not encrypted_text:
            print("Invalid input. Please enter a valid text.")
            continue
        # Get the shift value for decryption
        shift_value = int(input("Enter the shift value: "))
        # Decrypt the text and display the result
        decrypted_result = decrypt(encrypted_text, shift_value)
        print(f"Decrypted: {decrypted_result}")

    # Option 3: Brute Force Attack
    elif choice == "3":
        # Get the encrypted text input from the user
        encrypted_text = input("Enter the encrypted text: ")
        # Check if the encrypted text is empty and prompt the user for valid input
        if not encrypted_text:
            print("Invalid input. Please enter a valid text.")
            continue
        # Display the results of the brute force attack
        print("\nBrute Force Attack Results:")
        brute_force_attack(encrypted_text)

    # Option 4: Exit the program
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break

    # Invalid option: Prompt the user to choose a valid option
    else:
        print("Invalid option. Please choose a valid option.")
