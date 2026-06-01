import streamlit as st
import sys
import os

# -----------------------------------
# PROJECT PATH FIX
# -----------------------------------

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from chatbot import ask_question

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Scheme Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# CSS
# -----------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stSidebar"]{
    display:none;
}

.stApp{
    background:#F8FAFC;
}

.block-container{
    max-width:1200px;
    padding-top:2rem;
}

.banner{
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:40px;
    border-radius:22px;
    color:white;
    margin-bottom:35px;
    box-shadow:0px 10px 30px rgba(37,99,235,0.25);
}

.banner-title{
    font-size:52px;
    font-weight:800;
}

.banner-desc{
    font-size:20px;
    margin-top:10px;
}

.section-title{
    font-size:36px;
    font-weight:800;
    color:#0F172A;
    margin-bottom:20px;
}

.stTextArea textarea{
    border-radius:15px !important;
    font-size:17px !important;
}

.stButton button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:#2563EB;
    color:white;
    font-size:18px;
    font-weight:700;
}

.stButton button:hover{
    background:#1D4ED8;
    color:white;
}

.answer-card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    margin-top:25px;
    border-left:6px solid #2563EB;
}

.answer-title{
    font-size:28px;
    font-weight:800;
    color:#0F172A;
    margin-bottom:15px;
}

.answer-text{
    font-size:18px;
    line-height:1.8;
    font-weight:500;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# BANNER
# -----------------------------------

st.markdown("""
<div class="banner">

<div class="banner-title">
🤖 AI Scheme Assistant
</div>

<div class="banner-desc">
Ask questions about government schemes, eligibility,
scholarships, subsidies, startup funding and welfare programs.
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# QUESTION SECTION
# -----------------------------------

st.markdown("""
<div class="section-title">
💬 Ask Your Question
</div>
""", unsafe_allow_html=True)

question = st.text_area(
    "",
    placeholder="Example: What government schemes are available for women entrepreneurs?",
    height=150
)

ask = st.button(
    "🚀 Ask AI Assistant",
    use_container_width=True
)

# -----------------------------------
# RESPONSE
# -----------------------------------

if ask:

    st.write("Button clicked")

    if question.strip():

        st.write("Question received")

        try:

            with st.spinner("Analyzing your query..."):

                answer = ask_question(question)

            
            st.markdown(f"""
<div class="answer-card">

<div class="answer-title">
🤖 AI Response
</div>

<div style="color:black;font-size:18px;line-height:1.8;">
{answer}
</div>

</div>
""", unsafe_allow_html=True)

        except Exception as e:

            st.error(f"Error: {e}")

    else:

        st.warning("Please enter a question.")