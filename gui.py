import functions
import PySimpleGUI as psg

label = psg.Text("Type in a to-do: ")
input_box = psg.InputText(tooltip="Enter to-do", key="todo")
add_button = psg.Button("Add")

window = psg.Window("My To-Do App",
                    layout=[[label], [input_box, add_button]],
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
        case psg.WIN_CLOSED:
            break

window.close()
