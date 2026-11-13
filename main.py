
from bhram.analyzer import analyze_url


def main():
    print("=" * 40)
    print("          BHRAM")
    print("  Know the link before you trust it.")
    print("=" * 40)

    url = input("\nEnter a URL to analyze: ")

    result = analyze_url(url)

    if not result["is_valid"]:
        print("\nInvalid URL:", result["error"])
        return

    print("\nURL successfully parsed!")
    print("-" * 40)
    print("Original URL :", result["original_url"])
    print("Normalized   :", result["normalized_url"])
    print("Scheme       :", result["scheme"])
    print("Hostname     :", result["hostname"])
    print("Path         :", result["path"])
    print("Query        :", result["query"])


if __name__ == "__main__":
    main()
