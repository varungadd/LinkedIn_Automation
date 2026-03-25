# 🚀 LinkedIn Job Automation System

An automated Python-based pipeline that scrapes job listings, filters them by role, and sends structured email alerts — helping streamline the job search process efficiently.

---

## 📌 Overview

This project automates the process of discovering and organizing job opportunities from LinkedIn.

Instead of manually searching and applying, the system:

* Scrapes job listings
* Categorizes them into roles (Tech, Finance, Product)
* Filters relevant opportunities
* Sends structured email alerts
* Saves results into CSV files for tracking

---

## ⚙️ Features

### 🔍 Job Scraping

* Fetches job listings from LinkedIn
* Supports role-based keyword search

### 🧠 Role-Based Filtering

Separate pipelines for:

* 🚀 Tech Roles
* 💰 Finance Roles
* 📊 Product Roles

Each role has:

* Custom keywords
* Exclusion filters
* Clean separation (no overlap)

### 📧 Automated Email Alerts

* Sends role-wise job lists to your email
* Structured format for easy reading

### 📁 Data Storage

* Saves results into CSV files:

  * `data/tech_jobs.csv`
  * `data/finance_jobs.csv`
  * `data/product_jobs.csv`

### 🧹 Deduplication

* Removes duplicate job listings using unique links

---

## 🏗️ Project Structure

```
linkedin_automation/
│
├── main.py
├── config.py
│
├── scraper/
│   └── linkedin.py
│
├── filters/
│   └── filter.py
│
├── notifier/
│   └── email_sender.py
│
├── role_configs/
│   ├── tech_config.py
│   ├── finance_config.py
│   └── product_config.py
│
├── data/
│   ├── tech_jobs.csv
│   ├── finance_jobs.csv
│   └── product_jobs.csv
```

---

## 🚀 How It Works

1. Fetch jobs for each role separately
2. Remove duplicate listings
3. Apply role-specific filters
4. Save results to CSV
5. Send email alerts

---

## ▶️ Running the Project

```bash
python3 -m main
```

---

## ⚡ Example Output

```
Raw Tech jobs: 80
Raw Finance jobs: 40
Raw Product jobs: 35

After filtering:
Tech: 30
Finance: 15
Product: 10
```

---

## 🔧 Configuration

Update `config.py` with your credentials:

```python
EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"
```

---

## 📌 Future Improvements

* 🔥 Multi-keyword job fetching per role
* 📊 Job ranking system (ML-based relevance scoring)
* 🤝 Recruiter discovery and outreach automation
* ⏰ Scheduled daily automation (cron jobs)

---

## ⚠️ Disclaimer

This project uses publicly accessible job listings.
It does **not automate job applications** or violate LinkedIn policies.

---

## 💡 Motivation

The goal of this project is to:

* Reduce manual job search effort
* Improve targeting of relevant roles
* Build a scalable automation system for career opportunities

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub and feel free to contribute!

---
