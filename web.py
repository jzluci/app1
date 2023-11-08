import streamlit as st
import functions


def add_todo():
    todo_local = st.session_state["new_todo"] + '\n'
    todos.append(todo_local)
    functions.set_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my to-do app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder="Add new todo",
              key='new_todo',
              on_change=add_todo)
