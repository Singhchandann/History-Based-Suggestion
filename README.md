# History-Based-Suggestion
MongoDB-Powered History Based Autocomplete System with Gradio: A real-time autocomplete suggestion system using Trie data structure and MongoDB. This project integrates Gradio for the interface, and MongoDB for dynamic data updates, making it suitable for autocompleting search queries with added spelling correction.

## Project Folder Structure

📁 gradio-mongodb-autocomplete/  
├── 📁 src/  
│   ├── app.py               # Main script for running Gradio and MongoDB integration  
│   ├── trie.py              # Trie and spelling correction logic  
│   ├── db.py                # MongoDB connection and update logic  
├── 📄 requirements.txt       # Python dependencies  
├── 📄 README.md              # Project description  and instructions  
└── 📄 .gitignore             # Files to be ignored by Git


# MongoDB-Powered Autocomplete with Gradio

This project demonstrates an autocomplete system using MongoDB, Gradio, and a Trie data structure to provide fast search and spelling corrections.

## Features

- **Real-time Search:** Trie structure allows for fast search suggestions.
- **Spelling Correction:** Uses fuzzy matching to suggest corrections based on user input.
- **MongoDB Integration:** Dynamically updates the search data from MongoDB in the background.

## Prerequisites

- Python 3.x
- MongoDB instance

## Setup and Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/gradio-mongodb-autocomplete.git
    ```

2. Navigate to the project directory:

    ```bash
    cd gradio-mongodb-autocomplete
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Update the MongoDB connection string in `db.py`:

    ```python
    client = pymongo.MongoClient("mongodb://<your_mongodb_url>")
    ```

## Running the App

To launch the Gradio app:

```bash
python src/app.py
