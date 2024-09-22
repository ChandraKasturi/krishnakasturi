import streamlit as st
from groq import Groq

st.title("Chat with Llama 3.1")

# Initialize the Groq client with API key
client = Groq(api_key=st.secrets["API_KEY"])

# Set the default model if it's not in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "llama3-groq-70b-8192-tool-use-preview"

# Initialize messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant's response
    with st.chat_message("assistant"):
        # Stream the response from the API
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        
        # Collect and display the full response
        response_content = ""
        response_placeholder = st.empty()  # Placeholder for dynamic updates

        for chunk in stream:
            if chunk.choices[0].delta.content:
                response_content += chunk.choices[0].delta.content

            # Update the content in the placeholder dynamically
            response_placeholder.markdown(response_content)

    # Append assistant's response to session state
    st.session_state.messages.append({"role": "assistant", "content": response_content})
