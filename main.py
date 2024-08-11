import streamlit as st 
from PIL import Image

# Page Setup
about_page = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = ":material/account_circle:",
    default = True,
)
chatbot_page = st.Page(
    page = "views/sales_dashboard.py",
    title = "Sales Dashboard",
    icon = ":material/bar_chart:",
)
dashbord_page = st.Page(
    page = "views/chatbot.py",
    title = "Chat Bot",
    icon = ":material/smart_toy:",
)

# Navigation
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [chatbot_page, dashbord_page],
    }
)

# Visible on all pages
st.logo("assets/brenco.png")
st.sidebar.text("Computer Scientist")

# Run Navigation
pg.run()
