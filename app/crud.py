from sqlalchemy.orm import Session

from app import models, schemas


def get_monthly_usages(
    db: Session,
    year: int | None = None,
    month: int | None = None
):
    query = db.query(models.MonthlyUsage)

    if year is not None:
        query = query.filter(
            models.MonthlyUsage.year == year
        )

    if month is not None:
        query = query.filter(
            models.MonthlyUsage.month == month
        )

    return query.all()
    
def get_monthly_usage(
    db: Session,
    usage_id: int
):
    return (
        db.query(models.MonthlyUsage)
        .filter(models.MonthlyUsage.id == usage_id)
        .first()
    )


def create_monthly_usage(
    db: Session,
    usage: schemas.MonthlyUsageCreate
):
    db_usage = models.MonthlyUsage(
        **usage.model_dump()
    )

    db.add(db_usage)
    db.commit()
    db.refresh(db_usage)

    return db_usage


def replace_monthly_usage(
    db: Session,
    usage_id: int,
    usage: schemas.MonthlyUsageCreate
):
    db_usage = get_monthly_usage(db, usage_id)

    if db_usage is None:
        return None

    update_data = usage.model_dump()

    for key, value in update_data.items():
        setattr(db_usage, key, value)

    db.commit()
    db.refresh(db_usage)

    return db_usage


def update_monthly_usage(
    db: Session,
    usage_id: int,
    usage: schemas.MonthlyUsageUpdate
):
    db_usage = get_monthly_usage(db, usage_id)

    if db_usage is None:
        return None

    update_data = usage.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_usage, key, value)

    db.commit()
    db.refresh(db_usage)

    return db_usage


def delete_monthly_usage(
    db: Session,
    usage_id: int
):
    db_usage = get_monthly_usage(db, usage_id)

    if db_usage is None:
        return None

    db.delete(db_usage)
    db.commit()

    return db_usage