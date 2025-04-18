import streamlit as st
import sqlite3

# Database connection setup
def init_db():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (name TEXT, comment TEXT)''')
    conn.commit()
    conn.close()

def insert_feedback(name, comment):
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("INSERT INTO feedback (name, comment) VALUES (?, ?)", (name, comment))
    conn.commit()
    conn.close()

def get_feedback():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    rows = c.fetchall()
    conn.close()
    return rows

# Initialize DB
init_db()

# Streamlit UI
st.title("📝 Feedback Form")

with st.form(key='feedback_form'):
    name = st.text_input("Your Name")
    comment = st.text_area("Your Feedback")
    submit = st.form_submit_button("Submit")

    if submit:
        insert_feedback(name, comment)
        st.success("Thanks for your feedback!")

# Show past feedback
if st.checkbox("Show Feedback"):
    feedback = get_feedback()
    for entry in feedback:
        st.write(f"👤 **{entry[0]}**: {entry[1]}")
