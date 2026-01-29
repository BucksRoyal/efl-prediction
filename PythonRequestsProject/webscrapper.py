import requests


def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)  # fetch page with a 10-second timeout
        response.raise_for_status()  # raises HTTPError for bad status codes (e.g., 404, 500)
        print("\nPage fetched successfully! Here are the first 200 characters:\n")
        print(response.text[:200])
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching URL: {e}")
        print("Please check the URL or your internet connection.")


# Main program
if __name__ == "__main__":
    url = input("Enter a URL to fetch: ")
    fetch_url(url)
