import requests
from bs4 import BeautifulSoup

def fetch_jobs_for_role(keyword, location="India"):
    headers = {"User-Agent": "Mozilla/5.0"}

    query = keyword.replace(" ", "%20")
    url = f"https://www.linkedin.com/jobs/search/?keywords={query}&location={location}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job in soup.find_all("div", class_="base-card"):
        try:
            title = job.find("h3").text.strip()
            company = job.find("h4").text.strip()
            link = job.find("a")["href"]

            jobs.append({
                "title": title,
                "company": company,
                "link": link
            })
        except:
            continue

    return jobs