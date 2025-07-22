import random
import string

# Boolean
programKerja = True
Admin = True

# Variabel Kosong
namaPasien = None
DataPasien = None
coba = None

# int
percobaan = 3
limitRuangOperasi = 2
limitKamar = 50

pasienInap = {
    "CAD23": {
        "nama": "Muci Kari",
        "tanggal_lahir": "2022-05-21",
        "umur": 2,
        "jenis_kelamin": "Laki-laki",
        "bpjs": True,
        "dokter_jaga": "Sapudin",
        "dokter_spesialis": "Mandrake"
    }
}

# Menghitung maksimal panjang string di dictionary Pasien Inap
def len_dict_Inap():
    max_lengths = {}

    for pasien in pasienInap.values():
        for key, value in pasien.items():
            if isinstance(value, list):
                max_val = sum(len(str(item)) for item in value)
            else:
                max_val = len(str(value))

            if key not in max_lengths or max_val > max_lengths[key]:
                max_lengths[key] = max_val

    return max_lengths

# Antrian Pasien
# No Antrian <> BPJS <> Nama <> Dokter
pasienIGD = { # listAntrian
    "ABCDE": {
        "nama": "Kari Patura",
        "tanggal_lahir": "1990-05-21",
        "umur": 34,
        "jenis_kelamin": "Laki-laki",
        "bpjs": True,
        "status": None,
        "jam_datang": "08:30",
        "dokter_jaga": "Sapudin",
        "dokter_spesialis": "Shipo"
    },
    "JAK23": {
        "nama": "Sati Wuna",
        "tanggal_lahir": "1995-03-10",
        "umur": 29,
        "jenis_kelamin": "Perempuan",
        "bpjs": True,
        "status": "Rawat Inap",
        "jam_datang": "07:15",
        "dokter_jaga": "Udin",
        "dokter_spesialis": "Manala"
    },
    "121RT": {
        "nama": "Badu Harmuna",
        "tanggal_lahir": "1978-08-15",
        "umur": 46,
        "jenis_kelamin": "Laki-laki",
        "bpjs": False,
        "status": "Operasi",
        "jam_datang": "09:00",
        "dokter_jaga": "Udin",
        "dokter_spesialis": "Andryan"
    },
    "KL32S": {
        "nama": "Tiny Tina",
        "tanggal_lahir": "1972-11-30",
        "umur": 52,
        "jenis_kelamin": "Perempuan",
        "bpjs": True,
        "status": "Rawat Inap",
        "jam_datang": "06:50",
        "dokter_jaga": "Sapudin",
        "dokter_spesialis": "Shipo"
    },
    "AP23L": {
        "nama": "Dewi Lestari",
        "tanggal_lahir": "1987-06-12",
        "umur": 37,
        "jenis_kelamin": "Perempuan",
        "bpjs": False,
        "status": None,
        "jam_datang": "08:40",
        "dokter_jaga": "Sapudin",
        "dokter_spesialis": "Andryan"
    },
    "JKRT3": {
        "nama": "Rudy Kubawan",
        "tanggal_lahir": "1964-02-25",
        "umur": 60,
        "jenis_kelamin": "Laki-laki",
        "bpjs": True,
        "status": "Rawat Inap",
        "jam_datang": "05:30",
        "dokter_jaga": "Udin",
        "dokter_spesialis": "Shipo"
    },
    "AP32B": {
        "nama": "Nurah",
        "tanggal_lahir": "2001-07-03",
        "umur": 23,
        "jenis_kelamin": "Laki-laki",
        "bpjs": False,
        "status": "Operasi",
        "jam_datang": "09:15",
        "dokter_jaga": "Sapudin",
        "dokter_spesialis": None
    },
   "BS9RT": {
        "nama": "Maria Franky",
        "tanggal_lahir": "1984-09-14",
        "umur": 40,
        "jenis_kelamin": "Perempuan",
        "bpjs": True,
        "status": None,
        "jam_datang": "08:20",
        "dokter_jaga": "Udin",
        "dokter_spesialis": "Shipo"
    }
}

