from tabulate import tabulate
def format_rupiah(angka):
    return f"Rp{angka:,.0f}".replace(",", ".")
# menu 1: tabel menu kode transaksi dari kaca mata yang akan dipesan
dict_kacamata = [
    { "Kode Kacamata": "KK001", "Bahan Lensa": "Trivex", "Bahan Frame": "TR 90 Standard",   "Bentuk Frame": "Oval",        "Merek": "Arei",             "Harga Kacamata": 1000000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK002", "Bahan Lensa": "Glass",  "Bahan Frame": "TR 90 Rubber",     "Bentuk Frame": "Sporty",      "Merek": "Eiger",            "Harga Kacamata": 1400000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK003", "Bahan Lensa": "Trivex", "Bahan Frame": "Ontario Wood",     "Bentuk Frame": "Wayfarer",    "Merek": "Proof Eyewear",    "Harga Kacamata": 1600000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK004", "Bahan Lensa": "Glass",  "Bahan Frame": "Bud Wood",         "Bentuk Frame": "Round",       "Merek": "Woodys Barcelona", "Harga Kacamata": 1800000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK005", "Bahan Lensa": "Trivex", "Bahan Frame": "Stainless Steel",  "Bentuk Frame": "Square",      "Merek": "Oakley",           "Harga Kacamata": 2000000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK006", "Bahan Lensa": "Glass",  "Bahan Frame": "Stainless Steel",  "Bentuk Frame": "Aviator",     "Merek": "RayBan",           "Harga Kacamata": 2500000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK007", "Bahan Lensa": "Trivex", "Bahan Frame": "Aluminium",        "Bentuk Frame": "Cat Eye",     "Merek": "Levis",            "Harga Kacamata": 2550000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK008", "Bahan Lensa": "Glass",  "Bahan Frame": "Aluminium",        "Bentuk Frame": "Square",      "Merek": "Tag Heuer",        "Harga Kacamata": 2700000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK009", "Bahan Lensa": "Trivex", "Bahan Frame": "Titanium Gold",    "Bentuk Frame": "Round",       "Merek": "Adele Thompson",   "Harga Kacamata": 4000000, "Stok Kacamata": 8},
    { "Kode Kacamata": "KK010", "Bahan Lensa": "Glass",  "Bahan Frame": "Titanium Gold",    "Bentuk Frame": "Rectangular", "Merek": "Calvin Klein",     "Harga Kacamata": 4500000, "Stok Kacamata": 8},
]

# menampilkan_data_kacamata() Untuk menampilkan berbagai jenis tabel sesuai dengan kegunaannya
def menampilkan_data_kacamata():
    while True:
        print(50*'\n')
        print(42*'==')
        print('👓 READ MENU TOP OPTICAL GLASSES BY MAURITZ 👓'.center(72))
        print(42*'==')
        MenuInput=input('''               
List Menu Menampilkan Data Kacamata 👓 TOP OPTICAL GLASSES BY MAURITZ 👓:
1. Menampilkan Semua Data Kacamata
2. Menampilkan Data Kacamata menggunakan ID
3. Menampilkan Data Kacamata menggunakan Beberapa ID   
4. Keluar
                
Masukkan angka Menu yang ingin dijalankan : ''')
        if MenuInput == '1': # Menampilkan Semua Data Kacamata
            print('Menu:')
            tabel_dengan_format_rupiah = [
                {**kacamata, "Harga Kacamata": format_rupiah(kacamata["Harga Kacamata"])} for kacamata in dict_kacamata
            ]
            print(tabulate(tabel_dengan_format_rupiah, headers='keys', tablefmt='heavy_grid'))
            input("Tekan enter untuk kembali ke menu... ")

        elif MenuInput == '2':
            check=False
            primary_key = input("Masukkan Kode Kacamata yang mau ditampilkan: ")
            for kacamata in dict_kacamata:
                if primary_key == kacamata["Kode Kacamata"]: #key: Kode Kacamata
                    format_harga_kacamata_rupiah = {**kacamata, "Harga Kacamata": format_rupiah(kacamata["Harga Kacamata"])}
                    print(tabulate([format_harga_kacamata_rupiah], headers='keys', tablefmt='heavy_grid'))
                    check=True
                    break
            if check==False:
                print("Maaf, Kode Kacamata yang Saudara masukkan belum tersedia pada sistem 🙏")
            input("Tekan enter untuk kembali ke menu... ")

        elif MenuInput == '3':
            daftar_beberapa_kode_kacamata_dimasukkan = input("Masukkan beberapa Kode Kacamata (pisahkan dengan koma): ").upper().replace(" ", "").split(",")
            kode_kacamata_berhasil_ditemukan = []
            kode_kacamata_tidak_berhasil_ditemukan = []

            for beberapa_kode_kacamata in daftar_beberapa_kode_kacamata_dimasukkan:
                for kacamata in dict_kacamata:
                    if kacamata["Kode Kacamata"] == beberapa_kode_kacamata:
                        kode_kacamata_berhasil_ditemukan.append(kacamata)
                        break
                else:
                    kode_kacamata_tidak_berhasil_ditemukan.append(beberapa_kode_kacamata)

            if kode_kacamata_berhasil_ditemukan:
                data_format_rupiah = [
                    {**format_harga_kacamata_rupiah, "Harga Kacamata": format_rupiah(format_harga_kacamata_rupiah ["Harga Kacamata"])} for format_harga_kacamata_rupiah in kode_kacamata_berhasil_ditemukan
                ]
                print(tabulate(data_format_rupiah, headers="keys", tablefmt="heavy_grid"))

            if kode_kacamata_tidak_berhasil_ditemukan:
                print(f"Kode Kacamata belum berhasil ditemukan pada sistem 🙏: {', '.join(kode_kacamata_tidak_berhasil_ditemukan)}")
            input("Tekan enter untuk kembali ke menu... ")

        elif MenuInput=='4':
            break
        else:
            print(f'Maaf, Menu "{MenuInput}" tidak tersedia pada sistem 🙏')
            input("Tekan enter untuk kembali ke menu... ")

