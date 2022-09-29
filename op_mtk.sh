#!/bin/bash

x=100
y=20

# memakai let
let jumlah=$x+$y
let kurang=$x-$y
let kali=$x*$y

#memakai expr
bagi='expr $x/$y'

# memakai perintah substitusi $((ekspresi))
mod=$(($x % $y))

echo "x = $x"
echo "y = $y"
echo "x + y = $jumlah"
echo "x - y = $kurang"
echo "x * y = $kali"
echo "x / y = $bagi"
echo "x % y = $mod"

x=$y
echo "menyamakan nilai x dan y"
echo "x = $x"
echo "y = $y"
