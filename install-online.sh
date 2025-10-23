#!/bin/bash
echo "📦 Installing Technical Operations Suite..."
wget -q https://github.com/cmplg/technical-ops-suite/raw/main/technical-ops-suite_1.0.3_amd64.deb -O /tmp/tos.deb
sudo dpkg -i /tmp/tos.deb || sudo apt install -f -y
rm /tmp/tos.deb
echo "✅ Installation complete!"
echo "🚀 Run: /opt/technical-ops-suite/technical-ops-suite"
