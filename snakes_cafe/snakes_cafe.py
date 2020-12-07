import menu


def main():
    print(menu.menu)
    choice = {
        'wings': 0,
        'onion_rings': 0,
        'spring_rolls': 0,
        'salmon': 0,
        'steak': 0,
        'meat_tornado': 0,
        'a_literal_garden': 0,
        'ice_cream': 0,
        'cake': 0,
        'pie': 0,
        'cookies': 0,
        'beer': 0,
        'soda': 0,
        'coffee': 0,
        'tea': 0,
        'unicorn_tears': 0,
        'quit': 'quit',
    }

    while choice != 'quit':
        choice = input('> ')
        if choice == 'wings':
            # print()
            # choice['wings'] += 1
            return (str(choice['wings']) +
                    '** order of Wings have been added to your meal **')
        elif choice == 'quit':
            print('Thank you for your order!')
        else:
            print('Try again')

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
