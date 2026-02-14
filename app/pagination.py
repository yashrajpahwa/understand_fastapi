from typing import Sequence


def paginate(items: Sequence, total: int, skip: int, limit: int) -> dict:
    return {"items": items, "total": total, "skip": skip, "limit": limit}
