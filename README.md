# IoT Simulator API

A REST API prototype developed during my **remote internship** at **KEP Labs (Keshava Elite Projects), Bhopal**  
to simulate IoT device behaviour — battery, LED, and switch circuit logic — without requiring physical hardware.

Built with **FastAPI** to enable rapid internal prototyping and team demonstration of circuit connection logic.

---

## Purpose

This prototype was built to satisfy an internal requirement at KEP Labs:  
demonstrate device-to-device terminal connectivity and circuit validation through a clean API interface,  
usable by the team without any hardware setup.

---

## Features

- Connect battery and LED terminals (positive/negative)
- Toggle switch state (ON / OFF)
- Validate whether a complete circuit is formed
- Get real-time LED and switch status
- Disconnect all connections with a single call
- Health check and root verification endpoints

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Framework | FastAPI |
| Validation | Pydantic v2 |
| Server | Uvicorn (with WebSocket support) |
| Architecture | Modular routers |

---

## Project Structure

```
KEP-Prototype/
├── main.py          # App entry point, router registration
├── models.py        # Pydantic request/response models
├── routers/
│   └── device.py    # All IoT device endpoints
├── requirements.txt
└── README.md
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Verify API is running |
| GET | `/health` | Health check |
| GET | `/api/status` | Get LED and switch status |
| POST | `/api/connect` | Connect two device terminals |
| POST | `/api/disconnect` | Clear all connections |
| POST | `/api/switch` | Toggle switch ON / OFF |

---

## Running Locally

```bash
# Clone the repo
git clone https://github.com/jaayysoni/KEP-Prototype.git
cd KEP-Prototype

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

Visit **http://127.0.0.1:8000/docs** for the interactive Swagger UI.

---

## Example Usage

**Connect battery positive → LED positive:**
```json
POST /api/connect
{
  "from_device": "battery",
  "from_terminal": "positive",
  "to_device": "led",
  "to_terminal": "positive"
}
```

**Check circuit status:**
```json
GET /api/status

Response:
{
  "led_status": "ON",
  "switch": "ON",
  "valid_circuit": true
}
```

---

## Notes

> This is an internship prototype built for internal demonstration at KEP Labs.  
> It uses in-memory storage — no database. Not intended for production use.

---

## Author

**Jay Soni** — Backend Engineering Intern (Remote), KEP Labs

| Platform | Link |
|---|---|
| GitHub | [github.com/jaayysoni](https://github.com/jaayysoni) |
| LinkedIn | [linkedin.com/in/jaayysoni](https://linkedin.com/in/jaayysoni) |
| Email | jaayysoni@gmail.com |