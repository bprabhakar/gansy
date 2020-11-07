import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time


"""
# aarzoo
Enter a text query below and we'll parse out the task for you:
"""

title = st.text_input('Your wish is my command')
if title:
    with st.spinner('Wait for it...'):
        time.sleep(1)
    answer = {
        'who': 'Bharat',
        'what': 'Make some noise',
        'when': '2020-12-31'
    }
    answer
# col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
# with col3:
#     if st.button("Correct"):
#         st.text("Yay!")
#         st.balloons()
# with col4:
#     if st.button("Incorrect"):
#         st.text("Oh no! :(")
