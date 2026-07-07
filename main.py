import streamlit as st
from langchain_core.messages import HumanMessage

# Import your compiled graph
from Conditonal import app

st.set_page_config(
    page_title="🎯 Technical Interview Prep",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.title{
    text-align:center;
    color:#4CAF50;
    font-size:40px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:white;
    font-size:18px;
}

.stChatMessage{
    border-radius:12px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🤖 AI Technical Interview Assistant</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Ask Interview Questions from OOPs, OS, CN and DBMS</div>", unsafe_allow_html=True)

subject = st.sidebar.selectbox(
    "Choose Subject",
    ["OOPs","OS","CN","DBMS"]
)

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask your technical interview question...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = app.invoke(
                {
                    "programme":subject,
                    "messages":[
                        HumanMessage(content=prompt)
                    ]
                }
            )

            answer = result["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )