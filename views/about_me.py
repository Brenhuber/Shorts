import streamlit as st 

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# Section
col1, col2 = st.columns(2, gap = "small", vertical_alignment = "center")
with col1:
    st.image("assets/brenco.png", width = 230)
with col2:
    st.title("Bren Huber", anchor = False)
    st.write(
        "Computer Scientist, studying at Arizona State University."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# Experience & Qualifications
st.write("\n")
st.subheader("Experience & Qualifications", anchor = False) 
st.write(
    """
    Technical Skills
    - Proficient Languages: Java and Python
    - Other Languages: C#, MATLAB, MySQL, HTML, CSS, Prolog, Assembly
    """
)