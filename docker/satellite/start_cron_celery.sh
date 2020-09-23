#!/usr/bin/env bash
source /opt/conda/bin/activate base
which python
python docker/satellite/setup.py develop &
# make -f docker/satellite/Makefile configure_ci_satellite_app &
exec celery worker -A satellite_app.celeryapp -l info --concurrency=4 &
cron && tail -f /var/log/cron.log
