# 🏋️‍♀️ CrossFit Auto-Registration Bot

This mini project was created to solve a daily problem for my girlfriend.  
She attends CrossFit training sessions that are held only once a week and are extremely popular. As a result, she often couldn’t sign up in time.  

This project automates the sign-up process to ensure she never misses a session again.  

---

## 🚀 How It Works

The project consists of two scripts:

- **`logger.py`** – Logs into the CrossFit account using credentials stored in a `.env` file and saves the session in cookies.  
- **`app.py`** – Uses the saved session to sign up for specific training sessions.  

The whole process runs automatically on a **VPS** using **cron jobs**.