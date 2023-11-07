import functions
import PySimpleGUI as psg

label = psg.Text("Type in a to-do: ")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.get_todos(),
                       key="items",
                       enable_events=True,
                       size = [45, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

window = psg.Window("My To-Do App",
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.set_todos(todos)
            window['items'].update(values=todos)
        case "Edit":
            todo_to_edit = values['items'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.set_todos(todos)
            window['items'].update(values=todos)
        case "items":
            window['todo'].update(value=values['items'][0])
        case "Complete":
            todo_to_complete = values['items'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.set_todos(todos)
            window['items'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case psg.WIN_CLOSED:
            break

window.close()
