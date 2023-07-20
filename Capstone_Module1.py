def menu():
    print('''
    Selamat Datang di Perpustakaan Online
    -------------------------------------
    Menu :
    1. Menampilkan Data
    2. Menambahkan Buku ke dalam List
    3. Mengubah Data Buku dari List
    4. Menghapus Buku dari List
    5. Ingin Meminjam Buku
    6. Ingin Mengembalikan Buku
    
    0. Exit Program
    -------------------------------------

''')

    
listbuku = [
    [500010, 'Atomic Habits', 'James Clear', 'Pengembangan Diri', 2018],
    [500011, 'Laut Bercerita', 'Leila S. Chudori', 'Keluarga', 2017],
    [500012, 'Secrets of Divine Love', 'A. Helwa', 'Love and Religion', 2017],
    [500013, 'Kita Pergi Hari Ini', 'Tere Liye', 'Pertemanan', 2018],
    [500014, 'The Midnight Library', 'Matt Haig', 'Fiksi', 2020],
    [500015, 'Rich Dad Poor Dad', 'Robert T.Kiyosaki', 'Pengembangan Diri', 1997],
    [500016, 'One Piece 100', 'Eiichiro Oda', 'Komik', 2022],
    [500017, 'Think And Grow Rich', 'Napoleon Hill', 'Pengembangan Diri', 1937],
    [500018, 'Seni Hidup Minimalis', 'Fumio Sasaki', 'Lifestyle', 2018],
    [500019, 'River Of The Gods', 'Ian McDonald', 'Fiksi', 2004]
]

listHargaBuku = [
    [500010, 'Atomic Habits', 5000],
    [500011, 'Laut Bercerita', 3000],
    [500012, 'Secrets of Divine Love', 3000],
    [500013, 'Kita Pergi Hari Ini', 3000],
    [500014, 'The Midnight Library', 2500],
    [500015, 'Rich Dad Poor Dad', 5000],
    [500016, 'One Piece 100', 3500],
    [500017, 'Think And Grow Rich', 4000],
    [500018, 'Seni Hidup Minimalis', 3000],
    [500019, 'River Of The Gods', 5000]
]

book_info = [
    [500010, 'James Clear', 'Pengembangan Diri', 2018],
    [500011, 'Leila S. Chudori', 'Keluarga', 2017],
    [500012, 'A. Helwa', 'Love and Religion', 2017],
    [500013, 'Tere Liye', 'Pertemanan', 2018],
    [500014, 'Matt Haig', 'Fiksi', 2020],
    [500015, 'Robert T.Kiyosaki', 'Pengembangan Diri', 1997],
    [500016, 'Eiichiro Oda', 'Komik', 2022],
    [500017, 'Napoleon Hill', 'Pengembangan Diri', 1937],
    [500018, 'Fumio Sasaki', 'Lifestyle', 2018],
    [500019, 'Ian McDonald', 'Fiksi', 2004]
]


def rent_price():
    print('Harga Sewa Buku (SEWA PER 30 HARI)')
    print('No  | Seri       | Judul                     | Harga Sewa')
    for idx, sewa in enumerate(listHargaBuku, start=1):
        seribuku = str(sewa[0])
        judulbuku = sewa[1]
        hargasewa = str(sewa[2])
        print(f'{idx}{" "*(3-len(str(idx)))} | {seribuku}{" "*(10-len(seribuku))} | {judulbuku}{" "*(25-len(judulbuku))} | {hargasewa}')
    pass
    main_menu1()


def book_data():
    print('Berikut List Buku yang Tersedia\n')
    print('='*103)
    print('No  | Seri       | Judul                     | Penulis                 | Topik                 | Tahun')
    print('='*103)
    for idx, book in enumerate(listbuku, start=1):
        seribuku = str(book[0])
        judulbuku = book[1]
        penulis = ''
        topik = ''
        tahun = ''
        for info in book_info:
            if info[0] == book[0]:
                penulis = info[1]
                topik = info[2]
                tahun = str(info[3])
                break
        print(f'{idx}{" "*(3-len(str(idx)))} | {seribuku}{" "*(10-len(seribuku))} | {judulbuku}{" "*(25-len(judulbuku))} | {penulis}{" "*(23-len(penulis))} | {topik}{" "*(21-len(topik))} | {tahun}')
    print('='*103)
    main_menu1()

