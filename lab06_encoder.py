
# Name: Amit Athi Kesavan

def encode(password):
    output = ""

    for x in password:
        output += str(int(x) + 3)

    return output

def decode(password):
    decode_password = ""
    for digit in password:
        decode_digit = str((int(digit) - 3))
        decode_password += decode_digit
        return decode_password


def main():
    password = ""
    encoded_password = ""

    while True:
        print("""Menu  
------------- 
1. Encode  
2. Decode  
3. Quit

Please enter an option: """, end="")
        option = input()

        if option == "1":
            print("Please enter your password to encode: ", end="")
            password = input()
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "3":
            break
        elif option == "2":
            print(f"The encoded password is {encoded_password}, and the originl password is {decode(encoded_password)}.")


if __name__ == "__main__":
    main()