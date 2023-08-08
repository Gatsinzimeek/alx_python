def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_score = 0
    for key, score in a_dictionary.items():
        if score > highest_score:
            highest_score = score
            best_student = key
    return best_student
