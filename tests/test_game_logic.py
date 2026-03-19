from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, classification should be Too High
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    # If secret is 50 and guess is 40, classification should be Too Low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_guess_direction_hint_consistency():
    # Regression test for the bug where too-high and too-low hints were reversed
    high_outcome, high_message = check_guess(80, 50)
    low_outcome, low_message = check_guess(20, 50)

    assert high_outcome == "Too High"
    assert high_message == "📉 Go LOWER!"

    assert low_outcome == "Too Low"
    assert low_message == "📈 Go HIGHER!"
