# FastAPI Hello API for Render

這是一個使用 FastAPI 實作、專為部署至 Render 設計的簡單 API。

## 專案結構

- `main.py`：FastAPI 應用程式邏輯。
- `requirements.txt`：相依套件清單。
- `render.yaml`：Render Blueprint 部署設定檔。

## API 端點 (Endpoints)

- `GET /`：回傳 JSON 格式的 Hello。
  - 回傳範例：`{"message": "Hello"}`
- `GET /hello`：回傳純文字格式的 Hello。
  - 回傳範例：`Hello`
- `GET /health`：健康檢查端點（供 Render 監控使用）。
  - 回傳範例：`{"status": "healthy"}`

## 本地端開發與執行 (Local Development)

1. **建立並啟用虛擬環境 (選用但建議)**：
   ```bash
   python -m venv venv
   # Windows 啟用：
   .\venv\Scripts\activate
   # macOS/Linux 啟用：
   source venv/bin/activate
   ```

2. **安裝相依套件**：
   ```bash
   pip install -r requirements.txt
   ```

3. **啟動本地開發伺服器**：
   ```bash
   uvicorn main:app --reload
   ```
   啟動後，您可以在瀏覽器中開啟：
   - API 服務：[http://127.0.0.1:8000](http://127.0.0.1:8000)
   - 自動產生的互動式 API 文件 (Swagger UI)：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 部署至 Render (Deployment on Render)

### 方式 A：使用 Render Blueprint (推薦，全自動)

1. 將此專案推送至您的 GitHub 或 GitLab 儲存庫。
2. 登入 [Render Dashboard](https://dashboard.render.com/)。
3. 點選 **New** -> **Blueprint**。
4. 連結此專案的儲存庫，Render 將會自動偵測 `render.yaml` 並建立 Web Service。

### 方式 B：手動建立 Web Service

1. 登入 Render Dashboard，點選 **New** -> **Web Service**。
2. 連結此專案的儲存庫。
3. 進行以下設定：
   - **Language**: `Python`
   - **Branch**: `main` (或您的主要分支)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
4. 點擊 **Create Web Service** 開始部署。
