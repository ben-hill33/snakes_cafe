import menu


appetizers = {
    'wings': 0,
    # 'onion_rings': 0,
    # 'spring_rolls': 0,
}

entrees = {
    'wings': 0,
    # 'onion_rings': 0,
    # 'spring_rolls': 0,
}

desserts = {
    'wings': 0,
    # 'onion_rings': 0,
    # 'spring_rolls': 0,
}


def main():
    print(menu.menu)

    # print(menu)
    appetizer_order = appetizers['wings']

    user_input = input('> ')

    print(user_input)
    print(appetizer_order)

    appetizers['wings'] += 1
    print(appetizers)


if __name__ == "__main__":
    main()
