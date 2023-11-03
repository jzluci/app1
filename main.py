todos =[]


while True:
    userChoice = input("Type add, show, or exit: ")
    userChoice = userChoice.strip()

    match userChoice:
        case 'add':
            todo = input("Enter Todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case 'exit':
            break
