import streamlit as st

import functions
todos=functions.gets_todos()
def add_todo():
    newtodo=st.session_state["new_todo"] + "\n"
    todos.append(newtodo)
    functions.write_todos(todos)
st.title("My To-Do ")
st.subheader("Increase Your productivity ")
for index, todo in enumerate (todos):
    checkbox= st.checkbox(todo,key=todo)
    if checkbox:
      todos.pop(index)
      functions.write_todos(todos)
      del st.session_state[todo]
      st.rerun()
st.text_input(label="",placeholder="Add New Todo....",
              on_change=add_todo,key="new_todo")


