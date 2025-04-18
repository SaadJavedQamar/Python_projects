import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Rock Paper Scissors by Saad Qamar", page_icon="🎮", layout="centered")

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        .saad-name {
            font-size: 50px;
            font-weight: bold;
            text-align: center;
            color: #FF6347;
            text-shadow: 2px 2px 4px #00000030;
            margin-bottom: 10px;
        }
        .game-title {
            font-size: 32px;
            color: #00BFFF;
            text-align: center;
            margin-top: -10px;
        }
        .subtitle {
            font-size: 18px;
            color: #777;
            text-align: center;
        }
        .footer {
            text-align: center;
            color: gray;
            margin-top: 50px;
            font-size: 15px;
        }
        .footer a {
            color: #1E90FF;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header with Developer Name ---
st.markdown('<div class="saad-name">👑 Saad Qamar Presents</div>', unsafe_allow_html=True)
st.markdown('<div class="game-title">🎮 Rock • Paper • Scissors</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Play against the computer. Can you win? 🧠💥</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Game Section ---
st.markdown("### ✨ Pick Your Move:")
choices = {
    '🪨 Rock': 'rock',
    '📄 Paper': 'paper',
    '✂️ Scissors': 'scissors'
}
user_choice_emoji = st.radio("", list(choices.keys()), index=0)
user_choice = choices[user_choice_emoji]
computer_choice = random.choice(list(choices.values()))

if st.button("🔥 Play Now"):
    st.markdown(f"**🤖 Computer chose:** `{computer_choice.capitalize()}`")
    
    if user_choice == computer_choice:
        st.info("😐 It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        st.success("🎉 You Win!")
    else:
        st.error("😢 You Lose!")

# --- Footer with Developer Info ---
st.markdown("---")
st.markdown("""
    <div class="footer">
        Developed with ❤️ by <b>Saad Qamar</b><br><br>
        🎓 Student at <b>FAST National University of Computer and Emerging Sciences</b><br>
        📧 Email: <a href="mailto:saadqamar213569@gmail.com">saadqamar213569@gmail.com</a><br>
        🔗 <a href="www.linkedin.com/in/saad-qamar-30557b21b">LinkedIn</a> | 
        <a href="https://github.com/SaadJavedQamar/">GitHub</a>
    </div>
""", unsafe_allow_html=True)
