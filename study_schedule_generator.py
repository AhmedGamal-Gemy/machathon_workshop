import streamlit as st
from datetime import date, timedelta
import math

st.set_page_config(page_title="Study Schedule Generator", page_icon="📚")
st.title("📚 Study Schedule Generator")

# Input widgets
subject = st.text_input("Subject Name")
topics_text = st.text_area(
    "Topics to Cover", placeholder="Enter topics, one per line..."
)
tomorrow = date.today() + timedelta(days=1)
exam_date = st.date_input("Exam Date", min_value=tomorrow)
hours_per_day = st.slider("Study Hours Per Day", min_value=1, max_value=8, value=2)

topics = [t.strip() for t in topics_text.strip().splitlines() if t.strip()]

can_generate = bool(subject) and bool(topics)
generate_clicked = st.button("Generate Schedule", disabled=not can_generate)

if generate_clicked:
    total_days = (exam_date - date.today()).days

    days_per_topic = math.floor(total_days / len(topics))
    remaining_days = total_days - (days_per_topic * len(topics))

    schedule = []
    current_date = date.today()

    for topic in topics:
        for day in range(days_per_topic):
            current_date += timedelta(days=1)
            schedule.append({"date": current_date, "topic": topic, "type": "study"})

    for day in range(remaining_days):
        current_date += timedelta(days=1)
        schedule.append(
            {"date": current_date, "topic": "Full Review", "type": "review"}
        )

    st.subheader(f"Schedule for {subject}")

    study_plan_items = {
        "study": [
            "Read and understand the material",
            "Take detailed notes",
            "Solve practice problems",
            "Summarize key concepts",
        ],
        "review": [
            "Review all previous notes",
            "Take a practice exam",
            "Identify weak areas",
            "Revisit difficult concepts",
        ],
    }

    for day_num, entry in enumerate(schedule, 1):
        plan_items = study_plan_items[entry["type"]]

        hours_for_day = hours_per_day
        if entry["type"] == "review" and remaining_days > 0:
            hours_for_day = min(hours_per_day, 6)

        with st.expander(f"Day {day_num}: {entry['date'].strftime('%B %d, %Y')}"):
            st.markdown(f"**Topic:** {entry['topic']}")
            st.markdown(f"**Study Hours:** {hours_for_day}")
            st.markdown("**Study Plan:**")
            for item in plan_items:
                st.markdown(f"- {item}")

    total_hours = sum(hours_per_day for _ in schedule)
    st.divider()
    st.metric("Total Study Hours", total_hours)
    st.caption(
        f"{len(schedule)} days planned from {date.today().strftime('%B %d, %Y')} to {exam_date.strftime('%B %d, %Y')}"
    )
