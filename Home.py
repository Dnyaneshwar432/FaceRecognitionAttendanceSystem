import streamlit as st

st.set_page_config(page_title='Attendance System',layout='wide')


import face_rec
from auth import authenticator
import warnings

warnings.filterwarnings('ignore')

if 'authentication_status' not in st.session_state:
    st.session_state['logout':'authentication_status'] = False

    
if st.session_state['authentication_status']:
    authenticator.logout('Logout', 'sidebar', key='unique_key')

    st.write(f'Welcome *{st.session_state["name"]}*')

    
    st.header('Face Recognition Attendance System')
        
    st.success('Model loaded sucesfully')
    
    image = st.image('MainPageImg.jpg',use_column_width=True)

    st.success('Connected to DataBase Successfully')

else:
    login_info = authenticator.login('main')
if login_info:
    name, authentication_status, username = login_info



