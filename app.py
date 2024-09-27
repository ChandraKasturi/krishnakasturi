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
title="NCLT EOI",
icon=":material/bar_chart:"
)

pg = st.navigation(
    {
        
        "Info":[about_page],
        "Projects":[chat_page]
        
        }
        
        )

st.logo("assets/krishna_logo.png")
sentence = "Made with ❤️ Krishna"
st.sidebar.text(sentence)

pg.run()
