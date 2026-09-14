import streamlit as st
def header_home():

    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
                <div style='display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 30px; margin-bottom: 30px;'>
                    <img src='{logo_url}' style='height:100px;'/>
                </div>
                <h1 style='text-align:center; color: #E0E3FF'>Auto<br>Attendance</h1>
                """
            ,unsafe_allow_html=True)