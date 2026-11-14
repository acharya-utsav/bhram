# Bhram

**Know the link before you trust it.**

Bhram is a Python-based phishing website detection system designed to identify suspicious URLs and potential website impersonation.

Focused on Nepal's banking institutions, mobile wallets and digital payment platforms, and telecom providers, Bhram analyzes URLs using rule-based detection techniques and provides risk scores with explanations of suspicious indicators.

## Key Features

- URL analysis and validation
- IP address and suspicious URL structure detection
- HTTP and HTTPS checks
- Suspicious keyword identification
- Lookalike domain detection
- Nepal-focused trusted-domain database
- Explainable risk assessment

## Technologies

- Python
- JSON
- pytest

## Installation

Clone the repository:

    git clone https://github.com/acharya-utsav/bhram.git
    cd bhram

Create and activate a virtual environment:

    python -m venv .venv

Windows PowerShell:

    .venv\Scripts\Activate.ps1

Install development dependencies:

    pip install -r requirements-dev.txt

## Usage

Run Bhram:

    python main.py

Enter a URL when prompted to receive its analysis and risk assessment.

## Risk Levels

| Score | Risk Level |
|---|---|
| 0-29 | Low |
| 30-69 | Medium |
| 70-100 | High |

Risk scores are based on detection rules and their assigned weights.

## Running Tests

    python -m pytest -v

## Project Status

Under Development - Phase 1: Core Detection Engine.

## Limitations

- Detection is based on predefined rules and trusted-domain data.
- A low risk score does not guarantee that a website is safe.
- A high risk score does not prove that a website is malicious.
- Bhram analyzes URL information; it does not verify the live website.

## Disclaimer

Bhram is an educational cybersecurity and security-awareness project. Always verify website addresses through official sources before entering sensitive information.

## License

This project is licensed under the MIT License.