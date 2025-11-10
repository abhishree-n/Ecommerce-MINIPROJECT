# 🛒 E-Commerce Mini Project (Django)

## 📘 Overview
This is a **Full Stack Developer Hiring Assignment** – E-Commerce Mini Project built using **Django**.  
It includes both **user** and **admin** functionalities such as product management, order handling, and authentication.

---

## ⚙️ Tech Stack
- **Backend:** Django 5
- **Database:** SQLite (default)
- **Frontend:** Django Templates + Bootstrap
- **Authentication:** Django’s built-in auth system
- **Admin Panel:** Django Admin (for CRUD operations)

---

## 👥 User Features
✅ Register new user  
✅ Login / Logout  
✅ Browse product list  
✅ View product details  
✅ Place orders (Confirm Order → Success page)  

---

## 🧑‍💼 Admin Features
✅ Secure Admin Login (Django Admin Panel)  
✅ CRUD for Products (Create, Read, Update, Delete)  
✅ CRUD for Orders (View, Update Order Status)  
✅ View all users and their orders  

---

## 🚀 Setup Instructions

### 1. Clone or extract the project
```bash
unzip ecommerce.zip
cd ecommerce
```

### 2. Create virtual environment and activate
```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create admin user
```bash
python manage.py createsuperuser
```

### 6. Start the server
```bash
python manage.py runserver
```

Then open: 👉 **http://127.0.0.1:8000/**

---

## 🔑 Login Details

### 👥 **User**
Register directly from `/accounts/register/`

### 🧑‍💼 **Admin**
Access Django Admin at:
👉 **http://127.0.0.1:8000/admin/**

Use credentials created via:
```bash
python manage.py createsuperuser
```

---

## 📦 Folder Structure
```
ecommerce/
├── accounts/      # User authentication (register, login, logout, profile)
├── products/      # Product listing and details
├── orders/        # Order creation and management
├── templates/     # HTML templates (base.html, product pages, auth pages)
├── db.sqlite3     # Database
├── manage.py
└── README.md
```

---

## ✅ Project Status
| Feature | Status |
|----------|--------|
| User Registration/Login | ✅ |
| Product List & Details | ✅ |
| Order Placement | ✅ |
| Admin Login | ✅ |
| Product CRUD | ✅ |
| Order CRUD | ✅ |
| Dashboard / CSV Export | ⚠️ Optional (not required) |

---

## 🏁 Submission Note
This project meets all core requirements mentioned in  
📄 **“Full Stack Developer Hiring Assignment (E-Commerce Mini Project)”**
