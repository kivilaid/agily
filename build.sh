#!/bin/bash

# Build script with increased memory allocation
DOCKER_BUILDKIT=1 docker build --memory=8g --memory-swap=8g -t open-webui .
