# Cosmic Data Harvester

## 🚀 Overview

Cosmic Data Harvester is an ETL (Extract, Transform, Load) workflow that retrieves image metadata from NASA's public API, structures it into a well-formatted dataset, and presents it in a readable format on the terminal while also saving it as a CSV file. 

## 🌟 Features

- 🔍 Extract: Scrapes images and metadata from NASA's Image API based on a user-provided search query - can be parameterized in data pipelines.

- 🔄 Transform: Simply cleans and structures the retrieved data into a Pandas DataFrame.

- 📊 Load: Displays the processed data in a readable tabular format in the terminal and saves it to a CSV file for further analysis.

- ⏳ Progress Tracking: Uses tqdm to show real-time data transformation progress.

## 📂 Project Structure

```cosmic-data-harvester/
│── etl/
│   ├── extract.py   # Handles data extraction from NASA API
│   ├── transform.py # Processes and structures the extracted data
│   ├── load.py      # Displays data in the terminal and saves it as a CSV file
│── main.py          # Orchestrates the ETL pipeline
│── requirements.txt # List of dependencies
│── README.md        # Project documentation
```

## 🛠️ Dependencies

Ensure you have Python 3.x installed, then install the required packages using:

```pip install -r requirements.txt```

## 🔧 Installation & Usage

### 1. Clone the repository:
```
git clone https://github.com/mak1710/cosmic-data-harvester.git
cd cosmic-data-harvester
```
### 2. Install dependencies:
```
pip install -r requirements.txt
```
### 3. Run the ETL pipeline:
```
python main.py
```
### 4. Enter a search term when prompted (e.g., moon landing) to fetch related NASA images.

### 5. View and analyze the output displayed in the terminal and check the saved CSV file.

## 🏗️ ETL Process Flow

```
    A[User Input: Search Query] -->|Extract| B[Fetch Data from NASA API];
    B -->|Transform| C[Clean & Structure Data in DataFrame];
    C -->|Load| D[Display in Terminal];
    C -->|Save| E[Export to CSV];
```
## 🔥 Why This Project Matters

- Provides structured access to NASA’s vast media repository.

- Demonstrates a real-world ETL workflow with API integration.

- Allows users to efficiently retrieve, process and analyze image metadata.

## 📌 Future Enhancements

- ✨ Extracting other multimedia files that can be extracted efficiently through dynamic parameters (as relative URL). 

- 🛢️ Loading data into a preferred data warehouse for better analytics.

- 📊 Add visualization support for metadata analysis.

- 🚀 Expand API integration beyond NASA (e.g., ESA, SpaceX, etc.).

## 🤝 Contributions

Feel free to fork the repository and submit pull requests! Suggestions, issues and enhancements are always welcome.
