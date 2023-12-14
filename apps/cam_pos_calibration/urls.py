from fastapi import APIRouter, File
from typing import Union, Optional
from pydantic import BaseModel, Field
from typing import List

calibration = APIRouter()

# Patchcore Anomaly Detection
class CamCalibrationConfig(BaseModel):
    cameraSerial: str
    track_window: List[int] = [150, 190, 220, 410]
    img: Optional[str] = None
    imgName: Optional[str] = None
    iouTreshold: float = 0.95
    test: str = "22"
    typeName: Optional[str] = None
    typeNumber: Optional[int] = None

@calibration.post("/calibration")
async def send_cam_calibration_config(calibration_config: CamCalibrationConfig):
    return calibration_config