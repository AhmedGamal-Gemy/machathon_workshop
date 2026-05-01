import streamlit as st
import datetime

st.set_page_config(page_title="Study Schedule Generator")
st.title("Study Schedule Generator")

subject = st.text_input("Subject Name")
topics_input = st.text_area("Topics to cover (one per line)")
exam_date = st.date_input(
    "Exam Date", min_value=datetime.date.today() + datetime.timedelta(days=1)
)
study_hours = st.slider("Study Hours per Day", 1, 8, 2)

generate_disabled = not subject.strip() or not topics_input.strip()
if st.button("Generate Schedule", disabled=generate_disabled):
    topics = [t.strip() for t in topics_input.split("\n") if t.strip()]
    if not topics:
        st.error("Please enter at least one topic.")
    else:
        today = datetime.date.today()
        total_days = (exam_date - today).days
        num_topics = len(topics)

        days_per_topic = total_days // num_topics
        remaining_days = total_days % num_topics

        schedule = []
        current_date = today + datetime.timedelta(days=1)

        for topic in topics:
            for _ in range(days_per_topic):
                schedule.append({"date": current_date, "topic": topic})
                current_date += datetime.timedelta(days=1)

        for _ in range(remaining_days):
            schedule.append({"date": current_date, "topic": "Review"})
            current_date += datetime.timedelta(days=1)

        for i, day in enumerate(schedule):
            with st.expander(
                f"Day {i + 1}: {day['date'].strftime('%Y-%m-%d')} - {day['topic']}"
            ):
                st.write(f"**Date:** {day['date'].strftime('%B %d, %Y')}")
                st.write(f"**Topic:** {day['topic']}")
                st.write("**Study Plan:**")
                st.markdown("- Read and understand core concepts")
                st.markdown("- Practice with examples")
                st.markdown("- Review and take notes")
                st.markdown("- Test understanding with practice questions")

        total_study_hours = total_days * study_hours
        st.metric("Total Study Hours", total_study_hours)
