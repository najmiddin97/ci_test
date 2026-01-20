FROM python:3.11-slim

# Git va pip upgrade o‘rnatish
RUN apt-get update && \
    apt-get install -y git && \
    python3 -m pip install --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# Ishchi papka
WORKDIR /app

# Repository’ni clone qilamiz
RUN git clone https://github.com/najmiddin97/ci_test.git .

# Global o‘rnatish – barcha paketlar container-wide bo‘ladi
RUN pip install --no-cache-dir -r requirements.txt pytest

# Testlarni ishga tushirish
CMD ["pytest", "-s"]


