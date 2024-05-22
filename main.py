import modul as md

while True:
    md.menu()
    pilihan = int(input('Masukkan pilihan : '))
    print('-' *47)

    if pilihan == 1:
        md.tambah()
    elif pilihan == 2:
        md.edit()
    elif pilihan == 3:
        md.hapus()
    elif pilihan == 4:
        md.cari()
    elif pilihan == 5:
        md.tampil_data()
    elif pilihan == 6:
        md.tampil_jumlah()
    else:
        print('           Terimakasih telah mencoba           ')
        print('-' *47)
        exit()