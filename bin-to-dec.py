def get_input():
    user_bin = input('Enter binary up to 8 digits: ')
    while True:
        if len(user_bin > 8):
            print('Too long.')
            break
        else:
            return