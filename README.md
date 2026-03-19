# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - The game is a number-guessing app where the player enters a guess and receives feedback until they find the secret number.

- [x] Detail which bugs you found.
  - The secret number reset on each button click because it was re-generated on every rerun instead of stored in `st.session_state`.
  - The hint system returned reversed advice, e.g., saying "Higher" when the guess was already above the secret number.

- [x] Explain what fixes you applied.
  - Persisted the secret number lever using `st.session_state['secret_number']` so it remains stable between submissions.
  - Corrected hint logic to compare the guess correctly and display "higher" only when guess < secret and "lower" when guess > secret.
  - Refactored logic into `logic_utils.py` for unit-testable functions and verified behavior with `pytest`.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![game won](images/game1.png)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
