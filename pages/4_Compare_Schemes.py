
import streamlit as st
from compare import compare_schemes

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Compare Government Schemes",
    page_icon="⚖️",
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

/* Banner */

.banner{
    background:linear-gradient(135deg,#2563EB,#1D4ED8);
    padding:40px;
    border-radius:22px;
    color:white;
    margin-bottom:35px;
    box-shadow:0px 10px 30px rgba(37,99,235,0.25);
}

.banner-title{
    font-size:50px;
    font-weight:800;
}

.banner-desc{
    font-size:20px;
    margin-top:10px;
}

/* Section */

.section-title{
    font-size:36px;
    font-weight:800;
    color:#0F172A;
    margin-bottom:20px;
}

/* Button */

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

/* Result Card */

.result-card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 5px 20px rgba(0,0,0,0.08);
    margin-top:25px;
    border-left:6px solid #2563EB;
}

.result-title{
    font-size:28px;
    font-weight:800;
    color:#0F172A;
    margin-bottom:15px;
}

.scheme-name{
    color:black !important;
    font-size:28px !important;
    font-weight:700 !important;
}

.scheme-item{
    color:black !important;
    font-size:20px !important;
    font-weight:500 !important;
}
.stMarkdown,
.stMarkdown p,
.stMarkdown div,
.stMarkdown span,
.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4,
.stMarkdown h5,
.stMarkdown h6 {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# BANNER
# -----------------------------------

st.markdown("""
<div class="banner">

<div class="banner-title">
⚖️ Compare Government Schemes
</div>

<div class="banner-desc">
Compare benefits, eligibility, subsidies and key features of government schemes.
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# TITLE
# -----------------------------------

st.markdown("""
<div class="section-title">
📋 Select Schemes to Compare
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# SELECT BOXES
# -----------------------------------

col1, col2 = st.columns(2)

with col1:
    scheme1 = st.selectbox(
        "Scheme 1",
        [
            "PM Kisan",
            "PMEGP",
            "Mudra Loan",
            "Skill India"
        ]
    )

with col2:
    scheme2 = st.selectbox(
        "Scheme 2",
        [
            "PM Kisan",
            "PMEGP",
            "Mudra Loan",
            "Skill India"
        ],
        index=1
    )

# -----------------------------------
# BUTTON
# -----------------------------------

compare_btn = st.button(
    "🚀 Compare Schemes",
    use_container_width=True
)

# -----------------------------------
# RESULT
# -----------------------------------

if compare_btn:

    try:

        with st.spinner("Comparing schemes..."):

            result = compare_schemes(
                scheme1,
                scheme2
            )

        st.markdown("## 📊 Comparison Result")

        for scheme, details in result.items():

            st.markdown(f"### 🔹 {scheme}")

            for key, value in details.items():

                st.markdown(
                    f"**{key}:** {value}"
                )

            st.divider()

    except Exception as e:

        st.error(f"Error: {e}")