def main_menu1():
    print('''
    Silahkan Masukkan Input Menu Yang Anda Inginkan
    1. Tampilkan List Buku
    2. Tampilkan Harga Sewa Buku
    3. Tampilkan Jumlah Buku Berdasarkan Topik
    4. Mencari Buku melalui Seri
    0. Kembali ke Menu Utama
''')
    opsimenu = input('Silahkan Masukkan Input Menu Yang Anda Inginkan: ')
    if (opsimenu) == '1':
        book_data()
    elif opsimenu == '2':
        rent_price()
    elif opsimenu == '3':
        count_books_by_topic()
    elif opsimenu =='4' :
        find_book()
    elif opsimenu == '0':
        pass
    else:
        print('Input yang Anda Masukkan Tidak Valid.')

def main_menu2():
    print('''
    Silahkan Masukkan Input Menu Yang Anda Inginkan
    1. Tambahkan Buku
    0. Kembali ke Menu Utama
''')
    opsimenu = input('Silahkan Masukkan Input Menu Yang Anda Inginkan: ')
    if opsimenu == '1':
        add_book()
    elif opsimenu == '0':
        pass
    else:
        print('Input yang Anda Masukkan Tidak Valid.')

def main_menu3():
    print('''
    Silahkan Masukkan Input Menu Yang Anda Inginkan
    1. Mengubah Informasi Buku dari List
    0. Kembali ke Menu Utama
''')
    opsimenu = input('Silahkan Masukkan Input Menu Yang Anda Inginkan: ')
    if opsimenu == '1':
        update_book()
    elif opsimenu == '0':
        pass
    else:
        print('Input yang Anda Masukkan Tidak Valid.')
        main_menu3()

def main_menu5():
    print('''
    Silahkan Masukkan Input Menu Yang Anda Inginkan
    1. Ingin Meminjam Buku
    0. Kembali ke Menu Utama
    ''')
    option = input('Silahkan Masukkan Input Menu Yang Anda Inginkan: ')
    if option == '1':
        borrow_book()
    elif option == '0':
        menu()
    else:
        print('Input yang Anda Masukkan Tidak Valid.')
        main_menu5()

def main_menu6():
    print('''
    Silahkan Masukkan Input Menu Yang Anda Inginkan
    1. Ingin Mengembalikan Buku
    0. Kembali ke Menu Utama
    ''')
    option = input('Silahkan Masukkan Input Menu Yang Anda Inginkan: ')
    if option == '1':
        return_book()
    elif option == '0':
        menu()
    else:
        print('Input yang Anda Masukkan Tidak Valid.')
        main_menu6()


def count_books_by_topic():
    topics = ["Pengembangan Diri", "Keluarga", "Love and Religion", "Pertemanan", "Fiksi", "Komik", "Lifestyle"]
    book_counts = [0] * len(topics)

    for book in listbuku:
        topic = book[3]
        if topic in topics:
            index = topics.index(topic)
            book_counts[index] += 1
        else:
            topics.append(topic)
            book_counts.append(1)

    print("Jumlah Buku Berdasarkan Topik:")
    print("=============================")
    for i in range(len(topics)):
        print(f"{topics[i]}: {book_counts[i]} buku")
    print("=============================")
    main_menu1()

    
