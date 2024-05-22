def menu():
    print('Selamat datang di program Manajemen Stok Barang!')
    print('Pilihan :')
    print('1. Tambah Data Barang')
    print('2. Edit Data')
    print('3. Hapus Data Barang')
    print('4. Cari Data')
    print('5. Tampilkan Data Barang')
    print('6. Tampilkan Jumlah Data')
    print('7. Keluar')
    print('=' *47)

barang = []

def tambah():
    nama = str(input('Masukkan nama barang : '))
    stok = int(input('Masukkan stok barang : '))

    barang_baru = {'nama' : nama, 'stok' : stok}
    barang.append(barang_baru)
    print('\n')

def edit():
    edit = int(input('Edit data index ke : '))
    edit_nama = str(input('Masukkan nama barang : '))
    edit_stok = int(input('Masukkan stok barang : '))

    barang[edit]['nama'] = edit_nama
    barang[edit]['stok'] = edit_stok
    print('\n')

def hapus():
    hapus = int(input('Hapus data index ke : '))
    del barang[hapus]
    print('\n')

def cari():
    cari = str(input('Masukkan nama barang yang ingin dicari : '))

    pencarian = [item for item in barang if cari.lower() in item['nama']]

    print('------- Hasil Pencarian -------')
    if pencarian:
        for item in pencarian:
            print('-',item['nama'],', stok :',item['stok'])
    else:
        print('Barang Tidak Ditemukan')
    print('\n')

def tampil_data():
    print('======= Toko Kelontong =======')
    if not barang:
        print('Data Barang Kosong')
    else:
        print('Data Barang yang Telah Diinput')
        for i in barang:
            print('-',i['nama'],i['stok'])
    print('\n')

def tampil_jumlah():
    print('Jumlah Data Tersimpan :',len(barang), 'Barang')
    print('\n')
