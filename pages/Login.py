import streamlit as st
import sys
import os

# Project Path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from auth import login_user

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------------
# CSS
# -----------------------------------

st.markdown("""
<style>

/* Hide Streamlit Elements */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

[data-testid="stSidebar"]{
display:none;
}

/* Background */

.stApp{
background:#F8FAFC;
}

/* Main Container */

.block-container{
max-width:520px;
padding-top:80px;
}

/* Logo */

.logo{
font-size:60px;
text-align:center;
margin-bottom:10px;
}

/* Heading */

.title{
text-align:center;
font-size:38px;
font-weight:700;
color:#111827;
margin-bottom:10px;
}

/* Subtitle */

.subtitle{
text-align:center;
font-size:16px;
color:#6B7280;
margin-bottom:35px;
}

/* Input Fields */

.stTextInput input{
height:55px !important;
border-radius:12px !important;
font-size:16px;
}

/* Login Button */

.stButton button{
    width:135px;
    height:50px;
    background:#2563EB;
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:600;
    margin-left:150px;
    display:block;
}

.stButton button:hover{
background:#1D4ED8;
color:white;
}

/* Register Text */

.register{
text-align:center;
margin-top:25px;
font-size:16px;
color:#6B7280;
}

.register a{
color:#2563EB;
font-weight:600;
text-decoration:none;
}

.register a:hover{
text-decoration:underline;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# LOGO
# -----------------------------------

st.markdown("""
<div class="logo">
🏛️
</div>

<div class="title">
Welcome Back
</div>

<div class="subtitle">
Sign in to continue to SchemeSathi AI
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# LOGIN FORM
# -----------------------------------

email = st.text_input(
    "Email",
    placeholder="Enter your email"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)

# -----------------------------------
# LOGIN BUTTON
# -----------------------------------

if st.button("Login"):

    user = login_user(
        email,
        password
    )

    if user:

        st.success(
            "✅ Login Successful"
            
        )

        st.switch_page(
            "pages/1_Dashboard.py"
        )

    else:

        st.error(
            "❌ Invalid Email or Password"
        )

# -----------------------------------
# REGISTER LINK
# -----------------------------------

st.markdown("""
<div class="register">

Don't have an account?

<a href="/Register" target="_self">
Register
</a>

</div>
""", unsafe_allow_html=True)

