import streamlit as st
from google import genai
from database import save_interview

# Gemini API Key
client = genai.Client(api_key="AIzaSyDpnQqBBGkFtdh-kCDKrY-bI6_NLXUXY3A")

st.set_page_config(page_title="AI Interview Agent", page_icon="🤖", layout="centered")

st.title("🤖 AI Interview Agent")

st.markdown("### AI Powered Technical Interview Simulator")


candidate_name = st.text_input("Enter Candidate Name")
role = st.text_input("Enter Job Role")

skills = st.text_input("Enter Skills")

if st.button("Generate Interview Question"):

    prompt = f"""
    Generate one technical interview question
    for a {role} candidate with skills: {skills}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    question = response.text

    st.session_state.question = question

if "question" in st.session_state:

    st.subheader("Interview Question")

    st.write(st.session_state.question)

    answer = st.text_area("Enter Your Answer")

    if st.button("Evaluate Answer"):

        evaluation_prompt = f"""
        Evaluate this interview answer.

        Question:
        {st.session_state.question}

        Answer:
        {answer}

        Give:
        1. Score out of 10
        2. Feedback
        """

        evaluation = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=evaluation_prompt
        )

        result = evaluation.text

        st.subheader("Evaluation Result")

        st.write(result)

        score = "8/10"

        save_interview(
            candidate_name,
            role,
            st.session_state.question,
            answer,
            score,
            result
        )

        st.success("Interview Saved Successfully!")