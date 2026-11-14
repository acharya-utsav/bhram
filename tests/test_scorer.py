from bhram.scorer import calculate_risk


def test_no_warnings():
    result = calculate_risk([])

    assert result["score"] == 0
    assert result["level"] == "Low"


def test_low_risk():
    warnings = [
        "URL uses HTTP instead of HTTPS."
    ]

    result = calculate_risk(warnings)

    assert result["score"] == 10
    assert result["level"] == "Low"


def test_medium_risk():
    warnings = [
        "The domain may be impersonating a trusted website."
    ]

    result = calculate_risk(warnings)

    assert result["score"] == 30
    assert result["level"] == "Medium"


def test_high_risk():
    warnings = [
        "The URL uses an IP address instead of a domain name.",
        "The domain may be impersonating a trusted website."
    ]

    result = calculate_risk(warnings)

    assert result["score"] == 70
    assert result["level"] == "High"


def test_score_cannot_exceed_100():
    warnings = [
        "The URL uses an IP address instead of a domain name.",
        "The domain may be impersonating a trusted website.",
        "The URL contains an @ symbol in its address.",
        "The URL contains an unusually large number of domain parts.",
        "The URL is unusually long.",
        "The URL contains suspicious keywords often used in phishing attempts.",
        "URL uses HTTP instead of HTTPS."
    ]

    result = calculate_risk(warnings)

    assert result["score"] == 100
    assert result["level"] == "High"


def test_duplicate_warnings_count_once():
    warning = "The domain may be impersonating a trusted website."

    result = calculate_risk([warning, warning])

    assert result["score"] == 30
    assert result["level"] == "Medium"


def test_low_risk_upper_boundary():
    warnings = [
        "The URL contains an @ symbol in its address."
    ]

    result = calculate_risk(warnings)

    assert result["score"] == 25
    assert result["level"] == "Low"


def test_medium_risk_upper_boundary():
    warnings = [
        "The URL uses an IP address instead of a domain name.",
        "The URL contains an @ symbol in its address."
    ]

    result = calculate_risk(warnings)

    assert result["score"] == 65
    assert result["level"] == "Medium"
