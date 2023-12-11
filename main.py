from typing import Union
from fastapi import FastAPI, WebSocket, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import cv2
import numpy as np
from io import BytesIO
import base64
import os
import uuid
import io

from baumer_cam_handler import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the list of allowed origins, or ["*"] for any origin
    allow_credentials=True,
    allow_methods=["*"],  # Set this to the list of allowed methods, or ["*"] for any method
    allow_headers=["*"],  # Set this to the list of allowed headers, or ["*"] for any header
)

@app.get("/takeimg/{camserial}")
async def takeimg(camserial: int):
    try:
        camHandler = CamHandler(camserial)
        image = camHandler.getImage()

        if image is None:
            return {"error": "Empty Image"}

        npArray = image.GetNPArray()
        return StreamingResponse(io.BytesIO(npArray.tobytes()), media_type="image/jpeg")

    except Exception as error:
        return {"error": str(error)}
    


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item": item, "item_id": item_id}










# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")






# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item": item, "item_id": item_id}








# # Serve static files (for frontend)
# app.mount("/", StaticFiles(directory="static", html=True), name="static")

# # HTML endpoint to serve the frontend
# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def read_item(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

# # File upload endpoint
# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile = File(...)):
#     contents = await file.read()
#     image = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.IMREAD_COLOR)

#     # Save the captured image
#     cv2.imwrite("captured_image.jpg", image)

#     return {"message": "File uploaded successfully"}

# # Example: Serve the captured image in the HTML page
# @app.get("/captured_image/")
# async def get_captured_image(request: Request):
#     with open("captured_image.jpg", "rb") as f:
#         image_data = f.read()
#     return HTMLResponse(content=f'<img src="data:image/jpeg;base64,{base64.b64encode(image_data).decode()}" />', status_code=200)



# Baumer Camera
# camHandler = CamHandler("700005866925")
# try:
#     # print("Got Image")
#     image = camHandler.getImage()
#     if image is None:
#         print('Empty Image')
#     # ! Image from Camera
#     npArray = image.GetNPArray()
# except Exception as error:
#     print(error)
# print('Done')