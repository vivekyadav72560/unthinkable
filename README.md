# E-commerce Product Recommender with LLM Explanations

This project demonstrates a product recommendation system for an e-commerce platform. It combines a collaborative filtering algorithm to generate recommendations with a Large Language Model (LLM) to provide user-friendly explanations for why a product is suggested.

## Features

- **Backend API**: A Flask-based REST API to serve product recommendations.
- **Collaborative Filtering**: Uses Scikit-learn's Truncated SVD to find products liked by similar users.
- **LLM-Powered Explanations**: Integrates with Google's Gemini API to generate personalized, human-readable explanations for each recommendation.
- **Simple Database**: Uses SQLAlchemy and SQLite for managing product and user interaction data.
- **Frontend Dashboard**: A basic HTML/CSS/JS interface to interact with the API and view recommendations.

## Project Structure

```
/e-commerce-recommender
|-- /backend        # Contains the Flask API and all backend logic
|-- /frontend       # Simple HTML/CSS/JS for demonstration
|-- /data           # Script to seed the database
|-- requirements.txt  # Python dependencies
|-- README.md         # Project documentation
```

## Technical Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy
- **Recommendation Logic**: Pandas, Scikit-learn
- **LLM Integration**: `google-generativeai` (Gemini API)
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Setup and Installation

### 1. Prerequisites

- Python 3.8+
- An API key for the Google Gemini API.

### 2. Clone the Repository

```bash
git clone <your-repo-url>
cd e-commerce-recommender
```

### 3. Set Up a Virtual Environment

```bash
# For Windows
python -m venv venv
.\venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

You must set your Google Gemini API key as an environment variable.

```bash
# For Windows (Command Prompt)
set GOOGLE_API_KEY="YOUR_API_KEY"

# For macOS/Linux
export GOOGLE_API_KEY="YOUR_API_KEY"
```

### 6. Initialize the Database

Run the seeding script to create and populate the database with sample data.

```bash
cd data
python seed_data.py
```

After running, a `database.db` file will be created in the root folder. **Move this `database.db` file into the `/backend` directory.**

## How to Run

### 1. Start the Backend Server

Navigate to the `backend` directory and run the `run.py` script.

```bash
cd backend
python run.py
```

The Flask server will start, typically on `http://127.0.0.1:5000`.

### 2. Launch the Frontend

Open the `frontend/index.html` file in your web browser. You can usually do this by double-clicking the file.

### 3. Use the Application

- Enter a User ID (e.g., 1, 2, 3) into the input field.
- Click the "Get Recommendations" button.
- The dashboard will display recommended products along with an AI-generated explanation for each.

## API Endpoint

- **Endpoint**: `/recommendations`
- **Method**: `GET`
- **Query Parameter**: `user_id` (integer, required)
- **Success Response (200 OK)**:
  ```json
  {
    "user_id": 1,
    "recommendations": [
      {
        "product": {
          "id": 2,
          "name": "StellarSound Headphones",
          "category": "Electronics",
          "description": "..."
        },
        "explanation": "Since you've shown interest in electronics like the QuantumCore Laptop, you might also enjoy these high-quality StellarSound Headphones."
      }
    ]
  }
  ```
- **Error Response (400 Bad Request)**:
  ```json
  {
    "error": "user_id parameter is required"
  }
  ```
