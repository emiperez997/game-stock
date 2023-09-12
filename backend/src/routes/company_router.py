from fastapi import APIRouter, Request
from src.config.database import SessionLocal
from typing import Optional, List

from src.services.company_service import CompanyService

from src.schemas.Company import CompanyCreate, CompanyUpdate, CompanyBase as Company

from src.controllers.company_controller import CompanyController

router = APIRouter()

db = SessionLocal()


@router.get("/company")
async def get_all_companies(request: Request):
    companies = await CompanyController().get_all_companies(request)
    return companies


@router.get("/company/top")
async def get_top_companies():
    companies = CompanyService(db).get_top_companies()
    for company in companies:
        company.games
    return companies


@router.get("/company/{company_id}")
async def get_company_by_id(company_id: int):
    company = CompanyService(db).get_company_by_id(company_id)
    if company is None:
        return "Company not found"

    company.games
    return company


@router.post("/company")
async def create_company(company: CompanyCreate):
    return CompanyService(db).create_company(company)


@router.put("/company/{company_id}")
async def update_company(company_id: int, company: CompanyUpdate):
    return CompanyService(db).update_company(company_id, company)


@router.delete("/company/{company_id}")
async def delete_company(company_id: int):
    company = CompanyService(db).delete_company(company_id)
    if not company:
        return "Company not found"
    return company
