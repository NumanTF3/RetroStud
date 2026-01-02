@echo off
setlocal

REM -----------------------------
REM Check if Python is installed
REM -----------------------------
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python 3.x first.
    pause
    exit /b
)

REM -----------------------------
REM Install dependencies
REM -----------------------------
echo Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt

REM -----------------------------
REM Build with PyInstaller
REM -----------------------------
echo Building EXE with PyInstaller...
pyinstaller --noconsole --onefile --windowed --icon=Logo.ico --add-data "Logo.ico;." "retrostud.py"

echo Done! The EXE is in the dist folder.
pause
