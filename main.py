from fastapi import FastAPI, Form
import uvicorn

from apps.ai_vision_models.urls import cvmodel
from apps.cameras.urls import cam
from apps.cam_pos_calibration.urls import calibration

app = FastAPI()

app.include_router(cvmodel, tags=["Vision Model Config"])
app.include_router(cam, tags=["Camera Config"])
app.include_router(calibration, tags=["Camera Calibration Config"])


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)