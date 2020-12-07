import menu


def main():
    print(menu.menu)

    appetizers = {
        'wings': 0,
        'onion_rings': 0,
        'spring_rolls': 0,
        'quit': 'quit',
    }

    entrees = {
        'salmon': 0,
        'steak': 0,
        'meat_tornado': 0,
        'a_literal_garden': 0,
        'quit': 'quit',
    }
    desserts = {
        'ice_cream': 0,
        'cake': 0,
        'pie': 0,
        'cookies': 0,
        'quit': 'quit',
    }

    drinks = {
        'beer': 0,
        'soda': 0,
        'coffee': 0,
        'tea': 0,
        'unicorn_tears': 0,
        'quit': 'quit',
    }

    user_input = ''

    while user_input != 'quit':
        user_input = input('> ')
        if user_input == 'wings':
            appetizers['wings'] += 1
            print('** ' + str(appetizers['wings']) +
                  ' order of Wings have been added to your meal **')
        elif user_input == 'quit':
            print('Thank you for your order!')
        else:
            print('Try again')
        continue
    # print(choice)

    # print(user_input)


if __name__ == "__main__":
    main()


# appetizers = {
#     'wings': 0,
#     'onion_rings': 0,
#     'spring_rolls': 0,
# }

# entrees = {
#     'salmon': 0,
#     'steak': 0,
#     'meat_tornado': 0,
#     'a_literal_garden': 0,
# }

# desserts = {
#     'ice_cream': 0,
#     'cake': 0,
#     'pie': 0,
#     'cookies': 0,
# }

# beverages = {
#     'beer': 0,
#     'soda': 0,
#     'coffee': 0,
#     'tea': 0,
#     'unicorn_tears': 0,
# }
