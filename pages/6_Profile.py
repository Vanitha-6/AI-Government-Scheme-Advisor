
import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
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

.banner{
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:35px;
    border-radius:20px;
    color:white;
    margin-bottom:30px;
}

.banner-title{
    font-size:42px;
    font-weight:800;
}

.banner-desc{
    font-size:18px;
    margin-top:10px;
}

.profile-card{
    background:white;
    border-radius:20px;
    padding:35px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    text-align:center;
}

.avatar{
    font-size:90px;
}

.username{
    font-size:32px;
    font-weight:800;
    color:#111827;
}

.role{
    color:#64748B;
    font-size:18px;
}

.stat-card{
    background:white;
    border-radius:18px;
    padding:25px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.stat-number{
    font-size:34px;
    font-weight:800;
    color:#2563EB;
}

.stat-title{
    color:#475569;
    font-size:16px;
}

.info-card{
    background:white;
    border-radius:18px;
    padding:25px;
    margin-top:25px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.info-title{
    font-size:28px;
    font-weight:700;
    color:#111827;
    margin-bottom:20px;
}

.info-row{
    font-size:18px;
    color:#374151;
    margin-bottom:12px;
}

.stButton button{
    width:100%;
    height:55px;
    background:#DC2626;
    color:white;
    border:none;
    border-radius:12px;
    font-size:18px;
    font-weight:700;
}

.stButton button:hover{
    background:#B91C1C;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# USER DATA
# -----------------------------------

username = st.session_state.get(
    "username",
    "Guest User"
)

# -----------------------------------
# BANNER
# -----------------------------------

st.markdown("""
<div class="banner">

<div class="banner-title">
👤 My Profile
</div>

<div class="banner-desc">
Manage your SchemeSathi AI account and track your scheme exploration journey.
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# PROFILE CARD
# -----------------------------------

st.markdown(f"""
<div class="profile-card">

<div class="avatar">
🧑
</div>

<div class="username">
{username}
</div>

<div class="role">
Citizen Account
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# STATS
# -----------------------------------

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">12</div>
        <div class="stat-title">Schemes Viewed</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">5</div>
        <div class="stat-title">Recommendations</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-title">Comparisons</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">100%</div>
        <div class="stat-title">Profile Status</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------
# ACCOUNT DETAILS
# -----------------------------------

st.markdown("""
<div class="info-card">

<div class="info-title">
📋 Account Information
</div>

<div class="info-row">
<b>Account Type:</b> Citizen
</div>

<div class="info-row">
<b>Status:</b> Active
</div>

<div class="info-row">
<b>Member Since:</b> 2026
</div>

<div class="info-row">
<b>Platform:</b> SchemeSathi AI
</div>

<div class="info-row">
<b>Access Level:</b> Standard User
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# LOGOUT
# -----------------------------------

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚪 Logout"):

    st.session_state.clear()

    st.success(
        "Successfully Logged Out"
    )

    st.switch_page("app.py")
