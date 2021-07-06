import streamlit as st
import socket
import os

st.write("hello")

if os.getenv("HOSTNAME") == "streamlit":
  os.write("welcome to the cloud")

st.write(os.environ)