# Menghitung maksimal panjang string di dictionary Pasien Inap
def len_dict_IGD():
    max_lengths = {}

    for pasien in pasienIGD.values():
        for key, value in pasien.items():
            if isinstance(value, list):
                max_val = sum(len(str(item)) for item in value)  # << ini
            else:
                max_val = len(str(value))

            if key not in max_lengths or max_val > max_lengths[key]:
                max_lengths[key] = max_val

    return max_lengths

# Isi obat yang ada di apotek rumah sakit
# Kode <> Nama <> Nomor <> Jumlah
dictObat = {
    'pcm': {'Nama': 'pcm',
            'Stock': 20,
            'Harga': 1000},
    'Ibu': {'Nama': 'ibIbuprofenu',
            'Stock': 20,
            'Harga': 1500},
    'ctm': {'Nama': 'CTM', 
            'Stock': 20, 
            'Harga': 500},
    'abx': {'Nama': 'Ambroxol',
            'Stock': 20,
            'Harga': 1200},
    'amx': {'Nama':'Amoxicillin',
            'Stock': 20,
            'Harga': 1500},
    'ant': {'Nama': 'Antasida',
            'Stock': 20,
            'Harga': 1000},
    'dmp': {'Nama': 'Domperidone',
            'Stock': 20,
            'Harga': 1800},
    'pkb': {'Nama': 'Pil KB',
            'Stock': 20,
            'Harga': 2000}
}

listIya = ['Y', 'y', 'Iya', 'iya', 'Ya', 'ya', 'Yes', 'yes', 'Yeah', 'yeah']
listTidak = ['T', 't', 'Tidak', 'tidak', 'N', 'n', 'No', 'no']
listLakilaki = ['Laki-laki', 'laki-laki', 'Laki', 'LK', 'Lk', 'lk', 'L', 'l']
listPerempuan = ['Perempuan', 'perempuan', 'PR', 'Pr', 'pr', 'P', 'p']

def len_str_Obat(dictObat):
    max_lengths = {}

    for pasien in pasienIGD.values():
        for key, value in pasien.items():
            if isinstance(value, list):
                max_val = sum(len(str(item)) for item in value)  # << ini
            else:
                max_val = len(str(value))

            if key not in max_lengths or max_val > max_lengths[key]:
                max_lengths[key] = max_val

    return max_lengths

#staff
# Nomor <> Dokter <> Nama
staff = [
    (1, 'D-Umum','Udin')
    ,(2, 'D-Umum','Sapudin')
    ,(3, 'D-Penyakit Dalam','Andryan')
    ,(4, 'D-Anak','Mandrake')
    ,(5, 'D-Bedah','Shipo')
    ,(6, 'D-Obgyn', 'Manala')
    ,(7, 'Bidan', 'Drana')
    ,(8, 'Apoteker', 'Apoteker')
    ,(9, 'Management', 'Gangga')
]

maxLengthStaff = [max(len(str(item)) for item in col) for col in zip(*staff)]

# Check Pasien
def checkPasien(namaPasien):
    for id, key in pasienIGD.items():
        if (key['nama'] == namaPasien): return 2
    for id, key in pasienInap.items():
        if key['nama'] == namaPasien : return 1
    return 0

# Mencari kode pasien dengan nama pasien
def keyPasiennyadef(namaPasien):
    for id, key in pasienIGD.items():
        if (key['nama'] == namaPasien): return id
    for id, key in pasienInap.items():
        if key['nama'] == namaPasien : return id

