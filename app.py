import infoboard.config
#infoboard.config.setup_logging()
import logging
import asyncio

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles

import infoboard
import infoboard.slideshow as isl

logger = logging.getLogger(__name__)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

PREFIX="/static"

async def every(__seconds: float, func, *args, **kwargs):
    while True:
        func(*args, *kwargs)
        await asyncio.sleep(__seconds)

@app.get('/sites.json')
async def get_sites():
    sites = isl.get_sites()

    return jsonable_encoder(sites)

loop = asyncio.get_event_loop()
