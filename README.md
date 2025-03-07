# Coupon Management System

## 📌 Overview
This project is a **Flask-based REST API** for managing discount coupons, supporting **MongoDB** as the database. It uses **Pydantic** for data validation, **JWT authentication**, and is structured following **MVC principles**.

## 🚀 Features
- **Endpoint operations for coupons** (MongoDB)
- **Secure authentication** (JWT)
- **Advanced condition checking** (category, price, date range, AND/OR/NOT logic)
- **Unit & Integration tests** with `pytest`
- **Code linting & formatting** (`flake8`, `pylint`)
- **Docker support** for containerized deployment

## 📂 Project Structure
```
coupon_management/
│── app/                     # Main application folder
│   ├── __init__.py          # Package initialization
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   ├── config_base.py   # MongoDB connection
│   │   ├── coupon.py        # Coupon model
│   │   ├── user.py          # user model
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── coupon_service.py
│   ├── controllers/         # API routes (Flask)
│   │   ├── __init__.py
│   │   ├── coupon_controller.py
│   │   ├── auth_controller.py
│   ├── security/            # Security (auth, validation)
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── validation.py
│   ├── utils/               # Utility functions
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   ├── config.py        # Environment variables management
│   ├── app.py                # Entry point
│── tests/                    # Unit & integration tests
│   ├── __init__.py
│   ├── test_coupon.py
│   ├── test_auth.py
│── logs/  
│── htmlcov/  
│── requirements.txt          # Dependencies
│── .env                      # Environment variables
│── .gitignore                # Git ignored files
│── docker-compose.yml        # Docker for development setup
│── Dockerfile                # Docker containerization
│── pytest.ini                # Pytest configuration
│── coverage.xml              # Test coverage report
│── README.md                 # Project documentation
│── remlpir_db.py             # database
│── run.py 
```

## 🛠 Setup Instructions
### **1️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```

### **2️⃣ Setup environment variables**
Create a `.env` file:
```bash
SECRET_KEY=your_secret_key
MONGO_URI=mongodb://localhost:27017/
```

### **3️⃣ Run the application**
```bash
python run.py
```

### **4️⃣ Run tests & coverage**
```bash
pytest --cov=app --cov-report=xml
```

### **5️⃣ Linting & Formatting**
```bash
flake8 app/
pylint app/
```

### **6️⃣ Run the application in Docker**
```bash
docker-compose up --build