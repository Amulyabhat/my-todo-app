import streamlit as st
import functions

def add_todo():
    todo= st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)
todos= functions.get_todos()
st.title("My ToDo App")
st.subheader("Enter and organise your ToDos")

for index, todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add a new ToDo",
              on_change=add_todo, key="new_todo")

st.session_state