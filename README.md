# FastAPI CRUD Operations Example

This repository demonstrates how to implement **CRUD (Create, Read, Update, Delete)** operations using **FastAPI**. The app performs basic operations on a fake in-memory database using a Python dictionary.

## Features
- **GET**: Retrieve an item by its unique `item_id`.
- **POST**: Create a new item and assign it a unique ID.
- **PUT**: Update an existing item based on its `item_id`.
- **DELETE**: Delete an item by its `item_id`.

## Requirements
- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the application)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/abubinfahd/FastAPI-.git
   ```
2. Install the required dependencies
  ```bash
  pip install fastapi uvicorn
  ```
3. Running the Application
**To run the FastAPI application, use the following command:**
  ```bash
  uvicorn main:app --reload
  ```
## Testing the API
You can test the API directly using Swagger UI:
Open `http://127.0.0.1:8000/docs in your browser.`
FastAPI automatically generates an interactive documentation where you can test the above endpoints directly.
