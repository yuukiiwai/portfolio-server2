#!/bin/bash
# Django
echo "SECRET_KEY=$SECRET_KEY" >> portfolio/.env
echo "DEBUG=$DEBUG" >> portfolio/.env
echo "ALLOWED_HOSTS=$ALLOWED_HOSTS" >> portfolio/.env
echo "CORS_ALLOWED_ORIGINS=$CORS_ALLOWED_ORIGINS" >> portfolio/.env
