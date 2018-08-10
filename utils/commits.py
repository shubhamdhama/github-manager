from typing import Any, Dict
from utils.request_utils import request_get


def get_commits_info(paginate: bool=True) -> str:
    params = dict(
        author='shubhamdhamaofficial@gmail.com',
        since='2018-06-10T00:00:00ZZ',
        until='2018-08-10T00:00:00ZZ'
    )

    if paginate:
        params.update(
            page=1,
            per_page=300,
        )

    data = request_get("https://api.github.com/repos/zulip/zulip/commits", params=params)
    return data
