FILEPATH = "db.txt"

def get_lines(filepath=FILEPATH):
    """Reads the text file and returns the list of items."""
    with open(filepath, "r") as file:
        items = file.readlines()
    return items


def write_lines(items, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(items)