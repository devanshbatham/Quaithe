#!/bin/bash

# Define the install directory for the shadowclone.py script
INSTALL_DIR="/usr/local/bin"

# Copy the shadowclone.py script to the install directory
sudo cp shadowclone.py "$INSTALL_DIR/shadowclone"

# Make the shadowclone.py script executable
sudo chmod +x "$INSTALL_DIR/shadowclone"

echo "ShadowClone: Command Parallelizer has been installed successfully!"