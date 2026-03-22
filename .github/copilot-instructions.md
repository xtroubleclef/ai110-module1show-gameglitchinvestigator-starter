# Copilot instructions for Game Glitch Investigator

## 🧠 Big picture
- Core app is a Streamlit number-guessing game in `app.py`.
- Game logic should be in `logic_utils.py` (functions: `get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`).
- `app.py` orchestrates UI + session state via `st.session_state` and currently includes intentional glitches.
- `tests/test_game_logic.py` is the unit test harness; it imports from `logic_utils.py`.

## 🔁 Execution workflow
- Setup: `pip install -r requirements.txt`
- Run app: `python -m streamlit run app.py`
- Tests: `pytest -q` (or `pytest tests/test_game_logic.py`)
- Debug path: use "Developer Debug Info" expander in UI to inspect `secret`, `attempts`, `score`, `history`.

## 🧩 What to fix first
- Move logic from `app.py` into `logic_utils.py` (as README challenges describe).
- `app.py` currently sets `secret` as `str` every other attempt to force wrong branches in `check_guess`; preserve secret as int in correct behavior.
- `parse_guess` supports floats by coercion and returns `(ok, value, error)`; tests depend on proper invalid-input string behaviour.

## ✅ Project patterns
- `session_state` keys used: `secret`, `attempts`, `score`, `status`, `history`.
- Difficulty mapping exists in `get_range_for_difficulty` and `attempt_limit_map`.
- `check_guess` should return one of `"Win"`, `"Too High"`, or `"Too Low"` (and optionally messages for UI hint).
- `update_score` uses attempt parity and clamps min points at 10 on win.

## ⚙️ Integration+
- No external service APIs; only dependencies are `streamlit` and `pytest` (plus any from `requirements.txt`).
- UI+logic tight coupling to avoid a second run: state changes call `st.rerun()` on new game.

## 📌 Notes for AI agents
- Avoid generic guidance; focus on the actual bug in the current branch (secret being string-multiplied, wrong compare hint inversion, parse gap where `0` should be invalid for range 1..N).
- Preserve existing behavior for the exercise: tests are minimal and only cover `check_guess(guess, secret)` outcomes.
