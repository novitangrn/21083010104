#!/bin/bash

# deklarasi array
distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian" "CentOS" "Fedora")

# random distro
let pilih=$RANDOM%7

# eksekusi
echo "Saya Memilih Distro $pilih, ${distroLinux[$pilih]}!"

