from fastapi import Request
from src.config.database import SessionLocal

from src.services.company_service import CompanyService

# Schemas
from src.schemas.Company import CompanyCreate, CompanyUpdate, CompanyBase as Company

db = SessionLocal()


class CompanyController():

    async def get_all_companies(self, req: Request):
        order_by = req.query_params.get('order_by') if req.query_params.get(
            'order_by') else 'company_id'
        order = req.query_params.get('order') if req.query_params.get(
            'order') else 'asc'
        limit = req.query_params.get('limit') if req.query_params.get(
            'limit') else 10
        offset = req.query_params.get('offset') if req.query_params.get(
            'offset') else 0

        if limit == '0':
            limit = CompanyService(db).count_companies()

        companies = CompanyService(db).get_all_companies(
            order_by, order, limit, offset)

        for company in companies:
            print(company)

        for company in companies:
            company.games

        response = {
            'data': companies,
            'total': CompanyService(db).count_companies(),
            'page': int(offset) + 1,
            'total_pages': int(CompanyService(db).count_companies() / int(limit)) + 1,
            'limit': int(limit),
            'has_next': int(offset) + int(limit) < CompanyService(db).count_companies(),
            'has_prev': int(offset) > 0
        }
        return response

    async def get_company():
        company = CompanyService(db).get_company_by_id(company_id)
        if not company:
            return None

        company.games
        return company

    async def get_top_companies(self, req: Request):
        companies = CompanyService(db).get_top_companies()

        for company in companies:
            company.games
        return companies

    async def create_company(self, company: CompanyCreate):
        return CompanyService(db).create_company(company)

    async def update_company(self, company_id: int, company: CompanyUpdate):
        return CompanyService(db).update_company(company_id, company)

    async def delete_company(self, company_id: int):
        company = CompanyService(db).delete_company(company_id)
        if not company:
            return None
        return company
