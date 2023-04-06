from api.database.database_base import Session
from api.module.company.company_model import CompanyModel

class CompanyRepository:
    def list(self):
        session = Session()
        return session.query(CompanyModel).all()
    def create(self, company_name):
        print(company_name)
        session = Session()
        company = CompanyModel(company_name=company_name, logo_url='')
        session.add(company)
        session.commit()
        session.refresh(company)
        return company