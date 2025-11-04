#!/bin/bash
# Author: Christos Georgiades
# 27-10-2025

python -m venv todo-app
source todo-app/bin/activate  # On Windows: gkeepenv\Scripts\activate

# Install gkeepapi
pip install gkeepapi
pip install curses 
# Verify installation
python -c "import gkeepapi; print('gkeepapi installed successfully!')"
