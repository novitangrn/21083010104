echo "Berapa jumlah semester anda?"
read jumlah

echo "================================================"

echo "Masukkan IPS Anda (1 hingga semester terakhir): "
echo "Gunakan spasi sebagai pemisah. Contoh 3 4 4/4 3 3 2"

read -a array

echo "==============================================="

#sum=$( IFS=+; bc <<< ${array[*]}" )

tot=0
for i in "${array[@]}"; do
  tot=$(echo $tot + $i | bc -l);
done

echo "Total = ${tot}"

echo "Indeks Prestasi Semester: $tot/$jumlah"
echo "Indeks Prestasi Kumulatif: "

echo "scale=2; $tot / $jumlah" | bc

#printf %.2f\\n "$((($tot) / $jumlah))"
