import streamlit as st

# ---Page Set up---
about_page = st.Page(
page="views/about_me.py",
title="About Me",
icon=":material/account_circle:",
default=True
)

chat_page = st.Page(
page="views/chatbot.py",
title="Chat Bot",
icon=":material/smart_toy:"
)

skill_dashboard_page = st.Page(
page="views/skill_dashboard.py",
title="Skill Dashboard",
icon=":material/bar_chart:"
)

pg = st.navigation(
    {
        
        "Info1":[about_page],
        "Projects1":[skill_dashboard_page,chat_page]
        
        }
        
        )

st.logo("assets/krishna_logo.png")
sentence = "Made with ❤️ Krishna"
st.sidebar.text(sentence)

pg.run()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
