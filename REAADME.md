# HNG12 Stage 0 FASTAPI

## Description
A public API that returns:
- Registered email
- The current datetime (UTC, ISO 8601 format)
- GitHub URL of this repository

## Endpoint
`GET /userinfo`

### Sample Response:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
