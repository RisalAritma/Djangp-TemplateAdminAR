# 1. Gunakan image Python resmi versi slim (ringan tapi stabil)
FROM python:3.11-slim

# 2. Set environment variables agar Python tidak membuat file .pyc 
# dan output log langsung muncul di terminal Docker
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set direktori kerja di dalam container
WORKDIR /app

# 4. Install dependensi sistem yang dibutuhkan oleh MySQL dan build tools
# Ini adalah bagian krusial agar 'mysqlclient' bisa terinstall dengan lancar
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copy file requirements.txt terlebih dahulu (agar layer caching efisien)
COPY requirements.txt /app/

# 6. Install semua library Python yang ada di requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 7. Copy seluruh file proyek Django Anda ke dalam container
COPY . /app/

# 8. (Opsional) Jika Anda memiliki script entrypoint, bisa ditambahkan di sini.
# Jika tidak, biarkan docker-compose yang mengatur command jalannya.