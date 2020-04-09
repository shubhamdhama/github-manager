import json
import os
import pprint
import requests

from typing import Any, Dict

from utils.commits import get_commits_info
from utils.pulls import get_prs_info
from utils.users import get_user_info


TEMP_FILE = os.environ.get('TEMP_FILE', "data/output.md")

HELP_TEXT = """You can make following type of requests to GitHub v3 APIs (Enter the option number):
(Please change the queries' code according to your use case first)

(1) Get user information

(2) Get list of the PRs you've created

(3) Get the number of commits between a period.
"""

def print_data(data: Dict[str, Any]) -> None:
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)


def log_json_data(data: Dict[str, Any]) -> None:
    with open(TEMP_FILE, 'w') as f:
        json.dump(data, f, indent=4)


def log_data(data: str) -> None:
    with open(TEMP_FILE, 'w') as f:
        f.write(data)


if __name__ == '__main__':
    option = int(input(HELP_TEXT))

    if option == 1:
        user = input(
            "Enter the GitHub username of user whose GitHub public info you want: ")
        data = get_user_info(user)
        log_json_data(data)

    elif option == 2:
        data = get_prs_info()
        log_data(data)

    elif option == 3:
        data = get_commits_info()
        log_data(data)

    else:
        NotImplementedError()
