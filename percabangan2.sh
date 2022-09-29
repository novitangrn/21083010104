#!/bin/bash
printf "Model looseleaf apa yang kamu suka?\n"
printf "Polos?\n"
printf "Line?\n"
printf "Grid?\n"
printf "Atau berwarna?\n"

read model

case $model in
  "polos")
    echo "model polos cocok untuk coret-coret"
    ;;
  "line")
    echo "model line cocok untuk mencatat"
    ;;
  "grid")
    echo "model grid cocok untuk matematika"
    ;;
  "berwarna")
    echo "model berwarna cocok untuk hiasan"
    ;;
  *)
    echo "model yang kamu masukkan tidak ada."
    ;;
esac
