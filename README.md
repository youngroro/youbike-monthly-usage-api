# Taipei YouBike Monthly Usage RESTful API

以臺北市 YouBike 每月使用量 Open Data 為基礎，使用 Python、FastAPI、SQLAlchemy 與 SQLite 實作 RESTful API Server。

本專案提供完整 CRUD 操作，並支援依年份與月份查詢資料。FastAPI 會自動產生 Swagger UI API 文件，另外提供 Python API Client，可直接測試各項 API。

---

## 1. Open Data

本專案使用「YouBike 臺北市站位每月使用量」Open Data。

原始資料存放於：

```text
data/monthly_usage.csv
```

資料包含：

| 原始欄位 | API / Database 欄位 | 說明 |
|---|---|---|
| 民國年 | `roc_year` | 民國年份 |
| 西元年 | `year` | 西元年份 |
| 月份 | `month` | 統計月份 |
| 發布機關名稱 | `agency_name` | 資料發布機關 |
| 機關代碼 | `agency_code` | 發布機關代碼 |
| 臺北市YouBike每月使用量（次數） | `usage_count` | 當月 YouBike 使用次數 |

原始 CSV 資料會透過匯入程式寫入 SQLite Database，再由 FastAPI 提供 RESTful API 存取。

---

## 2. Technology

本專案使用：

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pandas
- Requests
- Swagger UI

---

## 3. Project Structure

```text
youbike-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── routers/
│       ├── __init__.py
│       └── monthly_usage.py
│
├── client/
│   └── api_client.py
│
├── data/
│   └── monthly_usage.csv
│
├── scripts/
│   └── import_data.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### 主要檔案

| 檔案 | 說明 |
|---|---|
| `app/main.py` | FastAPI Application 進入點 |
| `app/database.py` | SQLite / SQLAlchemy Database 設定 |
| `app/models.py` | SQLAlchemy Database Model |
| `app/schemas.py` | Pydantic Request / Response Schema |
| `app/crud.py` | CRUD Database 操作 |
| `app/routers/monthly_usage.py` | Monthly Usage RESTful API |
| `scripts/import_data.py` | Open Data CSV 匯入 SQLite |
| `client/api_client.py` | Python API Client |
| `data/monthly_usage.csv` | Open Data 原始資料 |

---

## 4. Environment Setup

### 建立 Python Virtual Environment

Linux / macOS：

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows：

```bash
python -m venv venv
venv\Scripts\activate
```

### 安裝 Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Import Open Data

第一次執行專案時，先將 CSV Open Data 匯入 SQLite：

```bash
python -m scripts.import_data
```

成功後會顯示：

```text
Imported 66 records.
```

並建立：

```text
data/monthly_usage.db
```

> `monthly_usage.db` 為執行時產生的 SQLite Database，因此未加入 Git Repository。

---

## 6. Start API Server

在專案根目錄執行：

```bash
uvicorn app.main:app --reload
```

Server 預設執行於：

```text
http://127.0.0.1:8000
```

測試：

```text
http://127.0.0.1:8000/
```

Response：

```json
{
  "message": "Taipei YouBike Monthly Usage API"
}
```

---

## 7. Swagger API Documentation

FastAPI 會自動產生 Swagger UI。

啟動 Server 後開啟：

```text
http://127.0.0.1:8000/docs
```

即可查看及直接測試所有 RESTful APIs。

---

## 8. RESTful API

Base Path：

```text
/api/v1/monthly-usage
```

### API List

| Method | Path | 功能 |
|---|---|---|
| GET | `/api/v1/monthly-usage` | 查詢全部資料 |
| GET | `/api/v1/monthly-usage/{usage_id}` | 查詢指定資料 |
| POST | `/api/v1/monthly-usage` | 新增資料 |
| PUT | `/api/v1/monthly-usage/{usage_id}` | 完整修改資料 |
| PATCH | `/api/v1/monthly-usage/{usage_id}` | 部分修改資料 |
| DELETE | `/api/v1/monthly-usage/{usage_id}` | 刪除資料 |

---

## 9. Query Parameters

查詢 API 支援依照西元年份及月份篩選。

### 查詢指定年份

```http
GET /api/v1/monthly-usage?year=2025
```

### 查詢指定年份及月份

```http
GET /api/v1/monthly-usage?year=2025&month=5
```

### 查詢不同年份的指定月份

```http
GET /api/v1/monthly-usage?month=5
```

---

## 10. API Examples

### GET - 查詢單筆資料

Request：

```http
GET /api/v1/monthly-usage/1
```

Response：

```json
{
  "id": 1,
  "roc_year": 109,
  "year": 2020,
  "month": 11,
  "agency_name": "臺北市政府交通局",
  "agency_code": "379530000H",
  "usage_count": 2730442
}
```

Status Code：

```text
200 OK
```

---

### POST - 新增資料

Request：

```http
POST /api/v1/monthly-usage
```

Request Body：

```json
{
  "roc_year": 115,
  "year": 2026,
  "month": 9,
  "agency_name": "臺北市政府交通局",
  "agency_code": "379530000H",
  "usage_count": 3000000
}
```

成功時回傳：

```text
201 Created
```

---

### PUT - 完整修改

```http
PUT /api/v1/monthly-usage/1
```

PUT 必須提供完整 Resource：

```json
{
  "roc_year": 115,
  "year": 2026,
  "month": 9,
  "agency_name": "臺北市政府交通局",
  "agency_code": "379530000H",
  "usage_count": 3500000
}
```

---

### PATCH - 部分修改

```http
PATCH /api/v1/monthly-usage/1
```

例如只修改使用量：

```json
{
  "usage_count": 4000000
}
```

---

### DELETE - 刪除資料

```http
DELETE /api/v1/monthly-usage/1
```

成功時：

```text
204 No Content
```

---

## 11. Python API Client

本專案另外提供 Python API Client：

```text
client/api_client.py
```

執行：

```bash
python client/api_client.py
```

Client 提供：

```text
Taipei YouBike Monthly Usage API Client

