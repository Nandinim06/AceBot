#installed streamlit
import streamlit as st
from streamlit_chat import message
from bardapi import Bard


token = 'XQjUurKVRCZM2v-6zalGD9cEJ8tyU-_H-0tCPOWEsGLovLbzbAD6-7bL76cwxDIxp0W1Xw.'

#function to generate the output
def generate_response(prompt):
    bard = Bard(token=token)
    response = bard.get_answer(prompt)['content']
    return response

#function to recieve user queries
def get_text():
    input_text = st.text_input("ACE bot", "Hello!", key='input')
    return input_text


#title of the streamlit app
st.title('AceBot')

#url = 'https://images.unsplash.com/photo-1582996782008-49e06ddac471?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80'
#data-testid="stAppViewContainer"
changes = '''
<style>
[data-testid="stAppViewContainer"]
    {
    background-image:url('https://images.unsplash.com/photo-1536183922588-166604504d5e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80');
    background-size:cover;
    }
    html{
    background:transparent
    }
    div.esravye2 > iframe
    {
    background-colour:transparent
    }

</style>
'''
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

#accepting user input
user_input = get_text()
if user_input:
    print(user_input)
    output = generate_response(user_input)
    print(output)
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_"+str(i), is_user=True)
