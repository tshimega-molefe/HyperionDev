#!/bin/bash
clear

# Create three directory folders
mkdir frontend
mkdir docker
mkdir backend

echo "Three directories created: frontend, docker, and backend"

# Change directory to one of the folders we previously created
cd frontend

# Create three directory folders inside the parent folder

mdkir server
mkdir lib
mkdir src

# Remove two folders I previously created in the parent layer

rm -r ../docker
rm -r ../backend
