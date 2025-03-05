import requests
import pandas as pd
from tqdm import tqdm

# NASA API base URL
BASE_URL = "https://images-api.nasa.gov/search"


def transform_data(data):
    """Transform raw NASA API data into a structured format."""
    records = []
    
    for item in tqdm(data, desc="Transforming Data"):
        record = {
            "Title": item["data"][0].get("title", "N/A"),
            "NASA ID": item["data"][0].get("nasa_id", "N/A"),
            "Date Created": item["data"][0].get("date_created", "N/A"),
            "Media Type": item["data"][0].get("media_type", "N/A"),
            "Description": item["data"][0].get("description", "N/A"),
            "Keywords": ", ".join(item["data"][0].get("keywords", ["N/A"])),
            "Center": item["data"][0].get("center", "N/A"),
            "Secondary Creator": item["data"][0].get("secondary_creator", "N/A"),
            "Location": item["data"][0].get("location", "N/A"),
            "Original URL": next((link.get("href") for link in item.get("links", []) if link.get("render") == "image"), "N/A"),
        }
        records.append(record)
    
    return pd.DataFrame(records)

query = input("Explore NASA's intergalactic multimedia collections! (Search for e.g. 'Mars Rover', 'Orion'): ")
# Fetch data from NASA API
response = requests.get(BASE_URL, params={"q": query, "media_type": "image", "page_size": 10})
data = response.json()

# Extract items from response
items = data.get("collection", {}).get("items", [])

df = transform_data(items)

# Display transformed data present in DataFrame
print(f"\nNASA Image Data - '{query}'\n")
print(df.head())  