# Melihat pasien IGD berdasarkan nama pasien
def lihatAntrianPasien(Nama_Pasien):
    print()
    print(f'Antrian Pasien atas nama {Nama_Pasien}')
    dict_len = len_dict_IGD()
    print()
    print(f"{'Kode':<6} | {'Nama':<{dict_len['nama']}} | {'tanggal':<{dict_len['tanggal_lahir']}} | {'Umur':<4} | {'Gender':<{dict_len['jenis_kelamin']}} | {'bpjs':<{dict_len['bpjs']}} | {'status':<{dict_len['status']}} | {'Jam':<{dict_len['jam_datang']}} | {'D-Jaga':<{dict_len['dokter_jaga']}} | {'D-Spes':<11}")
    for key, value in pasienIGD.items():
        if value['nama'] == Nama_Pasien:
            print(
                f"{key:<6} | "
                f"{value['nama']:<{dict_len['nama']}} | "
                f"{value['tanggal_lahir']:<{dict_len['tanggal_lahir']}} | "
                f"{value['umur']:<4} | "
                f"{value['jenis_kelamin']:<{dict_len['jenis_kelamin']}} | "
                f"{value['bpjs']:<{dict_len['bpjs']}} | "
                f"{str(value['status']):<{dict_len['status']}} | "
                f"{value['jam_datang']:<{dict_len['jam_datang']}} | "
                f"{value['dokter_jaga']:<{dict_len['dokter_jaga']}} | "
                f"{str(value['dokter_spesialis']):<11}")
    print()

# Melihat pasien rawat inap berdasarkan nama pasien
def lihatInapPasien(Nama_Pasien):
    print()
    print(f'Pasien Rawat Inap atas nama {Nama_Pasien}')
    print()
    dict_len = len_dict_Inap()
    print(f"{'Kode':<6} | {'Nama':<{dict_len['nama']}} | {'tanggal':<{dict_len['tanggal_lahir']}} | {'Umur':<4} | {'Gender':<{dict_len['jenis_kelamin']}} | {'bpjs':<{dict_len['bpjs']}} | {'D-Jaga':<{dict_len['dokter_jaga']}} | {'D-Spes':<{dict_len['dokter_spesialis']}}")
    for key, value in pasienInap.items():
        if value['nama'] == Nama_Pasien:
            print(
                f"{key:<6} | "
                f"{value['nama']:<{dict_len['nama']}} | "
                f"{value['tanggal_lahir']:<{dict_len['tanggal_lahir']}} | "
                f"{value['umur']:<4} | "
                f"{value['jenis_kelamin']:<{dict_len['jenis_kelamin']}} | "
                f"{value['bpjs']:<{dict_len['bpjs']}} | "
                f"{value['dokter_jaga']:<{dict_len['dokter_jaga']}} | "
                f"{str(value['dokter_spesialis']):<11}")
    print()
    print()

# Lihat tabel pasien yang berada di IGD
def lihatAntrianKosong():
    dict_len = len_dict_IGD()
    print()
    print(f"{'Kode':<6} | {'Nama':<{dict_len['nama']}} | {'tanggal':<{dict_len['tanggal_lahir']}} | {'Umur':<4} | {'Gender':<{dict_len['jenis_kelamin']}} | {'bpjs':<{dict_len['bpjs']}} | {'status':<{dict_len['status']}} | {'Jam':<{dict_len['jam_datang']}} | {'D-Jaga':<{dict_len['dokter_jaga']}} | {'D-Spes':<11}")
    for key, value in pasienIGD.items():
        print(
            f"{key:<6} | "
            f"{value['nama']:<{dict_len['nama']}} | "
            f"{value['tanggal_lahir']:<{dict_len['tanggal_lahir']}} | "
            f"{value['umur']:<4} | "
            f"{value['jenis_kelamin']:<{dict_len['jenis_kelamin']}} | "
            f"{value['bpjs']:<{dict_len['bpjs']}} | "
            f"{str(value['status']):<{dict_len['status']}} | "
            f"{value['jam_datang']:<{dict_len['jam_datang']}} | "
            f"{value['dokter_jaga']:<{dict_len['dokter_jaga']}} | "
            f"{str(value['dokter_spesialis']):<11}")
    print()

