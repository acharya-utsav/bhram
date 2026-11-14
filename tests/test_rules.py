from bhram.rules import (
    check_url_structure,
    check_suspicious_keywords,
    check_https,
    check_lookalike_domain
)


def test_ip_address_detection():
    url_info = {
        "url": "https://192.0.2.10",
        "hostname": "192.0.2.10"
    }

    warnings = check_url_structure(url_info)

    assert "The URL uses an IP address instead of a domain name." in warnings


def test_excessive_domain_parts():
    url_info = {
        "url": "https://a.b.c.d.e.com",
        "hostname": "a.b.c.d.e.com"
    }

    warnings = check_url_structure(url_info)

    assert "The URL contains an unusually large number of domain parts." in warnings


def test_at_symbol_detection():
    url_info = {
        "url": "https://user@example.com",
        "hostname": "example.com"
    }

    warnings = check_url_structure(url_info)

    assert "The URL contains an @ symbol in its address." in warnings


def test_long_url_detection():
    url_info = {
        "url": "https://example.com/" + "a" * 90,
        "hostname": "example.com"
    }

    warnings = check_url_structure(url_info)

    assert "The URL is unusually long." in warnings


def test_suspicious_keyword_detection():
    url_info = {
        "url": "https://example.com/login",
        "hostname": "example.com"
    }

    warnings = check_suspicious_keywords(url_info)

    assert "The URL contains suspicious keywords often used in phishing attempts." in warnings


def test_https_detection():
    url_data = {
        "is_valid": True,
        "scheme": "https"
    }

    result = check_https(url_data)

    assert result["flagged"] is False


def test_http_detection():
    url_data = {
        "is_valid": True,
        "scheme": "http"
    }

    result = check_https(url_data)

    assert result["flagged"] is True
    assert result["message"] == "URL uses HTTP instead of HTTPS."


def test_invalid_url_https_check():
    url_data = {
        "is_valid": False
    }

    result = check_https(url_data)

    assert result["flagged"] is False
    assert result["message"] == "Cannot check an invalid URL."


def test_trusted_domain_detection():
    url_data = {
        "is_valid": True,
        "hostname": "esewa.com.np"
    }

    warnings = check_lookalike_domain(url_data)

    assert warnings == []


def test_lookalike_domain_detection():
    url_data = {
        "is_valid": True,
        "hostname": "esewaa.com.np"
    }

    warnings = check_lookalike_domain(url_data)

    assert "The domain may be impersonating a trusted website." in warnings