def update_book():
    if not listbuku or not listHargaBuku:
        print("Maaf, Buku Sedang Tidak Tersedia.")
        return
    book_number = input('Silahkan Masukkan Seri Buku yang Ingin Anda Update\n(Silahkan Input 0 untuk membatalkan): ')
    if book_number == '0':
        print('Update Buku Dibatalkan.')
        main_menu3()
        return
    if book_number.isdigit():
        book_number = int(book_number)
        book_found = False
        for book in listbuku:
            if book[0] == book_number:
                print(f'\nBerikut Data Buku yang Akan Diupdate dengan Seri {book_number}.')
                print('=' * 115)
                print('| Seri Buku     | Judul Buku                          | Penulis              | Topik              | Tahun  ')
                print(f'| {book[0]}{" " * (13 - len(str(book[0])))} | {book[1]}{" " * (35 - len(book[1]))} | {book[2]}{" " * (20 - len(book[2]))} | {book[3]}{" " * (18 - len(book[3]))} | {book[4]}{" " * (6 - len(str(book[4])))} ')
                print('=' * 115)
                book_found = True
                break
        if book_found:
            confirmation1 = input("Apakah Anda yakin Mengubah Informasi tersebut? (ya atau tidak)\n(Silahkan Input 0 untuk membatalkan): ")
            if confirmation1 == '0':
                print('Update Buku Dibatalkan.')
                main_menu3()
                return
            if confirmation1.lower() == 'ya':
                print("Silahkan Pilih Kolom yang Ingin Anda Ubah:")
                print("1. Seri Buku")
                print("2. Judul Buku")
                print("3. Penulis")
                print("4. Topik")
                print("5. Tahun")
                print("0. Kembali ke Menu Utama")
                column_choice = input("Masukkan Pilihan Anda (1-5): ")
                if column_choice == '0':
                    print('Update Buku Dibatalkan.')
                    main_menu3()
                    return
                if column_choice not in ['1', '2', '3', '4', '5']:
                    print('Input yang Anda Masukkan Tidak Valid.')
                    main_menu3()
                    return

                if column_choice == '1':
                    new_seri = input("Masukkan Seri Buku yang baru\n(Silahkan Input 0 untuk membatalkan): ")
                    if new_seri == '0':
                        print('Update Buku Dibatalkan.')
                        main_menu3()
                        return

                    for book in listbuku:
                        if book[0] == int(new_seri) and book[0] != book_number:
                            print(f'Maaf, Seri Buku "{new_seri}" telah digunakan oleh buku lain.')
                            main_menu3()
                            return

                    for i in range(len(listbuku)):
                        if listbuku[i][0] == book_number:
                            listbuku[i][0] = int(new_seri)
                        if listHargaBuku[i][0] == book_number:
                            listHargaBuku[i][0] = int(new_seri)

                    print(f"\nData Buku dengan Seri {book_number} berhasil diubah menjadi Seri {new_seri}.")
                    main_menu3()

                elif column_choice == '2':
                    new_data = input("Masukkan Judul Buku yang baru\n(Silahkan Input 0 untuk membatalkan): ")
                    if new_data == '0':
                        print('Update Buku Dibatalkan.')
                        main_menu3()
                        return

                    for book in listbuku:
                        if book[1] == new_data and book[0] != book_number:
                            print(f'Maaf, Judul Buku "{new_data}" telah digunakan oleh buku lain.')
                            main_menu3()
                            return

                    for i in range(len(listbuku)):
                        if listbuku[i][0] == book_number:
                            listbuku[i][1] = new_data

                    for i in range(len(listHargaBuku)):
                        if listHargaBuku[i][0] == book_number:
                            listHargaBuku[i][1] = new_data

                    print(f"\nData Buku dengan Seri {book_number} pada kolom Judul Buku berhasil diupdate.")
                    main_menu3()

                elif column_choice == '3':
                    pass

            elif confirmation1.lower() == 'tidak':
                main_menu3()
            else:
                print("Input yang Anda Masukkan Tidak Valid.")
                main_menu3()
        else:
            print(f'Maaf, Buku Dengan Seri "{book_number}" Tidak Dapat Ditemukan.')
            main_menu3()
    else:
        print(f'Maaf, Seri Buku yang Anda Cari "{book_number}" Tidak Valid.')
        main_menu3()


def find_book():
    if not listbuku or not listHargaBuku:
        print("Maaf, Buku Sedang Tidak Tersedia.")
        return
    book_number = input('Silahkan Masukkan Seri Buku yang Anda Cari : ')
    if book_number.isdigit():
        book_number = int(book_number)
        for buku in listbuku:
            if buku[0] == book_number:
                print(f'\nBerikut Data Buku yang Anda Cari dengan Seri {book_number}.')
                print('=' * 115)
                print('| Seri Buku     | Judul Buku                          | Penulis              | Topik              | Tahun  ')
                print(f'| {buku[0]}{" " * (13 - len(str(buku[0])))} | {buku[1]}{" " * (35 - len(buku[1]))} | {buku[2]}{" " * (20 - len(buku[2]))} | {buku[3]}{" " * (18 - len(buku[3]))} | {buku[4]}{" " * (6 - len(str(buku[4])))} ')
                print('=' * 115)
                for rent in listHargaBuku:
                    if rent[0] == book_number:
                        print('| Seri Buku     | Judul Buku                          | Harga Sewa  ')
                        print(f'| {rent[0]}{" " * (13 - len(str(rent[0])))} | {rent[1]}{" " * (35 - len(rent[1]))} | {rent[2]}{" " * (12 - len(str(rent[2])))} ')
                        print('=' * 67)
                main_menu1()
                break
        else:
            print(f'Maaf, Buku Dengan Seri "{book_number}" Tidak Dapat Ditemukan.')
        main_menu1()
    else:
        print(f'Maaf, Seri Buku yang Anda Cari "{book_number}" Tidak Valid.')
    main_menu1()


