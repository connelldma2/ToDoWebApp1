
import streamlit as st
import ToDoFunctions

todos_list = ToDoFunctions.get_file_todos()

def add_todo():
    new_todo_item = st.session_state["new_todo"] + "\n"
    todos_list.append(new_todo_item)

    ToDoFunctions.write_file_todos(todos_list)

st.title("My Module App")
st.subheader("Academic Management Tool")
st.write("This app is designed to manage your module offerings.")

for index, item in enumerate(todos_list):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos_list.pop(index)
        ToDoFunctions.write_file_todos(todos_list)
        del st.session_state[item]
        st.experimental_rerun()


st.text_input(label="", placeholder="Enter a module name ...", key="new_todo", on_change=add_todo)

# st.session_state


