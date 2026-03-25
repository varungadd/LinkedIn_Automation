import role_configs.tech_config as tech
import role_configs.finance_config as fin
import role_configs.product_config as prod

from scraper.linkedin import fetch_jobs_for_role
from filters.filter import filter_jobs
from notifier.email_sender import send_email

import pandas as pd

def save_jobs(jobs, path):
    df = pd.DataFrame(jobs)
    df.to_csv(path, index=False)

def remove_duplicates(jobs):
    unique = {job['link']: job for job in jobs}
    return list(unique.values())

def main():
    print("Fetching jobs...")

    # 🔥 FETCH SEPARATELY FOR EACH ROLE
    tech_jobs_raw = fetch_jobs_for_role("software engineer intern")
    fin_jobs_raw = fetch_jobs_for_role("financial analyst intern")
    prod_jobs_raw = fetch_jobs_for_role("product manager intern")

    print(f"Raw Tech jobs: {len(tech_jobs_raw)}")
    print(f"Raw Finance jobs: {len(fin_jobs_raw)}")
    print(f"Raw Product jobs: {len(prod_jobs_raw)}")

    # 🔥 REMOVE DUPLICATES PER ROLE
    tech_jobs_raw = remove_duplicates(tech_jobs_raw)
    fin_jobs_raw = remove_duplicates(fin_jobs_raw)
    prod_jobs_raw = remove_duplicates(prod_jobs_raw)

    # 🔥 FILTER PER ROLE
    tech_jobs = filter_jobs(tech_jobs_raw, tech)
    fin_jobs = filter_jobs(fin_jobs_raw, fin)
    prod_jobs = filter_jobs(prod_jobs_raw, prod)

    print("After filtering:")
    print("Tech:", len(tech_jobs))
    print("Finance:", len(fin_jobs))
    print("Product:", len(prod_jobs))

    # 🔥 SAVE FILES
    save_jobs(tech_jobs, "data/tech_jobs.csv")
    save_jobs(fin_jobs, "data/finance_jobs.csv")
    save_jobs(prod_jobs, "data/product_jobs.csv")

    # 🔥 SEND EMAILS
    send_email(tech_jobs, "🚀 Tech Jobs")
    send_email(fin_jobs, "💰 Finance Jobs")
    send_email(prod_jobs, "📊 Product Jobs")

if __name__ == "__main__":
    main()