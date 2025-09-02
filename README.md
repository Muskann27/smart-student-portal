Added project overview and functionality details
# 🎓 Smart Student Portal with Analytics

A web-based platform for students and teachers to manage academic data and get insights to manage student records and attendance using **data analysis + machine learning**.  
Built with **Django, SQLite, HTML/CSS/JS, Pandas, Scikit-learn, Matplotlib**.
  
This project is part of my learning journey in Python, Django, and web development.  


## 🚀 Features
- 👩‍🎓 Student Dashboard → view grades, attendance, and performance graphs  
- 👨‍🏫 Teacher Dashboard → upload marks & attendance  
- 📊 Analytics → predict performance using ML & show insights  
- 🔐 Login/Signup with role-based access  

- Add and manage student details (Name, Roll Number, Email, Course, Year).  
- Track attendance (Subject, Date, Present/Absent).  
- Admin panel for easy management.  
- Extensible design for future features like results, notices, etc.  

---


## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Django  
- **Database:** SQLite  
- **Data Analysis/ML:** Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)  

---

## 📂 Project Structure
smart-student-portal/
│── portal/ # Main Django project
│ ├── home/ # Student app
│ ├── manage.py # Django project manager
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── .gitignore # Files to ignore in GitHub

---



# 📘 Project Functionality & Roles

## 🔹 Backend (Django + Database)
- Defines the **models**: `Student`, `Teacher`, `Marks`, `Attendance`.  
- Handles all the logic of storing, fetching, and processing data.  
- Not directly visible to students.  
- Used by **developers** and **admin panel**.

---

## 🔹 Frontend (Templates + Views)
- User-facing web pages (HTML, CSS, Django templates).  
- Students & teachers access these pages.  
- Example:
  - `/students/` → shows student directory.  
  - `/teachers/` → shows teacher list.  
  - `/marks/` → shows marks.  
  - `/attendance/` → shows attendance.  

👉 Data displayed here comes from the **backend (DB)**.

---

## 🔹 Django Admin Panel (`/admin/`)
- Part of the **backend**, but with a ready-made web interface.  
- Accessible only by **admins / staff (faculty, office staff)** with login credentials.  
- Allows non-technical users to manage the data:
  - Add / Edit / Delete **Students**
  - Add / Edit / Delete **Teachers**
  - Update **Marks**
  - Update **Attendance**

📌 Example Flow:  
- Admin adds “Parishi Mishra” in the Admin Panel.  
- The student appears automatically on `/students/` page (frontend).  

---

## 🧩 Summary
- **Frontend** → Students & teachers (view only).  
- **Backend (models + DB)** → Data storage & logic.  
- **Admin Panel** → Staff/faculty manage data without touching code.  

---

✨ This way, the system separates roles clearly:
- **Students/Teachers** → Only *view data*.  
- **Faculty/Admin Staff** → *manage data* via Admin Panel.  
- **Developer (you)** → Build & maintain backend/frontend.  


## ⚡ How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/Muskann27/smart-student-portal.git

2. Create a virtual environment & activate it.

3. Install dependencies:
   pip install -r requirements.txt

4. Run migrations:
   python manage.py migrate

5. Start the server:
   python manage.py runserver

6. Open http://localhost:8000 in your browser.


Author

Muskan Behl
Aspiring GDG On Campus Lead | Computer Science Student

⭐ If you like this project, give it a star!









