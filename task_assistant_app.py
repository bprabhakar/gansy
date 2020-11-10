import streamlit as st
import time
import requests

"""
# aarzoo
Enter a text query below and we'll parse out the task for you:
"""

title = st.text_input('Your wish is my command')

@st.cache
def wit_ai_parser(text):
    wit_resp = requests.get(
        "https://api.wit.ai/message", 
        params={
            "v": "20200513",
            "q": text
        }, 
        headers={
            "Authorization": "Bearer 6S3EOCISKXNEYMOEOGH54ELDOTI4EFW2"
        }
    )
    raw_pred = wit_resp.json().get("entities", {})
    response = {
        "Who": "?",
        "When": "?",
        "What": "?"
    }
    for entity_key, entity_vals in raw_pred.items():
        max_score = 0
        for entity in entity_vals:
            if entity.get("confidence", 0) > max_score:
                val = entity.get("body", "?")
                max_score = entity.get("confidence", 0)
        if entity_key == "wit$contact:contact":
            response["Who"] = val.capitalize()
        elif entity_key == "wit$datetime:datetime":
            response["When"] = val.capitalize()
        elif entity_key == "wit$reminder:reminder":
            response["What"] = val.capitalize()
    return response

if title:
    try:
        answer = wit_ai_parser(title)
    except:
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
