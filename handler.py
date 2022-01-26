import json
import os
from scrapinghub import ScrapinghubClient


def lambda_handler(event, context):

    scraping_hub_key = os.environ['scraping_hub_key']
    client = ScrapinghubClient(scraping_hub_key)
    project = client.get_project(494606)
    spider = project.spiders.get('job')
    spider.jobs.run(job_settings={'DELTAFETCH_ENABLED': 'False'})

    body = {
        "message": "success!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
