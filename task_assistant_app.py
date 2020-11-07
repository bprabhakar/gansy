import streamlit as st
import time
import openai; openai.api_key = "sk-w0wjYznY3lj2tn8m5SI18BBXFq6AtqHUEhDKIdFw"

"""
# aarzoo
Enter a text query below and we'll parse out the task for you:
"""

title = st.text_input('Your wish is my command')

gpt3_prompt = """Input: By tomorrow Shonty need to close this project..
Who: Shonty
When: Tomorrow
What: Close the project.
---
Input: Let's send an email to update our customers about our new pricing scheme.
Who: Us
When: ?
What: Send an email to update our customers about our new pricing scheme
---
Input: We should put up a post on instagram today.
Who: We
When: Today
What: Put up the Instagram post
---
Input: Vivek, can you please review my PR by tomorrow?
Who: Vivek
When: Tomorrow
What: Review PR
---
Input: This bug needs to get fixed ASAP.
Who: ?
When: As soon as possible
What: Fix bug
---
Input: """

@st.cache
def gpt3_parser(text, prompt=gpt3_prompt):
    gpt3_response = openai.Completion.create(
        prompt=(prompt + text + "\n"), 
        max_tokens=200, 
        temperature=0.2,
        stop="---",
        engine="davinci",
        top_p=1,
        n=1,
        stream=False,
        echo=False,
        logprobs=None
    )
    raw_pred = gpt3_response.get('choices')[0].get('text')
    response = {
        "Who": "?",
        "When": "?",
        "What": "?"
    }
    for line in raw_pred.splitlines():
        if "Who:" in line:
            response["Who"] = line.split("Who:")[-1].strip()
        elif "When:" in line:
            response["When"] = line.split("When:")[-1].strip()
        elif "What:" in line:
            response["What"] = line.split("What:")[-1].strip()
    return response

if title:
    try:
        answer = gpt3_parser(title, gpt3_prompt)
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
