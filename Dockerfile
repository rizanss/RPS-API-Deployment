# ======================================================================
#  Dockerfile v3.0 - The Professional Way
# ======================================================================

# Tahap 1: Mulai dari base image RESMI TensorFlow untuk CPU.
# Semua library TensorFlow dan CUDA sudah terinstall dan teroptimasi di sini.
FROM tensorflow/tensorflow:2.16.1

# Tahap 2: Siapkan "Area Kerja"
WORKDIR /app

# Tahap 3: Install dependency LAINNYA yang kita butuhkan
# Copy dulu file daftar belanja kita
COPY requirements.txt .

# Jalankan pip install (ini akan SANGAT CEPAT karena TensorFlow sudah ada)
RUN pip install --no-cache-dir -r requirements.txt

# Tahap 4: Install dependency sistem untuk OpenCV
# Ini tetap dibutuhkan
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Tahap 5: Copy sisa aplikasi kita
COPY . .

# Tahap 6: Perintah untuk menyalakan aplikasi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]