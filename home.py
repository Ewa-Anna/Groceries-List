import streamlit as st
import modules

st.title("Groceries List")
if st.button("Clear"):
    file = open("db.txt", "w")
    file.close()
    file2 = open("db_bought.txt", "w")
    file2.close
    st.experimental_rerun()

col1, col2 = st.columns(2)

items = modules.get_lines(filepath="db.txt")
items_bought = modules.get_lines(filepath="db_bought.txt")

def add_item():
    item = st.session_state["new_item"] + "\n" 
    if item not in items:
        items.append(item)
        modules.write_lines(items)
        st.session_state["new_item"] = ""
    else:
        st.warning("Item already on the list!", icon="⚠️")

with col1: 
    st.subheader("To Buy:")
    for index, item in enumerate(items):
        checkbox = st.checkbox(item, key=f"{index} - {item}")
        if checkbox:
            items.pop(index)
            modules.write_lines(items)
            items_bought.append(item)
            modules.write_lines(items_bought, filepath="db_bought.txt")
            del st.session_state[f"{index} - {item}"]
            st.experimental_rerun()

with col2:
    st.subheader("Bought:")
    for item in items_bought:
        st.write(f"<span style='color:green'><s> {item} </s></span>", unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new item...", 
              on_change=add_item, key="new_item")


    