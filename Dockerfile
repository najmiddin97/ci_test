# Python 3.11 slim image’dan foydalanamiz
FROM python:3.11-slim

# Git o‘rnatamiz (GitHub’dan clone qilish uchun)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Ishchi papka
WORKDIR /app

# GitHub repository’ni clone qilamiz
RUN git clone https://github.com/najmiddin97/ci_test.git .

# Dependency’larni o‘rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Testlarni ishga tushiramiz
CMD ["pytest", "-s"]


