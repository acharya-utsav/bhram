
import ipaddress
from urllib.parse import urlsplit


def check_url_structure(url_info):
    warnings = []

    url = url_info["url"]
    hostname = url_info["hostname"]

    parts = urlsplit(url)

    # Check if the hostname is an IP address
    try:
        ipaddress.ip_address(hostname)

        warnings.append(
            "The URL uses an IP address instead of a domain name."
        )

    except ValueError:
        # Check for too many domain parts
        domain_parts = hostname.split(".")

        if len(domain_parts) > 4:
            warnings.append(
                "The URL contains an unusually large number of domain parts."
            )

    # Check for @ symbol in the address
    if "@" in parts.netloc:
        warnings.append(
            "The URL contains an @ symbol in its address."
        )

    # Check if the URL is unusually long
    if len(url) > 100:
        warnings.append(
            "The URL is unusually long."
        )

    return warnings

def check_suspicious_keywords(url_info):
    warnings = []

    url = url_info["url"].lower()

    suspicious_keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "bonus"
    ]

    for keyword in suspicious_keywords:
        if keyword in url:
            warnings.append(
                "The URL contains suspicious keywords often used in phishing attempts."
            )
            break

    return warnings


def check_https(url_data):
    # Check whether the URL is valid
    if not url_data.get("is_valid"):
        return {
            "rule": "HTTPS Check",
            "flagged": False,
            "message": "Cannot check an invalid URL."
        }

    # Check the URL protocol
    if url_data["scheme"] == "http":
        return {
            "rule": "HTTPS Check",
            "flagged": True,
            "message": "URL uses HTTP instead of HTTPS."
        }

    return {
        "rule": "HTTPS Check",
        "flagged": False,
        "message": "URL uses HTTPS. This does not guarantee legitimacy."
    }
