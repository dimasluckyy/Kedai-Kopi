class CoffeeMenu:
    def __init__(self):
        self.menu = {
            "A": {"name": "ES Kopi Susu", "price": 11000},
            "B": {"name": "ES Kopi Coklat", "price": 12000},
            "C": {"name": "ES Kopi Hitam", "price": 11000},
            "D": {"name": "Ice Americano", "price": 14000}
        }

    def calculate_total_price(self, menu_choice, quantity):
        item = self.menu.get(menu_choice.upper())
        if item:
            price = item["price"] * quantity
            discount = 0
            if quantity >= 5:
                discount = int(price * 0.2)
            subtotal = price - discount
            tax = int(subtotal * 0.1)
            total_price = subtotal + tax
            return item["name"], price, discount, tax, total_price
        else:
            return "-", "-", "-", "-", "-"

    def display_menu(self):
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

    def display_order(self, menu_choice, quantity, name, price, discount, tax, total_price):
        print("--------------------------")
        print("Ananda Coffee")
        print("--------------------------")
        print("Menu:", name)
        print("Jumlah Pesan:", quantity)
        print("Harga:", price)
        print("Diskon:", discount)
        print("PPN:", tax)
        print("--------------------------")
        print("Jumlah Bayar:", total_price)
        print("--------------------------")


def main():
    coffee_menu = CoffeeMenu()
    choice = "Y"
    while choice == "Y":
        coffee_menu.display_menu()
        menu_choice = input("Masukkan list abjad menu kopi: ")
        quantity = int(input("Masukkan jumlah pesanan: "))
        name, price, discount, tax, total_price = coffee_menu.calculate_total_price(menu_choice, quantity)
        coffee_menu.display_order(menu_choice, quantity, name, price, discount, tax, total_price)
        choice = input("Apakah Anda ingin order kembali? (Y/N): ")


if __name__ == "__main__":
    main()
