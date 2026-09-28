from pydantic import BaseModel, ConfigDict


class MonthlyUsageBase(BaseModel):
    roc_year: int
    year: int
    month: int
    agency_name: str
    agency_code: str
    usage_count: int


class MonthlyUsageCreate(MonthlyUsageBase):
    pass


class MonthlyUsageUpdate(BaseModel):
    roc_year: int | None = None
    year: int | None = None
    month: int | None = None
    agency_name: str | None = None
    agency_code: str | None = None
    usage_count: int | None = None


class MonthlyUsageResponse(MonthlyUsageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)