def calculate_risk(warnings):
    score = 0

    # Points for each detected warning
    risk_points = {
        "The URL uses an IP address instead of a domain name.": 40,
        "The URL contains an @ symbol in its address.": 25,
        "The URL contains an unusually large number of domain parts.": 20,
        "The URL is unusually long.": 10,
        "The URL contains suspicious keywords often used in phishing attempts.": 10,
        "URL uses HTTP instead of HTTPS.": 10,
    }

    for warning in warnings:
        score += risk_points.get(warning, 0)

    # Keep the score within 0 to 100
    score = min(score, 100)

    if score >= 70:
        level = "High"
    elif score >= 30:
        level = "Medium"
    else:
        level = "Low"

    return {
        "score": score,
        "level": level
    }
