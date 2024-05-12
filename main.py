import requests as rq
import logging

logger = logging.getLogger('RequestsLogger')
logging.basicConfig(level=logging.INFO)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        if response.status_code == 200:
            logger.info(f'{site}, response - 200')
            with open('success_responses.log', 'a') as f:
                f.write(f'INFO: {site}, response - 200\n')
        elif response.status_code != 200:
            logger.warning(f'{site}, response - {response.status_code}')
            with open('bad_responses.log', 'a') as f:
                f.write(f'WARNING: {site}, response - {response.status_code}\n')
    except rq.exceptions.ConnectionError:
        logger.error(f'{site}, NO CONNECTION')
        with open('blocked_responses.log', 'a') as f:
            f.write(f'ERROR: {site}, NO CONNECTION\n')