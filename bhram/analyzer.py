
from urllib.parse import urlsplit


def analyze_url(url):
    url = url.strip()

    # Check if the input is empty
    if not url:
        return {
            "is_valid": False,
            "error": "Please enter a URL."
        }

    # Add https if the user doesn't provide a protocol
    if "://" not in url:
        url = "https://" + url

    # Check for spaces inside the URL
    if any(char.isspace() for char in url):
        return {
            "is_valid": False,
            "error": "URL cannot contain spaces."
        }

    try:
        parts = urlsplit(url)
        _ = parts.port

        if parts.scheme not in ["http", "https"]:
            return {
                "is_valid": False,
                "error": "Only HTTP and HTTPS are supported."
            }

        if not parts.hostname:
            return {
                "is_valid": False,
                "error": "URL must contain a hostname."
            }

        # Check if the hostname looks like a proper domain
        domain_parts = parts.hostname.split(".")

        if len(domain_parts) < 2 or any(not part for part in domain_parts):
            return {
                "is_valid": False,
                "error": "Please enter a valid domain name."
            }

        return {
            "is_valid": True,
            "url": url,
            "scheme": parts.scheme,
            "hostname": parts.hostname.lower(),
            "path": parts.path,
            "query": parts.query
        }

    except ValueError:
        return {
            "is_valid": False,
            "error": "Invalid URL format."
        }
