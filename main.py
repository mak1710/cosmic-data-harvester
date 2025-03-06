# main.py

from etl.extract import fetch_data
from etl.transform import transform_data
from etl.load import display_data, save_data  

def run_etl():
    print("Starting ETL process...")
    query = input("Explore NASA's intergalactic multimedia collections! (Search e.g. 'Mars Rover', 'Orion'): ")
    # Extract
    print("Extracting data...")
    raw_data = fetch_data(query=query, max_pages=20)  
    print(f"Total posts retrieved: {len(raw_data)}") 
    print("Data extraction successful.")

    # Transform
    print("Transforming data...")
    transformed_data = transform_data(raw_data)
    print("Data transformation successful.")

    # Load 
    print("Displaying data in terminal...")
    display_data(transformed_data)  

    # Save to CSV file (dynamic filename which can be parameterized in ETL workflows)
    filename = "nasa_data_extract.csv" 
    print(f"Saving data to CSV: {filename}...")
    save_data(transformed_data, filename) 

if __name__ == "__main__":
    run_etl()