import streamlit as st
import socket
import os

st.write(os.system('hostname'))

print(socket.gethostname())
st.write(socket.gethostname())
print(os.environ)
print(os.environ.STREAMLIT_HOST)
print(STREAMLIT_HOST)
