def get_input():
    while True:
        binary = input("Type a binary number up to 8 digits: ")
        if len(binary) >8:
            print("Too long.")
            break
        else:
            return binary

def convert_to_decimal():
    return