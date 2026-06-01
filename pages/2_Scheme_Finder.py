import streamlit as st
from recommender import recommend_schemes

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Scheme Finder",
    page_icon="🔍",
    layout="wide"
)

# -----------------------------------
# CSS
# -----------------------------------

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

/* Main Layout */

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
    font-size:52px;
    font-weight:800;
}

.banner-desc{
    font-size:20px;
    margin-top:10px;
    opacity:0.95;
}

/* Heading */

.section-title{
    font-size:38px;
    font-weight:800;
    color:#0F172A;
    margin-bottom:25px;
}


/* Inputs */

.stNumberInput input{
    border-radius:12px !important;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:12px !important;
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

/* Results */

.result-heading{
    font-size:34px;
    font-weight:800;
    color:#0F172A;
    margin-top:20px;
    margin-bottom:20px;
}

/* Scheme Card */

.scheme-card{
    background:white;
    border-radius:18px;
    padding:22px;
    margin-bottom:15px;
    border-left:6px solid #2563EB;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.scheme-title{
    font-size:22px;
    font-weight:700;
    color:#0F172A;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# BANNER
# -----------------------------------

st.markdown("""
<div class="banner">

<div class="banner-title">
🔍 Scheme Finder
</div>

<div class="banner-desc">
Discover government schemes based on your age,
occupation and income level.
</div>

</div>
""", unsafe_allow_html=True)

# -----------------------------------
# DETAILS TITLE
# -----------------------------------

st.markdown("""
<div class="section-title">
📋 Enter Your Details
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# FORM CARD
# -----------------------------------


col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25
    )

with col2:
    occupation = st.selectbox(
        "Occupation",
        [
            "Student",
            "Farmer",
            "Business Owner",
            "Employee",
            "Woman",
            "Senior Citizen"
        ]
    )

with col3:
    income = st.selectbox(
        "Income Level",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

st.markdown("<br>", unsafe_allow_html=True)

search = st.button(
    "🔎 Find Eligible Schemes",
    use_container_width=True
)


# -----------------------------------
# RESULTS
# -----------------------------------

if search:

    schemes = recommend_schemes(
        age,
        occupation,
        income
    )

    st.markdown("""
    <div class="result-heading">
    🎯 Recommended Schemes
    </div>
    """, unsafe_allow_html=True)

    if schemes:

        for scheme in schemes:

            st.markdown(f"""
            <div class="scheme-card">
                <div class="scheme-title">
                    🏛️ {scheme}
                </div>
            </div>
            """, unsafe_allow_html=True)

    else:

        st.warning(
            "No schemes found for the selected criteria."
        )