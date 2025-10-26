#!/bin/bash

# Link download langsung ke file .deb dari GitHub Releases Anda
DEB_URL="https://github.com/cmplg/technical-ops-suite/releases/download/v1.1-1/technical-ops-suite_1.0.0_all.deb"

# Lokasi penyimpanan file sementara
DEB_FILE="/tmp/technical-ops-suite.deb"

echo "Mengunduh Technical Ops Suite..."
# -L untuk mengikuti redirect, -o untuk menyimpan ke file
curl -L -o "$DEB_FILE" "$DEB_URL"

echo "Menginstal paket aplikasi (membutuhkan password)..."
# Menggunakan 'apt install' untuk menangani dependensi secara otomatis
sudo apt install "$DEB_FILE" -y

echo "Membersihkan file sisa..."
rm "$DEB_FILE"

echo ""
echo "======================================================"
echo "  Instalasi Selesai!"
echo "  Aplikasi 'Technical Ops Suite' siap digunakan."
echo "  Cari ikonnya di menu aplikasi Anda."
echo "  Jangan Cabul, jangan melecehkan, nanti apes."
echo "======================================================"