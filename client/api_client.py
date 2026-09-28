import requests

BASE_URL = "http://127.0.0.1:8000/api/v1/monthly-usage"


def print_response(response):
    print(f"Status Code: {response.status_code}")

    if response.content:
        try:
            print(response.json())
        except ValueError:
            print(response.text)

    print("-" * 50)


def get_all():
    response = requests.get(BASE_URL)
    print_response(response)


def get_one(usage_id):
    response = requests.get(f"{BASE_URL}/{usage_id}")
    print_response(response)


def search(year=None, month=None):
    params = {}

    if year is not None:
        params["year"] = year

    if month is not None:
        params["month"] = month

    response = requests.get(
        BASE_URL,
        params=params
    )

    print_response(response)


def create():
    print("\n--- 新增每月使用量資料 ---")

    year = int(input("西元年: "))
    roc_year = int(input("民國年: "))
    month = int(input("月份: "))
    agency_name = input("發布機關名稱: ")
    agency_code = input("機關代碼: ")
    usage_count = int(input("YouBike 每月使用量: "))

    data = {
        "roc_year": roc_year,
        "year": year,
        "month": month,
        "agency_name": agency_name,
        "agency_code": agency_code,
        "usage_count": usage_count
    }

    response = requests.post(
        BASE_URL,
        json=data
    )

    print_response(response)

def replace(usage_id):
    print("\n--- PUT 完整修改資料 ---")

    year = int(input("西元年: "))
    roc_year = int(input("民國年: "))
    month = int(input("月份: "))
    agency_name = input("發布機關名稱: ")
    agency_code = input("機關代碼: ")
    usage_count = int(input("YouBike 每月使用量: "))

    data = {
        "roc_year": roc_year,
        "year": year,
        "month": month,
        "agency_name": agency_name,
        "agency_code": agency_code,
        "usage_count": usage_count
    }

    response = requests.put(
        f"{BASE_URL}/{usage_id}",
        json=data
    )

    print_response(response)


def update(usage_id):
    print("\n--- PATCH 部分修改資料 ---")
    print("直接按 Enter 代表不修改該欄位")

    data = {}

    roc_year = input("民國年: ")
    year = input("西元年: ")
    month = input("月份: ")
    agency_name = input("發布機關名稱: ")
    agency_code = input("機關代碼: ")
    usage_count = input("YouBike 每月使用量: ")

    if roc_year:
        data["roc_year"] = int(roc_year)

    if year:
        data["year"] = int(year)

    if month:
        data["month"] = int(month)

    if agency_name:
        data["agency_name"] = agency_name

    if agency_code:
        data["agency_code"] = agency_code

    if usage_count:
        data["usage_count"] = int(usage_count)

    response = requests.patch(
        f"{BASE_URL}/{usage_id}",
        json=data
    )

    print_response(response)


def menu():
    while True:
        print()
        print("Taipei YouBike Monthly Usage API Client")
        print("1. 查詢全部")
        print("2. 查詢單筆")
        print("3. 依年份 / 月份搜尋")
        print("4. 新增資料")
        print("5. PUT 完整修改")
        print("6. PATCH 部分修改")
        print("7. 刪除資料")
        print("0. 離開")

        choice = input("請選擇功能: ")

        if choice == "1":
            get_all()

        elif choice == "2":
            usage_id = int(input("請輸入 ID: "))
            get_one(usage_id)

        elif choice == "3":
            year_input = input(
                "請輸入西元年（直接 Enter 代表不限）: "
            )

            month_input = input(
                "請輸入月份（直接 Enter 代表不限）: "
            )

            year = int(year_input) if year_input else None
            month = int(month_input) if month_input else None

            search(year, month)

        elif choice == "4":
            create()

        elif choice == "5":
            usage_id = int(input("請輸入 ID: "))
            replace(usage_id)

        elif choice == "6":
            usage_id = int(input("請輸入 ID: "))
            update(usage_id)

        elif choice == "7":
            usage_id = int(input("請輸入 ID: "))
            delete(usage_id)

        elif choice == "0":
            print("Bye")
            break

        else:
            print("無效的選項")


if __name__ == "__main__":
    menu()