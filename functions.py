FILEPATH = "todos.txt"


def printlist():
    with open(FILEPATH, 'r') as file_local:
        todos_local = file_local.readlines()

    print("Current list: ")
    for i, item in enumerate(todos_local, start=1):
        item = item.strip('\n')
        print(f"{i}. {item}")


#reads todos from txt file
def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#writes todos to txt file
def set_todos(todos_arg, filepath = FILEPATH):
    with (open(FILEPATH, 'w') as file_local):
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
