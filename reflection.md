# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  "Go lower" hint given for guess "1" when only numbers 1-100 are allowed (instruction leads to invalid input). Expected "Go lower" to not be a response altogether for any "1" guesses (response is either "go higher" or correct guess).
  Because Secret number was 47, "go higher" hint was expected.
  "Go lower" given for "0" while being a number not applicable for this game. Expected a reponse that tells the user that 0 isn't a valid entry / the lowest number allowed is 1, and to choose a different number up to 100.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  GitHub Copilot Agent Mode

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Correct: fix logic for check_guess. AI suggested inverting the comparison logic: if `guess > secret`, return `"Too High"` (meaning guess is too high, go lower). This was verified by:
    1. Running pytest — all 12 tests passed, including `test_guess_too_high` validated with `check_guess(60, 50) == "Too High"`.
    2. Playing the game and evaluating if hints are now correct (e.g., guessing 75 when the correct answer is 50 correctly outputs "Too High").
    3. The original issue had inverted hints. AI's fix aligned with expected responses.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - Incorrect: Initial suggestion for check_guess return type. AI initially suggested returning a tuple `("Win", "🎉 Correct!")` instead of just the outcome string. This failed tests because `test_winning_guess` expected `check_guess(50, 50) == "Win"`, not a tuple. 
    - Verification: The test failure showed `AssertionError: assert ('Win', '🎉 Correct!') == 'Win'`.
    - Fix: Reading the test expectations, then having AI return only the outcome string and map messages in `app.py` instead. The tests passed after this correction.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Actually playing the game and checking responses align with my guesses.  pytest regression tests — if the tests pass, the logic works as expected. 
  
  For the bug in the guesses made with even numbers, TypeError would occur, so I tested odd guesses and confirmed they worked as expected, which pointed directly to the `if st.session_state.attempts % 2 == 0: secret = str(...)` line being re-evaluated

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - Pytest: Running `pytest tests/test_game_logic.py -v` all 12 tests passed, including `test_check_guess_with_int_secret`. This test specifically validated that `check_guess(1, 47)` returns `"Too Low"` and `check_guess(100, 47)` returns `"Too High"`, which means the type-safety issue was fixed. The test indicated that the function could now correctly evaluate an int guess to an int secret without returning a TypeError

  - Manual game test: I ran `python -m streamlit run app.py`, guessed a low number (e.g., 1) against secret 47, and verified the hint correctly said "Go HIGHER" — confirming the inverted logic was fixed.

- Did AI help you design or understand any tests? How?
  - AI helped best with designing tests: "generate a pytest case targeting the bug that had just been fixed." AI made `test_check_guess_with_int_secret()` for testing the scenario that kept failing with an int secret and verifying all three outcomes (Win, Too High, Too Low) work correctly. This helped me work on just the type-safety issue. 
  
  AI also expanded the test suite to cover `parse_guess` and `get_range_for_difficulty`, ensuring confidence in me that the entire refactoring was sound.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - The secret number converted into a string every other attempt with `if st.session_state.attempts % 2 == 0: secret = str(st.session_state.secret)`. The stored secret wouldn't change in its session state, but it did create a new local `secret` as a string, passed to `check_guess()`. 
  
Camparison  with `check_guess()` of an int guess to a str secret would have a TypeError or just output wrong results. The actual stored `st.session_state.secret` doesn't change, so only the comparison value switched between int and str, making the game behavior inconsistent

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Every time the user interacts with the app, Streamlit runs entire script from top to bottom (click button, enter text, etc.). This is a "rerun." Without session state, variables reset to their initial values for every rerun, making the game unplayable.
  
  Session state (`st.session_state`) is a dictionary that persists through reruns, remembering values after a guess is made (secret number, attempt count, and score), like "surviving" a reload or refresh

- What change did you make that finally gave the game a stable secret number?
  - To change the logic that was converting `secret` to a string for even attempts, pass `st.session_state.secret` directly to `check_guess()` as an int instead of `if st.session_state.attempts % 2 == 0: secret = str(...) else: secret = ...` This ensures TypeError is eliminated.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
 - Tests designed by AI had reasoning that were super straightforward to follow. I'm still in the process of building my test-writing skills, so AI is something I think is great for the speed and picking up the logic for it faster, but I'll be mindful of to use sparingly until the refactor -> test -> verify -> document structure is well-established on my end.
 
  Pytest certainly caught mistakes much faster than me doing some manual testing.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I'd have AI elaborate a bit more on the tests designed and suggested for functions. In this project, AI suggested what it suggested, I understood their logic, and I didn't think much further on the details until some tests failed. For next time, I'd immediately jump to validating the AI's solution against tests, like checking test expectations before implementation

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI-generated code is nice for incorporating into projects. I felt like it was great for its test writing and debugging potential, and overall collaboration power—didn't feel like it bogged me down at all. Overall, very efficient for the basic tests involved in this game.
