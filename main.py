# ===================================================================================
#  main.py - Otak Utama dari API Klasifikasi Gestur Tangan
# ===================================================================================

# --- 1. Import Library yang Dibutuhkan ---
import uvicorn
import numpy as np
import tensorflow as tf
import cv2
from fastapi import FastAPI, UploadFile, File
from io import BytesIO
from PIL import Image

# --- 2. Inisialisasi Aplikasi FastAPI ---
# Ini adalah fondasi dari API kita
app = FastAPI(title="Rock-Paper-Scissors Classifier API",
              description="API untuk mengklasifikasikan gestur tangan menjadi Batu, Gunting, atau Kertas menggunakan model CNN.",
              version="1.0")

# --- 3. Load Model CNN Kita ---
# Model di-load sekali saat aplikasi pertama kali dijalankan agar efisien
MODEL_PATH = "models/rps_cnn_model.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Definisikan nama kelas sesuai urutan folder saat training
CLASS_NAMES = ["KERTAS", "BATU", "GUNTING"]

# --- 4. Definisikan Fungsi untuk Preprocessing Gambar ---
# Fungsi ini akan mengubah gambar yang di-upload menjadi format yang
# bisa "dimengerti" oleh model kita.
def preprocess_image(image_bytes: bytes):
    # Ubah bytes gambar menjadi format yang bisa dibaca OpenCV
    image = np.array(Image.open(BytesIO(image_bytes)))
    
    # Resize gambar ke 150x150 piksel, sesuai ukuran input model
    image = cv2.resize(image, (150, 150))
    
    # Normalisasi nilai piksel menjadi antara 0 dan 1
    image = image / 255.0
    
    # Tambahkan dimensi batch (model mengharapkan input bentuk (1, 150, 150, 3))
    image = np.expand_dims(image, axis=0)
    
    return image

# --- 5. Buat "Pintu Masuk" atau Endpoint API ---
# Ini adalah "alamat" yang akan dituju oleh user untuk mengirim gambar
@app.post("/predict", tags=["Prediction"])
async def predict_image(file: UploadFile = File(...)):
    """
    Endpoint untuk memprediksi gestur tangan dari file gambar.

    - **file**: File gambar yang akan di-upload (format: JPEG, PNG, dll).
    """
    # Baca file gambar yang di-upload oleh user
    image_bytes = await file.read()
    
    # Lakukan preprocessing pada gambar
    preprocessed_image = preprocess_image(image_bytes)
    
    # Lakukan prediksi menggunakan model
    prediction = model.predict(preprocessed_image)
    
    # Ambil indeks kelas dengan probabilitas tertinggi
    predicted_class_index = np.argmax(prediction)
    
    # Ambil nama kelasnya dari list CLASS_NAMES
    predicted_class = CLASS_NAMES[predicted_class_index]
    
    # Ambil nilai kepercayaan (confidence) dari prediksi
    confidence = float(np.max(prediction))
    
    # Kembalikan hasilnya dalam format JSON
    return {
        "prediction": predicted_class,
        "confidence": f"{confidence:.2%}" # Format jadi persentase
    }

# --- 6. Endpoint untuk Cek Kesehatan API ---
@app.get("/", tags=["Health Check"])
def read_root():
    return {"status": "API is running..."}