def is_duplicate(series):
    for book in listbuku:
        if book[0] == series:
            return True
    return False

def add_book():
    while True:
        book_series = input('''Masukkan Seri Buku yang ingin Anda Tambahkan\n(Silahkan Input 0 untuk membatalkan): ''')
        if book_series == '0':
            print('Menambahkan Buku Dibatalkan.')
            main_menu2()
            return
        if len(book_series) == 6 and book_series.isdigit():
            book_series = int(book_series)
            if is_duplicate(book_series):
                print('Seri yang Anda Masukkan Sudah Tersedia Dalam List Buku.')
            else:
                break
        else:
            print('Seri Buku harus terdiri dari 6 angka.')

    while True:
        book_title = input('''Masukkan Judul Buku yang ingin Anda Tambahkan\n(Silahkan Input 0 untuk membatalkan): ''')
        if book_title == '0':
            print('Menambahkan Buku Dibatalkan.')
            main_menu2()
            return
        if len(book_title) <= 25:
            break
        else:
            print('Judul Buku tidak boleh melebihi 25 karakter.')

    while True:
        book_author = input('''Masukkan Penulis Buku yang Ingin Anda Tambahkan\n(Silahkan Input 0 untuk membatalkan): ''')
        if book_author == '0':
            print('Menambahkan Buku Dibatalkan.')
            main_menu2()
            return
        if len(book_author) <= 25:
            break
        else:
            print('Penulis Buku tidak boleh melebihi 25 karakter.')

    while True:
        book_topic = input('''Masukkan Topik Buku yang Ingin Anda Tambahkan\n(Silahkan Input 0 untuk membatalkan): ''')
        if book_topic == '0':
            print('Menambahkan Buku Dibatalkan.')
            main_menu2()
            return
        if len(book_topic) <= 25:
            break
        else:
            print('Topik Buku tidak boleh melebihi 25 karakter.')

    while True:
        book_year = input('''Masukkan Tahun Buku yang Ingin Anda Tambahkan\n(Silahkan Input 0 untuk membatalkan): ''')
        if book_year == '0':
            print('Menambahkan Buku Dibatalkan.')
            main_menu2()
            return
        if len(book_year) == 4 and book_year.isdigit():
            break
        else:
            print('Tahun Buku harus terdiri dari 4 angka.')

    while True:
        book_price = input('''Masukkan Harga Sewa Buku yang Ingin Anda Tambahkan\n(Silahkan Input 0 untuk membatalkan): ''')
        if book_price == '0':
            print('Menambahkan Buku Dibatalkan.')
            main_menu2()
            return
        if len(book_price) <= 5 and book_price.isdigit():
            book_price = int(book_price)
            break
        else:
            print('Harga Sewa Buku harus berupa angka dengan maksimal 5 digit.')

    new_book = [book_series, book_title, book_author, book_topic, book_year]
    new_rent_price = [book_series, book_title, book_price]

    listbuku.append(new_book)
    listHargaBuku.append(new_rent_price)
    input_add = input('\nApakah Anda ingin menambahkan buku tersebut? (ya/tidak): ')
    if input_add.lower() == 'ya':
        print('Buku Telah ditambahkan.')
        main_menu2()
    elif input_add.lower() == 'tidak':
        listbuku.pop()
        listHargaBuku.pop()
        print('Buku Tidak ditambahkan')
        main_menu2()
    else:
        print('Input yang Anda Masukkan Tidak Valid')
        main_menu2()


def main_menu4():
    print('''
    Silahkan Masukkan Input Menu Yang Anda Inginkan
    1. Menghapus Buku dari List
    0. Kembali ke Menu Utama
    ''')
    option = input('Silahkan Masukkan Input Menu Yang Anda Inginkan: ')
    if option == '1':
        delete_data2()
    elif option == '0':
        pass
    else:
        print('Input yang Anda Masukkan Tidak Valid.')
        main_menu4()

def delete_data2():
    confirm = input('Apakah Anda Ingin Menghapus Buku dari List? (ya atau tidak): ')
    if confirm.lower() == 'ya':
        delete_book()
    elif confirm.lower() == 'tidak':
        main_menu4()
    else:
        print('Input yang Anda Masukkan Tidak Valid.')
        main_menu4()

