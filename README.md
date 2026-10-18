# 👗 OutfitAura — Backend API


## 📌 About the Project

**OutfitAura** is a fashion-tech application designed to support personalized outfit styling and wardrobe management. This repository contains the backend API, developed using Python and FastAPI, that powers the application's outfit-related features.

The backend provides API endpoints for outfit creation, outfit correction, wardrobe operations, and AuraMatch, forming the foundation for frontend integration.

## ✨ Key Features

- 👚 **Create My Outfit** — Accepts user profile details and styling preferences for personalized outfit recommendations.
- 🎨 **Correct My Outfit** — Handles outfit correction requests.
- 🪄 **AuraMatch** — Supports matching a desired style reference with wardrobe items.
- 👗 **Wardrobe Management** — Provides API functionality for managing wardrobe items.
- ⚡ **REST API** — Enables communication between the backend and frontend.
- 📚 **Interactive API Documentation** — Supports endpoint exploration and testing through Swagger UI.

## 🛠️ Tech Stack

| Technology     | Purpose                             |
| -------------- | ----------------------------------- |
| 🐍 Python      | Backend development                 |
| ⚡ FastAPI      | REST API framework                  |
| ✅ Pydantic     | Request validation and data schemas |
| 🗄️ SQLAlchemy | Database integration                |
| 💾 SQLite      | Local database storage              |
| 🚀 Uvicorn     | ASGI server                         |

## 📂 Project Structure

```text
OutfitAura/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   └── ...
│   ├── requirements.txt
│   └── ...
├── README.md
├── LICENSE
└── .gitignore
```

*Note: The structure above illustrates the expected layout. Refer to the actual repository for the complete file structure.*

## 🚀 Getting Started

### 📋 Prerequisites

- Python installed on your system
- pip package manager
- Git

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/manyasuresh113/OutfitAura.git
cd OutfitAura/backend
```

### 2️⃣ Create a Virtual Environment

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the Development Server

```bash
python -m uvicorn app.main:app --reload
```

### 5️⃣ Explore the API

Once the server is running, access the interactive documentation:

- 📘 **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- 📗 **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🔐 Security

- Keep API keys and sensitive credentials out of source control.
- Store secrets in environment variables.
- Exclude `.env` files and virtual environments from Git.
- Configure authentication and CORS appropriately before production deployment.

## 🚧 Project Status

**Currently in development.**

Ongoing development focuses on backend API functionality, outfit styling logic, wardrobe management, and frontend integration.

## 🔮 Future Enhancements

- 🤖 AI-powered outfit image generation
- 🎯 Enhanced outfit personalization
- 🔗 Complete frontend-backend integration
- 🧪 Automated testing and improved error handling
- ☁️ Production deployment

*These enhancements represent future work and are not claimed as completed features.*

## 👩‍💻 Author

**Anchal Rodrigues**

🌐 GitHub: [@]https://github.com/anchaR-creator

---


Made with ❤️ for smarter and more personalized fashion.

