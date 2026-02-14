from fastapi import APIRouter, BackgroundTasks, Depends

from app.deps import require_api_key
from app.exceptions import DemoException

router = APIRouter(tags=["basic"])


@router.get("/ping")
async def ping() -> dict:
    return {"message": "pong"}


@router.get("/protected", dependencies=[Depends(require_api_key)])
async def protected() -> dict:
    return {"status": "ok"}


@router.get("/oops")
async def oops() -> None:
    raise DemoException("Something went wrong")


@router.post("/tasks/notify")
async def notify(background_tasks: BackgroundTasks, email: str) -> dict:
    background_tasks.add_task(simulate_email, email)
    return {"queued": True}


def simulate_email(email: str) -> None:
    import time

    time.sleep(1)
