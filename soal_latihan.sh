#!/bin/bash

echo "Masukkan bilangan acuan kelipatan ganjil turun: "
read a

echo "Kelipatan ganjil turun."
for ((a=$a; a>=1; a=a-2))
do
   echo $a
done

echo "Masukkan bilangan acuan kelipatan ganjil naik: "
read b

echo "Kelipatan ganjil naik."
until [ ! $b -lt 100 ]
do
  echo $b
  b=$((b+2))
done 

