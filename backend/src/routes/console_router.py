from fastapi import APIRouter, Request
from src.config.database import SessionLocal

from typing import Optional, List

from src.services.console_service import ConsoleService

# Schemas
from src.schemas.Console import ConsoleCreate, ConsoleUpdate, ConsoleBase as Console

db = SessionLocal()

router = APIRouter()


@router.get("/console")
async def get_all_consoles(request: Request):
    consoles = ConsoleService(db).get_all_consoles()
    for console in consoles:
        console.games
    return consoles


@router.get("/console/{console_id}")
async def get_console_by_id(console_id: int):
    console = ConsoleService(db).get_console_by_id(console_id)
    if console is None:
        return "Console not found"
    return console


@router.post("/console")
async def create_console(console: ConsoleCreate):
    return ConsoleService(db).create_console(console)


@router.put("/console/{console_id}")
async def update_console(console_id: int, console: ConsoleUpdate):
    return ConsoleService(db).update_console(console_id, console)


@router.delete("/console/{console_id}")
async def delete_console(console_id: int):
    console = ConsoleService(db).delete_console(console_id)
    if not console:
        return "Console not found"
    return console
