#!/bin/bash

# Start frontend dev server and wait for it to initialize
npm run dev &

# Wait a few seconds for the frontend to start initializing
sleep 3

# Change to backend directory and run dev.sh
cd backend && sh dev.sh
