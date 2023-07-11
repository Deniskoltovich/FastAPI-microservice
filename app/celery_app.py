import os

from celery.app import Celery
from celery.schedules import crontab

redis_url = os.environ.get("BROKER_REDIS_URL")

celery_app = Celery(__name__, broker=redis_url, backend=redis_url)
celery_app.autodiscover_tasks(['app.assets.tasks'])

celery_app.conf.beat_schedule = {
    'parse-every-minute': {
        'task': 'app.assets.tasks.parse_assets',
        'schedule': crontab(),
        'args': (('IBM', 'AAPL', 'A', 'ADBE', 'AVK', 'BL'),),
    }
}

celery_app.conf.timezone = 'UTC'


if __name__ == '__main__':
    celery_app.start()
