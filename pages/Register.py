import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Register - SchemeSathi AI",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

/* Hide Streamlit Elements */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stSidebar"]{
    display:none;
}

/* Background */
.stApp{
    background:#F8FAFC;
}

/* Logo */
.logo{
    text-align:center;
    font-size:55px;
    margin-top:10px;
}

/* Title */
.title{
    text-align:center;
    font-size:48px;
    font-weight:700;
    color:#0F172A;
    margin-top:5px;
}

/* Subtitle */
.subtitle{
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:25px;
}

/* Input Fields */
.stTextInput input{
    height:52px !important;
    border-radius:10px !important;
    font-size:16px !important;
}

/* Register Button */
.stButton button{
    width:150px;
    height:52px;
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    font-size:18px;
    font-weight:600;
}

.stButton button:hover{
    background:#1D4ED8;
    color:white;
}

/* Login Text */
.login-text{
    margin-top:15px;
    text-align:center;
    color:#64748B;
    font-size:18px;
}

/* Login Link */
.login-link{
    text-align:center;
    margin-top:5px;
}

.login-link a{
    text-decoration:none;
    color:#2563EB;
    font-size:28px;
    font-weight:600;
}

.login-link a:hover{
    text-decoration:underline;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="logo">🏛️</div>

<div class="title">
Create Account
</div>

<div class="subtitle">
Register to access SchemeSathi AI
</div>
""", unsafe_allow_html=True)

# ---------------- REGISTER FORM ---------------- #

left, center, right = st.columns([1.5, 1.2, 1.5])

with center:

    username = st.text_input(
        "",
        placeholder="Enter your username"
    )

    email = st.text_input(
        "",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "",
        placeholder="Create your password",
        type="password"
    )

    # Center Register Button
    c1, c2, c3 = st.columns([1,1,1])

    with c2:

        if st.button("Register"):

            try:

                conn = sqlite3.connect(
                    "database/users.db"
                )

                cursor = conn.cursor()

                cursor.execute("""
                CREATE TABLE IF NOT EXISTS users(

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    username TEXT,

                    email TEXT UNIQUE,

                    password TEXT

                )
                """)

                cursor.execute(
                    """
                    INSERT INTO users
                    (username,email,password)

                    VALUES(?,?,?)
                    """,
                    (
                        username,
                        email,
                        password
                    )
                )

                conn.commit()
                conn.close()

                st.success(
                    "✅ Account Created Successfully"
                )

            except sqlite3.IntegrityError:

                st.error(
                    "❌ Email already registered"
                )

    st.markdown(
        """
        <div class="login-text">
        Already have an account?
        </div>

        <div class="login-link">
        <a href="Login">
        Login
        </a>
        </div>
        """,
        unsafe_allow_html=True
    )

   