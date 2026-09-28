# Phase 5: Project Development

## Development Environment
- IDE: Visual Studio Code
- Language: Python
- Web framework: FastAPI
- Local server: Uvicorn
- Templates: Jinja2 with HTML/CSS
- Story generation: Gemini API through Google GenAI SDK
- Image generation: Hugging Face Inference Client using a hosted provider

## Implementation Summary
### Backend
`main.py` defines the FastAPI application and routes. The home route renders the main page. The generation route accepts the user's idea, requests a story, requests an illustration, saves the image, and returns status and output data to the template.

### Frontend
`templates/index.html` provides the input form and displays the generated story, status message, and illustration when an image URL is available.

### Generated Assets
Generated illustration files are saved in `static/panels/` and served through the application's `/static` route.

## How to Run Locally
1. Open the ComicCraft folder in VS Code.
2. Open a PowerShell terminal in the project folder.
3. Activate the virtual environment:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\comiccraft-env\Scripts\Activate.ps1
   ```
4. Start the development server:
   ```powershell
   python -m uvicorn main:app --reload
   ```
5. Open `http://127.0.0.1:8000` in a browser.
6. Keep the terminal running while using the application. Press `Ctrl+C` to stop the server.

## Configuration and Secret Handling
- Store credentials in a local `.env` file.
- Never put actual API keys or tokens in this document, source code, screenshots, or GitHub.
- Ensure `.env` is listed in `.gitignore`.
- Do not commit virtual environment folders, caches, or private credentials.

## Development Evidence
Add screenshots of the working home page, a successful generated story, and a successfully displayed illustration. Remove or blur credentials and personal information from screenshots.
