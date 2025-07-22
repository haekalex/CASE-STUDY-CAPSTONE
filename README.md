# CASE-STUDY-CAPSTONE
Halo nama saya Haekal, ini program CRUD sederhana yang  dibuat menggunakan python, untuk menambah, melihat, mengubah, dan menghapus data. Program ini berbasis teks, hanya berbentuk 1 file, dan dijalankan dengan terminal.
Versi apk : Python 3.13.5
Case yang saya pakai adalah data pasien IGD rumah sakit
Hal yang perlu diperhatikan adalah Pertama menggunakan data dummy, dan menggunakan asuransi yang tidak reinbursement. Kedua Menggunakan import string dan random untuk membuat ID pasien dan tidak menggunakan import datetime sehingga tidak sempurna dalam pemasukan data. Ketiga hanya menyatukan data memori dummy menggunakan nested dist, keculai tuple nestedlist untuk staff, tanpa cs atau json. Keempat Ada data memori IGD dan data memori Rawat Inap yang akan berhubungan dengan data 'status' pasien yang hanya diubah oleh staff dokter spesialist. Kelima menghapus data pasien di data memori IGD dan sebelum memindahkannya ke data rawat inap. Dan terakhir data memori obat untuk melihat data memori, membeli obat dengan apoteker dan melihat dan menambah data memori obat dengan management.

Ada 3 tokoh dan semua menggunakan nama sebagai ID yang dipakai untuk bisa mengubah-ubah data
Pasien   - Nama Lama   - Lihat penempatan Pasien
                       - Lihat Pasien Inap dan IGD lain
                       - Pindah IGD ke Rawat Inap selama status rawat inap
Pasien   - Nama Baru    - Lihat penempatan Pasien
                        - Lihat Pasien Inap dan IGD lain
Staff   - Dokter Umum (ID atau password Nama) - lihat pasien sesuai key untuk dokter umum
Staff   - Dokter Spesialis                    - lihat pasien sesuai key untuk dokter spesialis
                                              - Merubah status pasien IGD, dengan isi apapun menjadi Rawat Inap atau Operasi
Staff      - Apoteker    - Membeli obat (biasanya mendapat resep dari pasien dan total yang perlu dibayar)
Staff      - Management  - Menambah, mengurangi stock obat, menambah baru dan menghapus data obat
