import streamlit as st
from rag import get_answer

st.set_page_config(page_title="MkDocs Assistant", page_icon="🤖")

st.title("MkDocs Assistant &nbsp; 🤖")
st.caption("Ask questions about MkDocs configuration and usage.")

# Initialize chat history
# session_state maintains state of global variables across reruns
if "messages" not in st.session_state:
    st.session_state.messages = [] 

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you with MkDocs?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from RAG
    with st.spinner("Thinking..."):
        try:
            response = get_answer(prompt)
        except Exception as e:
            response = f"⚠️ An error occurred: {str(e)}"

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})