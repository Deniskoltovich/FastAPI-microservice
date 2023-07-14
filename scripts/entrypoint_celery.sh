#!/bin/sh

celery -A app.celery_app worker -l info

exec "$@"