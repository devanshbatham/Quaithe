#!/bin/bash

# Define the install directory for the quaithe.py script
INSTALL_DIR="/usr/local/bin"

# Copy the quaithe.py script to the install directory
sudo cp quaithe.py "$INSTALL_DIR/quaithe"

# Make the quaithe.py script executable
sudo chmod +x "$INSTALL_DIR/quaithe"

echo "Quaithe: Command Parallelizer has been installed successfully!"