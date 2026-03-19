
# NGO CMS Website – Assignment 3

## 📌 Project Overview

This project is a **dynamic NGO website with a custom admin dashboard**, developed using **Django (Python)**.
It allows administrators to manage website content such as mission, vision, programs, team members, and impact directly from a custom-built dashboard instead of Django’s default admin panel.

---

## 🚀 Features

### 🔹 Frontend (User Side)

* Responsive NGO homepage
* Dynamic content rendering from database
* Sections included:

  * Our Story
  * Core Values
  * Programs
  * Meet Our Team
  * Mission & Vision
  * Impact Statistics

---

### 🔹 Admin Dashboard (Custom Built)

* Separate admin dashboard UI (HTML + CSS)
* Manage all website content:

  * ➕ Add new data
  * ✏️ Edit existing content (for some sections)
  * ❌ Delete records
* Modules:

  * Core Values
  * Programs
  * Team
  * Impact
  * Mission & Vision
  * Our Story

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Django (Python)
* **Database:** SQLite
* **Template Engine:** Django Templates

---

## 📂 Project Structure

```
ngo_cms/
│
├── accounts/                # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── templates/
│   ├── index.html           # Homepage
│   ├── login.html
│   ├── register.html
│   └── admin/               # Custom admin dashboard pages
│       ├── dashboard.html
│       ├── core_values.html
│       ├── programs.html
│       ├── team.html
│       ├── impact.html
│       ├── mission.html
│       └── story.html
│
├── static/
│   └── images/
│
├── db.sqlite3
└── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd ngo_cms
```

### 2️⃣ Create Virtual Environment (optional)

```
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install django
```

### 4️⃣ Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run Server

```
python manage.py runserver
```

---

## 🌍 Usage

### 🔹 Homepage

```
http://127.0.0.1:8000/
```

### 🔹 Custom Admin Dashboard

```
http://127.0.0.1:8000/admin-dashboard/
```

From the dashboard, you can:

* Add core values
* Manage programs
* Add team members
* Update mission & vision
* Track impact stats

---

## 📸 Screenshots (Optional)

<img width="940" height="467" alt="image" src="https://github.com/user-attachments/assets/266109fc-4a13-4eed-a605-ad23131b1306" />
<img width="940" height="435" alt="image" src="https://github.com/user-attachments/assets/7d1e046b-0b0a-40bf-ae7b-51ce84cabc0f" />
<img width="940" height="353" alt="image" src="https://github.com/user-attachments/assets/460c3ea0-6105-4b7a-bd2b-f4e55d324725" />
<img width="940" height="297" alt="image" src="https://github.com/user-attachments/assets/c034e1d7-851c-45a4-ba89-4657ff917fc0" />

<img width="940" height="377" alt="image" src="https://github.com/user-attachments/assets/ce5c2ccf-1ccf-4294-9577-8bb5315eee41" />
<img width="940" height="479" alt="image" src="https://github.com/user-attachments/assets/8a3706e2-7da2-42ef-8c70-c0aa7c49c833" />
<img width="940" height="408" alt="image" src="https://github.com/user-attachments/assets/9218ffd9-15f6-49b8-b5da-0948628eb321" />



---

## 🎯 Learning Outcomes

* Built a dynamic website using Django
* Created a custom admin dashboard (without default Django admin)
* Implemented CRUD operations (Create, Read, Update, Delete)
* Connected frontend with backend database
* Structured a full-stack web application

---

## 📌 Conclusion

This project demonstrates how a **content management system (CMS)** can be built using Django, enabling non-technical users to update website content easily through a custom interface.

---

## 👩‍💻 Author

**Vanshika Sahani**
Internship Assignment – 3

---
