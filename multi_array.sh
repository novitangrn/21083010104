#!/bin/bash

# deklarasi array
array2dimensi="1.1:1.2:1.3:1.4:1.5 2.1:2.2:2.3:2.4:2.5 3.1:3.2:3.3:3.4:3.5"

function dimensiBaris {
    for baris in $array2dimensi
    do
        dimensiKolom `echo $baris | tr : " "`
    done
}

function dimensiKolom {
    for kolom in $*
    do
        echo -n $kolom " "
    done
    echo
}

# memanggil fungsi
dimensiBaris
