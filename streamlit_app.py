import streamlit as st
import socket
import os

st.write(os.system('hostname'))

print(socket.gethostname())
st.write(socket.gethostname())


print(os.environ.get("STREAMLIT_HOST", ""))
