FILEPATH = "todos.txt"


def printlist():
    with open(FILEPATH, 'r') as file_local:
        todos_local = file_local.readlines()

    print("Current list: ")
    for i, item in enumerate(todos_local, start=1):
        item = item.strip('\n')
        print(f"{i}. {item}")


def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def set_todos(filepath, todos_arg):
    with (open(filepath, 'w') as file_local):
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
