#!/bin/bash

echo "Masukkan bilangan acuan kelipatan ganjil turun: "
read a

while [ $((a%2)) -eq 1 ]
do
  echo "Kelipatan ganjil turun."
  for ((a=$a; a>=1; a=a-2))
  do
     echo $a
  done
done

echo "Masukkan bilangan acuan kelipatan ganjil naik: "
read b
echo "Bilangan ganjil naik."
while [ $((b%2)) -eq 1 ]
do
  until [ ! $b -lt 100 ]
  do
    echo $b
    b=$((b+2))
  done
done

echo "Selesai"
