from typing import Any, Dict
from utils.request_utils import request_get


def get_user_info(user: str) -> Dict[str, Any]:
    return request_get("https://api.github.com/users/{user}".format(user=user))
