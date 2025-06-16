# 🚀 RPS Classifier API (FastAPI + Docker)

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green.svg)
![Docker](https://img.shields.io/badge/Docker-Powered-blue.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

## 📄 Project Overview

Proyek ini adalah sebuah implementasi **end-to-end MLOps dasar**, di mana sebuah model *Deep Learning* (CNN) untuk klasifikasi gestur tangan (Batu, Gunting, Kertas) di-deploy sebagai sebuah **API service yang tangguh menggunakan FastAPI dan sepenuhnya terbungkus dalam sebuah kontainer Docker.**

Aplikasi ini siap untuk di-deploy, dijalankan di mana saja, dan diskalakan berkat kontainerisasi, menunjukkan alur kerja produksi yang modern untuk model *Computer Vision*.

---

## ✨ Features

* **API Endpoint `/predict`**: Menerima input gambar dan mengembalikan prediksi gestur dalam format JSON.
* **Dokumentasi API Otomatis**: Dilengkapi dengan *interactive documentation* (Swagger UI) yang dibuat secara otomatis oleh FastAPI, dapat diakses di `/docs`.
* **Dockerized**: Seluruh aplikasi, termasuk model dan semua *dependencies*, dibungkus dalam sebuah Docker image yang portabel dan konsisten.
* **High Performance**: Dibangun di atas FastAPI dan Uvicorn, memberikan performa I/O yang sangat cepat dan asinkron.

---

## 🛠️ Tech Stack

* **Model**: TensorFlow (Keras)
* **API Framework**: FastAPI
* **Web Server**: Uvicorn
* **Image Processing**: OpenCV, Pillow
* **Containerization**: Docker
* **Dependencies**: Python 3.11, NumPy

---

## 📂 Project Structure

```
RPS-API-Deployment/
├── models/
│   └── rps_cnn_model.h5        # Model CNN yang sudah terlatih
│
├── .dockerignore
├── Dockerfile                    # "Resep" untuk membangun Docker image
├── main.py                       # Logika utama aplikasi FastAPI
├── README.md                     # Anda sedang membaca ini
└── requirements.txt              # Daftar library Python
```

---

## 🚀 How to Run with Docker (Recommended)

Pastikan Anda sudah meng-install **Docker Desktop** dan menjalankannya.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rizanss/RPS-API-Deployment.git](https://github.com/rizanss/RPS-API-Deployment.git)
    cd RPS-API-Deployment
    ```

2.  **Build the Docker image:**
    Perintah ini akan membaca `Dockerfile` dan merakit semua yang dibutuhkan ke dalam sebuah *image* bernama `rps-api`.
    ```bash
    docker build -t rps-api:1.0 .
    ```

3.  **Run the Docker container:**
    Perintah ini akan menyalakan kontainer dari *image* yang sudah dibuat dan menghubungkan port `8000` di laptop Anda ke port `80` di dalam kontainer.
    ```bash
    docker run -p 8000:80 rps-api:1.0
    ```

4.  **Aplikasi Anda sekarang berjalan!** Buka browser dan akses dokumentasi interaktif di [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## 🧪 API Usage Example

Anda bisa mengetes API melalui halaman `/docs` atau menggunakan `curl` dari terminal.

**Contoh menggunakan `curl`:**
```bash
curl -X POST -F "file=@/path/to/your/image.png" [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)
```

**Contoh Response Sukses:**
```json
{
  "prediction": "GUNTING",
  "confidence": "99.72%"
}
```

---

## 📬 Contact
* **Author:** Riza Nursyah
* **GitHub:** [rizanss](https://github.com/rizanss)
* **LinkedIn:** [Riza Nursyah](https://www.linkedin.com/in/riza-nursyah-31a6a7221/)