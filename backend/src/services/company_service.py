from src.models.company_model import Company as CompanyModel
from src.schemas.Company import CompanyCreate, CompanyUpdate

from sqlalchemy import text


class CompanyService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_companies(self, order_by: str, order: str, limit: int, offset: int):
        return self.db.query(CompanyModel).order_by(text(order_by + " " + order)).limit(limit).offset(offset).all()

    def get_company_by_id(self, company_id: int):
        return self.db.query(CompanyModel).filter(CompanyModel.company_id == company_id).first()

    def count_companies(self):
        return self.db.query(CompanyModel).count()

    def get_top_companies(self):
        # More quantity of games
        db_companies = self.db.query(CompanyModel).all()
        db_companies.sort(key=lambda x: len(x.games), reverse=True)
        return db_companies[:5]

    def create_company(self, company: CompanyCreate):
        db_company = CompanyModel(**company.dict())
        self.db.add(db_company)
        self.db.commit()
        self.db.refresh(db_company)
        return db_company

    def update_company(self, company_id: int, company: CompanyUpdate):
        db_company = self.db.query(CompanyModel).filter(
            CompanyModel.company_id == company_id).first()
        db_company.name = company.name if company.name else db_company.name
        db_company.foundation_year = company.foundation_year if company.foundation_year else db_company.foundation_year
        db_company.country = company.country if company.country else db_company.country
        self.db.commit()
        self.db.refresh(db_company)
        return db_company

    def delete_company(self, company_id: int):
        db_company = self.db.query(CompanyModel).filter(
            CompanyModel.company_id == company_id).first()
        if db_company is None:
            return None
        self.db.delete(db_company)
        self.db.commit()
        return db_company
