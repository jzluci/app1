def printlist():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()

    print("Current list: ")
    for i, item in enumerate(todos, start=1):
        item = item.strip('\n')
        print(f"{i}. {item}")


def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


def set_todos():
    with open('todos.txt', 'w') as file:
        file.writelines(todos)


while True:


    userChoice = input("Type add, show, edit, complete, or exit: ")
    userChoice = userChoice.strip()

    if userChoice.startswith("add"):
        todo = userChoice[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif userChoice.startswith("show"):
        printlist()
    elif userChoice.startswith("edit"):
        try:
            choice = int(userChoice[5:]) - 1

            todos = get_todos()

            update = input("Enter new To Do: ")

            todos[choice] = update + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Unrecognized input. Try again")
            continue

    elif userChoice.startswith("complete"):
        try:
            choice = int(userChoice[9:]) - 1

            todos = get_todos()

            todoToRemove = todos[choice].strip('\n')
            todos.pop(choice)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo item - '{todoToRemove}' was removed from the list."
            print(message)
        except IndexError:
            print("Value out of scope please try again")
            continue
    elif userChoice.startswith("exit"):
        break
    else:
        print("Unrecognized input, please try again")

print("Bye!")
