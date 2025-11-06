#!/bin/bash
echo "python3 $(pwd)/todo-app.py" | sudo tee /usr/local/bin/todo
sudo chmod +x /usr/local/bin/todo
