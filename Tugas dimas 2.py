class MenuKopi:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga


class AnandaCoffee:
    def __init__(self):
        self.__menu_kopi = [
            MenuKopi("ES Kopi Susu", 11000),
            MenuKopi("ES Kopi Coklat", 12000),
            MenuKopi("ES Kopi Hitam", 11000),
            MenuKopi("Ice Americano", 14000)
        ]

    def tampilkan_menu(self):
        print("""
        ==============================
        
        Ananda Coffee
        List Menu Minuman Kopi
     
        ==============================
        A. ES Kopi Susu : Rp 11.000
        B. ES Kopi Coklat : Rp 12.000
        C. ES Kopi Hitam : Rp 11.000
        D. Ice Americano : Rp 14.000
        ==============================
        """)

    def pesan_menu(self):
        pesan = input("Masukkan list abjad menu kopi = ").lower()
        jumlah_pesan = int(input("Masukkan jumlah pesanan = "))

        menu = self.__get_menu(pesan)
        if menu is not None:
            nama = menu.get_nama()
            harga = menu.get_harga() * jumlah_pesan
            ppn = int(harga * 0.1)

            if jumlah_pesan >= 5:
                diskon = int(harga * 0.2)
                total_harga = harga - diskon + ppn
            else:
                diskon = 0
                total_harga = harga + ppn

            print("--------------------------")
            print("Ananda Coffee")
            print("--------------------------")
            print("Menu :", nama)
            print("Jumlah Pesan :", jumlah_pesan)
            print("Harga :", harga)
            print("Diskon :", diskon)
            print("PPN :", ppn)
            print("--------------------------")
            print("Jumlah Bayar :", total_harga)
            print("--------------------------")
        else:
            print("Menu tidak tersedia.")

    def __get_menu(self, pesan):
        for menu in self.__menu_kopi:
            if pesan == menu.get_nama().lower():
                return menu
        return None


pilihan = "iya"
ananda_coffee = AnandaCoffee()

while pilihan == "iya":
    ananda_coffee.tampilkan_menu()
    ananda_coffee.pesan_menu()
    pilihan = input("Apakah Anda ingin order kembali? (iya/tidak) = ").lower()
