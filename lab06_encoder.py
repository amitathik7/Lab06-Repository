
# Name: Amit Athi Kesavan

def encode(password):
    output = ""

    for x in password:
        output += str(int(x) + 3)

    return output

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


if __name__ == "__main__":
    main()