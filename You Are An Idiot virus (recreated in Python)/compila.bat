@echo off
pip install pyinstaller pygame
pyinstaller --onefile --noconsole --add-data "idiot.mp3;." app.py
pause
