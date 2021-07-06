import streamlit as st
import socket
import os

st.write(os.environ.get("STREAMLIT_HOST", ""))
