Bugs found:

1. Hint direction reversed
   - Expected: when guess is too high, message says "lower", and when too low, message says "higher".
   - Actual: when guess is too high, message says "Go HIGHER!", and when too low, message says "Go LOWER!".

   This is happening because the outcome labels and hint strings are swapped in check_guess.

2. Inconsistent type handling of secret
   - Expected: secret stays integer and comparisons always are numeric.
   - Actual: code converts secret to string on even attempts, then uses string compare fallback, causing inconsistent behavior.

3. Incorrect range text & static new-game range
   - Expected: info message and new-game secret match difficulty range (Easy 1-20, Normal 1-100, Hard 1-50).
   - Actual: message always says 1-100 and new game always chooses 1-100, even on Easy/Hard.

## 2. How did you use AI as a teammate?

- Correct suggestion:
  - What AI suggested: Clear the reversed hint text paths in `check_guess` (Too High → Go LOWER, Too Low → Go HIGHER) and remove legacy string conversion behavior.
  - Correct/ Incorrect: Correct. This was the main logic bug in the game.
  - How verified: I changed `logic_utils.check_guess` to the correct mappings and executed unit tests (`pytest`). I also manually verified through `streamlit run app.py` that guess feedback now matches expected direction.

- Incorrect/misleading suggestion:
  - What AI suggested: Initially, the app had a hidden fallback in `check_guess` converting values to strings when `TypeError` occurs; the AI suggestion was to keep that fallback but it was not needed in a stable numeric path.
  - Correct/ Incorrect: Misleading. It preserved legacy bug behavior and complicated debugging.
  - How verified: I removed the fallback and then ran regression tests; these tests still passed while making the logic deterministic.

## 3. Debugging and testing your fixes

- How I decided whether a bug was really fixed:
  I mapped code to behavior in `app.py` and `logic_utils.py`, then wrote assertions in `tests/test_game_logic.py` for failure cases and expected outcomes. The new test `test_guess_direction_hint_consistency` made these specific enough.

- At least one test I ran:
  - `python -m pytest tests/test_game_logic.py` on the project root.
  - It confirmed correct tuple return values from `check_guess` for high/low cases and busted the reversed hint bug.

- AI in designing/understanding tests:
  AI suggested converting old single-value asserts (`result == "Win"`) to tuple checks (`outcome, message = ...`). That helped catch the exact bug and validate text in addition to outcome state.


