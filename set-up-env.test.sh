#!/bin/bash

# Django
echo "SECRET_KEY=$SECRET_KEY" >> .env
echo "DEBUG=$DEBUG" >> .env
echo "ALLOWED_HOSTS=$ALLOWED_HOSTS" >> .env
echo "CORS_ALLOWED_ORIGINS=$CORS_ALLOWED_ORIGINS" >> .env