from scraper.linkedin import fetch_linkedin_jobs
from filters.filter import filter_jobs
import role_configs.tech_config as config

jobs = fetch_linkedin_jobs()

filtered_jobs = filter_jobs(jobs, config)

print("Total jobs:", len(jobs))
print("Filtered jobs:", len(filtered_jobs))