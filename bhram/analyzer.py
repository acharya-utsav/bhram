import ipaddress
from urllib.parse import urlsplit


def analyze_url(url):
    # Check the input
    if not isinstance(url, str):
        return {
            "is_valid": False,
            "error": "URL must be text."
        }

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

        hostname = parts.hostname.lower()

          # Check whether the hostname is an IP address
        try:
            ipaddress.ip_address(hostname)
            is_ip = True
        except ValueError:
            is_ip = False

        # Check domain format only if it is not an IP address
        if not is_ip:
            domain_parts = hostname.split(".")

            if len(domain_parts) < 2 or any(not part for part in domain_parts):
                return {
                    "is_valid": False,
                    "error": "Please enter a valid domain name."
                }

            # Check for invalid numeric IP addresses
            if all(part.isdigit() for part in domain_parts):
                return {
                    "is_valid": False,
                    "error": "Please enter a valid domain name."
                }

            # Check domain length
            if len(hostname) > 253:
                return {
                    "is_valid": False,
                    "error": "Domain name is too long."
                }

            # Check each domain label
            for part in domain_parts:
                if len(part) > 63:
                    return {
                        "is_valid": False,
                        "error": "Domain label is too long."
                    }

                if (
                    not part.isascii()
                    or not all(char.isalnum() or char == "-" for char in part)
                    or part.startswith("-")
                    or part.endswith("-")
                ):
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
