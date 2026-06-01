
import streamlit as st

st.set_page_config(
    page_title="SchemeSathi AI",
    page_icon="🏛️",
    layout="wide"
)

# ------------------------------------------------
# HIDE STREAMLIT SIDEBAR & UI
# ------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

[data-testid="stSidebar"]{
    display:none;
}

[data-testid="collapsedControl"]{
    display:none;
}

.stApp{
    background:white;
}

.block-container{
    padding-top:0rem;
    padding-left:4rem;
    padding-right:4rem;
    max-width:100%;
}

/* NAVBAR */

.logo{
    font-size:40px;
    font-weight:800;
    color:#000000;
}

.tagline{
    color:#374151;
    font-size:16px;
    margin-top:-10px;
}

.hero-title{
    font-size:68px;
    font-weight:800;
    color:#000000;
    line-height:1.2;
    text-align:center;
}

.hero-blue{
    color:#2563EB;
}

.hero-desc{
    text-align:center;
    font-size:24px;
    color:#374151;
    max-width:900px;
    margin:auto;
    line-height:1.8;
    margin-top:20px;
}

.nav-btn{
    background:#2563EB;      /* Blue box */
    color:#000000 !important; /* Black text */
    padding:12px 28px;
    border-radius:10px;
    text-decoration:none;
    font-size:18px;
    font-weight:700;
    border:none;
    transition:0.3s;
}

.nav-btn:hover{
    background:#1D4ED8;      /* Darker blue on hover */
    color:#000000 !important;
}



/* FEATURE CARD */

.feature-card{
    background:#F8FAFC;
    padding:30px;
    border-radius:18px;
    text-align:center;
    border:1px solid #E2E8F0;
    height:220px;
}

.feature-icon{
    font-size:50px;
}

.feature-title{
    font-size:24px;
    font-weight:700;
    color:#0F172A;
}

.feature-desc{
    color:#64748B;
    font-size:16px;
    line-height:1.7;
}

/* SECTION */

.section-title{
    text-align:center;
    font-size:46px;
    font-weight:800;
    color:#0F172A;
    margin-top:50px;
}

/* STATS */

.stat-number{
    text-align:center;
    font-size:48px;
    font-weight:800;
    color:#2563EB;
}

.stat-label{
    text-align:center;
    color:#475569;
    font-size:18px;
}

/* CATEGORY */

.category{
    background:#EFF6FF;
    border:1px solid #BFDBFE;
    padding:18px;
    border-radius:12px;
    text-align:center;
    font-size:18px;
    font-weight:600;
    color:#1E293B;
}

/* CTA */

.cta{
    background:#2563EB;
    color:white;
    padding:60px;
    border-radius:20px;
    text-align:center;
}

.footer{
    text-align:center;
    color:#64748B;
    padding:30px;
    margin-top:50px;
}


div.stButton > button {
    background-color:#2563EB;
    color:black;
    border:none;
    border-radius:10px;
    padding:12px 18px;
    font-weight:700;
    font-size:16px;
    transition:0.3s;
}

div.stButton > button:hover{
    background-color:#1D4ED8;
    color:black;
}
     


</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# NAVIGATION
# ------------------------------------------------

col1,col2 = st.columns([5,2])

with col1:
    st.markdown("""
    <div class='logo'>🏛️ SchemeSathi AI</div>
    <div class='tagline'>
    AI Powered Government Scheme Discovery Platform
    </div>
    """, unsafe_allow_html=True)

with col2:

    n1,n2,n3 = st.columns(3)

    with n1:
        if st.button("Login"):
            st.switch_page("pages/Login.py")

    with n2:
        if st.button("Register"):
            st.switch_page("pages/Register.py")

    with n3:
        if st.button("Profile"):
            st.switch_page("pages/6_Profile.py")

st.divider()

# ------------------------------------------------
# HERO
# ------------------------------------------------

st.markdown("""
<br><br>

<div class='hero-title'>

Find Government Schemes

<br>

<span class='hero-blue'>
Powered By Artificial Intelligence
</span>

</div>

<div class='hero-desc'>

Discover scholarships, farmer benefits,
business loans, startup support,
employment opportunities, pension schemes,
healthcare assistance and welfare programs
tailored specifically to your profile.

</div>

<br><br>

""", unsafe_allow_html=True)

center1,center2,center3 = st.columns([2,1,2])

with center2:
    if st.button("🚀 Start Exploring"):
        st.switch_page("pages/2_Scheme_Finder.py")

# ------------------------------------------------
# FEATURES
# ------------------------------------------------

st.markdown("""
<div class='section-title'>
Everything You Need In One Place
</div>
<br>
""", unsafe_allow_html=True)

f1,f2,f3,f4 = st.columns(4)

with f1:
    st.markdown("""
    <div class='feature-card'>
    <div class='feature-icon'>🎯</div>
    <div class='feature-title'>Scheme Finder</div>
    <div class='feature-desc'>
    Get personalized recommendations based on your profile.
    </div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class='feature-card'>
    <div class='feature-icon'>🤖</div>
    <div class='feature-title'>AI Assistant</div>
    <div class='feature-desc'>
    Ask questions naturally and receive instant answers.
    </div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class='feature-card'>
    <div class='feature-icon'>⚖️</div>
    <div class='feature-title'>Compare Schemes</div>
    <div class='feature-desc'>
    Compare benefits, eligibility and advantages.
    </div>
    </div>
    """, unsafe_allow_html=True)

with f4:
    st.markdown("""
    <div class='feature-card'>
    <div class='feature-icon'>📚</div>
    <div class='feature-title'>Directory</div>
    <div class='feature-desc'>
    Browse schemes from various government sectors.
    </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------------------------
# STATS
# ------------------------------------------------

st.markdown("""
<div class='section-title'>
Platform Impact
</div>
<br>
""", unsafe_allow_html=True)

s1,s2,s3,s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class='stat-number'>1000+</div>
    <div class='stat-label'>Government Schemes</div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class='stat-number'>50K+</div>
    <div class='stat-label'>Citizens Assisted</div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class='stat-number'>95%</div>
    <div class='stat-label'>Recommendation Accuracy</div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class='stat-number'>24/7</div>
    <div class='stat-label'>AI Support</div>
    """, unsafe_allow_html=True)

# ------------------------------------------------
# CATEGORIES
# ------------------------------------------------

st.markdown("""
<div class='section-title'>
Schemes Covered
</div>
<br>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("<div class='category'>🎓 Students</div><br>", unsafe_allow_html=True)
    st.markdown("<div class='category'>👩 Women</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='category'>🌾 Farmers</div><br>", unsafe_allow_html=True)
    st.markdown("<div class='category'>👴 Senior Citizens</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='category'>🚀 Entrepreneurs</div><br>", unsafe_allow_html=True)
    st.markdown("<div class='category'>💼 Employees</div>", unsafe_allow_html=True)

# ------------------------------------------------
# CTA
# ------------------------------------------------

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class='cta'>

<h1>
Unlock Government Benefits Today
</h1>

<p>
Use Artificial Intelligence to discover
government opportunities within seconds.
</p>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("""
<div class='footer'>

© 2026 SchemeSathi AI

<br>

Empowering Citizens Through AI

</div>
""", unsafe_allow_html=True)
