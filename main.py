import requests

# NASA API base URL
BASE_URL = "https://images-api.nasa.gov/search"

# Fetch data from NASA API
response = requests.get(BASE_URL, params={"q": "moon landing", "media_type": "image", "page_size": 10})
data = response.json()

# Extract items from response
items = data.get("collection", {}).get("items", [])

# Print first 10 results
for item in items[:10]:  
    print(f"\nTitle: {item['data'][0].get('title', 'N/A')}")
    print(f"NASA ID: {item['data'][0].get('nasa_id', 'N/A')}")
    print(f"Date Created: {item['data'][0].get('date_created', 'N/A')}")
    print(f"Media Type: {item['data'][0].get('media_type', 'N/A')}")
    print(f"URL: {item.get('links', [{}])[0].get('href', 'N/A')}")