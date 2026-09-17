import streamlit as st
from pypdf import PdfReader

# -------------------------------
# PAGE SETTINGS
# -------------------------------

st.set_page_config(
    page_title="Resume Analyzer Chatbot",
    page_icon="🤖"
)

# -------------------------------
# TITLE
# -------------------------------

st.title("🤖 Resume Analyzer Chatbot")
st.write("Upload your resume and ask questions about it.")

# -------------------------------
# UPLOAD RESUME
# -------------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    # -------------------------------
    # READ PDF
    # -------------------------------

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    resume_lower = resume_text.lower()

    st.success("✅ Resume uploaded and analyzed!")

    # -------------------------------
    # SKILL DETECTION
    # -------------------------------

    skills_list = [
        "python",
        "java",
        "c++",
        "javascript",
        "html",
        "css",
        "mysql",
        "sql",
        "django",
        "flask",
        "machine learning",
        "deep learning",
        "nlp",
        "artificial intelligence",
        "tensorflow",
        "pytorch",
        "git",
        "github",
        "aws",
        "azure",
        "bootstrap",
        "react",
        "node.js"
    ]

    found_skills = []

    for skill in skills_list:

        if skill in resume_lower:
            found_skills.append(skill.title())

    # -------------------------------
    # RESUME SCORE
    # -------------------------------

    score = 0

    if found_skills:
        score += 2

    if (
        "education" in resume_lower
        or "b.tech" in resume_lower
        or "bachelor" in resume_lower
        or "degree" in resume_lower
    ):
        score += 2

    if "project" in resume_lower:
        score += 2

    if (
        "experience" in resume_lower
        or "internship" in resume_lower
    ):
        score += 2

    if (
        "certification" in resume_lower
        or "certificate" in resume_lower
    ):
        score += 2

    # -------------------------------
    # RESUME ANALYSIS
    # -------------------------------

    st.subheader("📊 Resume Analysis")

    st.metric(
        "Resume Score",
        f"{score}/10"
    )

    # -------------------------------
    # SKILLS DISPLAY
    # -------------------------------

    if found_skills:

        st.write("### 🛠️ Skills Found")

        st.write(
            ", ".join(found_skills)
        )

    # -------------------------------
    # SUGGESTIONS
    # -------------------------------

    st.write("### 💡 Suggestions")

    if not found_skills:
        st.write("• Add a clear Skills section.")
    else:
        st.write("✅ Skills section is present.")

    if "project" not in resume_lower:
        st.write(
            "• Add 2–3 relevant projects with technologies used."
        )
    else:
        st.write("✅ Projects are included.")

    if (
        "experience" not in resume_lower
        and "internship" not in resume_lower
    ):
        st.write(
            "• Add internship or work experience if available."
        )
    else:
        st.write("✅ Experience or internship is included.")

    if (
        "certification" not in resume_lower
        and "certificate" not in resume_lower
    ):
        st.write(
            "• Add relevant certifications if available."
        )
    else:
        st.write("✅ Certifications are included.")

    st.write(
        "• Use clear bullet points and measurable achievements."
    )

    st.write(
        "• Keep the resume concise and easy to read."
    )

    # -------------------------------
    # CHATBOT
    # -------------------------------

    st.subheader("💬 Resume Chatbot")

    question = st.text_input(
        "Ask something about your resume:"
    )

    if question:

        q = question.lower()

        # -------------------------------
        # SKILLS
        # -------------------------------

        if "skill" in q:

            if found_skills:

                st.write(
                    "🤖 Your skills are:"
                )

                st.write(
                    ", ".join(found_skills)
                )

            else:

                st.write(
                    "🤖 No matching skills were found."
                )

        # -------------------------------
        # PROJECTS
        # -------------------------------

        elif "project" in q:

            st.write(
                "🤖 Your resume contains project-related information."
            )

            st.write(
                "Please check the Projects section of your resume."
            )

        # -------------------------------
        # EDUCATION
        # -------------------------------

        elif (
            "education" in q
            or "degree" in q
            or "study" in q
        ):

            st.write(
                "🎓 Your resume contains education information."
            )

            st.write(
                "Please check the Education section of your resume."
            )

        # -------------------------------
        # EXPERIENCE
        # -------------------------------

        elif (
            "experience" in q
            or "internship" in q
            or "work" in q
        ):

            st.write(
                "💼 Your resume contains experience/internship information."
            )

            st.write(
                "Please check the Experience section of your resume."
            )

        # -------------------------------
        # CERTIFICATIONS
        # -------------------------------

        elif (
            "certification" in q
            or "certificate" in q
        ):

            st.write(
                "🏆 Your resume contains certification information."
            )

            st.write(
                "Please check the Certifications section of your resume."
            )

        # -------------------------------
        # RESUME SCORE
        # -------------------------------

        elif (
            "score" in q
            or "rating" in q
        ):

            st.write(
                f"📊 Your resume score is {score}/10."
            )

        # -------------------------------
        # IMPROVEMENT
        # -------------------------------

        elif (
            "improve" in q
            or "better" in q
            or "suggestion" in q
            or "improvement" in q
        ):

            st.write(
                "💡 Here are some suggestions to improve your resume:"
            )

            if found_skills:
                st.write(
                    "✅ Your resume has relevant technical skills."
                )
            else:
                st.write(
                    "• Add technical skills."
                )

            if "project" in resume_lower:
                st.write(
                    "✅ Projects are included."
                )
            else:
                st.write(
                    "• Add 2–3 relevant projects."
                )

            if (
                "experience" in resume_lower
                or "internship" in resume_lower
            ):
                st.write(
                    "✅ Experience/internship is included."
                )
            else:
                st.write(
                    "• Add internship or practical experience if available."
                )

            if (
                "certification" in resume_lower
                or "certificate" in resume_lower
            ):
                st.write(
                    "✅ Certifications are included."
                )
            else:
                st.write(
                    "• Add relevant certifications if available."
                )

            st.write(
                "• Add measurable achievements to projects."
            )

            st.write(
                "• Use simple and clear bullet points."
            )

            st.write(
                "• Keep the resume concise."
            )

        # -------------------------------
        # SUMMARY
        # -------------------------------

        elif (
            "summary" in q
            or "about" in q
        ):

            st.write(
                "📋 Resume Summary"
            )

            summary_text = resume_text[:1000]

            st.write(summary_text)

        # -------------------------------
        # NAME
        # -------------------------------

        elif "name" in q:

            st.write(
                "👤 Your name is mentioned in the uploaded resume."
            )

        # -------------------------------
        # HELP
        # -------------------------------

        else:

            st.write(
                "🤖 You can ask me about:"
            )

            st.write(
                "• Skills"
            )

            st.write(
                "• Projects"
            )

            st.write(
                "• Education"
            )

            st.write(
                "• Experience"
            )

            st.write(
                "• Certifications"
            )

            st.write(
                "• Resume Score"
            )

            st.write(
                "• How to improve my resume"
            )