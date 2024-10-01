print ("===========================================================================")
print ("Program menghitung total harga barang berdasarkan harga barang dan jumlah pembelian")
print ("===========================================================================")

print("Registrasi Akun")
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
print("Registrasi akun berhasil")

#Masukkan harga barang dan jumlah pembelian
harga_barang = int(input("Masukkan harga barang : "))
jumlah_pembelian = float(input("Masukkan jumlah pembelian : "))
total_harga = harga_barang * jumlah_pembelian

if total_harga > 250000:
    diskon = total_harga * 0.25
    total_harga -= diskon
    print("Anda mendapat diskon 25%", total_harga)
else:
    print("Anda tidak mendapat diskon, total harga =", total_harga)

while True:
    ulang = input("Apakah anda ingin menghitung lagi? (y/t): ")
    if ulang == 'y':
        harga_barang = int(input("Masukkan harga barang : "))
        jumlah_pembelian = float(input("Masukkan jumlah pembelian : "))
        total_harga = harga_barang * jumlah_pembelian
        if total_harga > 250000:
            diskon = total_harga * 0.25
            total_harga -= diskon
            print("Anda mendapat diskon 25%", total_harga)
        else:
            print("Anda tidak mendapat diskon, total harga=", total_harga)

    elif ulang == 't':
        print("Program selesai.")
        break 