# Membuat daftar IGD pasien baru
def daftarAntrian(namaPasien, BPJS, Gender, Tanggal_Lahir, Umur, jamDatang):
    global pasienIGD
    generate_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))

    lihatDokterUmum()
    Nomor1 = int(input('Dokter umum mana yang akan anda kunjungi, tulis menggunakan nomor? '))

    lihatDokterSpesialis()
    Nomor2 = int(input('Dokter Spesialis mana yang akan anda kunjungi, tulis menggunakan nomor? '))

    for i in range(len(staff) - 1):
        if Nomor1 == staff[i][0]:
            namaDokter = staff[i][2]
            continue
        if Nomor2 == staff[i][0]:
            namaDokter2 = staff[i][2]
            continue
    
    if (namaDokter is None) and (namaDokter2 is None):
        return print('Nomor dokter tidak ditemukan')
    
    pasienIGD[generate_id] = {
        "nama" : namaPasien,
        "tanggal_lahir" : Tanggal_Lahir,
        "umur": Umur,
        "jenis_kelamin": Gender,
        "bpjs": BPJS,
        "status": None,
        "jam_datang": jamDatang,
        "dokter_jaga": namaDokter,
        "dokter_spesialis": namaDokter2
    }
    print(pasienIGD[generate_id])

# Menghapus atau memulangkan pasien dengan menggunakan kode ID pasien
def hapusAntrian(Kode):
    k = None
    for i in pasienIGD.keys():
        if i == Kode:
            k = i
            print(k)
            break
    if k : 
        del pasienIGD[k]
        return
    else : return print('Maaf Kode tidak ada')

# Pasien IGD pindah ke rawat inap
def pindahInap(keyPasiennya):
    if keyPasiennya not in pasienIGD.keys() : return print('Maaf key kodenya salah')
    Pindah = pasienIGD[keyPasiennya].copy()
    Pindah.pop('status')
    Pindah.pop('jam_datang')
    pasienInap[keyPasiennya] = Pindah
    del pasienIGD[keyPasiennya]

# Check apakah dia staff selain dokter umum, spesialis, apoteker, management
def checkStaff (StaffAdmin):
    # Jika apoteker
    if StaffAdmin == 'Apoteker' : return 0.0

    # Buat management
    if (staff[len(staff) - 1][1] == StaffAdmin) or (staff[len(staff) - 1][2] == StaffAdmin) : return 2.0

    # Buat mencari dokter
    for i in range(len(staff) - 1):

        # Dokter Umum
        if (staff[i][1] == 'D-Umum') and (staff[i][2] == StaffAdmin):
            return 1.0
        # Dokter Spesialis
        elif (staff[i][1].startswith('D-')) and (staff[i][1] != 'D-Umum') and (staff[i][2] == StaffAdmin):
            return 1.5
    
    # Jika nama tidak ada
    return None

# Melihat Obat yang di tempat penyimpanan
def lihatObat():
    print()
    print(f"Kode | {'Nama':<20} | {'Stock':<6}| Harga")
    for kode, data in dictObat.items():
        print(f"{kode}  | {data['Nama']:<20} | {data['Stock']:>6} | {data['Harga']:>5}")

