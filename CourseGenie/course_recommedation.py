import streamlit as st
from Services.ml_course_recommendation_model import predict_course

# Streamlit UI
st.title("AI Course Recommendation")

# Take in profile data
st.subheader("Enter LinkedIn Profile Details")

name = st.text_input("Name", "Dr. Ananya Sharma")
position = st.text_input(
    "Position", "AI Research Scientist | AI Fundamentals Specialist"
)
company = st.text_input("Company", "AI Solutions Ltd.")
location = st.text_input("Location", "San Francisco, CA")
linkedin_summary = st.text_area(
    "LinkedIn Summary",
    "Experienced AI professional focused on the fundamentals of Artificial Intelligence, building foundational models and training AI systems.",
)
skills = st.text_area(
    "Skills (comma separated)",
    "Artificial Intelligence Fundamentals, AI Systems, Machine Learning",
)

course_ids = {
    "AI Fundamentals+": {
        "Course Code": "GIT-AI-001",
        "Course Name": "Artificial Intelligence Fundamentals",
        "Alias": "AI Fundamentals+",
        "Price": "40.00"
    },
    "AI Data+": {
        "Course Code": "GIT-AI-002",
        "Course Name": "AI Data Analytics and Knowledge Mining",
        "Alias": "AI Data+",
        "Price": "40.00"
    },
    "AI Gen+": {
        "Course Code": "GIT-AI-003",
        "Course Name": "Generative AI",
        "Alias": "AI Gen+",
        "Price": "40.00"
    },
    "AI Deep+": {
        "Course Code": "GIT-AI-004",
        "Course Name": "Machine And Deep Learning",
        "Alias": "AI Deep+",
        "Price": "40.00"
    },
    "AI Responsible+": {
        "Course Code": "GIT-AI-005",
        "Course Name": "Responsible AI",
        "Alias": "AI Responsible+",
        "Price": "40.00"
    },
    "None": {
        "Course Code": "GIT-AI-001",
        "Course Name": "Artificial Intelligence Fundamentals",
        "Alias": "AI Fundamentals+",
        "Price": "40.00"
    }
}

# Predict button
if st.button("Recommend Course"):
    # Combine profile details into one text for prediction
    profile_text = linkedin_summary + " " + skills

    # Get the predicted course
    recommended_course = predict_course(profile_text)

    course_details = course_ids[recommended_course]
    st.subheader(f"Recommended Course: \n\n Course Code: {course_details["Course Code"]} \n\n Course Name: {course_details["Course Name"]} \n\n Alias: {course_details["Alias"]} \n\n Price: {course_details["Price"]}")
