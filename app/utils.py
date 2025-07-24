import yaml
import re
from typing import Tuple

with open("config/whitelist.yaml", "r") as f:
    whitelist = yaml.safe_load(f)

def is_whitelisted(message: str) -> Tuple[bool, str]:
    message = message.lower()

    for phrase in whitelist["phrases"]:
        if phrase.lower() in message:
            return True, "phrase"

    for domain in whitelist["domains"]:
        if domain.lower() in message:
            return True, "domain"

    return False, ""
