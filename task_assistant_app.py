import streamlit as st
import time
import requests
import pendulum
import json

"""
# aarzoo
Enter a text query below and we'll parse out the task for you:
"""

title = st.text_input('Your wish is my command')

@st.cache
def extract_interval(raw_value, tz="Asia/Kolkata"):
    if raw_value['type'] == 'interval':
        start_ts = pendulum.parse(raw_value['from']['value']).in_timezone(tz)
        end_ts = pendulum.parse(raw_value['to']['value']).in_timezone(tz)
    elif raw_value['type'] == 'value':
        start_ts = pendulum.parse(raw_value['value']).in_timezone(tz)
        end_ts = start_ts.end_of(raw_value['grain'])
    else:
        start_ts = pendulum.now(tz)
        end_ts = pendulum.now(tz)

    return start_ts.to_date_string(), end_ts.to_date_string()

@st.cache
def wit_ai_parser(text):
    wit_resp = requests.get(
        "https://api.wit.ai/message", 
        params={
            "v": "20200513",
            "q": text,
            "context": json.dumps({
                "timezone": "Asia/Kolkata",
                "locale": "en_IN"
            })
        }, 
        headers={
            "Authorization": "Bearer 6S3EOCISKXNEYMOEOGH54ELDOTI4EFW2"
        }
    )
    raw_pred = wit_resp.json().get("entities", {})
    response = {
        "What": "?",
        "Who": "?",
        "When": "?"
    }
    for entity_key, entity_vals in raw_pred.items():
        max_score = 0
        val = {}
        for entity in entity_vals:
            if entity.get("confidence", 0) > max_score:
                val = entity
                matched_text = entity.get("body", "?").capitalize()
                max_score = entity.get("confidence", 0)
        if entity_key == "wit$reminder:reminder":
            response["What"] = matched_text
        elif entity_key == "wit$contact:contact":
            response["Who"] = matched_text
        elif entity_key == "wit$datetime:datetime":
            start_dt, end_dt = extract_interval(val)
            response["When"] = {
                "Text": matched_text, 
                "From": start_dt, 
                "To": end_dt
            }
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
