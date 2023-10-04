from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from utils.gas import *

router = APIRouter()

@router.post("/alert/gas", response_class=PlainTextResponse)
async def gas_alert(data:dict):
    return sample_function(data)
