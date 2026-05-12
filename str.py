import streamlit as st 
import requests
st.title('Ckecking the api calls or not')
url = 'http://127.0.0.1:8000/books/' 
if st.button('click'):
    try:
        response = requests.get(url=url)
        if response.status_code==200:
            st.json(response.json())
    except Exception as e:
        st.write('there is an errro here ')
