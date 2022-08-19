from email.policy import default
import os, yaml, sys
import re
from typing import Any
from envparse import env



from .utils.logger import log

CONFIGS = {}


with open('config.ynl', 'r', encoding='utf-8') as buffer:
    data = yaml.load(buffer, Loader=yaml.FullLoader)
    log.info("Loaded config.ynl")
    log.debug("Loaded Total %s keys from config.ynl ", len(data))
    CONFIGS.update(data)


def del_key(key: str = None)-> bool:
    """ Delete a key from config.ynl """
    if key in CONFIGS:
        del CONFIGS[key]
    else:
        return False


def add_key(key: str = None, value: Any = None )-> bool:
    """ Add a key to config.ynl """
    if value is None:
        return False
    if key in CONFIGS:
        return False
    else:
        CONFIGS.add(key, value)
        return False




def get_str(key: str= None, imp: bool = False):
    """Get Str object from config.ynl"""
    default = CONFIGS[key.upper()] if key.upper() in CONFIGS else None
    data = env.str(key.upper(), default=default)
    if data:
        return data
    elif imp and not data:
        log.error(f"{key} is not set in config.ynl")
        sys.exit(1)
    else:
        return data




def get_int(key: str= None, imp: bool = False):
    """Get Int object from config.ynl"""
    default = CONFIGS[key.upper()] if key.upper() in CONFIGS else None
    data = env.int(key.upper(), default=default)
    if data:
        return data
    elif imp and not data:
        log.error(f"{key} is not set in config.ynl")
        sys.exit(1)
    else:
        return data



def get_bool(key: bool= None, imp: bool = False):
    """Get bool Object from config.ynl"""
    default = CONFIGS[key.upper()] if key.upper() in CONFIGS else None
    data = env.bool(key.upper(), default=default)
    if data:
        return data
    elif imp and not data:
        log.error(f"{key} is not set in config.ynl")
        sys.exit(1)
    else:
        return data





def get_list(key: list= None, imp: bool = False):
    """Get Array object from config.ynl"""
    default = CONFIGS[key.upper()] if key.upper() in CONFIGS else None
    data = env.list(key.upper(), default=default)
    if data:
        return data
    elif imp and not data:
        log.error(f"{key} is not set in config.ynl")
        sys.exit(1)
    else:
        return data