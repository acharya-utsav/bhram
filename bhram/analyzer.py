
from urllib.parse import urlsplit


def analyze_url(url):
    """
    Normalize and parse a URL.
    Returns basic URL information or an error.
    """

    original_url = url.strip()

    if not original_url:
        return {
            "is_valid": False,
            "error": "URL cannot be empty."
        }

    # Add HTTPS when the user does not provide a scheme.
    if "://" not in original_url:
        normalized_url = "https://" + original_url
    else:
        normalized_url = original_url

    # Reject whitespace inside the URL.
    if any(char.isspace() for char in normalized_url):
        return {
            "is_valid": False,
            "error": "URL must not contain spaces."
        }

    try:
        parsed = urlsplit(normalized_url)

        # Accessing .port also checks whether a supplied port is valid.
        _ = parsed.port

        if parsed.scheme not in ("http", "https"):
            return {
                "is_valid": False,
                "error": "Only HTTP and HTTPS URLs are supported."
            }

        if not parsed.hostname:
            return {
                "is_valid": False,
                "error": "URL must contain a valid hostname."
            }

        return {
            "is_valid": True,
            "original_url": original_url,
            "normalized_url": normalized_url,
            "scheme": parsed.scheme,
            "hostname": parsed.hostname.lower(),
            "path": parsed.path,
            "query": parsed.query
        }

    except ValueError:
        return {
            "is_valid": False,
            "error": "Invalid URL format."
        }
