import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(page_title="🔤 Word Finder by Saad Qamar", page_icon="🔤", layout="centered")

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
        .grid {
            text-align: center;
            font-size: 24px;
            font-family: 'Courier New', Courier, monospace;
            margin-bottom: 20px;
            color: #333;
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
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
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .button:hover {
            background-color: #45a049;
        }
        .input {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header with Developer Name ---
st.markdown('<div class="saad-name">👑 Saad Qamar Presents</div>', unsafe_allow_html=True)
st.markdown('<div class="game-title">🔤 Word Finder Game</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Find as many words as you can from the given letters! ⏳</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Game Section ---
# Word list (common English words)
word_list = ["apple", "banana", "orange", "grape", "pear", "peach", "plum", "melon", "cherry", "kiwi", "fruit", "juice", "grape", "lemon", "berry", "apricot", "fruit", "peach"]

# Randomly generate a 4x4 grid of letters
letters = random.sample('abcdefghijklmnopqrstuvwxyz', 16)  # Random 16 letters

# Display the grid in a nice box
st.markdown("<div class='grid'>", unsafe_allow_html=True)
st.markdown("```\n" + "\n".join([" ".join(letters[i:i+4]) for i in range(0, 16, 4)]) + "\n```")
st.markdown("</div>", unsafe_allow_html=True)

# Session state for tracking game state
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.time_left = 60  # 60 seconds for the game
    st.session_state.found_words = []
    st.session_state.start_time = time.time()

# Countdown Timer
remaining_time = 60 - int(time.time() - st.session_state.start_time)
st.markdown(f"### Time Left: {remaining_time} seconds")

# Check if the game has ended
if remaining_time <= 0:
    st.balloons()
    st.success(f"🎉 Time's up! You found {len(st.session_state.found_words)} words. Your score: {st.session_state.score}")
    if st.button("🔁 Play Again", key="play_again", help="Click to restart the game", use_container_width=True):
        del st.session_state.score
        del st.session_state.found_words
        del st.session_state.start_time
        st.experimental_rerun()

# Input for word guess
word_guess = st.text_input("Enter a word (from the grid):", key="word_input", max_chars=15, help="Try finding words from the grid", label_visibility="collapsed")

if word_guess:
    # Check if the word is valid and in the grid
    word_guess = word_guess.lower()
    if word_guess in word_list and word_guess not in st.session_state.found_words:
        st.session_state.found_words.append(word_guess)
        st.session_state.score += len(word_guess)  # More letters = more points
        st.success(f"✅ Great! '{word_guess}' is a valid word. Current score: {st.session_state.score}")
    elif word_guess in st.session_state.found_words:
        st.warning(f"❌ You already found the word '{word_guess}'. Try a different one.")
    else:
        st.error(f"❌ '{word_guess}' is not a valid word. Try again!")

# Show the list of found words
st.markdown(f"### Found Words: {', '.join(st.session_state.found_words)}", unsafe_allow_html=True)

# Show current score
st.markdown(f"### Current Score: {st.session_state.score}")

# --- Footer with Developer Info ---
st.markdown("---")
st.markdown("""
    <div class="footer">
        Developed with ❤️ by <b>Saad Qamar</b><br><br>
        🎓 Student at <b>FAST National University of Computer and Emerging Sciences</b><br>
        📧 Email: <a href="mailto:saadqamar213569@gmail.com">saadqamar213569@gmail.com</a><br>
        🔗 <a href="https://www.linkedin.com/in/saad-qamar-30557b21b" target="_blank">LinkedIn</a> | 
        <a href="https://github.com/SaadJavedQamar/" target="_blank">GitHub</a>
    </div>
""", unsafe_allow_html=True)
