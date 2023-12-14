from fastapi import APIRouter, File
from typing import Union, Optional
from pydantic import BaseModel, Field
from typing import List

cvmodel = APIRouter()

# Patchcore Anomaly Detection
class ModelConfig(BaseModel):
    feature_name: Optional[str] = None
    coord: Optional[List[int]] =[0,0,0,0]
    thresh: float = 0.95
    select: bool = True
    model: Optional[str] = None
@cvmodel.get("/model")
async def connect_cvmodel():
    return {"cvmodel connection": "successful"}

@cvmodel.post("/model/config")
async def send_patchcore_config(ano_config: ModelConfig):
    return ano_config