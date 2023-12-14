from fastapi import APIRouter, File
from typing import Union, Optional
from pydantic import BaseModel, Field
from typing import List


cam = APIRouter()

class CameraConfig(BaseModel):
    cameraName: Optional[str] = None
    cameraSerial: str = "700005866925"
    ipAddress: Optional[str] = None
    subnetMask: Optional[str] = None
    exposureTime: int = Field(default=25000, lt=2500000, gt=250)
    autoExposure: int = 0
    balanceWhiteAuto: int = 0
    gainAuto: int = 0
    gain: float = 1.0
    gamma: float = 1.0
    jobs: List[int] = [0]
    active: bool = True
    


@cam.post("/cam")
async def send_cam_config(camconfig: CameraConfig):
    return camconfig
