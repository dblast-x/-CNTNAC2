def list_entries() -> list[str]:
    """
    .    Home page     .
    . New entries page .
    """
    elements = list()

    run = True
    while run:
        element = input("Enter a new element or q to quit >>\n~> ").lower()
        if element == "q":
            run = False
        else:
            elements.append(element)

    return elements


def create_table(elements: list) -> dict:
    """
    . Page to account sells .
    .        Logger         .
    """
    table = dict()
    for element in elements:
        table[element] = 2

    return table


def print_table(table: dict):
    """
    . Display page .
    """
    for key in table.keys():
        print(key + " ->> " + str(table[key]))


def run():
    entries = list_entries()
    table = create_table(entries)
    print_table(table)


if __name__ == "__main__":
    run()
