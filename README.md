# 📄 Resume Analyzer

A Python-based Resume Analyzer built with **Streamlit** that analyzes a PDF resume, evaluates its ATS readiness, identifies skills and resume sections, and compares the resume with a given job description.

## 🚀 Features

- 📄 Upload and analyze PDF resumes
- 🎯 Calculate an ATS-style resume score
- 🧑 Extract candidate information
  - Name
  - Email
  - Phone number
- 🛠️ Detect technical skills
- 📚 Detect important resume sections
  - Education
  - Experience
  - Projects
  - Skills
  - Certifications
  - Achievements
  - Summary
- 🔗 Detect online profiles
  - LinkedIn
  - GitHub
  - Portfolio
- 📊 Analyze resume quality
  - Word count
  - Bullet points
  - Action verbs
  - Measurable achievements
- 💼 Compare resume with a job description
- ✅ Identify matching skills
- ❌ Identify missing skills
- 💡 Generate personalized resume improvement recommendations
- 📥 Download an analysis report

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **PyMuPDF**
- **Regular Expressions (Regex)**

## 📂 Project Structure

```text
Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/resume-analyzer.git
```

### 2. Navigate to the project folder

```bash
cd resume-analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 🔍 How It Works

The application follows these main steps:

```text
Upload Resume PDF
        ↓
Extract Resume Text
        ↓
Identify Candidate Information
        ↓
Detect Skills & Resume Sections
        ↓
Analyze Resume Quality
        ↓
Calculate ATS Score
        ↓
Compare With Job Description
        ↓
Generate Recommendations
        ↓
Download Analysis Report
```

## 📊 ATS Analysis

The analyzer evaluates multiple aspects of a resume, including:

- Contact information
- Technical skills
- Education
- Projects
- Experience
- Certifications
- Achievements
- LinkedIn and GitHub profiles
- Resume length
- Resume structure

The score is intended as a **guideline**, not as an exact representation of how a company's ATS will evaluate a resume.

## 💼 Job Description Matching

Users can paste a job description to compare it against their resume.

The analyzer identifies:

- Matching skills
- Missing skills
- Skill match percentage
- Keyword overlap
- Overall job match score

This can help candidates identify areas that may need improvement before applying.

## 💡 Example Use Case

A student applying for a **Java Developer** position can upload their resume and paste the job description.

The application can identify whether the resume contains relevant skills such as:

```text
Java
SQL
Git
Spring Boot
REST API
```

It can then highlight missing skills and provide recommendations for improving the resume.

## 🔮 Future Enhancements

Possible future improvements include:

- Machine-learning-based resume classification
- Support for DOCX resumes
- More advanced NLP-based job matching
- Resume keyword recommendations
- Resume section quality scoring
- Cloud deployment
- User authentication
- Database integration

## 👨‍💻 Author

**Rushindar**

Built as a portfolio project to practice Python, Streamlit, PDF processing, text analysis, and practical application development.

## ⭐ Project Goal

The goal of this project is to build a practical tool that helps job seekers understand how well their resume matches a job description and identify areas for improvement.