# Apoteker belanja obat
def BelanjaObat():
    True_Index = 0
    List_cart = []
    costumer_stuck_of_choise = True
    
    while costumer_stuck_of_choise:
        lihatObat()

        #Cart on the list
        #Command masukkan index obat

        Kode_Obat_yang_dibeli = str(input("\nMasukkan kode obat yang akan dibeli : "))

        if Kode_Obat_yang_dibeli not in dictObat.keys():
            print(f"\nMaaf obat dengan {Kode_Obat_yang_dibeli} tidak ditemukan")
            continue

        # Command masukkan jumlah obat
        indexBeli = int(input("\nMasukkan jumlah obat yang ingin dibeli : "))
        Obat_Dibeli = dictObat[Kode_Obat_yang_dibeli]['Nama']

        if indexBeli <= dictObat[Kode_Obat_yang_dibeli]['Stock']:
            k = [dictObat[Kode_Obat_yang_dibeli]['Nama'], indexBeli, dictObat[Kode_Obat_yang_dibeli]['Harga']]
            List_cart.append(k)
        else:
            print(f"Stock tidak cukup, stock {Obat_Dibeli} tinggal {dictObat[Kode_Obat_yang_dibeli]['Stock']}")
        
        choise = str(input("\nMau beli yang lain? (ya/tidak) : "))
        if choise in listIya:
            continue
        elif choise in listTidak:
            costumer_stuck_of_choise = False
    
    if not List_cart:
        return print('Anda tak jadi membeli')
    
    print("\nDetail Belanja")        
    print(f"{'Nama':<20} | {'Qty':<5} | {'Harga':<8} | {'Total Harga':<12}")
    T_THarga = 0
    for i in range(len(List_cart)):
        TotalHarga = List_cart[i][1] * List_cart[i][2]
        List_cart[i].append(TotalHarga)
        print(f"{List_cart[i][0]:<20} | {List_cart[i][1]:<5} | {List_cart[i][2]:<8} | {List_cart[i][3]:<12}")
        T_THarga = T_THarga + TotalHarga
    
    # Jika punya asuransi bpjs

    bpjs = str(input('Apakah pasien ada bpjs(y/n)?'))

    if bpjs in listIya : return print('Sudah dibayar BPJS')

    print(f"Total Yang Harus Dibayar = {T_THarga}")
    _Uang = int(input("Masukkan uang anda : "))
    if _Uang < T_THarga:
            return print(f"Transaksi anda dibatalkan \n uangnya kurang sebesar {T_THarga - _Uang}")
    elif _Uang == T_THarga:
        return print("Terima Kasih\n")
    elif _Uang > T_THarga:
        return print(f"\n Uang kembali anda : {_Uang - T_THarga}")

# Lihat tabel pasien di tempat ruang inap dengan nama dokter
def lihatInap(namaDokter):
    #maxLengthsInap
    print()
    print(f'Pasien Rawat Inap atas nama {namaDokter}')
    print()
    dict_len = len_dict_Inap()
    print(f"{'Kode':<6} | {'Nama':<{dict_len['nama']}} | {'tanggal':<{dict_len['tanggal_lahir']}} | {'Umur':<4} | {'Gender':<{dict_len['jenis_kelamin']}} | {'bpjs':<{dict_len['bpjs']}} | {'D-Jaga':<{dict_len['dokter_jaga']}} | {'D-Spes':<11}")
    for key, value in pasienInap.items():
        if (value['dokter_jaga'] == namaDokter) or (value['dokter_spesialis'] == namaDokter):
            print(
                f"{key:<6} | "
                f"{value['nama']:<{dict_len['nama']}} | "
                f"{value['tanggal_lahir']:<{dict_len['tanggal_lahir']}} | "
                f"{value['umur']:<4} | "
                f"{value['jenis_kelamin']:<{dict_len['jenis_kelamin']}} | "
                f"{value['bpjs']:<{dict_len['bpjs']}} | "
                f"{value['dokter_jaga']:<{dict_len['dokter_jaga']}} | "
                f"{str(value['dokter_spesialis']):<11}")
    print()

