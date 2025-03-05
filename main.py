import requests

# NASA API base URL
BASE_URL = "https://images-api.nasa.gov/search"

query = input("Explore the wonders of space! What would you like to search for? (e.g., 'Mars Rover', 'Apollo 11', 'black holes'): ")
# Fetch data from NASA API
response = requests.get(BASE_URL, params={"q": query, "media_type": "image", "page_size": 10})
data = response.json()

# Extract items from response
items = data.get("collection", {}).get("items", [])

# Print first 10 results
if not items:
    print("\n❌ No results found. Try a different search term!")
else:
    print(f"\n✅ Showing results for: '{query}'\n")

    for item in items[:10]:  
        metadata = item["data"][0]
        
        print("\nTitle:", metadata.get("title", "N/A"))
        print("NASA ID:", metadata.get("nasa_id", "N/A"))
        print("Date Created:", metadata.get("date_created", "N/A"))
        print("Media Type:", metadata.get("media_type", "N/A"))
        print("Description:", metadata.get("description", "N/A"))
        print("Keywords:", ", ".join(metadata.get("keywords", ["N/A"])))
        print("Center:", metadata.get("center", "N/A"))
        print("Secondary Creator:", metadata.get("secondary_creator", "N/A"))
        print("Location:", metadata.get("location", "N/A"))
        print("Original URL:", next((link.get("href") for link in item.get("links", []) if link.get("render") == "image"), "N/A"))