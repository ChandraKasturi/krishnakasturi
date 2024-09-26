import streamlit as st
from openai import OpenAI
import re
import os
import json

##st.title("IP Module Agent")

# Predefined list of NCLT bench locations
BENCH_LOCATIONS = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Hyderabad', 'Bengaluru', 'Ahmedabad', 'Chandigarh', 'Jaipur', 'Guwahati']
def parse_user_input(user_input):
    """Use OpenAI ChatCompletion API to extract CIN, default amount, bench location, and show/hide company details from natural language input. If Available Take fields from the previous Context"""
    extraction_prompt = f"""
    User Input: {user_input}
    
    Previous JSON: {st.session_state.localug}
    Extract the following details from the above input if available And Respond with a Valid JSON without markdown {{"CIN":"","Amount":"","NCTL Bench Location":"","Show Company Details":"", "Last Date to Submit Interest":""'}}:
    - If the details are already present in the previous JSON update the JSON    
    - Company Identification Number (CIN)
    - Default amount (in crores or lakhs)
    - NCLT Bench Location
    - Whether the user wants to show company details if the user wants to show details keep it as YES if the user wants to hide keep it as NO
    - If date is found please format that in the DD-MMM-YYYY format
    """

    stream = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.2,  # You can replace this with "gpt-4" if available
        messages=[
            {"role": "system", "content": "You are an assistant that extracts company information from user input."},
            {"role": "user", "content": extraction_prompt}
        ],
        max_tokens=150
    )
    streamug = stream.choices[0].message.content.strip()
    #return response['choices'][0]['message']['content'].strip()
    return streamug

def validate_extracted_info(extracted_info):
    """Use regex or simple checks to validate the extracted information."""
    cin_match = re.search(r"CIN:\s*(\w{21})", extracted_info)
    amount_match = re.search(r"Default amount:\s*([\d.]+)\s*(crores|lakhs)", extracted_info, re.IGNORECASE)
    bench_match = re.search(r"Bench Location:\s*([A-Za-z]+)", extracted_info)
    show_company_match = re.search(r"Show company details:\s*(Yes|No)", extracted_info, re.IGNORECASE)

    # Extract values or set them to None if not found
    cin = cin_match.group(1) if cin_match else None
    default_amount = amount_match.group(1) if amount_match else None
    default_unit = amount_match.group(2).lower() if amount_match else None
    bench_location = bench_match.group(1) if bench_match and bench_match.group(1) in BENCH_LOCATIONS else None
    show_company = show_company_match.group(1).lower() == "yes" if show_company_match else None
    print(f"UGUG{cin}")
    return {
        "cin": cin,
        "default_amount": default_amount,
        "default_unit": default_unit,
        "bench_location": bench_location,
        "show_company": show_company
    }

def ask_for_missing_info(data):
    """Prompt user for missing or invalid fields."""
    missing_info = []

    if not data['cin']:
        missing_info.append("Company Identification Number (CIN)")
    if not data['default_amount']:
        missing_info.append("Default amount")
    if not data['bench_location']:
        missing_info.append(f"NCLT Bench location (choose from: {', '.join(BENCH_LOCATIONS)})")
    if data['show_company'] is None:
        missing_info.append("Show company details (Yes/No)")

    return missing_info

def agent_page():
    """Interactive AI Assistant Page with Chat-like Interface."""

    st.title("Expresson of Interest for NCLT")
    if "localug" not in st.session_state:
        st.session_state.localug = []
    # Initialize session state to store chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display previous chat messages
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])
    # Capture user input via chat-like interface
    user_input = st.chat_input("Describe your request...")

    if user_input:
        # Display user's message in the chat
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
    
        # Step 1: Parse and extract relevant details using OpenAI
        extracted_info = parse_user_input(user_input)
        # Step 2: Display AI response and extracted information
        st.session_state.localug = json.loads(extracted_info)
        if not all([v for k,v in st.session_state.localug.items()]):
            ug_return = "**Please Provide the Below Information To Process The Request**\n"
            for k,v in st.session_state.localug.items():
                if not v:
                    ug_return = ug_return + f"- {k}\n"
            with st.chat_message("assistant"):
                st.markdown(ug_return)
            st.session_state.chat_history.append({"role":"assistant","content":ug_return})
        else:
            ug_return_ug = "**Processed  The Request With the Below Information Please Review**\n"
            for k,v in st.session_state.localug.items():
                ug_return_ug = ug_return_ug + f"- {k} : {v}\n"
            with st.chat_message("assistant"):
                st.markdown(ug_return_ug)
            st.session_state.chat_history.append({"role":"assistant","content":ug_return_ug})
            st.session_state.localug = {}
                
        # Step 3: Validate the extracted information
        

# Calling agent_page function to ensure it's loaded when this page is accessed
if __name__ == "__main__":
    agent_page()
