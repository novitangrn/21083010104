from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def angka(i):
   if i%2 == 0:
      print(i+1, "Ganjil - ID Proses", getpid())
   else:
     print(i+1, "Genap - ID Proses", getpid())
   sleep(1)

lim = int(input("Masukkan input: "))

#Sekuensial
first_seq = time()
print("\n Sekuensial")
for i in range(lim):
  angka(i)
last_seq = time()


#multiprocessing.Process
print("\n multiprocessing.Process")
array_proses = []
first_process = time()
for i in range(lim):
    proses = Process(target=angka, args=(i, ))
    array_proses.append(proses)
    proses.start() 
for i in array_proses:
    proses.join()
last_process = time()


#multiprocessing.Pool
print("\n multiprocessing.Pool")
first_pool = time()
pool = Pool()
pool.map(angka, range(0, lim))
pool.close()
last_pool = time()

#Perbandingan
total_seq = last_seq - first_seq
total_process = last_process - first_process
total_pool = last_pool - first_pool

print("\nWaktu eksekusi sekuensial: ", total_seq, "detik")
print("Waktu eksekusi multiprocessing.Process: ", total_process, "detik")
print("Waktu eksekusi multiprocessing.Pool:" , total_pool, "detik")
