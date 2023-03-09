def encode(password):
    new_password = ''
    for element in str(password):
        if element == '9':
            new_password += '2'
        elif element == '8':
            new_password += '1'
        elif element == '7':
            new_password += '0'
        else:
            char = int(element) + 3
            new_password += str(char)

    return new_password


def print_menu():
    print('menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')



def main():
    while True:
        print_menu()
        user_input = input('Please enter an option: ')
        if user_input == '1':
            password = input('Please enter your password to decode: ')
            encoded = encode(password)
            print('Your password has been encoded and stored\n')
        elif user_input == '2':
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.\n')
        elif user_input == '3':
            quit()


if __name__ == '__main__':
    main()
