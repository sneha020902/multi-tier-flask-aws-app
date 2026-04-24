# 🌐 Multi-Tier Flask Web Application on AWS

> A full-stack, cloud-deployed web application built with a proper 3-tier architecture — frontend, backend, and database — all running on AWS.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=flat-square&logo=amazonec2&logoColor=white)
![Amazon RDS](https://img.shields.io/badge/Amazon_RDS-527FFF?style=flat-square&logo=amazonrds&logoColor=white)

---

## 🧩 The Problem

Most beginners deploy apps locally and call it done. Real cloud engineering means separating concerns — your frontend, backend, and database should be independent, scalable, and properly secured. This project replicates that pattern on AWS.

---

## 🏗️ Architecture

```
 User Browser
      │
      ▼
 AWS EC2 (Ubuntu)
 └── Flask App (port 5000)
      ├── Jinja2 HTML Templates (Frontend)
      ├── Flask Routes (Backend Logic)
      └── PyMySQL ──────────────────▶ Amazon RDS (MySQL)
                                          └── sneha_db.users table
```

**3 Tiers:**
| Tier | Technology | Where |
|---|---|---|
| Frontend | HTML + Jinja2 Templates | EC2 |
| Backend | Python + Flask | EC2 |
| Database | MySQL via PyMySQL | Amazon RDS |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python & Flask | Backend web framework |
| Jinja2 | Server-side HTML templating |
| Amazon EC2 (Ubuntu) | App server in the cloud |
| Amazon RDS (MySQL) | Managed relational database |
| PyMySQL | Python → MySQL connector |
| AWS Security Groups | Network access control |

---

## ✨ Features

- Submit a user form (name + email) via a web page
- Flask backend processes and validates the input
- Data is stored in an **Amazon RDS MySQL** database
- View all submitted users at `/users`
- Deployed live on an EC2 public IP

---

## 🚀 How to Run It Yourself

### Prerequisites
- AWS account (Free Tier works)
- EC2 instance (Ubuntu 22.04)
- Amazon RDS MySQL instance

### Step 1 — Set Up RDS (MySQL)
Create a MySQL DB instance in Amazon RDS, then run:

```sql
CREATE DATABASE sneha_db;
USE sneha_db;
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);
```

### Step 2 — Set Up EC2
```bash
ssh -i your-key.pem ubuntu@your-ec2-public-ip
sudo apt update && sudo apt install -y python3 python3-pip git
pip3 install flask pymysql
```

### Step 3 — Configure the App
Edit `config.py` with your RDS credentials:
```python
DB_HOST = 'your-rds-endpoint'
DB_USER = 'your-username'
DB_PASSWORD = 'your-password'
DB_NAME = 'sneha_db'
```
> ⚠️ **Never push real credentials to GitHub.** Use environment variables or AWS Secrets Manager in production.

### Step 4 — Run the App
```bash
git clone https://github.com/sneha020902/multi-tier-flask-aws-app.git
cd multi-tier-flask-aws-app
python3 app.py
```

### Step 5 — Access the App
Open your browser at `http://your-ec2-public-ip:5000`
Make sure port **5000** is open in your EC2 Security Group.

---

## 💡 What I Learned

- How to design and deploy a proper **3-tier architecture** on AWS
- Configuring and connecting to **Amazon RDS** from an EC2 instance
- Using **PyMySQL** to run queries from Python
- Managing **AWS Security Groups** to allow specific port traffic
- Debugging real cloud issues: DB connection timeouts, port conflicts, IAM permissions
- Why **never to hardcode credentials** and how to use config files safely

---

## 🔮 Future Improvements

- [ ] Dockerize the Flask app for consistent deployments
- [ ] Replace raw SQL with **SQLAlchemy ORM**
- [ ] Add form validation and error handling
- [ ] Set up **HTTPS** with AWS ACM + Load Balancer
- [ ] Use **AWS Secrets Manager** for credential management
- [ ] Add a **CI/CD pipeline** with GitHub Actions

---

## 👩‍💻 Author

**Sneha Agrawal** — Aspiring Cloud & DevOps Engineer
🔗 [LinkedIn](https://www.linkedin.com/in/-snehaagrawal/) · [GitHub](https://github.com/sneha020902) · [Portfolio](https://sneha020902.github.io)
