
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from google import genai
import os

# Load the API key from .env
load_dotenv()

# Connect to Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

app = FastAPI(title="ComicCraft")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "story": "",
            "message": "",
            "comic": ""
        }
    )


@app.post("/generate")
def generate_comic(
    request: Request,
    story: str = Form(...)
):
    prompt = f"""
    Create a short comic story based on this idea:

    {story}

    Divide the story into 4 comic panels.

    For each panel, provide:
    Panel number
    Scene description
    Character dialogue

    Make the story creative and suitable for a comic.
    """

    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=prompt
        )

        comic = response.text or "No story was generated."

        message = "Your AI comic story was generated!"

    except Exception as e:
        comic = ""
        message = f"Gemini error: {str(e)}"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "story": story,
            "message": message,
            "comic": comic
        }
    )