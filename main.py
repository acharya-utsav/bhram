
from bhram.analyzer import analyze_url


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

    print("URL      :", result["url"])
    print("Protocol :", result["scheme"])
    print("Hostname :", result["hostname"])
    print("Path     :", result["path"])
    print("Query    :", result["query"])


if __name__ == "__main__":
    main()