def menambah_satu_data_kacamata():
    dict_kacamata_baru = {
        "Kode Kacamata": None,
        "Bahan Lensa": None,
        "Bahan Frame": None, 
        "Bentuk Frame": None,
        "Merek": None,
        "Harga Kacamata": None,
        "Stok Kacamata": None
    }

    while True:
        primary_key = input("Masukkan Kode Kacamata yang diawali dengan 2 huruf 'KK'(Contoh: KK005): ").upper()
        if not (primary_key[:2] == 'KK' and primary_key[2:].isdigit()):
            print("Format Kode Kacamata tidak sesuai 🙏. Format Kode Kacamata Harus diawali dengan 'KK' dan hanya diikuti oleh angka bulat.")
            input("Tekan enter untuk kembali ke menu... ")  
            continue

        duplikat_penginputan_kode_kacamata = any(kacamata['Kode Kacamata'] == primary_key for kacamata in dict_kacamata)
        if duplikat_penginputan_kode_kacamata:
            print('Kode Kacamata yang Saudara masukkan sudah ada di dalam sistem 🙏. Silakan masukkan Kode Kacamata yang berbeda.')
            input("Tekan enter untuk kembali ke menu... ")  
            continue
        
        else:
            dict_kacamata_baru["Kode Kacamata"] = primary_key
            break

    list_bahan_lensa=["Plastic", "Polikarbonat", "Trivex", "High-Index Plastic", "Glass"]
    while True:
        input_bahan_lensa = input(f'Masukkan Bahan Lensa {list_bahan_lensa}: ').strip().casefold()
        cek_tambah_bahan_lensa = next((tambah_bahan_lensa for tambah_bahan_lensa in list_bahan_lensa if tambah_bahan_lensa.casefold() == input_bahan_lensa), None)
        if cek_tambah_bahan_lensa:
            dict_kacamata_baru["Bahan Lensa"] = cek_tambah_bahan_lensa
            break
        print ("Maaf, nama Bahan Lensa yang Saudara masukkan tidak sesuai dengan Bahan Lensa yang di program oleh optik 🙏")
        input("Tekan enter untuk kembali ke menu... ")  

    list_bahan_frame=["TR 90 Standard", "TR 90 Rubber", "Wood", "Stainless Steel", "Aluminium","Titanium Gold"]
    while True:
        input_bahan_frame=input(f'Masukkan Bahan Frame {list_bahan_frame}: ').strip().casefold()
        cek_tambah_bahan_frame = next((tambah_bahan_frame for tambah_bahan_frame in list_bahan_frame if tambah_bahan_frame.casefold() == input_bahan_frame), None)
        if cek_tambah_bahan_frame:
            dict_kacamata_baru["Bahan Frame"] = cek_tambah_bahan_frame
            break
        print("Maaf, nama Bahan Frame yang Saudara masukkan tidak sesuai dengan Bahan Frame yang di program oleh optik 🙏")
        input("Tekan enter untuk kembali ke menu... ") 
 
    list_bentuk_frame=["Round", "Oval", "Rectangular", "Cat Eye", "Wayfarer", "Aviator", "Brownline", "Geometric", "Rimless", "Oversized"]
    while True:
        input_bentuk_frame=input(f'Masukkan Bentuk Frame {list_bentuk_frame}: ').strip().casefold()
        cek_tambah_bentuk_frame = next((tambah_bentuk_frame for tambah_bentuk_frame in list_bentuk_frame if tambah_bentuk_frame.casefold() == input_bentuk_frame), None)
        if cek_tambah_bentuk_frame:
            dict_kacamata_baru["Bentuk Frame"] = cek_tambah_bentuk_frame
            break
        print("Maaf, nama Bentuk Frame yang Saudara masukkan tidak sesuai dengan Bentuk Frame yang di program oleh optik 🙏")
        input("Tekan enter untuk kembali ke menu... ") 
    
    list_merek=["Arei", "Eiger", "Proof Eyewear", "Woodys Barcelona", "Oakley", "RayBan", "Levis", "Tag Heuer", "Calvin Klein", "Adele Thompson", "Michael Korps"]
    while True:
        input_merek=input(f'Masukkan Merek {list_merek}: ').strip().casefold()
        cek_tambah_merek = next((tambah_merek for tambah_merek in list_merek if tambah_merek.casefold() == input_merek), None)
        if cek_tambah_merek:
            dict_kacamata_baru["Merek"] = cek_tambah_merek
            break
        print("Maaf, nama Merek yang Saudara masukkan tidak sesuai dengan nama Merek yang di program oleh optik 🙏")
        input("Tekan enter untuk kembali ke menu... ") 
            
    while True:
        input_harga_kacamata = input("Masukkan Harga Kacamata (hanya angka bulat saja, tanpa Rp, dan titik): ").strip()
        if not input_harga_kacamata.isdigit():
            print("Harga Kacamata yang Saudara masukkan wajib berupa angka bulat tanpa format Rupiah 🙏")
            input("Tekan enter untuk kembali ke menu... ") 
            continue
        tambah_harga_kacamata = int(input_harga_kacamata)
        if tambah_harga_kacamata <= 0:
            print("Harga Kacamata yang Saudara masukkan wajib lebih besar dari 0 🙏")
            input("Tekan enter untuk kembali ke menu... ") 
            continue
        konfirmasi_input_harga_kacamata = input(f"Apakah Saudara ingin menyimpan Harga Kacamata ini: {format_rupiah(tambah_harga_kacamata)} ? (Ya / Tidak): ").strip().lower()
        if konfirmasi_input_harga_kacamata.lower() == 'ya':
            dict_kacamata_baru["Harga Kacamata"] = tambah_harga_kacamata
            break
        elif konfirmasi_input_harga_kacamata == 'tidak':
            print("Silakan Saudara memasukkan ulang Harga Kacamata.")

    while True:
        input_stok_kacamata = input("Masukkan jumlah Stok Kacamata (angka): ").strip()
        if not input_stok_kacamata.isdigit():
            print("Stok Kacamata yang dimasukkan wajib berupa angka bulat 🙏")
            continue
        tambah_stok_kacamata = int(input_stok_kacamata)
        if tambah_stok_kacamata <= 0:
            print("Stok Kacamata yang dimasukkan wajib lebih besar dari 0 🙏")
            continue
        konfirmasi_input_stok_kacamata = input(f" Apakah Saudara ingin menyimpan Stok Kacamata ini: {tambah_stok_kacamata} ? (Ya / Tidak): ").strip().lower()
        if konfirmasi_input_stok_kacamata == 'ya':
            dict_kacamata_baru["Stok Kacamata"] = tambah_stok_kacamata
            break
        elif konfirmasi_input_stok_kacamata == 'tidak':
            print("Silakan Saudara memasukkan ulang Stok Kacamata.")

    while True:
        simpan_tambahan_data_kacamata = input ("Apakah Saudara ingin menyimpan Data Kacamata ini (Ya / Tidak)? ").strip().lower()
        if simpan_tambahan_data_kacamata=='ya':
            dict_kacamata.append(dict_kacamata_baru)
            print('Data Kacamata Berhasil Ditambahkan! ')
            print("Detail Data Kacamata yang Telah Disimpan:")
            data_format_rupiah = {**dict_kacamata_baru, "Harga Kacamata": format_rupiah(dict_kacamata_baru["Harga Kacamata"])}
            print(tabulate([data_format_rupiah], headers='keys', tablefmt='heavy_grid'))
            break

        elif simpan_tambahan_data_kacamata=='tidak':
            print('Data Kacamata Tidak Berhasil Ditambahkan! ')
            break
        else:
            print('Jawaban yang Saudara Masukkan Tidak Valid! Silakan masukkan pilihan antara "Ya" dan "Tidak" Saja!')
           
