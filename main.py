while True:
    userChoice = input("Type add, show, edit, complete, or exit: ")
    userChoice = userChoice.strip()


    def printList():
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for i, item in enumerate(todos, start=1):
            item = item.strip('\n')
            print(f"{i}. {item}")


    if 'add' in userChoice:
        todo = userChoice[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo +'\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif "show" in userChoice:
        printList()
    elif "edit" in userChoice:
        printList()
        choice = int(userChoice[5:]) - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        update = input("Enter new To Do: ")

        todos[choice] = update + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif "complete" in userChoice:
        printList()
        choice = int(userChoice[9:]) - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todoToRemove = todos[choice].strip('\n')
        todos.pop(choice)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo item - '{todoToRemove}' was removed from the list."
        print(message)
    elif 'exit' in userChoice:
        break
    else:
        print("Unrecognized input, please try again")

print("Bye!")
