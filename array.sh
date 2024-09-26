#!/bin/bash

# deklarasi array
distroLinux=("Mint" "Ubuntu" "Kali" "Arch" "Debian" "CentOS" "Fedora")

# random distro
let pick=$RANDOM%7

# eksekusi
echo "Saya Memilih Distro $pick, ${distroLinux[$pick]}!"

