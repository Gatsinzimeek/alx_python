def multiple_returns(sentence):
    if len(sentence) == 0:
        return None
    else:
        letter = sentence[0]
        return len(sentence), letter