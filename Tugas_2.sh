#!bin/bash

printf "Apakah anda bisa matematika? (y/n) "
read bisa

case "$bisa" in
  "y")
   echo "Oke, lanjut ke soal!"
   ;;
  "n")
   echo "Kamu harus berlatih soal!"
   ;;
  *)
   echo "Yuk, kamu harus berlatih."
   ;;
esac

x=110
y=101

let jumlah=$x+$y
kurang='expr $x - $y'
kali=$(($x*$y))
bagi=$(($x/$y))
mod=$(($x%$y))

printf "Berapakah $x + $y?  "
read jawab1

if [ $jawab1 == $jumlah ]
then
  echo "Nice!"
else
  echo "Wah, salah!"
fi

printf "Berapakah $x - $y?  "
read jawab2

case "$jawab2" in
  "9")
   echo "Nice!"
   ;;
  *)
   echo "Wah, salah!"
   ;;
esac

printf "Yuk lihat operasi matematika lainnya!\n"
printf "Ketik apapun untuk melanjutkan\n"
read lanjut

echo "x * y = $kali"
echo "x / y = $bagi"
echo "x % y = $mod"

echo "x = $x"
echo "y = $y"

if [ $x == $y ]
then
  echo "x sama dengan y" 
elif [ $x -gt $y ]
then
  echo "x lebih besar daripada y"
elif [ $x -lt $y ]
then
  echo "x lebih kecil daripada y"
else
  echo "Tidak ada kondisi yang memenuhi"
fi
