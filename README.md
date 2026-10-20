# Auto Attendance System Using Face Recognition

## Overview
Auto Attendance is a face recognition-based attendance management system built with Python and Streamlit. It automates student identification and attendance tracking, helping simplify classroom attendance management.

## Features
- **Face Recognition:** Identifies students using facial embeddings and machine learning.
- **Automated Attendance:** Streamlines attendance recording for enrolled students.
- **Teacher Management:** Supports teacher registration and login.
- **Student Management:** Allows student registration and student data management.
- **Subject Management:** Enables teachers to create subjects and manage student enrollment.
- **Attendance Tracking:** Stores and retrieves student attendance records.
- **Database Integration:** Uses Supabase to manage student, teacher, subject, and attendance data.

## Tech Stack
- **Language:** Python
- **Frontend:** Streamlit
- **Face Recognition:** Dlib, face_recognition_models
- **Machine Learning:** Scikit-learn (Support Vector Machine — SVM)
- **Database:** Supabase
- **Data Processing:** NumPy, Pandas

## How It Works
1. Teachers register and log in to the system.
2. Teachers create subjects and manage student enrollment.
3. The system extracts facial embeddings from student images.
4. A trained SVM classifier identifies students based on their facial features.
5. Attendance records are stored and retrieved through the database.

## Installation and Setup

### 1. Clone the Repository
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

Activate it on Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
If your project contains a `requirements.txt` file, run:
```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your project and add them to a requirements file.

### 4. Configure Supabase
Create a Supabase project and configure the required credentials in `.streamlit/secrets.toml`, following the secret names expected by your application.

**Important:** Never commit API keys, passwords, or other secrets to GitHub.

### 5. Run the Application
```bash
streamlit run app.py
```

Replace `app.py` with your actual Streamlit entry-point filename if it is different.

## Future Improvements
- Improve recognition accuracy under different lighting conditions.
- Add attendance reports with export options.
- Introduce role-based access control.
- Enhance attendance analytics and reporting.

## Author
**Miral Abhangi**

- GitHub: [miralabhangi13](https://github.com/miralabhangi13)
- LinkedIn: [Miral Abhangi](https://www.linkedin.com/in/miral-abhangi-a17b54391/)
