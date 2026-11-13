from bhram.analyzer import analyze_url
from bhram.rules import check_url_structure

def main():
    print("=" * 40)
    print("              BHRAM")
    print("   Know the link before you trust it.")
    print("=" * 40)

    url = input("\nEnter a URL: ")

    result = analyze_url(url)

    if not result["is_valid"]:
        print("\nInvalid URL:", result["error"])
        return

    print("\nURL Analysis Result")
    print("-" * 40)
    print("Protocol :", result["scheme"])
    print("Hostname :", result["hostname"])

    warnings = check_url_structure(result)

    print("\nSecurity Checks")
    print("-" * 40)

    if warnings:
        for warning in warnings:
            print("[!]", warning)
    else:
        print("No suspicious URL structures found.")

    print("\nAnalysis completed.")

if __name__ == "__main__":
    main()
