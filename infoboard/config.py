import logging
import logging.config
import tomllib

from pathlib import Path

def setup_logging(file: Path = Path('config.toml')):
    with file.open('rb') as f:
        d = tomllib.load(f)['logging']
    logging.config.dictConfig(d)
