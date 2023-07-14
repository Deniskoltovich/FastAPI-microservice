#!/bin/sh

celery -A app.celery_app beat -l info

exec "$@"