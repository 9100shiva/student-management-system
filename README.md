📚 Student Management System

A simple and efficient Student Management System built using Python, Flask, SQL (SQLite/MySQL), HTML, CSS, JavaScript.
This project helps manage student details with full CRUD operations — Create, Read, Update, Delete.

🚀 Features

➕ Add New Students

📄 View All Students

✏️ Update Student Details

❌ Delete Student Records

🔍 Search Student by ID or Name

🗄️ Database Integration (SQLite/MySQL)

🎨 Frontend using HTML, CSS, Bootstrap

🖥️ Backend using Flask (Python)

🛠️ Tech Stack
Layer	Technology
Frontend	HTML, CSS, Bootstrap, JavaScript
Backend	Python, Flask Framework
Database	SQLite (default) or MySQL
Tools	VS Code, Git, GitHub
📂 Folder Structure
student-management-system/
│
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── static/               # CSS, JS, Images
│   ├── style.css
│   └── script.js
├── templates/            # HTML Templates
│   ├── index.html
│   ├── add_student.html
│   ├── edit_student.html
│   └── students.html
└── database/
    └── students.db       # SQLite database file

⚙️ Installation & Setup
✔️ 1. Clone the Repository
git clone https://github.com/9100shiva/student-management-system.git
cd student-management-system

✔️ 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # For Windows

✔️ 3. Install Dependencies
pip install -r requirements.txt

✔️ 4. Run the Application
python app.py


➡️ Open the browser and go to:
http://127.0.0.1:5000/

📸 Screenshots (Optional)

You can add images like:

![Dashboard](static/screenshots/dashboard.png)

🧠 How It Works

User interacts with UI (HTML forms)

Flask handles routes (/add, /edit, /delete, /students)

SQL queries store and fetch data from database

Data is displayed in a clean Bootstrap table

🚧 Future Enhancements

🔐 Admin Login System

📊 Student Dashboard with Charts

📝 Import/Export Excel

🔍 Advanced Search & Filters

☁️ Deploy on Heroku / Render / PythonAnywhere
