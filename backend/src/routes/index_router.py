from fastapi import APIRouter

from src.routes import company_router, game_router, genre_router, console_router
router = APIRouter()

router.include_router(company_router.router, tags=["Company"])
router.include_router(game_router.router, tags=["Game"])
router.include_router(genre_router.router, tags=["Genre"])
router.include_router(console_router.router, tags=["Console"])


@router.get("/", tags=["Root"])
def read_root():
    return {"Hello": "World wey"}
