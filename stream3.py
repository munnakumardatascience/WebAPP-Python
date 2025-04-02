import streamlit as st

name=st.text_input('Enter your name:')
fname=st.text_input('Enter fathers name:')
addr=st.text_area('Enter your address')
classdata=st.selectbox('select your class',[1,2,3,4,6,7])

button =st.button('done')
if button:
    st.markdown(
        f'name:{name}, fname:{fname}, addr:{addr},classdata:{classdata}'
        )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    