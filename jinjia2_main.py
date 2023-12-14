# main.py
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.middleware.trustedhost import TrustedHostMiddleware
import os
import shutil

app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Add middleware for handling cross-origin requests
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# Function to save the uploaded file to a specified directory
def save_uploaded_file(file: UploadFile, save_path: str):
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

# Main route to render the HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to handle file upload and save
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    save_uploaded_file(file, file_path)
    return {"filename": file.filename}

# Route to display the uploaded image
@app.get("/showimage/{filename}", response_class=HTMLResponse)
async def read_item(request: Request, filename: str):
    return templates.TemplateResponse("show_image.html", {"request": request, "filename": filename})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
