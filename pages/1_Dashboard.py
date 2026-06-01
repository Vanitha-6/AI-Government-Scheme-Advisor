import streamlit as st

st.set_page_config(
    page_title="Dashboard - SchemeSathi AI",
    page_icon="🏛️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Hide Streamlit branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0F172A;
}

section[data-testid="stSidebar"] .stButton button{
    width:100%;
    background:#1E293B;
    color:white;
    border:none;
    border-radius:10px;
    font-size:16px;
    font-weight:600;
    padding:12px;
    margin-bottom:8px;
}

section[data-testid="stSidebar"] .stButton button:hover{
    background:#2563EB;
    color:white;
}

/* Main */
.stApp{
    background:#F8FAFC;
}

/* Banner */
.banner{
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:40px;
    border-radius:20px;
    color:white;
    margin-bottom:35px;
}

.banner-title{
    font-size:46px;
    font-weight:800;
}

.banner-desc{
    font-size:20px;
    margin-top:10px;
}

/* Section Heading */
.heading{
    font-size:38px;
    font-weight:800;
    color:#0F172A;
    margin-bottom:25px;
}

/* Cards */
.card{
    background:white;
    border-radius:20px;
    padding:25px;
    text-align:center;
    box-shadow:0px 6px 20px rgba(0,0,0,0.08);
    min-height:420px;
}

.card img{
    width:120px;
    height:120px;
    object-fit:contain;
    margin-bottom:15px;
}

.card-title{
    font-size:30px;
    font-weight:700;
    color:#0F172A;
    margin-bottom:15px;
}

.card-desc{
    color:#64748B;
    font-size:18px;
    line-height:1.7;
}

/* Overview Box */
.overview{
    background:white;
    padding:35px;
    border-radius:20px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    margin-top:30px;
}

.overview-title{
    font-size:40px;
    font-weight:800;
    color:#000000 !important;
    opacity:1 !important;
}

.overview-text{
    font-size:18px;
    color:#475569;
    line-height:1.9;
}

.overview-text p{
    margin-bottom:18px;
}

.overview-text ul{
    padding-left:25px;
}

.overview-text li{
    margin-bottom:10px;
    font-size:18px;
}     

/* Hide Streamlit default multipage navigation */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Hide Pages section */
section[data-testid="stSidebar"] div[data-testid="stSidebarNav"] {
    display: none;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:

    st.markdown("""
    <h2 style='color:white;text-align:center;'>
    🏛️ SchemeSathi AI
    </h2>
    <hr>
    """, unsafe_allow_html=True)


    if st.button("🎯 Scheme Finder"):
        st.switch_page("pages/2_Scheme_Finder.py")

    if st.button("🤖 AI Assistant"):
        st.switch_page("pages/3_AI_Assistant.py")

    if st.button("⚖️ Compare Schemes"):
        st.switch_page("pages/4_Compare_Schemes.py")

    if st.button("📚 Scheme Directory"):
        st.switch_page("pages/5_Scheme_Directory.py")

    if st.button("👤 Profile"):
        st.switch_page("pages/6_Profile.py")

# --------------------------------------------------
# MAIN PAGE
# --------------------------------------------------

username = st.session_state.get("username", "Citizen")

st.markdown(f"""
<div class="banner">
    <div class="banner-title">
        👋 Welcome, {username}
    </div>
    <div class="banner-desc">
        Discover scholarships, farmer benefits, startup loans,
        employment opportunities and welfare schemes powered by AI.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="heading">
🚀 Quick Access
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

# CARD 1
with c1:
    st.markdown("""
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png">
        <div class="card-title">Scheme Finder</div>
        <div class="card-desc">
        Find government schemes based on age,
        occupation, income and eligibility.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Finder"):
        st.switch_page("pages/2_Scheme_Finder.py")

# CARD 2
with c2:
    st.markdown("""
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png">
        <div class="card-title">AI Assistant</div>
        <div class="card-desc">
        Ask questions and receive instant
        AI-powered guidance for schemes.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Assistant"):
        st.switch_page("pages/3_AI_Assistant.py")

# CARD 3
with c3:
    st.markdown("""
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2910/2910791.png">
        <div class="card-title">Compare Schemes</div>
        <div class="card-desc">
        Compare benefits, eligibility,
        subsidies and financial support.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Compare"):
        st.switch_page("pages/4_Compare_Schemes.py")

# CARD 4
with c4:
    st.markdown("""
    <div class="card">
        <img src="https://cdn-icons-png.flaticon.com/512/2232/2232688.png">
        <div class="card-title">Scheme Directory</div>
        <div class="card-desc">
        Browse all government schemes
        available across India.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Browse"):
        st.switch_page("pages/5_Scheme_Directory.py")

# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------
st.markdown("""
<div class="overview">
<h1 class="overview-title">📌 About SchemeSathi AI</h1>

<div class="overview-text">

SchemeSathi AI is an intelligent government scheme recommendation platform
that helps citizens identify welfare schemes, scholarships, startup funding
opportunities, farmer benefits, pensions and employment programs.

<br><br>

The platform uses Artificial Intelligence to match user profiles with suitable
government schemes and provides eligibility guidance, benefits comparison and
instant assistance through an AI chatbot.

<br><br>

✅ Personalized Recommendations<br>
✅ AI-Powered Guidance<br>
✅ Scheme Comparison<br>
✅ Centralized Scheme Directory<br>
✅ Easy Access to Government Benefits

</div>
</div>
""", unsafe_allow_html=True)