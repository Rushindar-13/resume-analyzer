
import streamlit as st
import fitz
import re
from io import BytesIO


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ============================================================
# SKILL DATABASE
# ============================================================

SKILLS = {
    "Python": ["python"],
    "Java": ["java"],
    "C": ["c"],
    "C++": ["c++", "cpp"],
    "C#": ["c#", "c sharp"],
    "SQL": ["sql"],
    "HTML": ["html"],
    "CSS": ["css"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript", "ts"],
    "React": ["react", "reactjs", "react.js"],
    "Angular": ["angular"],
    "Vue": ["vue", "vue.js"],
    "Node.js": ["node.js", "nodejs"],
    "Express": ["express", "express.js"],
    "Django": ["django"],
    "Flask": ["flask"],
    "FastAPI": ["fastapi"],
    "Spring Boot": ["spring boot"],
    "Machine Learning": [
        "machine learning",
        "machine-learning",
        "ml"
    ],
    "Deep Learning": [
        "deep learning",
        "deep-learning"
    ],
    "Artificial Intelligence": [
        "artificial intelligence",
        "artificial-intelligence",
        "ai"
    ],
    "Data Science": ["data science"],
    "Data Analysis": ["data analysis"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Matplotlib": ["matplotlib"],
    "Scikit-learn": [
        "scikit-learn",
        "scikit learn",
        "sklearn"
    ],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Git": ["git"],
    "GitHub": ["github"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb", "mongo db"],
    "SQLite": ["sqlite"],
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "Google Cloud": [
        "google cloud",
        "gcp"
    ],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes", "k8s"],
    "Linux": ["linux"],
    "REST API": [
        "rest api",
        "restful api",
        "rest"
    ],
    "Power BI": ["power bi"],
    "Tableau": ["tableau"],
    "Excel": [
        "excel",
        "microsoft excel"
    ],
    "Firebase": ["firebase"],
    "PHP": ["php"],
    "Android": ["android"],
    "Kotlin": ["kotlin"],
    "Swift": ["swift"],
    "R": ["r programming"],
    "MATLAB": ["matlab"],
    "Selenium": ["selenium"],
    "Jenkins": ["jenkins"],
    "GitLab": ["gitlab"],
    "Jira": ["jira"],
    "Figma": ["figma"]
}


# ============================================================
# SECTION KEYWORDS
# ============================================================

SECTION_KEYWORDS = {
    "Education": [
        "education",
        "academic",
        "qualification",
        "academic background"
    ],

    "Experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "internship",
        "internships"
    ],

    "Projects": [
        "projects",
        "project"
    ],

    "Skills": [
        "skills",
        "technical skills",
        "technical knowledge",
        "technologies"
    ],

    "Certifications": [
        "certifications",
        "certification",
        "certificates",
        "certificate"
    ],

    "Achievements": [
        "achievements",
        "achievement",
        "awards",
        "honors"
    ],

    "Summary": [
        "summary",
        "professional summary",
        "profile",
        "objective",
        "career objective"
    ]
}


# ============================================================
# ACTION VERBS
# ============================================================

ACTION_VERBS = [
    "developed",
    "designed",
    "implemented",
    "created",
    "built",
    "engineered",
    "optimized",
    "improved",
    "automated",
    "analyzed",
    "managed",
    "led",
    "deployed",
    "tested",
    "integrated",
    "configured",
    "maintained",
    "delivered",
    "develop",
    "design",
    "implement",
    "create",
    "build",
    "engineer",
    "optimize",
    "improve",
    "automate",
    "analyze",
    "manage",
    "lead",
    "deploy",
    "test",
    "integrate",
    "configure",
    "maintain",
    "deliver"
]


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def normalize_text(text):
    """Convert text into a simpler form for matching."""

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def contains_keyword(text, keyword):
    """Safely check whether a keyword exists in text."""

    text_lower = normalize_text(text)
    keyword_lower = normalize_text(keyword)

    if keyword_lower in ["c", "r"]:

        return bool(
            re.search(
                r"(?<![a-z])"
                + re.escape(keyword_lower)
                + r"(?![a-z])",
                text_lower
            )
        )

    return keyword_lower in text_lower


# ============================================================
# PDF EXTRACTION
# ============================================================

def extract_pdf_text(uploaded_file):

    file_bytes = uploaded_file.getvalue()

    pdf = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    pages = []

    for page in pdf:

        pages.append(
            page.get_text()
        )

    pdf.close()

    return "\n".join(pages)


# ============================================================
# EMAIL EXTRACTION
# ============================================================

def extract_email(text):

    pattern = (
        r"[a-zA-Z0-9._%+-]+"
        r"@[a-zA-Z0-9.-]+"
        r"\.[a-zA-Z]{2,}"
    )

    matches = re.findall(
        pattern,
        text
    )

    if matches:
        return matches[0]

    return "Not Found"


# ============================================================
# PHONE EXTRACTION
# ============================================================

def extract_phone(text):

    patterns = [

        r"(?:\+91[\s-]?)?[6-9]\d{9}",

        r"[6-9]\d{4}[\s-]\d{5}",

        r"(?:\+91[\s-]?)?[6-9]\d{2}[\s-]?\d{3}[\s-]?\d{4}"
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text
        )

        if matches:

            return matches[0]

    return "Not Found"


# ============================================================
# NAME EXTRACTION
# ============================================================

def extract_name(text):

    lines = text.splitlines()

    ignored_words = [
        "resume",
        "curriculum vitae",
        "email",
        "phone",
        "mobile",
        "linkedin",
        "github",
        "portfolio",
        "address",
        "objective",
        "summary"
    ]

    for line in lines[:15]:

        line = line.strip()

        if not line:
            continue

        if "@" in line:
            continue

        if re.search(
            r"\d",
            line
        ):
            continue

        lower_line = line.lower()

        if any(
            word in lower_line
            for word in ignored_words
        ):
            continue

        words = line.split()

        if not 2 <= len(words) <= 4:
            continue

        valid = all(
            re.fullmatch(
                r"[A-Za-z.'-]+",
                word
            )
            for word in words
        )

        if valid:
            return line.title()

    return "Not Found"


# ============================================================
# SKILL EXTRACTION
# ============================================================

def extract_skills(text):

    found_skills = []

    for skill, aliases in SKILLS.items():

        for alias in aliases:

            if contains_keyword(
                text,
                alias
            ):

                found_skills.append(
                    skill
                )

                break

    return found_skills


# ============================================================
# SECTION DETECTION
# ============================================================

def detect_sections(text):

    result = {}

    normalized = normalize_text(
        text
    )

    for section, keywords in SECTION_KEYWORDS.items():

        result[section] = any(
            keyword in normalized
            for keyword in keywords
        )

    return result


# ============================================================
# PROFILE DETECTION
# ============================================================

def detect_profiles(text):

    normalized = normalize_text(
        text
    )

    linkedin = (
        "linkedin.com" in normalized
        or "linkedin" in normalized
    )

    github = (
        "github.com" in normalized
        or "github" in normalized
    )

    portfolio = (
        "portfolio" in normalized
        or "http://" in normalized
        or "https://" in normalized
    )

    return linkedin, github, portfolio


# ============================================================
# RESUME LENGTH
# ============================================================

def analyze_length(text):

    words = text.split()

    word_count = len(words)

    if word_count < 150:

        status = "Too Short"

    elif word_count <= 700:

        status = "Good"

    elif word_count <= 1000:

        status = "Long"

    else:

        status = "Very Long"

    return word_count, status


# ============================================================
# BULLET ANALYSIS
# ============================================================

def get_bullet_lines(text):

    lines = text.splitlines()

    bullets = []

    for line in lines:

        stripped = line.strip()

        if (
            stripped.startswith("•")
            or stripped.startswith("-")
            or stripped.startswith("*")
            or stripped.startswith("·")
        ):

            bullets.append(
                stripped
            )

    return bullets


def analyze_bullets(text):

    bullets = get_bullet_lines(
        text
    )

    strong_bullets = 0

    measurable_bullets = 0

    for bullet in bullets:

        bullet_lower = bullet.lower()

        if any(
            re.search(
                r"\b"
                + re.escape(verb)
                + r"\b",
                bullet_lower
            )
            for verb in ACTION_VERBS
        ):

            strong_bullets += 1

        if re.search(
            r"\d+%|\d+\+|\d+x|\$\d+|\b\d+\b",
            bullet
        ):

            measurable_bullets += 1

    return (
        len(bullets),
        strong_bullets,
        measurable_bullets
    )


# ============================================================
# CONTACT QUALITY
# ============================================================

def analyze_email_quality(email):

    if email == "Not Found":
        return False

    free_email_domains = [
        "gmail.com",
        "outlook.com",
        "hotmail.com",
        "yahoo.com"
    ]

    domain = email.split("@")[-1].lower()

    return domain in free_email_domains


# ============================================================
# ATS SCORE
# ============================================================

def calculate_ats_score(
    name,
    email,
    phone,
    skills,
    sections,
    linkedin,
    github,
    word_count,
    bullet_count,
    measurable_bullets
):

    breakdown = {}


    # Personal information
    breakdown["Name"] = (
        5 if name != "Not Found"
        else 0
    )

    breakdown["Email"] = (
        5 if email != "Not Found"
        else 0
    )

    breakdown["Phone"] = (
        5 if phone != "Not Found"
        else 0
    )


    # Skills
    breakdown["Skills"] = min(
        len(skills) * 2,
        20
    )


    # Resume sections
    breakdown["Education"] = (
        10 if sections["Education"]
        else 0
    )

    breakdown["Projects"] = (
        10 if sections["Projects"]
        else 0
    )

    breakdown["Experience"] = (
        10 if sections["Experience"]
        else 0
    )

    breakdown["Certifications"] = (
        5 if sections["Certifications"]
        else 0
    )


    # Online profiles
    breakdown["LinkedIn"] = (
        5 if linkedin
        else 0
    )

    breakdown["GitHub"] = (
        5 if github
        else 0
    )


    # Resume length
    breakdown["Length"] = (
        5
        if 150 <= word_count <= 700
        else 0
    )


    # Measurable achievements
    if bullet_count > 0:

        ratio = (
            measurable_bullets
            / bullet_count
        )

        if ratio >= 0.50:

            breakdown["Achievements"] = 5

        elif ratio >= 0.25:

            breakdown["Achievements"] = 3

        else:

            breakdown["Achievements"] = 0

    else:

        breakdown["Achievements"] = 0


    score = sum(
        breakdown.values()
    )

    score = min(
        score,
        100
    )

    return score, breakdown


# ============================================================
# JOB DESCRIPTION MATCHING
# ============================================================

def analyze_job_match(
    resume_text,
    job_description
):

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )

    matching = []

    missing = []

    for skill in job_skills:

        if skill in resume_skills:

            matching.append(
                skill
            )

        else:

            missing.append(
                skill
            )


    if job_skills:

        skill_match = (
            len(matching)
            / len(job_skills)
        ) * 100

    else:

        skill_match = 0


    # Keyword analysis
    resume_words = set(
        re.findall(
            r"\b[a-zA-Z][a-zA-Z+#.-]{2,}\b",
            normalize_text(resume_text)
        )
    )

    job_words = set(
        re.findall(
            r"\b[a-zA-Z][a-zA-Z+#.-]{2,}\b",
            normalize_text(job_description)
        )
    )


    common_words = {
        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "are",
        "from",
        "you",
        "your",
        "our",
        "will",
        "have",
        "has",
        "job",
        "work",
        "role",
        "looking",
        "using",
        "required"
    }


    meaningful_job_words = (
        job_words - common_words
    )

    matched_words = (
        meaningful_job_words
        & resume_words
    )


    if meaningful_job_words:

        keyword_match = (
            len(matched_words)
            / len(meaningful_job_words)
        ) * 100

    else:

        keyword_match = 0


    # Combined score
    if job_skills:

        overall_match = (
            skill_match * 0.75
            + keyword_match * 0.25
        )

    else:

        overall_match = keyword_match


    return {
        "job_skills": job_skills,
        "matching_skills": matching,
        "missing_skills": missing,
        "skill_match": skill_match,
        "keyword_match": keyword_match,
        "overall_match": min(
            overall_match,
            100
        )
    }


# ============================================================
# RECOMMENDATIONS
# ============================================================

def generate_recommendations(
    name,
    email,
    phone,
    skills,
    sections,
    linkedin,
    github,
    portfolio,
    word_count,
    bullet_count,
    strong_bullets,
    measurable_bullets,
    missing_skills
):

    recommendations = []


    if name == "Not Found":

        recommendations.append(
            "Place your full name clearly at the top of the resume."
        )


    if email == "Not Found":

        recommendations.append(
            "Add a professional email address."
        )


    if phone == "Not Found":

        recommendations.append(
            "Add a valid phone number."
        )


    if len(skills) < 5:

        recommendations.append(
            "Add more relevant technical skills that match the jobs you are targeting."
        )


    if not sections["Summary"]:

        recommendations.append(
            "Consider adding a short professional summary tailored to your target role."
        )


    if not sections["Education"]:

        recommendations.append(
            "Add a clearly labelled Education section."
        )


    if not sections["Projects"]:

        recommendations.append(
            "Add 2–3 relevant projects and mention the technologies used."
        )


    if not sections["Experience"]:

        recommendations.append(
            "Add internships, work experience, training, or practical experience where applicable."
        )


    if not sections["Certifications"]:

        recommendations.append(
            "Add relevant certifications if you have completed any."
        )


    if not linkedin:

        recommendations.append(
            "Add your LinkedIn profile."
        )


    if not github:

        recommendations.append(
            "Add your GitHub profile for technical/software roles."
        )


    if word_count < 150:

        recommendations.append(
            "Your resume appears too short. Add relevant projects, skills, achievements, or experience."
        )


    if word_count > 1000:

        recommendations.append(
            "Your resume is quite long. Remove repetitive or less relevant information."
        )


    if bullet_count == 0:

        recommendations.append(
            "Use bullet points for project and experience descriptions."
        )


    elif strong_bullets < bullet_count * 0.50:

        recommendations.append(
            "Use stronger action verbs such as Developed, Designed, Implemented, Built, Optimized, and Automated."
        )


    if (
        bullet_count > 0
        and measurable_bullets < bullet_count * 0.25
    ):

        recommendations.append(
            "Add measurable results such as percentages, numbers, users, time saved, or performance improvements."
        )


    if missing_skills:

        recommendations.append(
            "For this job, consider learning or highlighting: "
            + ", ".join(missing_skills)
            + "."
        )


    if not recommendations:

        recommendations.append(
            "Your resume passed all current quality checks. Continue tailoring it to each job."
        )


    return recommendations


# ============================================================
# REPORT GENERATOR
# ============================================================

def create_report(
    name,
    email,
    phone,
    skills,
    ats_score,
    score_breakdown,
    sections,
    word_count,
    length_status,
    bullet_count,
    strong_bullets,
    measurable_bullets,
    job_analysis,
    recommendations
):

    lines = []

    lines.append(
        "RESUME ANALYZER REPORT"
    )

    lines.append(
        "=" * 50
    )

    lines.append("")

    lines.append(
        f"Name: {name}"
    )

    lines.append(
        f"Email: {email}"
    )

    lines.append(
        f"Phone: {phone}"
    )

    lines.append("")

    lines.append(
        f"ATS Score: {ats_score}/100"
    )

    lines.append("")

    lines.append(
        "DETECTED SKILLS"
    )

    lines.append(
        "-" * 30
    )

    lines.append(
        ", ".join(skills)
        if skills
        else "None detected"
    )

    lines.append("")

    lines.append(
        "RESUME SECTIONS"
    )

    lines.append(
        "-" * 30
    )

    for section, exists in sections.items():

        lines.append(
            f"{section}: "
            + (
                "Present"
                if exists
                else "Missing"
            )
        )

    lines.append("")

    lines.append(
        "RESUME QUALITY"
    )

    lines.append(
        "-" * 30
    )

    lines.append(
        f"Word Count: {word_count}"
    )

    lines.append(
        f"Length Status: {length_status}"
    )

    lines.append(
        f"Bullet Points: {bullet_count}"
    )

    lines.append(
        f"Strong Action Bullets: {strong_bullets}"
    )

    lines.append(
        f"Measurable Bullets: {measurable_bullets}"
    )

    lines.append("")

    lines.append(
        "ATS SCORE BREAKDOWN"
    )

    lines.append(
        "-" * 30
    )

    for category, points in score_breakdown.items():

        lines.append(
            f"{category}: {points}"
        )

    if job_analysis:

        lines.append("")

        lines.append(
            "JOB MATCH ANALYSIS"
        )

        lines.append(
            "-" * 30
        )

        lines.append(
            "Overall Match: "
            f"{job_analysis['overall_match']:.1f}%"
        )

        lines.append(
            "Skill Match: "
            f"{job_analysis['skill_match']:.1f}%"
        )

        lines.append(
            "Keyword Match: "
            f"{job_analysis['keyword_match']:.1f}%"
        )

        lines.append("")

        lines.append(
            "Matching Skills:"
        )

        lines.append(
            ", ".join(
                job_analysis["matching_skills"]
            )
            if job_analysis["matching_skills"]
            else "None"
        )

        lines.append("")

        lines.append(
            "Missing Skills:"
        )

        lines.append(
            ", ".join(
                job_analysis["missing_skills"]
            )
            if job_analysis["missing_skills"]
            else "None"
        )

    lines.append("")

    lines.append(
        "RECOMMENDATIONS"
    )

    lines.append(
        "-" * 30
    )

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        lines.append(
            f"{index}. {recommendation}"
        )

    return "\n".join(
        lines
    )


# ============================================================
# APPLICATION HEADER
# ============================================================

st.title(
    "📄 Resume Analyzer"
)

st.write(
    "Analyze your resume, evaluate ATS readiness, "
    "compare it with a job description, and receive "
    "actionable improvement suggestions."
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

resume_column, job_column = st.columns(
    2
)


with resume_column:

    st.subheader(
        "📤 Upload Resume"
    )

    uploaded_file = st.file_uploader(
        "Upload your resume as a PDF",
        type=["pdf"]
    )


with job_column:

    st.subheader(
        "💼 Job Description"
    )

    job_description = st.text_area(
        "Paste the job description here",
        height=180,
        placeholder=(
            "Paste the job description here "
            "to calculate your job match..."
        )
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

if uploaded_file:

    try:

        # ----------------------------------------------------
        # Extract text
        # ----------------------------------------------------

        resume_text = extract_pdf_text(
            uploaded_file
        )


        if not resume_text.strip():

            st.error(
                "The PDF does not contain readable text. "
                "Try a text-based PDF instead of a scanned image PDF."
            )

            st.stop()


        # ----------------------------------------------------
        # Extract candidate details
        # ----------------------------------------------------

        name = extract_name(
            resume_text
        )

        email = extract_email(
            resume_text
        )

        phone = extract_phone(
            resume_text
        )


        # ----------------------------------------------------
        # Extract skills
        # ----------------------------------------------------

        skills = extract_skills(
            resume_text
        )


        # ----------------------------------------------------
        # Detect sections
        # ----------------------------------------------------

        sections = detect_sections(
            resume_text
        )


        # ----------------------------------------------------
        # Detect profiles
        # ----------------------------------------------------

        linkedin, github, portfolio = (
            detect_profiles(
                resume_text
            )
        )


        # ----------------------------------------------------
        # Resume quality
        # ----------------------------------------------------

        (
            word_count,
            length_status
        ) = analyze_length(
            resume_text
        )


        (
            bullet_count,
            strong_bullets,
            measurable_bullets
        ) = analyze_bullets(
            resume_text
        )


        # ----------------------------------------------------
        # ATS score
        # ----------------------------------------------------

        (
            ats_score,
            score_breakdown
        ) = calculate_ats_score(
            name,
            email,
            phone,
            skills,
            sections,
            linkedin,
            github,
            word_count,
            bullet_count,
            measurable_bullets
        )


        # ----------------------------------------------------
        # Job analysis
        # ----------------------------------------------------

        job_analysis = None

        missing_skills = []

        if job_description.strip():

            job_analysis = analyze_job_match(
                resume_text,
                job_description
            )

            missing_skills = (
                job_analysis[
                    "missing_skills"
                ]
            )


        # ----------------------------------------------------
        # Recommendations
        # ----------------------------------------------------

        recommendations = (
            generate_recommendations(
                name,
                email,
                phone,
                skills,
                sections,
                linkedin,
                github,
                portfolio,
                word_count,
                bullet_count,
                strong_bullets,
                measurable_bullets,
                missing_skills
            )
        )


        st.success(
            "✅ Resume analyzed successfully!"
        )


        # ====================================================
        # CANDIDATE INFORMATION
        # ====================================================

        st.header(
            "👤 Candidate Information"
        )


        c1, c2, c3 = st.columns(
            3
        )


        with c1:

            st.metric(
                "Name",
                name
            )


        with c2:

            st.metric(
                "Email",
                email
            )


        with c3:

            st.metric(
                "Phone",
                phone
            )


        # ====================================================
        # MAIN DASHBOARD
        # ====================================================

        st.header(
            "📊 Resume Dashboard"
        )


        d1, d2, d3, d4 = st.columns(
            4
        )


        with d1:

            st.metric(
                "ATS Score",
                f"{ats_score}/100"
            )


        with d2:

            st.metric(
                "Skills",
                len(skills)
            )


        with d3:

            st.metric(
                "Words",
                word_count
            )


        with d4:

            if job_analysis:

                st.metric(
                    "Job Match",
                    f"{job_analysis['overall_match']:.1f}%"
                )

            else:

                st.metric(
                    "Job Match",
                    "N/A"
                )


        st.progress(
            ats_score / 100
        )


        if ats_score >= 80:

            st.success(
                "🌟 Strong resume based on the current checks."
            )

        elif ats_score >= 60:

            st.info(
                "👍 Good resume with some areas to improve."
            )

        elif ats_score >= 40:

            st.warning(
                "⚠️ Your resume needs improvement."
            )

        else:

            st.error(
                "❗ Your resume needs significant improvement."
            )


        # ====================================================
        # SKILLS
        # ====================================================

        st.header(
            "🛠️ Detected Skills"
        )


        if skills:

            skill_columns = st.columns(
                4
            )

            for index, skill in enumerate(
                skills
            ):

                with skill_columns[
                    index % 4
                ]:

                    st.success(
                        skill
                    )

        else:

            st.warning(
                "No known technical skills were detected."
            )


        # ====================================================
        # SECTIONS
        # ====================================================

        st.header(
            "📑 Resume Sections"
        )


        section_columns = st.columns(
            3
        )


        for index, (
            section,
            exists
        ) in enumerate(
            sections.items()
        ):

            with section_columns[
                index % 3
            ]:

                if exists:

                    st.success(
                        f"✅ {section}"
                    )

                else:

                    st.error(
                        f"❌ {section}"
                    )


        # ====================================================
        # PROFILE CHECK
        # ====================================================

        st.header(
            "🌐 Online Profiles"
        )


        p1, p2, p3 = st.columns(
            3
        )


        with p1:

            if linkedin:

                st.success(
                    "✅ LinkedIn detected"
                )

            else:

                st.warning(
                    "❌ LinkedIn not detected"
                )


        with p2:

            if github:

                st.success(
                    "✅ GitHub detected"
                )

            else:

                st.warning(
                    "❌ GitHub not detected"
                )


        with p3:

            if portfolio:

                st.success(
                    "✅ Portfolio/link detected"
                )

            else:

                st.info(
                    "ℹ️ Portfolio not detected"
                )


        # ====================================================
        # RESUME QUALITY
        # ====================================================

        st.header(
            "🔍 Resume Quality"
        )


        q1, q2, q3, q4 = st.columns(
            4
        )


        with q1:

            st.metric(
                "Word Count",
                word_count
            )

            st.caption(
                length_status
            )


        with q2:

            st.metric(
                "Bullet Points",
                bullet_count
            )


        with q3:

            st.metric(
                "Strong Bullets",
                strong_bullets
            )


        with q4:

            st.metric(
                "Measured Bullets",
                measurable_bullets
            )


        # ====================================================
        # JOB MATCH
        # ====================================================

        if job_analysis:

            st.divider()

            st.header(
                "🎯 Job Match Analysis"
            )


            j1, j2, j3 = st.columns(
                3
            )


            with j1:

                st.metric(
                    "Overall Match",
                    f"{job_analysis['overall_match']:.1f}%"
                )


            with j2:

                st.metric(
                    "Skill Match",
                    f"{job_analysis['skill_match']:.1f}%"
                )


            with j3:

                st.metric(
                    "Keyword Match",
                    f"{job_analysis['keyword_match']:.1f}%"
                )


            st.progress(
                job_analysis["overall_match"]
                / 100
            )


            if job_analysis["overall_match"] >= 80:

                st.success(
                    "🌟 Excellent match for the detected requirements."
                )

            elif job_analysis["overall_match"] >= 60:

                st.info(
                    "👍 Good match, but there are some areas to improve."
                )

            elif job_analysis["overall_match"] >= 40:

                st.warning(
                    "⚠️ Moderate match. Review the missing skills."
                )

            else:

                st.error(
                    "❗ Low match. Consider tailoring your resume."
                )


            match_column, missing_column = (
                st.columns(2)
            )


            with match_column:

                st.subheader(
                    "✅ Matching Skills"
                )

                if job_analysis[
                    "matching_skills"
                ]:

                    for skill in job_analysis[
                        "matching_skills"
                    ]:

                        st.success(
                            skill
                        )

                else:

                    st.write(
                        "No matching skills detected."
                    )


            with missing_column:

                st.subheader(
                    "❌ Missing Skills"
                )

                if job_analysis[
                    "missing_skills"
                ]:

                    for skill in job_analysis[
                        "missing_skills"
                    ]:

                        st.error(
                            skill
                        )

                else:

                    st.success(
                        "No detected job skills are missing."
                    )


            st.subheader(
                "💼 Skills Detected in Job Description"
            )


            if job_analysis[
                "job_skills"
            ]:

                st.write(
                    ", ".join(
                        job_analysis[
                            "job_skills"
                        ]
                    )
                )

            else:

                st.info(
                    "No known skills were detected in the job description."
                )


        # ====================================================
        # ATS BREAKDOWN
        # ====================================================

        with st.expander(
            "📊 View ATS Score Breakdown"
        ):

            for category, points in (
                score_breakdown.items()
            ):

                st.write(
                    f"**{category}:** {points} points"
                )


        # ====================================================
        # RECOMMENDATIONS
        # ====================================================

        st.header(
            "💡 Recommendations"
        )


        for index, recommendation in enumerate(
            recommendations,
            start=1
        ):

            st.write(
                f"**{index}.** {recommendation}"
            )


        # ====================================================
        # DOWNLOAD REPORT
        # ====================================================

        report = create_report(
            name,
            email,
            phone,
            skills,
            ats_score,
            score_breakdown,
            sections,
            word_count,
            length_status,
            bullet_count,
            strong_bullets,
            measurable_bullets,
            job_analysis,
            recommendations
        )


        st.header(
            "📥 Download Analysis"
        )


        st.download_button(
            label="📄 Download Resume Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )


        # ====================================================
        # EXTRACTED TEXT
        # ====================================================

        with st.expander(
            "🔍 View Extracted Resume Text"
        ):

            st.text_area(
                "Extracted Resume Text",
                resume_text,
                height=450
            )


    except Exception as error:

        st.error(
            "❌ Something went wrong while analyzing the resume."
        )

        st.exception(error)


else:

    st.info(
        "👆 Upload your PDF resume to begin."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Resume Analyzer | Python • Streamlit • PyMuPDF"
)