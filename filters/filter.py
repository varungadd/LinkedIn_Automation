def filter_jobs(jobs, config):
    filtered = []

    for job in jobs:
        title = job["title"].lower()

        # ✅ strict keyword match
        if any(k.lower() in title for k in config.KEYWORDS):

            # exclude unwanted roles
            if not any(ex.lower() in title for ex in config.EXCLUDE):
                filtered.append(job)

    return filtered