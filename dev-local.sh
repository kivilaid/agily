#!/bin/bash

# Local development script with increased memory allocation
export NODE_OPTIONS=--max-old-space-size=8192 && npm run dev
