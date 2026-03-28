def grade_classification(pred, actual):
    if pred == actual:
        return 1.0
    elif pred in actual:
        return 0.5
    return 0.0

def grade_extraction(pred, actual):
    return 1.0 if any(word in pred for word in actual.split()) else 0.3

def grade_priority(pred, actual):
    return 1.0 if pred == actual else -0.5