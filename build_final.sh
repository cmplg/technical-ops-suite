#!/bin/bash
set -e

echo "=== Building Technical Operations Suite ==="

cd ~/technical-ops-suite-build

# Setup virtual environment
if [ ! -d "techops_venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv techops_venv
fi

# Activate virtual environment
source techops_venv/bin/activate

# Install dependencies
echo "Installing PyInstaller..."
pip install pyinstaller > /dev/null 2>&1

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist *.spec

# Build application
echo "Building application with PyInstaller..."
pyinstaller --onefile --windowed --name technical-ops-suite src/main_fixed.py

# Update .deb package
echo "Updating .deb package..."
cp dist/technical-ops-suite deb-build/opt/technical-ops-suite/

# Build .deb package
echo "Building .deb package..."
fakeroot dpkg-deb --build deb-build output/technical-ops-suite_1.0.3_amd64.deb

echo ""
echo "=== BUILD SUCCESSFUL ==="
echo "Package created: output/technical-ops-suite_1.0.3_amd64.deb"
echo ""
echo "To install: sudo dpkg -i output/technical-ops-suite_1.0.3_amd64.deb"
echo "To test: /opt/technical-ops-suite/technical-ops-suite"
echo ""
echo "Features:"
echo "✅ Fixed error handling"
echo "✅ Safe messagebox calls"
echo "✅ Proper window management"
echo "✅ Logging system"
