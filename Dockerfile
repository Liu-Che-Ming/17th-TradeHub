# 使用官方 Python 映像檔作為基底
FROM python:3.13.0-bookworm

# 設置工作目錄
WORKDIR /app

# 將專案中的所有檔案複製到容器中
COPY . .

# 安裝依賴
RUN pip install requirements.txt
RUN npm i 

# 開放專案運行的端口
EXPOSE 8000

# 運行命令
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
