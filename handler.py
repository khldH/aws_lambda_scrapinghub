import json
import os
from scrapinghub import ScrapinghubClient

print('here')
scraping_hub_key = os.environ['scraping_hub_key']
client = ScrapinghubClient(scraping_hub_key)
project = client.get_project(494606)
spider = project.spiders.get('job')
spider.jobs.run(job_settings={'DELTAFETCH_ENABLED': 'False'})
print(scraping_hub_key)
print(project.spiders)

# def lambda_handler():
#     scraping_hub_key = os.environ['scraping_hub_key']
#     client = ScrapinghubClient(scraping_hub_key)
#     project = client.get_project(494606)
#     spider = project.spiders.get('job')
#     spider.jobs.run(job_settings={'DELTAFETCH_ENABLED': 'False'})
#     print(scraping_hub_key)
#     print(project.spiders)

    # return {"statusCode": 200, "body": json.dumps(body)}
