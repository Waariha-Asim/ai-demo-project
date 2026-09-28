# AI DEMO PROJECT

## Overview
This project consists of a Streamlit web application (`app.py`) and a Flask-based screenshot service (`screenshot_service.py`). The Streamlit interface presents an "AI Project Release Agent" with metrics and a workflow pipeline for project sanitization, documentation, and publishing. The Flask service provides automated screenshot capture using Selenium WebDriver.

## Tech Stack
- **Streamlit** – Web application framework
- **Python** – Primary programming language
- **Flask** – Backend service for screenshot capture
- **Selenium** – Browser automation for screenshots
- **AI** – Referenced in UI metrics (Gemini mentioned)

## Project Structure
```
.
├── app.py                 # Streamlit entrypoint
└── screenshot_service.py  # Flask screenshot service
```

## Setup
1. Ensure Python 3.8+ is installed.
2. Install dependencies (not explicitly listed; infer from imports):
   - `streamlit`
   - `flask`
   - `selenium`
   - `webdriver-manager`
   - `pillow`
   - Standard library modules: `subprocess`, `tempfile`, `os`, `base64`, `time`, `sys`, `io`, `socket`, `zipfile`
3. Chrome/Chromium browser must be available for Selenium.

## Environment Variables
None detected in the provided code.

## Usage
### Run Streamlit Application
```bash
streamlit run app.py --server.headless true --server.address 0.0.0.0 --server.port 8501
```
The app will be accessible at `http://localhost:8501`.

### Screenshot Service
The `screenshot_service.py` runs a Flask server (port not specified in snippet). It exposes endpoints for capturing screenshots of provided URLs using headless Chrome.

## Visual Preview
A screenshot of the application has been captured.

## Security
- The screenshot service uses headless Chrome with `--no-sandbox` and `--disable-dev-shm-usage` flags.
- Port cleanup logic attempts to kill processes on target ports via `netstat`.
- No authentication or authorization mechanisms are visible in the provided code.
- Secret scanning is mentioned as a workflow step in the UI but implementation is not shown.

## License
Not specified in the provided files.