def delete_book():
    while True:
        if not listbuku or not listHargaBuku:
            print("Maaf, Buku Sedang Tidak Tersedia.")
            break
        book_number = input('Silahkan Masukkan Seri Buku yang Ingin Anda Hapus: ')
        if book_number.isdigit():
            book_number = int(book_number)
            book_found = False
            book_to_delete = None
            for book in listbuku:
                if book[0] == book_number:
                    book_to_delete = book
                    listbuku.remove(book)
                    book_found = True
                    break
            for rent in listHargaBuku:
                if rent[0] == book_number:
                    listHargaBuku.remove(rent)
                    break
            if book_found:
                print("Berikut Data Buku yang Ingin Anda Hapus:")
                print('=' * 115)
                print('| Seri Buku     | Judul Buku                          | Penulis              | Topik              | Tahun  ')
                print(f'| {book_to_delete[0]}{" " * (13 - len(str(book_to_delete[0])))} | {book_to_delete[1]}{" " * (35 - len(book_to_delete[1]))} | {book_to_delete[2]}{" " * (20 - len(book_to_delete[2]))} | {book_to_delete[3]}{" " * (18 - len(book_to_delete[3]))} | {book_to_delete[4]}{" " * (6 - len(str(book_to_delete[4])))} ')
                print('=' * 115)
                print("Apakah Anda yakin ingin menghapus buku ini? (ya atau tidak)")
                confirm = input('Silahkan Masukkan Input Anda: ')
                if confirm.lower() == 'ya':
                    print(f"Buku dengan Seri {book_number} berhasil dihapus dari list.")
                    main_menu4()
                elif confirm.lower() == 'tidak':
                    main_menu4()
                else:
                    print('Input yang Anda Masukkan Tidak Valid.')
                    main_menu4()
            else:
                print(f'Maaf, Buku Dengan Seri "{book_number}" Tidak Dapat Ditemukan.')
                main_menu4()
            break
        else:
            print(f'Maaf, Seri Buku yang Anda Cari "{book_number}" Tidak Valid.')
            main_menu4()

listPeminjaman = []

def get_rent_price(book_number):
    for price_data in listHargaBuku:
        if price_data[0] == book_number:
            return price_data[2]
    return None

def borrow_book():
    if not listbuku:
        print("Maaf, Buku Tidak Tersedia.")
        menu()
        return

    print("\nMenu Meminjam Buku:")
    print("1. Cari Buku berdasarkan Seri Buku")
    print("0. Batalkan Peminjaman")
    
    while True:
        choice = input("Silahkan pilih menu (1/0): ")
        
        if choice == '0':
            print('Peminjaman Buku Dibatalkan.')
            main_menu5()
            break
        elif choice == '1':
            book_number = input('Silahkan Masukkan Seri Buku yang Ingin Anda Pinjam:\n(Silahkan Input 0 untuk membatalkan): ')
            if book_number == '0':
                print('Peminjaman Buku Dibatalkan.')
                main_menu5()
                return
            if book_number.isdigit():
                book_number = int(book_number)
                book_found = False
                for book in listbuku:
                    if book[0] == book_number:
                        print('Berikut Data Buku yang Akan Anda Pinjam:')
                        print('=' * 115)
                        print('| Seri Buku     | Judul Buku                          | Penulis              | Topik              | Tahun  ')
                        print(f'| {book[0]}{" " * (13 - len(str(book[0])))} | {book[1]}{" " * (35 - len(book[1]))} | {book[2]}{" " * (20 - len(book[2]))} | {book[3]}{" " * (18 - len(book[3]))} | {book[4]}{" " * (6 - len(str(book[4])))} ')
                        print('=' * 115)
                        book_found = True
                        break
                if book_found:
                    confirmation = input("Apakah Anda yakin ingin meminjam buku ini? (ya atau tidak)\n(Silahkan Input 0 untuk membatalkan): ")
                    if confirmation == '0':
                        print('Peminjaman Buku Dibatalkan.')
                        main_menu5()
                        return
                    if confirmation.lower() == 'ya':
                        rent_price = get_rent_price(book_number)
                        print("Berikut Tabel Harga Sewa Buku:")
                        print('=' * 70)
                        print('| Seri Buku     | Judul Buku                          | Harga Sewa')
                        print(f'| {book[0]}{" " * (13 - len(str(book[0])))} | {book[1]}{" " * (35 - len(book[1]))} | {rent_price}{" " * (9 - len(str(rent_price)))}')
                        print('=' * 70)
                        while True:
                            payment = input("Silahkan Masukkan Jumlah Uang yang Anda Bayarkan:\n(Silahkan Input 0 untuk membatalkan): ")
                            if payment == '0':
                                print('Peminjaman Buku Dibatalkan.')
                                main_menu5()
                                return
                            if payment.isdigit():
                                payment = int(payment)
                                if payment == rent_price:
                                    print("Terima Kasih, Mohon Menjaga Buku dan Mengembalikkan Buku Tepat Waktu.")
                                    borrowed_book = [book[0], book[1], book[2], book[3], book[4]]
                                    listPeminjaman.append(borrowed_book)
                                    listbuku.remove(book)
                                    main_menu5()
                                    return
                                elif payment > rent_price:
                                    change = payment - rent_price
                                    print("Terima Kasih, Mohon Menjaga Buku dan Mengembalikkan Buku Tepat Waktu.")
                                    print(f"Kembalian Anda: Rp {change}")
                                    borrowed_book = [book[0], book[1], book[2], book[3], book[4]]
                                    listPeminjaman.append(borrowed_book)
                                    listbuku.remove(book)
                                    main_menu5()
                                    return
                                else:
                                    deficit = rent_price - payment
                                    print(f"Maaf, Uang yang Anda Berikan Tidak Cukup. Nominal yang kurang sebesar Rp {deficit}")
                            else:
                                print("Input yang Anda Masukkan Tidak Valid.")
                    elif confirmation.lower() == 'tidak':
                        main_menu5()
                        break
                    else:
                        print("Input yang Anda Masukkan Tidak Valid.")
                        main_menu5()
                        break
                else:
                    print(f'Maaf, Buku Dengan Seri "{book_number}" Tidak Dapat Ditemukan.')
                    main_menu5()
                    break
            else:
                print(f'Maaf, Seri Buku yang Anda Cari "{book_number}" Tidak Valid.')
                main_menu5()
                break
        else:
            print("Menu tidak valid. Silahkan masukkan pilihan yang benar.")



