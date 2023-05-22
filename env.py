from decouple import Config, RepositoryEnv
from functools import lru_cache
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
ENV_PATH = BASE_DIR / ".env"

@lru_cache()
def getConfig():
    if ENV_PATH.exists():
        return Config(RepositoryEnv(str(ENV_PATH)))
    else:
        from decouple import config
        return config

config = getConfig()