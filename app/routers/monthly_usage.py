from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db


router = APIRouter(
    prefix="/api/v1/monthly-usage",
    tags=["Monthly Usage"]
)


# 查詢全部
@router.get(
    "",
    response_model=list[schemas.MonthlyUsageResponse]
)
def get_monthly_usages(
    year: int | None = None,
    month: int | None = None,
    db: Session = Depends(get_db)
):
    return crud.get_monthly_usages(
        db,
        year=year,
        month=month
    )


# 查詢單筆
@router.get(
    "/{usage_id}",
    response_model=schemas.MonthlyUsageResponse
)
def get_monthly_usage(
    usage_id: int,
    db: Session = Depends(get_db)
):
    usage = crud.get_monthly_usage(db, usage_id)

    if usage is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Monthly usage not found"
        )

    return usage


# 新增
@router.post(
    "",
    response_model=schemas.MonthlyUsageResponse,
    status_code=status.HTTP_201_CREATED
)
def create_monthly_usage(
    usage: schemas.MonthlyUsageCreate,
    db: Session = Depends(get_db)
):
    return crud.create_monthly_usage(db, usage)


# 完整修改
@router.put(
    "/{usage_id}",
    response_model=schemas.MonthlyUsageResponse
)
def replace_monthly_usage(
    usage_id: int,
    usage: schemas.MonthlyUsageCreate,
    db: Session = Depends(get_db)
):
    updated_usage = crud.replace_monthly_usage(
        db,
        usage_id,
        usage
    )

    if updated_usage is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Monthly usage not found"
        )

    return updated_usage


# 部分修改
@router.patch(
    "/{usage_id}",
    response_model=schemas.MonthlyUsageResponse
)
def update_monthly_usage(
    usage_id: int,
    usage: schemas.MonthlyUsageUpdate,
    db: Session = Depends(get_db)
):
    updated_usage = crud.update_monthly_usage(
        db,
        usage_id,
        usage
    )

    if updated_usage is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Monthly usage not found"
        )

    return updated_usage


# 刪除
@router.delete(
    "/{usage_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_monthly_usage(
    usage_id: int,
    db: Session = Depends(get_db)
):
    deleted_usage = crud.delete_monthly_usage(
        db,
        usage_id
    )

    if deleted_usage is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Monthly usage not found"
        )

    return