# Lihat tabel pasien IGD nama dokter
def lihatAntrian(namaDokter):
    print()
    print(f'Antrian Pasien atas nama {namaDokter}')
    dict_len = len_dict_IGD()
    print()
    print(f"{'Kode':<6} | {'Nama':<{dict_len['nama']}} | {'tanggal':<{dict_len['tanggal_lahir']}} | {'Umur':<4} | {'Gender':<{dict_len['jenis_kelamin']}} | {'bpjs':<{dict_len['bpjs']}} | {'status':<{dict_len['status']}} | {'Jam':<{dict_len['jam_datang']}} | {'D-Jaga':<{dict_len['dokter_jaga']}} | {'D-Spes':<11}")
    for key, value in pasienIGD.items():
        if (value['dokter_jaga'] == namaDokter) or (value['dokter_spesialis'] == namaDokter):
            print(
                f"{key:<6} | "
                f"{value['nama']:<{dict_len['nama']}} | "
                f"{value['tanggal_lahir']:<{dict_len['tanggal_lahir']}} | "
                f"{value['umur']:<4} | "
                f"{value['jenis_kelamin']:<{dict_len['jenis_kelamin']}} | "
                f"{value['bpjs']:<{dict_len['bpjs']}} | "
                f"{str(value['status']):<{dict_len['status']}} | "
                f"{value['jam_datang']:<{dict_len['jam_datang']}} | "
                f"{value['dokter_jaga']:<{dict_len['dokter_jaga']}} | "
                f"{str(value['dokter_spesialis']):<11}")
    print()

# Rubah status pasien oleh dokter jika ,hanya dokter spesialis yang bisa, pasien diperlukan untuk rawat inap atau operasi            
def rubahStatusPasien(kode,kodePasien):
    # Jika kode tidak ditemukan
    if kodePasien not in pasienIGD.keys(): return print('Maaf kode pasien tidak ditemukan')

    # Kode ditentukan di awal, kode 1 untuk merubah status apa saja hanya pasien IGD menjadi status 'Operasi'
    if kode == 1: 
        pasienIGD[kodePasien]['status'] = 'Operasi'
    
    # Kode ditentukan di awal, kode 2 untuk merubah status apa saja hanya pasien IGD menjadi status 'Operasi'
    elif kode == 2:
        pasienIGD[kodePasien]['status'] = 'Rawat Inap'

# Melihat dokter Umum yang ada
def lihatDokterUmum():
    print()
    print(f"{'No':<{maxLengthStaff[0]}} | {'Dokter':<{maxLengthStaff[1]}} | {'Nama':<{maxLengthStaff[2]}} | ")
    for i in range(len(staff) - 1):
        if staff[i][1] == 'D-Umum':
            print(
                f"{staff[i][0]:<{maxLengthStaff[0]}}  | "
                f"{staff[i][1]:<{maxLengthStaff[1]}} | "
                f"{staff[i][2]:<{maxLengthStaff[2]}} | ")
    print()

# Melihat dokter spesialis yang ada
def lihatDokterSpesialis():
    print()
    print(f"{'No':<{maxLengthStaff[0]}} | {'Dokter':<{maxLengthStaff[1]}} | {'Nama':<{maxLengthStaff[2]}} | ")
    for i in range(len(staff) - 1):
        if staff[i][1] != 'D-Umum':
            print(
                f"{staff[i][0]:<{maxLengthStaff[0]}}  | "
                f"{staff[i][1]:<{maxLengthStaff[1]}} | "
                f"{staff[i][2]:<{maxLengthStaff[2]}} | ")
    print()


