import random
  
print("\n")
nama = input("  Halo! Siapa namamu? ")
print("\n")

print("_"*70)
print("|                                                                     |")
print("|                                                                     |")
print("|                Selamat datang di Tebak Kata Misteri                 |")
print(f"              Hai, {nama}! Mari kita mulai permainan ini!             ")
print("|                                                                     |")
print("|                                                                     |")
print("|"+"="*69+"|")
print("|                                                                     |")
print("|                                                                     |")
print("|                    ***Tebak Kata Misteri***                         |")
print("|                                                                     |")
print("|                                                                     |")
print("| Kamu hanya memiliki 10 kesempatan untuk menebak kata hingga benar.  |")
print("|                                                                     |")
print("|                                                                     |")
print("|                                                                     |")
print("|"+"="*69+"|")

def start():
    benda = ['asbak', 'buku', 'baju', 'bantal', 'cermin', 'celana', 'dadu', 'ember', 'foto', 'gelas', 'guling', 
              'garpu', 'handuk', 'jam', 'jendela', 'kursi', 'kompor', 'kasur', 'lemari', 'laptop', 'meja', 'medali',
              'piring', 'pintu', 'pisau', 'piala', 'pagar', 'rak', 'sepatu', 'sandal', 'selimut', 'sendok', 'televisi', 
              'uang', 'vas', 'wajan', 'yoyo']
    
    hewan = ['ayam', 'anjing', 'angsa', 'bebek', 'babi', 'badak', 'belut', 'buaya', 'burung',
              'cacing', 'cicak', 'capung', 'domba', 'gajah', 'gurita', 'hamster', 'harimau',
              'ikan', 'iguana', 'jerapah', 'jangkrik', 'katak', 'kera', 'kuda', 'kukang', 'kambing', 
              'kancil', 'kalong', 'kucing', 'lebah', 'lalat', 'luwak', 'landak', 'macan', 'merak', 
              'monyet', 'musang', 'nyamuk', 'panda', 'paus', 'penguin', 'penyu', 'rakun', 'rubah', 
              'rusa', 'singa', 'semut', 'serigala', 'sapi', 'siput', 'tokek', 'tupai', 'ular', 'udang',
              'unta', 'ulat', 'ular', 'zebra']
    
    buah = ['apel', 'alpukat', 'arbei', 'blewah', 'delima', 'duku', 'durian', 'jambu', 'jeruk', 
              'kelapa', 'kiwi', 'kurma', 'leci', 'lemon', 'mangga', 'manggis', 'markisa', 'melon',
              'murbai', 'nanas', 'nangka', 'pepaya', 'pir', 'persik', 'pisang', 'rambutan', 'salak',
              'sirsak', 'srikaya', 'semangka', 'timun', 'tomat']
    
    kota = ['ambon', 'bandung', 'banjar', 'batam', 'batu', 'bekasi', 'bengkulu', 'bima', 'binjai', 'blitar', 
            'bogor', 'cirebon', 'cimahi', 'denpasar', 'depok', 'jakarta', 'jambi', 'jayapura', 'jombang', 'kediri', 'kendari', 'kudus', 
            'kupang', 'lombok', 'madiun', 'magelang', 'makassar', 'malang', 'manado', 'mataram', 'medan', 'padang', 'palu', 'ponorogo',
            'sabang', 'salatiga', 'semarang', 'serang', 'solo', 'sorong', 'sukabumi', 'surabaya', 'tarakan', 'tegal', 'ternate']
    
    negara = ['arab', 'amerika', 'autria', 'afrika', 'brazil', 'brunei', 'belanda', 'china', 'georgia', 'hungaria', 'indonesia', 'irlandia',
                'india', 'inggris', 'irak', 'iran', 'jepang', 'jerman', 'jordan', 'korea', 'kuwait', 'kamboja', 'laos', 'malaysia', 'mesir', 
                'mongolia', 'marroko', 'nepal', 'nigeria', 'pakistan', 'portugal', 'prancis', 'rusia', 'romania', 'swiss', 'swedia', 'spayol', 
                'turki', 'thailand', 'filipina', 'ukraina', 'uganda', 'uruguay', 'vietnam', 'yunani', 'yaman']

    print("\n1. Nama Benda \n2. Nama Buah \n3. Nama Hewan \n4. Nama Kota di Indonesia \n5. Nama Negara di Dunia\n")
    pilih = input("Mau tebak Kata Misteri apa, nih? ")
    print()

    if pilih == '1':
        kata = random.choice(benda)
        print("Kamu memilih Kata Misteri Nama Benda🛒")

    elif pilih == '2':
        kata = random.choice(buah)
        print("Kamu memilih Kata Misteri Nama Buah🍏")

    elif pilih == '3':
        kata = random.choice(hewan)
        print("Kamu memilih Kata Misteri Nama Hewan🐈")

    elif pilih == '4':
        kata = random.choice(kota)
        print("Kamu memilih Kata Misteri Nama Kota🌆")

    elif pilih == '5':
        kata = random.choice(negara)
        print("Kamu memilih Kata Misteri Nama Negara🌎")

        
    space_kata = ['_']*len(kata)

    print("_"*70)
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                               Mulai!                                |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|"+"_"*69+"|")

    # menyimpan huruf yang salah
    list_salah = []

    # memilih kata acak
    kata_misteri = kata
    print(f"\n🔎 Panjang Kata Misteri adalah {len(kata_misteri)} huruf 🔍")
    print('_'*70)
    print("\n")


    # menyimpan list kata yang berhasil ditebak 
    kata_tertebak = []

    for huruf in range(len(kata_misteri)):
        kata_tertebak.append("__")
    print(*([huruf for huruf in kata_tertebak]))

    c = 10

    while(c):
        c = c-1 

        # masukan dari pemain
        huruf_tertebak = input("Tebak sebuah huruf dalam Kata Misteri: ")

          # memastikan input adalah sebuah alfabet
        if not huruf_tertebak.isalpha():
            print('Masukkan sebuah huruf.')

          # memastikan input hanya satu buah karakter
        elif(len(huruf_tertebak)>1):
            print('Masukkan hanya satu huruf saja, ya!')

          # memastikan input belum pernah ditebak sebelumnya
        elif(huruf_tertebak in list_salah):
            print('Kamu sudah menebak huruf ini sebelumnya.')

          # input sesuai dengan kata misteri
        if huruf_tertebak in kata_misteri:
            for i in range(len(kata_misteri)):
                if kata_misteri[i] == huruf_tertebak:
                    kata_tertebak[i] = kata_misteri[i] 
                    print("🤩")
                    list_salah.append(huruf_tertebak)
        else:
            # feedback jika input salah
            print("Kamu menebak karakter yang salah😥")
            list_salah.append(huruf_tertebak)

        tebak_kata = [i for i in kata_tertebak]
        tebak_kata = "".join(tebak_kata)

        if kata_misteri == tebak_kata:
            print(*([huruf for huruf in kata_tertebak]))
            print('_'*70)
            print()
            print('Yeay! Kamu berhasil menebak kata misteri!🥳')
            print(f"Kata Misteri adalah {kata_misteri}")
            print()
            break

        # print kata tertebak
        print(*([huruf for huruf in kata_tertebak]))

        # sisa kesempatan
        if c != 0:
            print(f"Kamu memiliki {c} kesempatan tersisa.")
            print('_'*70)
            print()

        if c == 0:
            if  kata_misteri != kata_tertebak:
                print('_'*70)
                print('\n\n')
                print("Kesempatan menebak sudah habis.")
                print(f"Kamu gagal menebak Kata Misteri:( Kata Misteri adalah {kata_misteri}")
                exit(0)

def main_lagi():
    print()
    print("_"*70)
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|      ***Terima kasih karena sudah bermain Tebak Kata Misteri***     |")
    print("|                    Apakah kamu ingin bermain lagi?                  |")
    print("| 1. Ya                                                               |")
    print("| 2. Tidak                                                            |")
    global pilih
    pilih = input("   Hanya masukkan angka (1/2): ")
    print("|                                                                     |")
    print("|                                                                     |")
    print("|"+"_"*69+"|")
    return pilih 

def selesai():
    print("_"*70)
    print("|                                                                     |")
    print("|                                                                     |")
    print("|                          Sampai jumpa!                              |")
    print("|      ***Terima kasih karena sudah bermain Tebak Kata Misteri***     |")
    print("|                                                                     |")
    print("|"+"_"*69+"|")
    
def main():
    start()
    main_lagi()
    if pilih == '1':
        main()
    else:
        selesai()
        
main()
