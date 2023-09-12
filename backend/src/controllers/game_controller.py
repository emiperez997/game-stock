from fastapi import Request
from src.config.database import SessionLocal

from src.services.game_service import GameService

db = SessionLocal()


class GameController():

    async def get_all_games(self, req: Request):
        order_by = req.query_params.get('order_by') if req.query_params.get(
            'order_by') else 'game_id'
        order = req.query_params.get('order') if req.query_params.get(
            'order') else 'asc'
        limit = req.query_params.get('limit') if req.query_params.get(
            'limit') else 10
        offset = req.query_params.get('offset') if req.query_params.get(
            'offset') else 0

        if limit == '0':
            limit = GameService(db).count_games()

        games = GameService(db).get_all_games(order_by, order, limit, offset)

        for game in games:
            game.genres
            game.company
            game.consoles
        return games