1. 查詢全部
2. 查詢單筆
3. 依年份 / 月份搜尋
4. 新增資料
5. PUT 完整修改
6. PATCH 部分修改
7. 刪除資料
0. 離開
```

可透過 Python Client 完整測試 RESTful API 的 CRUD 操作。

---

## 12. HTTP Status Codes

API 主要使用以下 HTTP Status Code：

| Status Code | 說明 |
|---|---|
| `200 OK` | 查詢或修改成功 |
| `201 Created` | 新增成功 |
| `204 No Content` | 刪除成功 |
| `404 Not Found` | 找不到指定資料 |
| `422 Unprocessable Entity` | Request 資料格式錯誤 |

---

## 13. CRUD Design

本專案 RESTful API CRUD 對應：

| CRUD | HTTP Method | 功能 |
|---|---|---|
| Create | POST | 建立每月使用量資料 |
| Read | GET | 查詢每月使用量資料 |
| Update | PUT / PATCH | 修改每月使用量資料 |
| Delete | DELETE | 刪除每月使用量資料 |

其中：

- `PUT` 用於完整更新 Resource。
- `PATCH` 用於部分更新 Resource。

---

## 14. Run Project

完整執行流程：

```bash
# 1. 建立 Virtual Environment
python3 -m venv venv

# 2. 啟用 Virtual Environment
source venv/bin/activate

# 3. 安裝 Dependencies
pip install -r requirements.txt

# 4. 匯入 Open Data
python -m scripts.import_data

# 5. 啟動 FastAPI
uvicorn app.main:app --reload
```

接著開啟 Swagger：

```text
http://127.0.0.1:8000/docs
```

或另外開啟 Terminal 執行 Python API Client：

```bash
python client/api_client.py
```