import streamlit as st
from forms.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/my_profile_pic.png", width=230)

with col2:
    st.title("Sri Krishna Kasturi", anchor=False)
    st.write(
        "Product / Delivery Manager and Gen AI Consultant"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")

st.subheader("The journey so far", anchor=False)

st.markdown('<div style="text-align: justify;">In my journey of over 20 years of experience in the tech and business world, I specialize in turning complex challenges into growth opportunities. My expertise spans AI, banking, and insurance, where I’ve led high-impact projects that not only meet but exceed expectations. From integrating AI solutions to streamlining operations to ensuring compliance for banking systems, I thrive at the intersection of technology and business strategy. My leadership style combines innovation with practical execution, all while keeping teams motivated and clients satisfied. I’m passionate about delivering success through collaboration, cutting-edge technology, and a clear vision for the future.</div>', unsafe_allow_html=True)


st.subheader("Key Achievements", anchor=False)
st.write(
    """
    - AI Integration for Customer Success: Implemented AI agent, to handle customer queries, reducing support tickets by 20% and increasing client satisfaction. Responsible from idea to execution.
    - Revenue Boost Cloud Migration: Successfully migrated 3 major clients from on-premises systems to AWS, improving company revenue and reducing operational costs.
    - Client Retention with Cutting-Edge Tech: Upgraded banking systems to ensure compliance with SWIFT 2021, helping to retain 14 major clients.
    - Streamlining Product Delivery: Delivered 30+ projects with 70% on-time completion while maintaining high standards of quality and staying within budget.
    - Award-Winning Leadership: Recognized with the Best Manager Award (CGI, 2017-2018) for successfully delivering the Trade 360 Transformation Project.
    - New Revenue Streams: Developed a new service offering that contributed to increased company revenue and improved client satisfaction.
    """
)


