#!/bin/sh

cd /app

exec gunicorn \
        -n bsport \
        -w ${NUM_WORKERS:-8} \
        -t ${TIMEOUT:-300} \
        -b 0.0.0.0:8000 \
        -k uvicorn.workers.UvicornWorker \
        --log-level=info \
        --access-logfile=- \
        --error-logfile=- \
        src.asgi:application
