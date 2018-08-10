import requests

from typing import Any, Dict


def request_get(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    r = requests.get(*args, **kwargs)
    r.raise_for_status()
    return r.json()
