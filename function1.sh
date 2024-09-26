#!/bin/bash

# Mendeklarasikan fungsi
nama() {
echo "Siapakah namamu?"
read nama
}
npm() {
echo "Sebutkan npm-mu!"
read npm
echo -e "Hai $nama dengan npm $npm, selamat datang \n di praktikum sistem operasi yang asyik ini ya!"
}

# Memanggil fungsi
nama
npm