def return_book():
    if not listPeminjaman:
        print("Tidak Ada Buku yang Sedang Dipinjam.")
        return

    while True:
        book_number = input("Masukkan Seri Buku yang Ingin Anda Kembalikan:\n(Silahkan Input 0 untuk membatalkan): ")
        if book_number == '0':
            print("Pengembalian Buku Dibatalkan.")
            menu()
            return
        if book_number.isdigit():
            book_number = int(book_number)
            book_found = False
            for i, book in enumerate(listPeminjaman):
                if book[0] == book_number:
                    print("Berikut Data Buku yang Akan Anda Kembalikan:")
                    print("=" * 115)
                    print("| Seri Buku     | Judul Buku                          | Penulis              | Topik              | Tahun  ")
                    print(f"| {book[0]}{' ' * (13 - len(str(book[0])))} | {book[1]}{' ' * (35 - len(book[1]))} | {book[2]}{' ' * (20 - len(book[2]))} | {book[3]}{' ' * (18 - len(book[3]))} | {book[4]}{' ' * (6 - len(str(book[4])))} ")
                    print("=" * 115)
                    book_found = True
                    confirmation = input("Apakah Anda yakin ingin mengembalikan buku ini? (ya atau tidak)\n(Silahkan Input 0 untuk membatalkan): ")
                    if confirmation == '0':
                        print("Pengembalian Buku Dibatalkan.")
                        main_menu6()
                        return
                    if confirmation.lower() == 'ya':
                        returned_book = listPeminjaman.pop(i)
                        listbuku.append(returned_book)
                        print("Buku berhasil dikembalikan.")
                        main_menu6()
                        break
                    elif confirmation.lower() == 'tidak':
                        main_menu6()
                    else:
                        print("Input yang Anda Masukkan Tidak Valid.")
                        main_menu6()
                    break
            if not book_found:
                print(f"Maaf, Buku dengan Seri {book_number} Tidak Ditemukan dalam Data Peminjaman.")
                main_menu6()
        else:
            print(f"Maaf, Seri Buku yang Anda Cari {book_number} Tidak Valid.")
            main_menu6()

while True:
    menu()
    option = input('Silahkan Masukkan Opsi yang Anda Inginkan: ')
    
    if option == '1':
        main_menu1()
    elif option == '2':
        main_menu2()
    elif option == '3':
        main_menu3()
    elif option == '4':
        main_menu4()
    elif option == '5':
        main_menu5()
    elif option == '6':
        main_menu6()
    elif option == '0':
        print('Terimakasih Sudah Mengunjungi Perpustakaan Online')
        break
    else:
        print('Opsi yang Anda Masukkan Tidak Valid.')