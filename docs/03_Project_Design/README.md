# Phase 3: Project Design

## 1. System Architecture
ComicCraft follows a simple client-server design.

1. User enters an idea in the browser.
2. The HTML form sends the idea to the FastAPI backend.
3. FastAPI sends a story-generation prompt to the Gemini service.
4. FastAPI sends an illustration prompt to the configured Hugging Face inference provider.
5. The generated image is saved under `static/panels/`.
6. FastAPI returns the result to the Jinja2 template.
7. The browser displays the story and available image.

## 2. Main Components
| Component | Responsibility |
|---|---|
| Browser / `templates/index.html` | Collects user input and displays output |
| FastAPI (`main.py`) | Handles routes, API calls, errors, and response data |
| Gemini API | Generates the comic story |
| Hugging Face Inference provider | Generates the comic illustration |
| `static/panels/` | Stores generated image files |
| `.env` | Stores local API credentials; must remain untracked |

## 3. Data Flow
`User Idea → HTML Form → FastAPI → Gemini Story → Image Provider → Save Image → HTML Result`

The story and image calls may fail independently. The application should communicate which output was successfully generated.

## 4. User Interface Design
The main page contains:
- Project title and brief introduction.
- Text area or form field for the comic idea.
- Generate button.
- Status/message area.
- Generated story section.
- Illustration section, shown when an image URL is available.

## 5. Project Folder Structure
```text
ComicCraft/
├── main.py
├── templates/
│   └── index.html
├── static/
│   └── panels/
├── .env                 # local secrets; do not upload
├── .gitignore
├── requirements.txt     # include if maintained in project
└── docs/
    ├── 01_Brainstorming_and_Ideation/
    ├── 02_Requirement_Analysis/
    ├── 03_Project_Design/
    ├── 04_Project_Planning/
    ├── 05_Project_Development/
    ├── 06_Project_Testing/
    ├── 07_Project_Documentation/
    └── 08_Project_Demonstration/
```

## 6. Design Notes
This describes the intended/current high-level design. Update it if the implementation changes. Add a hand-drawn or digital architecture diagram if your trainer requires one.
