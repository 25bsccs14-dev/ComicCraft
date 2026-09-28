
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from google import genai
from huggingface_hub import InferenceClient
from pathlib import Path
import os
import uuid

# Load API keys from .env
load_dotenv()

# Check API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

# Connect to Gemini
client = genai.Client(
    api_key=GEMINI_API_KEY
)

# Connect to Hugging Face fal
image_client = InferenceClient(
    provider="fal-ai",
    api_key=HF_TOKEN
)

# Create folders
IMAGE_DIR = Path("static/panels")
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# Create FastAPI app
app = FastAPI(title="ComicCraft")

# Serve static files and generated images
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# Load HTML templates
templates = Jinja2Templates(directory="templates")


# Home page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "story": "",
            "message": "",
            "comic": "",
            "image_url": ""
        }
    )


# Generate comic
@app.post("/generate")
def generate_comic(
    request: Request,
    story: str = Form(...)
):
    # Prepare story prompt
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

    comic = ""
    image_url = ""
    message = ""

    # Generate story using Gemini
    try:
        response = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        comic = response.output_text or "No story was generated."

        message = "Your AI comic story was generated!"

    except Exception as e:
        message = f"Gemini error: {e}"

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "story": story,
                "message": message,
                "comic": "",
                "image_url": ""
            }
        )

    # Generate one illustration using fal
    try:
        image_prompt = f"""
        Create a colorful comic book illustration
        based on this story idea: {story}

        Use a vibrant cartoon style, expressive characters,
        clear scene composition, and no text or lettering.
        """

        image = image_client.text_to_image(
            image_prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0"
        )

        # Save generated image
        filename = f"{uuid.uuid4().hex}.png"
        image_path = IMAGE_DIR / filename
        image.save(image_path)

        # Image URL for the website
        image_url = f"/static/panels/{filename}"
        print("IMAGE SAVED:", image_path.resolve())
        print("IMAGE URL:", image_url)

        message = (
            "Your comic story and illustration were generated!"
        )

    except Exception as image_error:
        message = (
            "Story generated successfully, but image "
            f"generation failed: {image_error}"
        )

    # Display results on the website
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "story": story,
            "message": message,
            "comic": comic,
            "image_url": image_url
        }
    )