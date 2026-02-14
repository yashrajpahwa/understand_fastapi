import time
from typing import Any

_cache: dict[str, tuple[Any, float]] = {}


def set_cache(key: str, value: Any, ttl: int = 30) -> None:
    _cache[key] = (value, time.time() + ttl)


def get_cache(key: str) -> Any | None:
    entry = _cache.get(key)
    if not entry:
        return None
    value, expires = entry
    if time.time() > expires:
        _cache.pop(key, None)
        return None
    return value


def clear_cache() -> None:
    _cache.clear()
