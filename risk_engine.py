def calculate_risk(features):

    score = 0

    if features["has_ip"]:
        score += 40

    if features["has_at"]:
        score += 30

    if features["url_length"] > 50:
        score += 15

    if features["dot_count"] > 3:
        score += 10

    if features["hyphen_count"] > 2:
        score += 10

    if features["digit_count"] > 5:
        score += 10

    if features["https"] == 0:
        score += 5

    return min(score, 100)