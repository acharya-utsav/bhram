from main import main


def test_trusted_url_low_risk(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "https://esewa.com.np"
    )

    main()

    output = capsys.readouterr().out

    assert "Risk Score : 0/100" in output
    assert "Risk Level : Low" in output


def test_lookalike_url_medium_risk(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "https://esewaa.com.np"
    )

    main()

    output = capsys.readouterr().out

    assert "impersonating a trusted website" in output
    assert "Risk Score : 30/100" in output
    assert "Risk Level : Medium" in output


def test_invalid_url(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "not a url"
    )

    main()

    output = capsys.readouterr().out

    assert "Invalid URL:" in output
    assert "Risk Assessment" not in output


def test_http_url_low_risk(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "http://esewa.com.np"
    )

    main()

    output = capsys.readouterr().out

    assert "URL uses HTTP instead of HTTPS." in output
    assert "Risk Score : 10/100" in output
    assert "Risk Level : Low" in output