
import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Scheme Directory",
    page_icon="📚",
    layout="wide"
)

# -----------------------------------
# CSS
# -----------------------------------

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {
    visibility: hidden;
}

/* Hide Footer */
footer {
    visibility: hidden;
}

/* Hide Header */
header {
    visibility: hidden;
}

/* Completely Hide Sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Remove space reserved for sidebar */
[data-testid="stSidebarCollapsedControl"] {
    display: none;
}

/* Expand main content to full width */
section.main > div {
    max-width: 100%;
}

/* Page Background */
.stApp{
    background:#F8FAFC;
}


.stApp{
    background:#F8FAFC;
}
[data-testid="stMarkdownContainer"] h3 {
    color: black !important;
    font-weight: 700 !important;
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

.scheme-card{
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    margin-bottom:20px;
    border-left:6px solid #2563EB;
}

.scheme-title{
    font-size:24px;
    font-weight:700;
    color:#0F172A;
}

.scheme-desc{
    font-size:16px;
    color:#475569;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# BANNER
# -----------------------------------

st.markdown("""
<div class="banner">

<div class="banner-title">
📚 Government Scheme Directory
</div>

<div class="banner-desc">
Explore official government schemes, scholarships, startup funding,
farmer welfare schemes and skill development programs.
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# SCHEMES
# -----------------------------------

schemes = [

{
    "name":"PM Kisan",
    "icon":"🌾",
    "desc":"Income support scheme providing ₹6000 per year to eligible farmer families.",
    "link":"https://pmkisan.gov.in"
},

{
    "name":"PMEGP",
    "icon":"🏭",
    "desc":"Employment generation scheme providing financial assistance for new enterprises.",
    "link":"https://www.kviconline.gov.in"
},

{
    "name":"Mudra Loan",
    "icon":"💰",
    "desc":"Business loans for micro and small enterprises up to ₹10 lakh.",
    "link":"https://www.mudra.org.in"
},

{
    "name":"Skill India",
    "icon":"🎓",
    "desc":"Skill development and vocational training programs for youth.",
    "link":"https://www.skillindia.gov.in"
},

{
    "name":"National Scholarship Portal",
    "icon":"📖",
    "desc":"Central portal for scholarships offered by Government of India.",
    "link":"https://scholarships.gov.in"
},

{
    "name":"AICTE Scholarship",
    "icon":"🏅",
    "desc":"Scholarships and financial support for technical education students.",
    "link":"https://www.aicte-india.org"
},

{
    "name":"Startup India",
    "icon":"🚀",
    "desc":"Support, funding and benefits for startups and entrepreneurs.",
    "link":"https://www.startupindia.gov.in"
},

{
    "name":"Stand-Up India",
    "icon":"📈",
    "desc":"Bank loans for women entrepreneurs and SC/ST entrepreneurs.",
    "link":"https://www.standupmitra.in"
},

{
    "name":"Ayushman Bharat",
    "icon":"🏥",
    "desc":"Health insurance coverage for economically vulnerable families.",
    "link":"https://pmjay.gov.in"
},

{
    "name":"PM Awas Yojana",
    "icon":"🏠",
    "desc":"Affordable housing scheme for urban and rural citizens.",
    "link":"https://pmaymis.gov.in"
},

{
    "name":"Digital India",
    "icon":"💻",
    "desc":"Digital empowerment and online government services initiative.",
    "link":"https://digitalindia.gov.in"
},

{
    "name":"Atal Pension Yojana",
    "icon":"👴",
    "desc":"Pension scheme for workers in the unorganized sector.",
    "link":"https://www.npscra.nsdl.co.in"
}

]

# -----------------------------------
# DISPLAY CARDS
# -----------------------------------

for scheme in schemes:

    with st.container(border=True):

        st.subheader(
            f"{scheme['icon']} {scheme['name']}"
        )

        st.write(
            scheme["desc"]
        )

        st.link_button(
            "🌐 Visit Official Website",
            scheme["link"],
            use_container_width=True
        )