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
def header_dashbord():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;">
            <img src="{logo_url}" style="
                height: 85px;
                width: auto;">
            <h2 style="
                color: #5865F2;
                margin: 0;
                padding: 0;
                white-space: nowrap;
                font-size: 28px;">
                Auto<br>Attendance
            </h2>
        </div>
        """,unsafe_allow_html=True)