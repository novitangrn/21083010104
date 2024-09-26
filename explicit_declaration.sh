#!/bin/bash

# deklarasi array 
declare -a angka

#clear
i=0;
while [ $i -le 6 ];
do
   let isi=$i*2;
   angka[$i]=$isi;
   let i=$i+1;
done

# menampilan semua elemen array dengan index * atau @
echo ${angka[@]}
