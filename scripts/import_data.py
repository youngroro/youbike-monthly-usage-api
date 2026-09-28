import pandas as pd

from app.database import SessionLocal
from app.models import MonthlyUsage


CSV_PATH = "data/monthly_usage.csv"


def import_data():
    df = pd.read_csv(
        CSV_PATH,
        encoding="cp950"
    )

    db = SessionLocal()

    try:
        for _, row in df.iterrows():
            usage = MonthlyUsage(
                roc_year=int(row["民國年"]),
                year=int(row["西元年"]),
                month=int(row["月份"]),
                agency_name=row["發布機關名稱"],
                agency_code=row["機關代碼"],
                usage_count=int(
                    row["臺北市YouBike每月使用量（次數）"]
                ),
            )

            db.add(usage)

        db.commit()

        print(f"Imported {len(df)} records.")

    except Exception as e:
        db.rollback()
        print(f"Import failed: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    import_data()