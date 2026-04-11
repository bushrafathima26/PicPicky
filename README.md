# 📸 PicPicky — Image Quality Assessment & Photographer Profiling

PicPicky is a web application that analyzes uploaded photos for technical and aesthetic quality, detects duplicates, and builds a profiling system for photographers based on their submission history.

Built as a Final Year Project (BCA) — Backend & ML pipeline by [Bushra Fathima](https://github.com/bushrafathima26).

---

## 🚀 Features

- **Blur Detection** — Flags out-of-focus images using Laplacian variance analysis
- **Duplicate Detection** — Identifies near-duplicate images using perceptual hashing
- **Technical Quality Analysis** — Evaluates exposure, noise, sharpness, and color balance
- **Aesthetic Scoring** — Rates images using the MANIQA deep learning model (CLIP-IQA based)
- **Photographer Profiling** — Tracks submission quality over time and builds a profile score
- **Cloudinary Integration** — Cloud-based image storage and delivery
- **User Authentication** — Register/login system with secure session handling

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI (Python) |
| Database | MongoDB Atlas |
| Image Storage | Cloudinary |
| ML Models | PyTorch, CLIP-IQA, MANIQA |
| Auth | JWT / Session-based |
| Frontend | HTML, CSS, JavaScript |

---

## 📁 Project Structure

```
image-quality-assessment/
│
├── main.py                  # FastAPI app entry point
├── config.py                # Environment & configuration
├── database.py              # MongoDB Atlas connection
├── requirements.txt         # Python dependencies
│
├── models/
│   └── user.py              # User data model
│
├── routes/
│   ├── auth.py              # Login / Register endpoints
│   └── upload.py            # Image upload & analysis endpoints
│
├── services/
│   ├── blur_detection.py        # Laplacian-based blur scoring
│   ├── duplicate_detection.py   # Perceptual hash duplicate check
│   ├── technical_quality.py     # Exposure, noise, sharpness analysis
│   ├── clipiqa_scorer.py        # CLIP-IQA aesthetic scoring
│   └── explainability.py        # Score explanation generation
│
└── frontend/
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── upload.html
    ├── analysis.html
    ├── profile.html
    ├── best-album.html
    └── sidebar.html
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/bushrafathima26/PicPicky.git
cd PicPicky
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
MONGODB_URI=your_mongodb_atlas_connection_string
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
SECRET_KEY=your_jwt_secret_key
```

### 5. Run the application

```bash
uvicorn main:app --reload
```

The app will be available at `http://localhost:8000`

---

## 🧠 ML Pipeline Overview

```
Image Upload
     │
     ▼
Blur Detection  ──►  Flagged as blurry? → Reject
     │
     ▼
Duplicate Check ──►  Duplicate found? → Reject
     │
     ▼
Technical Quality Analysis
(Exposure · Noise · Sharpness · Color)
     │
     ▼
Aesthetic Score (MANIQA / CLIP-IQA)
     │
     ▼
Composite Score → Photographer Profile Update
```

---

## 📊 Demo Setup (Google Colab + ngrok)

For demo day, the ML inference runs on Google Colab (GPU) exposed via ngrok tunnel, while the FastAPI backend communicates with it over HTTP.

---

## 👩‍💻 Author

**Bushra Fathima**
BCA Final Year — Bangalore
[GitHub](https://github.com/bushrafathima26)

---

## 📄 License

This project is for academic purposes only.
