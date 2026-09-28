from sqlalchemy import Column, Integer, String

from app.database import Base


class MonthlyUsage(Base):
    __tablename__ = "monthly_usage"

    id = Column(Integer, primary_key=True, index=True)

    roc_year = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)

    agency_name = Column(String, nullable=False)
    agency_code = Column(String, nullable=False)

    usage_count = Column(Integer, nullable=False)