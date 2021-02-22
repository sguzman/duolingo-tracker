import duolingo
import logging
from typing import Tuple


def login(user: str, password: str) -> duolingo.Duolingo:
    lingo = duolingo.Duolingo(user, password)

    return lingo


def creds() -> Tuple[str, str]:
    import os

    user: str = os.environ['USER']
    password: str = os.environ['PASS']

    return user, password


def main() -> None:
    logging.debug('init')

    c = creds()
    logging.debug(c)
    lingo = login(c[0], c[1])
    print(lingo.get_user_info())

    logging.debug('end')


main()
