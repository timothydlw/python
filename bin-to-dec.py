   
def convert_binary_to_decimal():
    def get_input():
        user_bin = input('Enter binary up to 8 digits: ') 
        while True:
            if len(user_bin) > 8:
                print('Too long.')
                break
            else:
                return user_bin

    def convert_bin_to_dec(user_bin):
        dec_out = int(user_bin, 2)
        print(dec_out)

    user_bin = get_input()
    convert_bin_to_dec(user_bin)

convert_binary_to_decimal()