def menambah_data_kacamata():
    while True:
        print(50*'\n')
        print(42*'==')
        print('👓 CREATE MENU TOP OPTICAL GLASSES BY MAURITZ 👓'. center(72))
        print(42*'==')
        MenuInput=input('''               
List Menu Menambah Data Kacamata 👓 TOP OPTICAL GLASSES BY MAURITZ 👓:
1. Menambah Satu Data Kacamata 
2. Menambah Beberapa Data Kacamata
3. Keluar
                
Masukkan angka Menu yang ingin dijalankan : ''')   
        if MenuInput == '1': # Menambah Satu Data Kacamata
            menambah_satu_data_kacamata()

        elif MenuInput == '2':  # Menambah Beberapa Data Kacamata
            jumlah_data_kacamata_yang_diinput= input("Masukkan jumlah data kacamata yang ingin ditambahkan: ")
            if not jumlah_data_kacamata_yang_diinput.isdigit() or int(jumlah_data_kacamata_yang_diinput) <= 0:
                print("Masukkan wajib angka bulat dan lebih besar dari 0.")
                input("Tekan enter... ")
                continue
            jumlah_data_kacamata_yang_diinput = int(jumlah_data_kacamata_yang_diinput)
        
            for jumlah_data_kacamata in range(jumlah_data_kacamata_yang_diinput):
                print(f"\n--- Data ke-{jumlah_data_kacamata+1} ---")
                menambah_satu_data_kacamata()
            input("Tekan enter...")

        elif MenuInput=='3':
            break

        else:
            print(f'Menu "{MenuInput}" tidak tersedia pada sistem 🙏')
        input('Tekan enter... ')

