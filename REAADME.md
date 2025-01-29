# HNG12 Stage 0 - Public API

## Overview
This is a simple public API built using **FastAPI** for the **HNG12 Internship Stage 0 Task**. The API provides basic information in JSON format, including:
- Your registered email address.
- The current datetime in **ISO 8601** format (UTC).
- The GitHub repository URL of this project.

## Technologies Used
- **Programming Language**: Python
- **Framework**: FastAPI
- **Timezone Handling**: pytz
- **CORS Middleware**: fastapi.middleware.cors

## API Endpoints

### **GET /**
**Description**: Returns basic user information in JSON format.

#### **Response Format (200 OK)**
```json
{
  "email": "heyobims@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/heisobims/HNGINTENSHIP-FASTAPI"
}
```

## Getting Started

### **Prerequisites**
Ensure you have Python installed (recommended: Python 3.8+).

### **Installation & Setup**
1. **Clone the Repository**
```sh
git clone https://github.com/heisobims/HNGINTENSHIP-FASTAPI.git
cd HNGINTENSHIP-FASTAPI
```
2. **Create a Virtual Environment** (Optional but recommended)
```sh
python -m venv hngenv
source hngenv/bin/activate  # On macOS/Linux
hngenv\Scripts\activate    # On Windows
```
3. **Install Dependencies**
```sh
pip install fastapi uvicorn pytz
```

### **Running the API Locally**
Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### **Testing the API**
- Open your browser or use **Postman** to test the endpoint:
  ```
  GET http://127.0.0.1:8000/
  ```
- Or use **cURL**:
  ```sh
  curl http://127.0.0.1:8000/
  ```
- You can also access the **interactive API documentation** at:
  - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Deployment
To make the API publicly accessible, deploy it on any hosting platform that supports FastAPI, such as:
- **Render** ([render.com](https://render.com/))
- **Railway** ([railway.app](https://railway.app/))
- **Vercel** ([vercel.com](https://vercel.com/))
- **Heroku** ([heroku.com](https://www.heroku.com/))

## Contribution
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add new feature"`).
4. Push the changes (`git push origin feature-branch`).
5. Open a Pull Request.

## Useful Resources
- **FastAPI Documentation**: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- **Python Developers Hiring**: [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

## License
This project is licensed under the Apache 2.0.

---


