#!/usr/bin/env bash

celery -A tasks worker -c 1 --loglevel=info
