# 🌐 Multi-Tier Flask Web Application on AWS (Free Tier)

This project is a complete **multi-tier web application** built using:

- **Frontend**: HTML form via Flask Jinja templates
- **Backend**: Python (Flask)
- **Database**: Amazon RDS (MySQL)
- **Hosting**: AWS EC2 instance
- **Storage/Static Hosting**: AWS S3 (Optional UI/Docs)
- **Deployment**: Publicly accessible via EC2 Public IP

---

## 🚀 Project Objective

To build a scalable, cloud-hosted multi-tier architecture where:
- Users submit a form (name + email) through a web page
- Data is processed in real-time by a Flask backend
- Data is stored and retrieved from an Amazon RDS (MySQL) instance
- Hosted live on an AWS EC2 instance

---

## 🧠 Key Learnings

- 🔧 Set up an EC2 instance with security groups, Python, and Flask
- 🔐 Created a secure MySQL database on Amazon RDS and configured user access
- 🧪 Tested RDS connection from EC2 using PyMySQL
- 🧱 Built Flask backend (routes, templates, DB integration)
- 🎨 Designed simple frontend using Jinja2 + HTML forms
- 🌍 Made app live using EC2 public IP + port 5000
- 🛠️ Debugged MySQL connection errors, port issues, and tested end-to-end flow

---

## 🗂️ Folder Structure
multi-tier-flask-aws-app/
├── app.py # Flask application
├── config.py # Database credentials (do NOT expose in production)
├── requirements.txt # Python dependencies
├── templates/
│ ├── form.html # HTML form to add user
│ └── users.html # List of users
├── .gitignore # Ignore Python cache files
└── README.md # This documentation

## 🔧 Setup Instructions

### 1. Configure RDS (MySQL)

- Created MySQL DB instance via **Amazon RDS**
- DB Identifier: `sneha-db`
- Endpoint: `sneha-db.cl0m8aa8o62s.ap-south-1.rds.amazonaws.com`
- Username: `admin`
- Password: `password54321`
- Created database: `sneha_db` and table `users`

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
### 2. Setup EC2 (Ubuntu)
Launched EC2 instance (Amazon Linux/Ubuntu)

Installed Python, pip, Flask, pymysql:

sudo yum update -y
sudo yum install python3 git -y
pip3 install Flask pymysql
Allowed port 5000 in Security Groups for web access

### 3. Flask App
app.py(file already added)

### 4. HTML Templates
form.html(file already added)

### Final Output
Deployed URL (via EC2 Public IP):

http://13.126.202.53:5000
Access to:

/ — Add new user

/users — View all users in the DB

Screenshots added:
1- EC2 instance (Flask backend)
2- RDS database (sneha-db)
3- frontend
4- S3 bucket to store data of users
5- I added a user with it's name and email address
6- Made frontend a littlebit readable.

🧭 Roadmap Summary
Step	Description
✅ 1	Created RDS MySQL DB and table
✅ 2	Launched EC2, installed Python, Flask
✅ 3	Built app.py Flask routes
✅ 4	Connected to RDS using PyMySQL
✅ 5	Built frontend with HTML + Jinja
✅ 6	Made app live via EC2 public IP
✅ 7	Debugged DB access, 5000 port issues

🔐 Note
Do NOT push your real DB credentials (config.py) to GitHub in production.

For real deployment, use environment variables or AWS Secrets Manager.

👩‍💻 Author
Sneha Agrawal
Cloud & DevOps Enthusiast | Passionate about full-stack projects
🌐 GitHub: github.com/sneha020902
Linkedin:

💡 Future Enhancements
Add form validation
Use SQLAlchemy instead of raw SQL

Dockerize the Flask app
Host with domain + HTTPS using AWS Route 53 + ACM
ALL THE BEST!!
