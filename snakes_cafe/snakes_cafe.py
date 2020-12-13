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
        input_to_lower = user_input.lower()
        if input_to_lower == 'quit':
            print('Thank you for your order!')
            continue
        elif input_to_lower in order:
            order[input_to_lower] += 1
            print(f'** {order[input_to_lower]} order of {input_to_lower} have been added to your meal **')
            continue
        else:
            print('Sorry, we don\'t serve that here')
            
        

if __name__ == "__main__":
    main()
