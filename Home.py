import streamlit as st
from stmol import *
import io

st.set_page_config(page_title="Stmol", page_icon="🧬",layout="wide")
st.sidebar.markdown('''
    [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&color=black&label)](https://github.com/vatsn/stmol/tree/master)
    ''')  
with io.open(f'README.md', mode='r', encoding='utf-8') as f:           
    st.markdown(f.read(),unsafe_allow_html=True)
