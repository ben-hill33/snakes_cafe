import menu


def main():
    print(menu.menu)
    
    order = {
        'wings': 0,
        'onion rings': 0,
        'spring rolls': 0,
        'salmon': 0,
        'steak': 0,
        'meat tornado': 0,
        'a literal garden': 0,
        'ice cream': 0,
        'cake': 0,
        'pie': 0,
        'cookies': 0,
        'beer': 0,
        'soda': 0,
        'coffee': 0,
        'tea': 0,
        'unicorn tears': 0,
        'quit': 'quit',
    }

    user_input = ''

    while user_input != 'quit':
        user_input = input('> ')
        input_lower = user_input.lower()
        if user_input == user_input:
            order[input_lower] += 1
            print('** ' + str(order[input_lower]) + ' order of ' + input_lower + ' have been added to your meal **')
        elif input_lower == 'quit':
            print('Thank you for your order!')
        else:
            print('Try again')
        

if __name__ == "__main__":
    main()