while programKerja:
    percobaanMasuk = True
    print('Selamat datang di rumah sakit anda')

    # Mengecek apakah pasien atau dokter
    Akun = str(input('pasien (Y/N) : ')) 
    if Akun in listIya:
        
        # Loopingnya
        while Admin:

            # Variable pasien jika ada pasien masuk, atau pasien akan merubah data
            DataPasien = None

            # Tulis nama pasien masuk, atau pasien akan merubah data
            if not namaPasien : 
                namaPasien = str(input('Masukkan nama Anda : '))
                namaPasien = namaPasien.title()

            # Apakah pasien telah terdaftar di rawat inap atau antrian
            # Jika inap berarti 2
            # Jika antri berarti 1
            # Jika None berarti kosong

            if not DataPasien: 
                DataPasien = checkPasien(namaPasien)
                keyPasiennya = keyPasiennyadef(namaPasien)
            print()
            
            # Jika pasien inap
            if DataPasien == 2 : lihatAntrianPasien(namaPasien)

            # Jika pasien IGD
            elif DataPasien == 1 : lihatInapPasien(namaPasien)
            # Jika pasien baru masuk
            else : print('Maaf pasien belum terdaftar \n')

            print(''' \n Pilihan
1. List pasien
2. Pasien Masuk
3. Pasien Pulang
4. Pasien masuk rawat inap atau tidak
5. Selesai''')
            
            # Masukkan nomor pada pasien
            coba = int(input('\nSilahkan pilih nomor dan program apa yang akan anda ingin dijalankan? '))
            print()

            # Melihat antrian sekarang
            if(coba == 1):
                lihatAntrianKosong()

            # Memasukkan kelengkapan data Pasien
            elif(coba == 2): 
                BPJS = str(input('Apakah punya BPJS(y/n) ?'))
                if BPJS in listIya : BPJS = True
                elif BPJS in listTidak : BPJS = False
                Gender = str(input('Apakah Jenis kelamin(L/P) ?'))
                if Gender in listLakilaki : Gender = 'Laki-laki'
                elif Gender in listPerempuan : Gender = 'Perempuan'
                Tanggal_Lahir = str(input(' Masukkan tanggal lahir(YYYY-MM-DD) : '))
                Umur = int(input('Umur pasien? '))
                jamDatang = str(input('Jam datang (Jam:Menit) '))

                daftarAntrian(namaPasien, BPJS, Gender, Tanggal_Lahir, Umur, jamDatang)

            # Bagi pasien yang akan dipulangkan
            elif(coba == 3):
                kodenya = str(input('Masukkan kode pasien : '))
                hapusAntrian(kodenya)
                print(f'Kode {kodenya} sudah hilang')     
                DataPasien = None          
            
            # Bagi pasien dipindahkan ke rawat inap
            elif(coba == 4):
                if pasienIGD[keyPasiennya]['status'] == 'Rawat Inap': pindahInap(keyPasiennya)
                elif pasienIGD[keyPasiennya]['status'] == 'Operasi': print('silahkan menunggu...')
                else: print('maaf anda tidak bisa, perlu keterangan dokter')

            # Looping keluar
            elif(coba == 5):
                Admin = False

    elif Akun in listTidak:
        
        # Looping programnya
        while percobaanMasuk:

            # Jika percobaan masuk cuman 3 kali
            if percobaan == 0 : 
                percobaanMasuk = False

            # Buat masukkan nama dari staff pengganti ID
            StaffAdmin = str(input('Masukkan nama Anda :'))
            StaffAdmin = StaffAdmin.capitalize()

            # Mengecheck apakah ada nama staff, dan termasuk dokter atau management
            AccountStaff = checkStaff(StaffAdmin)
            if AccountStaff is None : 
                print('Maaf anda tidak terdaftar')

            # Jika staff adalah apoteker
            while AccountStaff == 0.0 :
                BelanjaObat()
                keluar = str(input('Keluar aplikasi(y/n) ?'))
                if keluar in listIya: 
                    percobaan += 1
                    AccountStaff = None

            # Jika staff adalah dokter
            while AccountStaff == 1.0  :

                # Melihat pasien di rawat inap atas nama dokter
                lihatInap(StaffAdmin)

                # Melihat antrian pasien atas atau rujukan dari dokter
                lihatAntrian(StaffAdmin)
                
                stop = str(input('tekan apapun dan enter untuk keluar'))
                stop = None
                AccountStaff = None

            while AccountStaff == 1.5  :

                # Melihat pasien di rawat inap atas nama dokter
                lihatInap(StaffAdmin)

                # Melihat antrian pasien atas atau rujukan dari dokter
                lihatAntrian(StaffAdmin)
                
                stop = int(input('Apakah menyarankan pasien untuk operasi atau rawat (0 <Tidak> , 1 <Operasi> , 2 <Rawat Inap>)? '))
                if stop == 0: stop = None
                elif stop in [1, 2]: 
                    kodePasien = str(input('Tolong tulis kode pasien? '))
                    rubahStatusPasien(stop, kodePasien)  

                stop = None
                AccountStaff = None

            # Buat management masukkan obat
            while AccountStaff == 2.0 :
                print(''' Pilihan
1. Lihat pasokan obat
2. Masukkan obat
3. Tambah atau Kurangi obat
4. Hapus Obat
5. Selesai''')

                coba4 = int(input('Tolong pilih nomor perintah '))# Bagusin lagi
                
                # Lihat list obat di rumah sakit
                if coba4 == 1 : lihatObat()

                # Masukkan obat
                elif coba4 == 2 : 

                    # Buat memasukkan obat
                    NamaObat = str(input('Nama Obat : '))
                    Kode = str(input('Kode Obat : '))
                    Dup = False # Duplicat
                    if Kode not in dictObat.keys() :
                        for Obat in (item['nama'] for item in dictObat.values()):
                            if Obat == NamaObat : Dup = True

                        if not Dup:
                            Stock = int(input('Jumlah stock obat : '))
                            hargaObat = int(input('Harga obat : '))
                            # Masukkan obat ke dictionary
                            dictObat.update({
                                NamaObat:{
                                    'Kode': Kode,
                                    'Stock' : Stock,
                                    'Harga' : hargaObat
                                }
                            })
                            
                        # Jika obat sudah ada
                        else : print('Obat sudah ada')
                    
                    # Jika kode obat sudah ada
                    else: print('Kode obat telah digunakan')


                # Menambah atau mengurangi stock obat
                elif coba4 == 3 : 
                    # memasukkan nama obat
                    kodeObat = str(input('Kode obatnya apa? '))

                    # Jika mau ditambah atau dikurangi
                    Tambah = str(input('Apakah ditambah, jika tidak akan dikurangi (Y/N)? '))

                    if Tambah in listIya : Tambah = True
                    elif Tambah in listTidak : Tambah = False
                    else : Tambah = False
                    
                    if kodeObat in dictObat.keys():
                        Jumlah = int(input('Berapa obat yang ditambah atau dikurangi '))
                        if Tambah : dictObat[kodeObat]['Stock'] += Jumlah
                        elif not Tambah : dictObat[kodeObat]['Stock'] -= Jumlah
                        print(f'Stock {kodeObat} sekarang : {dictObat[kodeObat]['Stock']}')
                    else : print('Maaf nama obat tidak ditemukan')

                #Menghapus obat
                elif coba4 == 4 : 
                    kodeObat = str(input('Kode obatnya apa? '))
                    if kodeObat in dictObat:
                        print(f'{dictObat[kodeObat]['nama']} telah dihapus')
                        del dictObat[kodeObat]
                    else : print('Nama obat tidak ditemukan')

                # Keluar Program Looping
                elif coba4 == 5 : 
                    percobaan += 1
                    AccountStaff = None
        
            # Keluar loop untuk staff
            KeluarProgram = str(input('Keluar aplikasi staff (Y/N) :'))
            if KeluarProgram in listIya :
                percobaanMasuk = False

            # Jika gagal sekali atau pertama kali
            # Dan kalau keluar tidak akan ditanya
            if (percobaan < 3) and (percobaanMasuk == True) : print(f'\nAnda bisa mencoba {percobaan} kali lagi')
            percobaan -= 1
    
    KeluarProgram = str(input('Keluar aplikasi (Y/N) :'))
    if KeluarProgram in listIya : 
        programKerja = False




        
    



