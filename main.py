from functions import *
import time

datetime = time.strftime("%b %d, %Y %H:%M:%S")
print(datetime)

while True:

    userChoice = input("Type add, show, edit, complete, or exit: ")
    userChoice = userChoice.strip()

    if userChoice.startswith("add"):
        todo = userChoice[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        set_todos('todos.txt', todos)

    elif userChoice.startswith("show"):
        printlist()
    elif userChoice.startswith("edit"):
        try:
            choice = int(userChoice[5:]) - 1

            todos = get_todos()

            update = input("Enter new To Do: ")

            todos[choice] = update + '\n'

            set_todos('todos.txt', todos)

        except ValueError:
            print("Unrecognized input. Try again")
            continue

    elif userChoice.startswith("complete"):
        try:
            choice = int(userChoice[9:]) - 1

            todos = get_todos()

            todoToRemove = todos[choice].strip('\n')
            todos.pop(choice)

            set_todos('todos.txt', todos)

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
