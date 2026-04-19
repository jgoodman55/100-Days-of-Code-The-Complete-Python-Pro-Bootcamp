# 🎂 Automated Birthday Email Sender

A Python automation script that sends personalized birthday emails using pre-written templates and a CSV file of recipients.

---

## 📌 Overview

This project automatically checks for birthdays on the current date and sends a customized email to each matching recipient. It selects a random template, replaces placeholders with real data, and delivers the email via SMTP.

This project demonstrates:
- Automation workflows
- Data processing with pandas
- Email handling with smtplib
- File and template management
- Date-based logic

---

## 📂 Project Structure

```
.
├── main.py
├── birthdays.csv
├── letter_templates/
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── python_mail.txt
```

---

## ⚙️ How It Works

1. Load birthday data from CSV
2. Match today's date
3. Select a random template
4. Replace [NAME] with recipient name
5. Send email via SMTP

---

## 🧾 Example birthdays.csv

```
name,email,year,month,day
John Doe,john@example.com,1990,4,19
```

---

## 🔐 Setup

1. Install dependencies:
   pip install pandas

2. Add your email password to python_mail.txt

3. Update your email in main.py

4. Run:
   python main.py

---

## ⚠️ Notes

- Use Gmail App Passwords (recommended)
- Do not commit sensitive files

---

## 🚀 Improvements

- Add logging
- Use environment variables
- Add retry logic
- Support HTML emails
- Schedule execution

---

## 📄 License

Free to use for personal or educational purposes.
