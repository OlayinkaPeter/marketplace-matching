# Freelance Marketplace Matching

This repository contains a FastAPI application that implements a matching algorithm to connect 
employers / buyers with freelancers based on predefined criteria. The criteria considered are skills, 
location, and experience, with specific weights assigned to each. This project aims to simplify 
the freelance hiring process, provide fair opportunities for freelancers, and ensure a 
seamless user experience.

![image](https://github.com/OlayinkaPeter/marketplace-matching/blob/main/src/screenshot_.png)

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/freelance-marketplace.git
   cd freelance-marketplace

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt

4. Running the Application
Start the FastAPI server using Uvicorn:

    ```bash
    uvicorn main:app --reload
The application will be accessible at http://127.0.0.1:8000.



# API Endpoints
## `POST /match`
This endpoint accepts a MatchRequest payload and returns a sorted list of freelancers based on the match scores.

### Request Example:

    {
      "buyer": {
        "id": 4,
        "skills": ["python"],
        "location": "NY",
        "experience": 4
      },
      "freelancers": [
        {"id": 1, "skills": ["python", "fastapi"], "location": "NY", "experience": 5},
        {"id": 2, "skills": ["java", "spring"], "location": "SF", "experience": 3},
        {"id": 3, "skills": ["python", "flask"], "location": "NY", "experience": 2}
      ]
    }


### Response Example:

    {
      "matches": [
        {"id": 1, "skills": ["python", "fastapi"], "location": "NY", "experience": 5, "match_score": 0.96},
        {"id": 3, "skills": ["python", "flask"], "location": "NY", "experience": 2, "match_score": 0.76},
        {"id": 2, "skills": ["java", "spring"], "location": "SF", "experience": 3, "match_score": 0.1}
      ]
    }


## `GET /test_match`

This endpoint provides a test endpoint to verify the matching logic with example data.


# Contributing
We welcome contributions! Please follow these steps to contribute:

* Fork the repository.
* Create a new branch (git checkout -b feature-branch).
* Make your changes and commit them (git commit -am 'Add new feature').
* Push to the branch (git push origin feature-branch).
* Create a new Pull Request.
