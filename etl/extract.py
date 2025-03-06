# etl/extract.py

import requests
import logging
from tenacity import retry, stop_after_attempt, wait_exponential
from config import BASE_URL

# Configure logging
logging.basicConfig(level=logging.INFO)

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=2, min=1, max=10))
def fetch_data(query, media_type="image", max_pages=20):
    """Fetch data from NASA API with retry mechanism and pagination"""
    all_data = []  # To store data from multiple pages
    page = 1

    while page <= max_pages:
        url = f"{BASE_URL}/search"  # BASE_URL from config file can be parameterized as pipeline parameter
        params = {
            "q": query,
            "media_type": media_type,
            "page": page
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()
            
            # Extract number of posts retrieved for this page
            page_total = len(data.get("collection", {}).get("items", []))
            logging.info(f"✅ Total posts retrieved (page {page}): {page_total}")
            
            # Append the current page's data
            all_data.extend(data.get("collection", {}).get("items", []))
            
            # Check if there are more pages to fetch
            if page_total == 0:
                logging.info(f"🚨 No more data available after page {page}.")
                break  # Stop if no data is being returned from this page

            page += 1  # Iterate to next page

        except requests.exceptions.RequestException as e:
            logging.error(f"❌ API request failed: {e}")
            raise

    # Log the total number of posts across all pages
    logging.info(f"✅ Total posts retrieved: {len(all_data)}")
    return all_data
