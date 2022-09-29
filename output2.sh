#!/bin/bash

# inisialisasi var
x=50;
y=4;
distroLinux="Ubuntu 19.04 LTS";
let z=x%y;

# output printf
printf "x = $x\n"
printf "y = $y\n"
printf "OS : $distroLinux \n";
printf "$z \n";
printf "%.2f float \n" $x;
printf "%.1f float \n" $x;
printf "%.2f float \n" $y;
printf "%.1f float \n" $y;
