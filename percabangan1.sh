# If - Else

x=102
y=52

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
