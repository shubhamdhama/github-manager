from typing import Any, Dict
from utils.request_utils import request_get


def get_prs_info(paginate: bool=True) -> str:
    params = dict(
        q='is:pr author:shubhamdhama archived:false created:>2018-03-27 sort:created-asc user:zulip is:closed',
        state='open',
    )

    if paginate:
        params.update(
            page=1,
            per_page=100,
        )

    data = request_get("https://api.github.com/search/issues", params=params)
    result = str()
    for item in data['items']:
        result += '{title}\nLink: [#{number}]({html_url})\n\n'.format(
            title=item['title'].strip(),
            number=item['number'],
            html_url=item['html_url']
        )
    return result
