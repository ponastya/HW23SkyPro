import re
from typing import Iterable, Any, Set, Iterator


def filter_query(value: str, data: Iterable[str]) ->Iterator[str]:
    return filter(lambda x: value in x, data)


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    return map(lambda x: x.split()[int(value)], data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> Set[str]:
    return set(data)


def sort_query(value:str, data:Iterable[str]) -> list[str]:
    reverse = value == "desc"
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]) -> list[str]:
    limit: int = int(value)
    return list(data)[:limit]


def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)