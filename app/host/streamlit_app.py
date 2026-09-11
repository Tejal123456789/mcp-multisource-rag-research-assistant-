import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
import streamlit as st

# Import your MCP functions directly for now
from server.mcp_server import ask_anything

st.set_page_config(
    page_title="MCP Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 MCP + RAG Research Assistant")

# Store conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for message in st.session_state.messages:

    if message["role"] == "user":
        st.chat_message("user").write(
            message["content"]
        )

    else:
        st.chat_message("assistant").write(
            message["content"]
        )

# Chat input
question = st.chat_input(
    "Ask a question..."
)

if question:

    # Show user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.chat_message("user").write(question)

    # Call your MCP workflow
    response = ask_anything(question)

    # Show assistant response
    st.chat_message("assistant").write(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )