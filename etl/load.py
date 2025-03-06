# etl/load.py

from rich.table import Table
from rich.console import Console
import pandas as pd 

console = Console()

def display_data(dataframe, limit=100, max_column_width=30):  
    """Display transformed data in a table format"""
    
    # Create a table based on columns in the dataframe
    table = Table(title="Extracted from NASA's Image Library")

    # Add table columns based on the DataFrame columns
    for column in dataframe.columns:
        table.add_column(column, style="cyan", no_wrap=False, max_width=max_column_width)

    # Add data rows
    for _, row in dataframe.head(limit).iterrows():
        table.add_row(*[str(value)[:50] if isinstance(value, str) and len(str(value)) > 50 else str(value) for value in row])

    console.print(table)

def save_data(dataframe, filename): 
    """Save the transformed data to a CSV file"""
    try:
        # Save DataFrame to CSV
        dataframe.to_csv(filename, index=False)
        print(f"✅ Data successfully saved to {filename}")
    except Exception as e:
        print(f"❌ Failed to save data to CSV: {e}")
