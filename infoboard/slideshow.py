from pathlib import Path
import tomllib
import json
from pydantic import BaseModel

class SlideshowEntry(BaseModel):
    duration_sec: int 
    path: str

def get_sites(prefix: str=''):
    with Path('site_config.toml').open('rb') as f:
       entries = tomllib.load(f)
    return [SlideshowEntry(
                duration_sec=int(entry['duration']),
                path=prefix + entry['path']) 
            for entry in entries['sites']]