def mengupdate_data_kacamata():
    while True:
        print(50*'\n')
        print(42*'==')
        print('👓 UPDATE MENU TOP OPTICAL GLASSES BY MAURITZ 👓'.center(72))
        print(42*'==')
        MenuInput=input('''               
List Menu Mengupdate Data Kacamata Menggunakan ID 👓 TOP OPTICAL GLASSES BY MAURITZ 👓:
1. Mengupdate Data Kacamata Menggunakan ID 
2. Mengupdate Beberapa Data Kacamata Menggunakan ID  
3. Keluar
                
Masukkan angka Menu yang ingin dijalankan : ''')   
        if MenuInput == '1': # Mengupdate Data Kacamata Menggunakan ID

            primary_key = input("Masukkan Kode Kacamata yang diawali dengan 2 huruf 'KK'(Contoh: KK005): ").upper()
            
            if (primary_key[:2] != 'KK') or (not primary_key[2:].isdigit()):
                print("Maaf, Format Kode Kacamata yang Saudara Masukkan Salah. Mohon masukkan Format Kode Kacamata yang Benar 🙏")
                continue
            
            check_kode = False

            for kacamata in dict_kacamata:
                if kacamata['Kode Kacamata'] == primary_key:
                    print(tabulate([kacamata], headers='keys', tablefmt='heavy_grid'))
                    check_kode = True
                    data_lanjutan=input("Apakah Saudara ingin mengupdate data kacamata ini (Ya / Tidak)? " ).lower()
                    if data_lanjutan=="ya":
                        MenuInput=input('''               
Bagian mana yang Saudara ingin update?:
1. Bahan Lensa 👓 TOP OPTICAL GLASSES BY MAURITZ 👓   
2. Bahan Frame
3. Bentuk Frame
4. Merek
5. Harga Kacamata
6. Stok Kacamata
            
Masukkan angka Menu yang ingin dijalankan : ''')
                        if MenuInput=="1": #Mengupdate Bahan Lensa 
                            list_bahan_lensa=["Plastic", "Polikarbonat", "Trivex", "High-Index Plastic", "Glass"]
                            while True:
                                bahan_lensa = input(f"Masukkan Bahan Lensa {list_bahan_lensa}: ").strip().casefold()
                                cek_update_nama_bahan_lensa = next ((update_nama_bahan_lensa for update_nama_bahan_lensa in list_bahan_lensa if update_nama_bahan_lensa.casefold() == bahan_lensa), None)
                                if not cek_update_nama_bahan_lensa:
                                    print("Maaf, nama Bahan Lensa yang Saudara masukkan tidak sesuai dengan Bahan Lensa yang di program oleh optik 🙏")
                                    input('Tekan enter untuk kembali ke menu...')
                                    continue
                                konfirmasi_update_nama_bahan_lensa = input ("Apakah ingin mengupdate data ini (Ya / Tidak)? ").strip().lower()
                                if konfirmasi_update_nama_bahan_lensa == "Ya":
                                    kacamata["Bahan Lensa"] = cek_update_nama_bahan_lensa
                                    print('Data Bahan Lensa Kacamata Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu...')
                                else:
                                    print('Data Bahan Lensa Kacamata Tidak Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu...') 
                                break
            
                        elif MenuInput=="2": #Mengupdate Bahan Frame Kacamata
                            list_bahan_frame=["TR 90 Standard", "TR 90 Rubber", "Wood", "Stainless Steel", "Aluminium","Titanium Gold"]
                            while True:
                                bahan_frame=input(f"Masukkan Bahan Frame {list_bahan_frame}: ").strip().casefold()
                                cek_update_nama_bahan_frame = next ((update_nama_bahan_frame for update_nama_bahan_frame in list_bahan_frame if update_nama_bahan_frame.casefold() == bahan_frame), None)
                                if not cek_update_nama_bahan_frame:
                                    print("Maaf, nama Bahan Frame yang Saudara masukkan tidak sesuai dengan Bahan Frame yang di program oleh optik 🙏")
                                    input('Tekan enter untuk kembali ke menu...')
                                    continue
                                konfirmasi_update_nama_bahan_frame = input ("Apakah ingin mengupdate data ini (Ya / Tidak)? ").strip().lower()
                                if konfirmasi_update_nama_bahan_frame == "Ya":
                                    kacamata["Bahan Frame"] = cek_update_nama_bahan_frame
                                    print('Data Bahan Frame Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu...')
                                else:
                                    print('Data Bahan Frame Tidak Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu...')
                                break
                            
                        elif MenuInput=="3": #Mengupdate Bentuk Frame
                            list_bentuk_frame=["Round", "Oval", "Rectangular", "Cat Eye", "Wayfarer", "Aviator", "Brownline", "Geometric", "Rimless", "Oversized"]
                            while True:
                                bentuk_frame=input(f"Masukkan Bentuk Frame {list_bentuk_frame}: ").strip().casefold()
                                cek_update_nama_bentuk_frame = next ((update_nama_bentuk_frame for update_nama_bentuk_frame in list_bentuk_frame if update_nama_bentuk_frame.casefold() == bentuk_frame), None)
                                if not cek_update_nama_bentuk_frame:
                                    print("Maaf, nama Bentuk Frame yang Saudara masukkan tidak sesuai dengan Bentuk Frame yang di program oleh optik 🙏")
                                    input('Tekan enter untuk kembali ke menu...')
                                    continue
                                konfirmasi_update_nama_bentuk_frame = input ("Apakah ingin mengupdate data ini (Ya / Tidak)? ").strip().lower()
                                if konfirmasi_update_nama_bentuk_frame == "Ya":
                                    kacamata["Bentuk Frame"] = cek_update_nama_bentuk_frame
                                    print('Data Bentuk Frame Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu... ') 
                                else:
                                    print('Data Bentuk Frame Tidak Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu... ')
                                break
         
                        elif MenuInput=="4": #Mengupdate Merek Kacamata
                            list_merek=["Arei", "Eiger", "Proof Eyewear", "Woodys Barcelona", "Oakley", "RayBan", "Levis", "Tag Heuer", "Calvin Klein", "Adele Thompson", "Michael Korps"]
                            while True:                 
                                merek=input(f"Masukkan Merek {list_merek}: "). strip().casefold()
                                cek_update_nama_merek = next ((update_nama_merek for update_nama_merek in list_merek if update_nama_merek.casefold() == merek ), None)
                                if not cek_update_nama_merek:
                                    print("Maaf, nama Merek yang Saudara masukkan tidak sesuai dengan nama Merek yang di program oleh optik 🙏") 
                                    input('Tekan enter untuk kembali ke menu...')
                                    continue
                                konfirmasi_update_nama_merek = input ("Apakah ingin mengupdate data ini (Ya / Tidak)? ").strip().lower()
                                if konfirmasi_update_nama_merek == "Ya":
                                    kacamata["Merek"] = cek_update_nama_merek
                                    print('Data Merek Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu... ')
                                else:
                                    print('Data Merek Tidak Berhasil Di Update! ')
                                    input('Tekan enter untuk kembali ke menu... ')
                                break

                        elif MenuInput=="5": #Mengupdate Harga Kacamata
                            while True:
                                harga = input("Masukkan Harga Kacamata (angka tanpa Rp): ").strip()
                                if harga.isdigit():
                                    harga= int(harga)
                                    if harga>0:
                                        while True:
                                            print("Apakah ingin mengupdate data Harga Kacamata ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                    kacamata["Harga Kacamata"] = harga
                                                    print('Data Harga Kacamata Berhasil Di Update! ')
                                                    print("Harga Kacamata Setelah Berhasil Di Update:")
                                                    print(format_rupiah(kacamata["Harga Kacamata"]))
                                                    input('Tekan enter... ')
                                                    break
                                            elif save=='Tidak':
                                                print('Data Harga Kacamata Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Harga Kacamata yang Dimasukkan Tidak Valid! ')   
                                                input('Tekan enter... ')
                                        break
                                    else:
                                        print("Harga Kacamata yang dimasukkan wajib Lebih Besar dari 0")
                                        input('Tekan enter... ')
                                else:
                                    print('Masukkan Harga Kacamata dalam bentuk format angka bulat saja!!')  
                                    input('Tekan enter... ')      

                        elif MenuInput=="6": # Mengupdate Stok Kacamata                               
                            while True:
                                stok = input("Masukkan Stok Kacamata: ")
                                if (stok.isdigit()):
                                    stok= int(stok)
                                    if stok>0:
                                        while True:
                                            print("Apakah ingin mengupdate data Stok Kacamata ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Stok Kacamata"] = stok
                                                print('Data Stok Kacamata Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Stok Kacamata Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Stok Kacamata yang Dimasukkan Tidak Valid! ')
                                                input('Tekan enter... ')
                                        break
                                    else:
                                        print("Stok Kacamata yang dimasukkan wajib Lebih Besar dari 0")
                                        input('Tekan enter... ')
                                else:
                                    print('Masukkan Stok Kacamata dalam bentuk format angka bulat saja!!')
                                    input('Tekan enter... ')
                        
                        else:
                            print('Pilihan yang Saudara Masukkan Tidak Sesuai dengan Pilihan yang Tertera')
                            input('Tekan enter... ')

                    break
            if check_kode == False:
                print('Kode yang Saudara masukkan tidak ditemukan dalam sistem optik ini')
                input('Tekan enter... ')

        elif MenuInput == '2':
            beberapa_kode_kacamata_yang_mau_diupdate = input("Masukkan beberapa Kode Kacamata (pisahkan dengan koma): ").upper().replace(" ", "").split(",")
            bagian_dari_kode_kacamata = input('''Bagian dari Kode Kacamata yang ingin diupdate (pilih angka):
1. Bahan Lensa
2. Bahan Frame
3. Bentuk Frame
4. Merek
5. Harga Kacamata
6. Stok Kacamata
: ''')
            
            jumlah_kode_kacamata_yang_diupdate = 0

            for beberapa_kode_kacamata_telah_diupdate in beberapa_kode_kacamata_yang_mau_diupdate:
                for kacamata in dict_kacamata:
                    if kacamata["Kode Kacamata"] == beberapa_kode_kacamata_telah_diupdate:
                        if bagian_dari_kode_kacamata == "1":
                            list_bahan_lensa=["Plastic", "Polikarbonat", "Trivex", "High-Index Plastic", "Glass"]
                            while True:
                                bahan_lensa=input('Masukkan Bahan Lensa ("Plastic", "Polikarbonat", "Trivex", "High-Index Plastic", "Glass"): ').title()
                                if not bahan_lensa in list_bahan_lensa:
                                    print("Maaf, nama Bahan Lensa yang Saudara masukkan tidak sesuai dengan Bahan Lensa yang di program oleh optik 🙏")
                                    continue 
                                else:
                                    while True:
                                            print("Apakah ingin mengupdate data (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Bahan Lensa"] = bahan_lensa
                                                print('Data Bahan Lensa Kacamata Berhasil Di Update! ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Bahan Lensa Kacamata Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Bahan Lensa Kacamata yang Dimasukkan Tidak Valid! ')   
                                    break
                                
                        elif bagian_dari_kode_kacamata == "2":
                            list_bahan_frame=["TR 90 Standard", "TR 90 Rubber", "Wood", "Stainless Steel", "Aluminium","Titanium Gold"]
                            while True:
                                bahan_frame=input('Masukkan Bahan Frame ("TR 90 Standard", "TR 90 Rubber", "Wood", "Stainless Steel", "Aluminium", "Titanium Gold"): ')
                                if not bahan_frame in list_bahan_frame:
                                    print("Maaf, nama Bahan Frame yang Saudara masukkan tidak sesuai dengan Bahan Frame yang di program oleh optik 🙏")
                                    continue 
                                else:
                                    while True:
                                            print("Apakah ingin mengupdate data Bahan Frame ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Bahan Frame"] = bahan_frame
                                                print('Data Bahan Frame Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Bahan Frame Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Bahan Frame yang Dimasukkan Tidak Valid! ')   
                                                input('Tekan enter... ')
                                    break    

                        elif bagian_dari_kode_kacamata == "3":
                            list_bentuk_frame=["Round", "Oval", "Rectangular", "Cat Eye", "Wayfarer", "Aviator", "Brownline", "Geometric", "Rimless", "Oversized"]
                            while True:
                                bentuk_frame=input('Masukkan Bentuk Frame ("Round", "Oval", "Rectangular", "Cat Eye", "Wayfarer", "Aviator", "Brownline", "Geometric", "Rimless", "Oversized"): ').title()
                                if not bentuk_frame in list_bentuk_frame:
                                    print("Maaf, nama Bentuk Frame yang Saudara masukkan tidak sesuai dengan Bentuk Frame yang di program oleh optik 🙏")
                                    continue 
                                else:
                                    while True:
                                            print("Apakah ingin mengupdate data Bentuk Frame ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Bentuk Frame"] = bentuk_frame
                                                print('Data Bentuk Frame Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Bentuk Frame Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Bentuk Frame yang Dimasukkan Tidak Valid! ')   
                                                input('Tekan enter... ')
                                    break

                        elif bagian_dari_kode_kacamata == "4":
                            list_merek=["Arei", "Eiger", "Proof Eyewear", "Woodys Barcelona", "Oakley", "RayBan", "Levis", "Tag Heuer", "Calvin Klein", "Adele Thompson", "Michael Korps"]
                            while True:                 
                                merek=input('Masukkan Merek ("Arei", "Eiger", "Proof Eyewear", "Woodys Barcelona", "Oakley", "RayBan", "Levis", "Tag Heuer", "Calvin Klein", "Adele Thompson", "Michael Korps"): ').title()
                                if not merek in list_merek:
                                    print("Maaf, nama Merek yang Saudara masukkan tidak sesuai dengan nama Merek yang di program oleh optik 🙏")
                                    continue 
                                else:
                                    while True:
                                            print("Apakah ingin mengupdate data Merek ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Merek"] = merek
                                                print('Data Merek Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Merek Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Merek yang Dimasukkan Tidak Valid! ')   
                                                input('Tekan enter... ')
                                    break

                        elif bagian_dari_kode_kacamata == "5":
                            while True:
                                harga = input("Masukkan Harga Kacamata: ")
                                if (harga.isdigit()):
                                    harga= int(harga)
                                    if harga>0:
                                        while True:
                                            print("Apakah ingin mengupdate data Harga Kacamata ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Harga Kacamata"] = harga
                                                print('Data Harga Kacamata Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Harga Kacamata Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Harga Kacamata yang Dimasukkan Tidak Valid! ')   
                                                input('Tekan enter... ')
                                        break
                                    else:
                                        print("Harga Kacamata yang dimasukkan wajib Lebih Besar dari 0")
                                        input('Tekan enter... ')
                                else:
                                    print('Masukkan Harga Kacamata dalam bentuk format angka bulat saja!!')  
                                    input('Tekan enter... ') 
    
                        elif bagian_dari_kode_kacamata == "6":
                            while True:
                                stok = input("Masukkan Stok Kacamata: ")
                                if (stok.isdigit()):
                                    stok= int(stok)
                                    if stok>0:
                                        while True:
                                            print("Apakah ingin mengupdate data Stok Kacamata ini (Ya / Tidak)? ")
                                            save = input().capitalize()
                                            if save=='Ya':
                                                kacamata["Stok Kacamata"] = stok
                                                print('Data Stok Kacamata Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            elif save=='Tidak':
                                                print('Data Stok Kacamata Tidak Berhasil Di Update! ')
                                                input('Tekan enter... ')
                                                break
                                            else:
                                                print('Data Stok Kacamata yang Dimasukkan Tidak Valid! ')
                                                input('Tekan enter... ')
                                        break
                                    else:
                                        print("Stok Kacamata yang dimasukkan wajib Lebih Besar dari 0")
                                        input('Tekan enter... ')
                                else:
                                    print('Masukkan Stok Kacamata dalam bentuk format angka bulat saja!!')
                                    input('Tekan enter... ')
                        
                        else:
                            print('Pilihan yang Saudara Masukkan Tidak Sesuai dengan Pilihan yang Tertera')
                            input('Tekan enter... ')

                        jumlah_kode_kacamata_yang_diupdate += 1
                        break

            print(f"{jumlah_kode_kacamata_yang_diupdate} data berhasil diupdate.")
            input("Tekan enter... ")

        elif MenuInput == '3':
            break
        else:
            print(f'Maaf, Menu "{MenuInput}" tidak tersedia pada versi sistem optik kami 🙏')
        input('Tekan enter... ')

def menghapus_data_kacamata():
    while True:
        print(50*'\n')
        print(42*'==')
        print('👓 HAPUS MENU TOP OPTICAL GLASSES BY MAURITZ 👓'.center(72))
        print(42*'==')
        MenuInput=input('''               
List Menu Menghapus Data Kacamata 👓 TOP OPTICAL GLASSES BY MAURITZ 👓:
1. Menghapus Data Kacamata Menggunakan ID
2. Menghapus Beberapa Data Kacamata Menggunakan ID   
3. Keluar
Masukkan angka Menu yang ingin dijalankan : ''')
        if MenuInput=="1": # Menghapus data kacamata
            primary_key = input("Masukkan Kode Kacamata yang diawali dengan 2 huruf 'KK'(Contoh: KK005): ").upper()
            
            if (primary_key[:2] != 'KK') or (not primary_key[2:].isdigit()):
                print("Maaf, Format Kode Kacamata yang Saudara Masukkan Salah. Mohon masukkan Format Kode Kacamata yang Benar 🙏")
                continue
                
            check_kode = False

            for kacamata in dict_kacamata:
                if kacamata['Kode Kacamata'] == primary_key:
                    print(tabulate([kacamata], headers='keys', tablefmt='heavy_grid'))
                    check_kode = True

                    data_lanjutan=input("Apakah Saudara ingin menghapus Data Kode Kacamata ini (Ya / Tidak)? " )
                    if data_lanjutan=="Ya":
                        # hapus
                        dict_kacamata.remove(kacamata)
                        print("Data Kode Kacamata Berhasil Dihapus!")
                    else:
                        print("Data Kode Kacamata Tidak Berhasil Dihapus!")

            if check_kode == False:
                print("Data Kode Kacamata Tidak Ditemukan!")

        elif MenuInput == "2":
            daftar_kode_kacamata_yang_akan_dihapus= input("Masukkan beberapa Kode Kacamata yang masing-masing Kode Kacamata diawali dengan 2 huruf 'KK' (Contoh: KK005) (Pisahkan dengan koma): ").upper().replace(" ", "").split(",")
            jumlah_kode_terhapus = 0

            for kode_kacamata_yang_akan_dihapus in daftar_kode_kacamata_yang_akan_dihapus:
                if not (kode_kacamata_yang_akan_dihapus.startswith('KK') and kode_kacamata_yang_akan_dihapus[2:].isdigit()):
                    print(f"Maaf, Format Kode Kacamata yang Saudara masukkan yaitu: {kode_kacamata_yang_akan_dihapus} Salah. Mohon masukkan Format Kode Kacamata yang Benar 🙏")
                    continue

            check_kode = False

            for kode_kacamata_yang_akan_dihapus in daftar_kode_kacamata_yang_akan_dihapus:
                for i, kacamata in enumerate(dict_kacamata):
                    if kacamata["Kode Kacamata"] == kode_kacamata_yang_akan_dihapus:
                        print(tabulate([kacamata], headers="keys", tablefmt="heavy_grid"))
                        check_kode= True
                        konfirmasi = input(f"Apakah Saudara ingin menghapus Kode Kacamata ini {kode_kacamata_yang_akan_dihapus}? (Ya/Tidak): ").capitalize()
                        if konfirmasi == "Ya":
                            dict_kacamata.pop(i)
                            jumlah_kode_terhapus +=1
                            print(f"Data dengan Kode Kacamata {kode_kacamata_yang_akan_dihapus} Berhasil Dihapus!")
                            input("Tekan enter... ")
                        else:
                            print(f"Data dengan Kode Kacamata {kode_kacamata_yang_akan_dihapus} Tidak Berhasil Dihapus!")
                            input("Tekan enter... ")
                
            if check_kode == False:
                print(f"Kode Kacamata {kode_kacamata_yang_akan_dihapus} Tidak Ditemukan!")
                input("Tekan enter... ")

        elif MenuInput=="3":
            break
        else:
            print(f'Menu "{MenuInput}" tidak tersedia pada versi sistem optik kami 🙏')
        input('Tekan enter... ')

def menu_utama():
    while True:
        print(50*'\n')
        print(42*'==')
        print('👓 SELAMAT DATANG DI TOP OPTICAL GLASSES BY MAURITZ 👓'.center(72))
        print(42*'==')
        MenuInput=input('''               
List Menu Utama 👓 TOP OPTICAL GLASSES BY MAURITZ 👓:
1. Menampilkan Data Kacamata 
2. Menambah Data Kacamata 
3. Mengupdate Data Kacamata  
4. Menghapus Data Kacamata            
5. Keluar
                
Masukkan angka Menu yang ingin dijalankan : ''')
        if MenuInput == '1':
            menampilkan_data_kacamata()
        elif MenuInput == '2':
            menambah_data_kacamata()
        elif MenuInput == '3':
            mengupdate_data_kacamata()
        elif MenuInput == '4':
            menghapus_data_kacamata()
        elif MenuInput=='5':
            break
        else:
            print(f'Menu "{MenuInput}" tidak tersedia pada versi sistem optik kami 🙏')
        input('Tekan enter... ')
        
menu_utama()
  
  
  
  
  
  
  
