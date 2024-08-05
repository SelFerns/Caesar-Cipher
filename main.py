def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            result += char

    return result


def get_user_input():
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    return text, shift


def main():
    while True:
        print("Enter text to encrypt.")
        text, shift = get_user_input()
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")

        choice = input("Do you want to decrypt the text? (y/n): ").lower()
        if choice == 'y':
            decrypted_text = decrypt(encrypted_text, shift)
            print(f"Decrypted Text: {decrypted_text}")

        print()
        another = input("Do you want to perform another operation? (y/n): ").lower()
        if another != 'y':
            break


if __name__ == "__main__":
    main()
