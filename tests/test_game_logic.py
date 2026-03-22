from logic_utils import check_guess, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_check_guess_with_int_secret():
    # Regression test: secret must remain an int, not converted to string
    # This bug caused TypeError: '>' not supported between 'int' and 'str'
    # on even-numbered attempts
    secret = 47
    result = check_guess(1, secret)
    assert result == "Too Low"
    
    result = check_guess(100, secret)
    assert result == "Too High"
    
    result = check_guess(47, secret)
    assert result == "Win"

def test_parse_guess_valid_inputs():
    # Regression test: parse_guess should handle valid integer inputs
    ok, value, error = parse_guess("42")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_guess_float_inputs():
    # Regression test: parse_guess should coerce floats to integers
    ok, value, error = parse_guess("42.5")
    assert ok is True
    assert value == 42
    assert error is None

def test_parse_guess_invalid_inputs():
    # Regression test: parse_guess should reject non-numeric inputs
    ok, value, error = parse_guess("abc")
    assert ok is False
    assert value is None
    assert error == "That is not a number."

def test_parse_guess_empty_input():
    # Regression test: parse_guess should reject empty strings
    ok, value, error = parse_guess("")
    assert ok is False
    assert value is None
    assert error == "Enter a guess."

def test_parse_guess_none_input():
    # Regression test: parse_guess should reject None
    ok, value, error = parse_guess(None)
    assert ok is False
    assert value is None
    assert error == "Enter a guess."

def test_get_range_for_difficulty_easy():
    # Regression test: Easy difficulty should return (1, 20)
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_get_range_for_difficulty_normal():
    # Regression test: Normal difficulty should return (1, 100)
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_get_range_for_difficulty_hard():
    # Regression test: Hard difficulty should return (1, 50)
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50

