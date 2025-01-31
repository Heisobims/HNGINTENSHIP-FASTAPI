# Stage 0 Backend - Public API to Retrieve Basic Information

## Overview

This project involves developing a public API that returns basic information in JSON format. The API provides the following details:
- Your registered email address (used to register on the HNG12 Slack workspace).
- The current datetime in ISO 8601 format (UTC).
- The GitHub URL of the project's codebase.

The API is built using Python with the FastAPI framework and deployed to a publicly accessible endpoint. It is designed to be simple, fast, and accessible, with a response time of less than 500ms.

---

## Technology Stack

- Programming Language/Framework: Python (FastAPI)
- Deployment Platform: [Render](https://render.com) (or any other platform of your choice)
- CORS Handling: The API is configured to handle Cross-Origin Resource Sharing (CORS) appropriately using FastAPI's built-in CORS middleware.

---

## API Specification

### Endpoint
- Method: `GET`
- URL: `https://hngintenship-fastapi.onrender.com`

### Response Format (200 OK)
The API returns a JSON response with the following structure:
```json
{
  "email": "Heisobims@gmail.com",
  "current_datetime": "2025-01-30T21:04:35Z",
  "github_url": "https://github.com/heisobims/HNGINTENSHIP-FASTAPI"
}
```

### Example Usage
1. Make a `GET` request to the API endpoint:
   ```bash
   curl -X GET https://hngintenship-fastapi.onrender.com
   ```
2. Sample Response:
   ```json
   {
     "email": "Heisobims@gmail.com",
     "current_datetime": "2025-01-30T21:04:35Z",
     "github_url": "https://github.com/heisobims/HNGINTENSHIP-FASTAPI"
   }
   ```

---

## Setup Instructions

### Prerequisites
- Ensure you have the following installed:
  - Python 3.7 or higher
  - Pip (Python package manager)
  - Git for version control

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/heisobims/HNGINTENSHIP-FASTAPI.git
   cd HNGINTENSHIP-FASTAPI
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
4. Access the API at `http://localhost:8000`.

---

## Deployment

The API is deployed to Render. Below are the steps to deploy to Render:

# Steps to Deploy on Render
1. Create a new Web Service on Render.
2. Connect your GitHub repository (`https://github.com/heisobims/HNGINTENSHIP-FASTAPI`).
3. Specify the following settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn mainFastApi:app --host 0.0.0.0 --port 8000`
4. Deploy the application.
5. Access the API at the provided Render URL (e.g., `https://hngintenship-fastapi.onrender.com`).

---

## Documentation

### API Documentation
- Endpoint: `GET https://hngintenship-fastapi.onrender.com`
- Response Format:
  ```json
  {
    "email": "Heisobims@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/heisobims/HNGINTENSHIP-FASTAPI"
  }
  ```

### Backlink

- For more information about hiring Python developers, visit:
  - https://hng.tech/hire/python-developers

---

## Testing

Before submission, ensure the API is thoroughly tested:
1. Verify the response format and status codes.
2. Test the API's response time (should be < 500ms).
3. Ensure CORS is handled correctly.

---

## Repository Information
- GitHub Repository: https://github.com/heisobims/HNGINTENSHIP-FASTAPI
- **Visibility**: Public

---

## Contact
For any questions or issues, please contact:
- **Name**: Heisobims
- **Email**: Heisobims@gmail.com
- **Slack**: Heisobims


This Project is Licensed by Apache 2.0
