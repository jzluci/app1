while True:
    userChoice = input("Type add, show, edit, complete, or exit: ")
    userChoice = userChoice.strip()

    def printList():
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        for i, item in enumerate(todos, start=1):
            print(f"{i}. {item}")

    match userChoice:
        case 'add':
            todo = input("Enter Todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            printList()
        case "edit":
            printList()
            choice = int(input("Select number of To Do to edit: ")) - 1
            update = input("Enter new To Do: ")
            todos[choice] = update
        case "complete":
            printList()
            choice = int(input("Select number of To Do to complete: ")) - 1
            todos.pop(choice)
        case 'exit':
            break

print("Bye!")
