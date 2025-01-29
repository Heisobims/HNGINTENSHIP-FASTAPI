"""
This FastAPI application provides an endpoint that returns information including email, current datetime, and GitHub URL.
"""

from fastapi import FastAPI
from datetime import datetime
import pytz
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_info():
    """
    Returns information including email, current datetime, and GitHub URL.
    """
    response = {
        "email": "Heisobims@gmail.com",
        "current_datetime": datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "<https://github.com/heisobims/HNGINTENSHIP-FASTAPI>"
}
    return response