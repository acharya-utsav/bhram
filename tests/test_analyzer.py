from bhram.analyzer import analyze_url


def test_empty_url():
    result = analyze_url("")

    assert result["is_valid"] is False


def test_url_without_protocol():
    result = analyze_url("example.com")

    assert result["is_valid"] is True
    assert result["scheme"] == "https"
    assert result["hostname"] == "example.com"


def test_https_url():
    result = analyze_url("https://example.com")

    assert result["is_valid"] is True
    assert result["scheme"] == "https"


def test_http_url():
    result = analyze_url("http://example.com")

    assert result["is_valid"] is True
    assert result["scheme"] == "http"


def test_ip_address_url():
    result = analyze_url("http://192.168.1.1")

    assert result["is_valid"] is True
    assert result["hostname"] == "192.168.1.1"


def test_invalid_port():
    result = analyze_url("https://example.com:99999")

    assert result["is_valid"] is False


def test_unsupported_protocol():
    result = analyze_url("ftp://example.com")

    assert result["is_valid"] is False


def test_url_with_path_and_query():
    result = analyze_url("https://example.com/login?user=test")

    assert result["is_valid"] is True
    assert result["path"] == "/login"
    assert result["query"] == "user=test"

def test_url_with_whitespace():
    result = analyze_url("https://example .com")

    assert result["is_valid"] is False


def test_url_with_empty_hostname():
    result = analyze_url("https://")

    assert result["is_valid"] is False


def test_url_with_multiple_subdomains():
    result = analyze_url("https://login.accounts.example.com")

    assert result["is_valid"] is True
    assert result["hostname"] == "login.accounts.example.com"


def test_ipv6_address_url():
    result = analyze_url("http://[2001:db8::1]")

    assert result["is_valid"] is True
    assert result["hostname"] == "2001:db8::1"