#!bin/bash/sh

function panjang {
	echo "Masukkan panjang: "
	read panjang
}
function lebar {
	echo "Masukkan lebar: "
}
function luas {
	let luas=$panjang*$lebar
	echo "Luas Persegi: "
	echo $luas

#Memanggil fungsi
panjang
lebar
luas
