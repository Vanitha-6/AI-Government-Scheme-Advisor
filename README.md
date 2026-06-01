# 🤖 AI Government Scheme Advisor

An AI-powered web application that helps citizens discover, compare, and understand Government Schemes in India using Artificial Intelligence.

## 📌 Overview

AI Government Scheme Advisor simplifies access to government welfare schemes, subsidies, scholarships, startup funding programs, agricultural benefits, and employment schemes.

Users can:

* Ask questions in natural language
* Get AI-generated responses about schemes
* Compare multiple government schemes
* Explore a scheme directory with official websites
* View personalized user profiles
* Access scheme information instantly

---

## 🚀 Features

### 🤖 AI Scheme Assistant

Ask questions such as:

* What are the benefits of PM-KISAN?
* Which schemes are available for women entrepreneurs?
* Government schemes for startups in India
* Scholarship schemes for engineering students

The AI assistant provides quick and relevant answers.

---

### ⚖️ Scheme Comparison

Compare two schemes side-by-side.

Example:

| Feature | PM Kisan   | PMEGP         |
| ------- | ---------- | ------------- |
| Target  | Farmers    | Entrepreneurs |
| Benefit | ₹6000/year | Business Loan |
| Subsidy | No         | Yes           |

---

### 📚 Scheme Directory

Browse important government schemes:

* PM Kisan
* PMEGP
* Mudra Loan
* Skill India
* Startup India
* Stand-Up India
* Ayushman Bharat
* PM Awas Yojana
* National Scholarship Portal
* AICTE Scholarships
* Digital India
* Atal Pension Yojana

Each scheme includes:

* Description
* Official Website
* Eligibility Information

---

### 👤 User Profile

Personalized profile dashboard containing:

* Username
* Email
* Account Status
* Registered User Information
* Login & Logout Support

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### AI

* Hugging Face Inference API
* NLP Models

### Database

* JSON Storage

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```
AI-Government-Scheme-Advisor/

│
├── app.py
├── chatbot.py
├── compare.py
├── schemes.py
│
├── pages/
│   ├── AI_Assistant.py
│   ├── Compare_Schemes.py
│   ├── Scheme_Directory.py
│   └── User_Profile.py
│
├── data/
│   └── schemes.json
│
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Vanitha-6/AI-Government-Scheme-Advisor.git

cd AI-Government-Scheme-Advisor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will open at:

```text
http://localhost:8501
```

---

## 🌟 Future Enhancements

* Voice-based scheme search
* Regional language support
* Eligibility checker
* Recommendation engine
* PDF report generation
* Government API integration
* User authentication with database

---

## 🎯 Use Cases

* Farmers
* Students
* Entrepreneurs
* Job Seekers
* Women Welfare Beneficiaries
* Senior Citizens
* Researchers

---

## 👩‍💻 Developed By

**Vanitha V**

AI & Machine Learning Enthusiast

KPR Institute of Engineering and Technology

---

## 📜 License

This project is developed for educational and research purposes.
