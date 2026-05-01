Build a Streamlit app called "Study Schedule Generator". The app should:

Have a text input for the subject name
Have a text area for topics to cover, one per line
Have a date picker for the exam date, minimum value is tomorrow
Have a slider for study hours per day, range 1 to 8, default 2
Have a "Generate Schedule" button that is disabled if subject or topics are empty
When clicked, calculate the number of days until the exam, divide them evenly across the topics, and assign any remaining days as full review days
Display each day as a Streamlit expander showing the date, topic, and a bullet point study plan for that day
Show total study hours at the bottom
Use only: streamlit, datetime, math. No external APIs or dependencies.