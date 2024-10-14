print('\n-----------------------------------------')
print('Nama     : Aliyah Azzah Sekedang         ')
print('Program  : Mini Projek Dasar Pemograman 2')
print('NIM      : 2409116021                    ')
print('Kelas    : A                             ')
print('-----------------------------------------')

from prettytable import PrettyTable

# Mendeskripsikan Paket
packages = [
    {"number": 1, "name": "Basic", "price": 75000},
    {"number": 2, "name": "Standard", "price": 120000},
    {"number": 3, "name": "Premium", "price": 185000},
]

# Mencatat Transaksi
transactions = []

# Login sebagai Admin atau Member
def login(role):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    while True:
        if role == "admin" and username == "mba_admin" and password == "kerjalembur":
            print("\nLogin successful! Welcome, admin.")
            return "admin"
        elif role == "member" and username == "aliyahazs" and password == "nontondulu":
            print("\nLogin successful! Welcome, member.")
            return "member"
        else:
            print("\n⚠️  Login failed! Please enter 'username' and 'password' again. ⚠️")
            username = input("\nEnter your username: ")
            password = input("Enter your password: ")

# Menu Admin
def admin_menu():
    while True:
        print("\n☰  Admin Menu")
        print("1. View all Packages")
        print("2. Add a Package")
        print("3. Update a Package")
        print("4. Delete a Package")
        print("5. View Transactions")
        print("6. Logout")
        
        opsi = input("\nWhat do you want to do? Pick an option: ")
        
        if opsi == "1":
            view_packages()
        elif opsi == "2":
            add_package()
        elif opsi== "3":
            update_package()
        elif opsi == "4":
            delete_package()
        elif opsi == "5":
            view_transactions()
        elif opsi == "6": 
            print("Logging out... Returning to login menu!")
            return
        else:
            print("\n⚠️  Invalid option! Please try again. ⚠️")

# Menampilkan Paket
def view_packages():
    table = PrettyTable()
    table.field_names = ["No", "Package Name", "Price"]
    for package in packages:
        table.add_row([package["number"], package["name"], package["price"]])
    print("\n==========================================")
    print("📽.ᐟ  🍿 ✧˖ Available Packages ˖✧ 🍿 ᐟ. 📽")
    print("==========================================")
    print(table)

# Menambahkan Paket
def add_package():
    name = input("\nEnter new package name: ")
    price = int(input("Enter package price: "))
    new_number = max(pkg["number"] for pkg in packages) + 1
    packages.append({"number": new_number, "name": name, "price": price})
    print(f"Package '{name}' added successfully!")

# Memperbarui Paket
def update_package():
    view_packages()
    package_number = int(input("\nEnter the number of the package you want to update: "))
    for package in packages:
        if package["number"] == package_number:
            package["name"] = input("Enter new name: ")
            package["price"] = int(input("Enter new price: "))
            print("Package updated successfully!")
            return
    print("\n⚠️  Package not found. ⚠️")

# Menghapus Paket
def delete_package():
    view_packages()
    package_number = int(input("\nEnter the number of the package you want to delete: "))
    global packages
    packages = [package for package in packages if package["number"] != package_number]
    print("Package deleted successfully! ")

# Menu Member
def member_menu():
    while True:
        print("\n☰  Member Menu")
        print("1. View Packages")
        print("2. Purchase a Package")
        print("3. View Transactions")
        print("4. Logout")
        
        opsi = input("\nWhat do you want to do? Pick an option: ")
        
        if opsi == "1":
            view_packages()
        elif opsi== "2":
            purchase_package()
        elif opsi == "3":
            view_transactions()
        elif opsi == "4":  # Member menu logout
            print("Logging out... Returning to login menu!")
            return 
        else:
            print("\n⚠️  Invalid option! Please try again. ⚠️")

# Pembelian Paket Streaming
def purchase_package():
    while True:
        view_packages()
        package_number = int(input("\nEnter the package number you want to purchase: "))
        
        for package in packages:
            if package["number"] == package_number:
                confirmation = input(f"You've selected '{package['name']}' for {package['price']}. Proceed with payment? (yes/no): ")
                if confirmation.lower() == 'yes':
                    # Masukkan tanggal pembelian paket
                    purchase_date = input("Enter purchase date (YYYY-MM-DD): ")

                    # Transaksi
                    transaction = {
                        "name": package["name"],
                        "price": package["price"],
                        "date": purchase_date
                        }
                    transactions.append(transaction)
                    print("\n💳 Payment successful! You are now subscribed!")
                break
        else:
            print("\n⚠️  Package not found. ⚠️")

        # Melakukan transaksi kembali?
        another_purchase = input("\nDo you want to make another transaction? (yes/no): ").lower()
        if another_purchase != "yes":
            break

# Menampilkan semua Transaksi
def view_transactions():
    if not transactions:
        print("No transactions yet.")
        return
    
    table = PrettyTable()
    table.field_names = ["Package", "Price", "Purchase Date"]

    for transaction in transactions:
        table.add_row([transaction["name"], transaction["price"], transaction["date"]])

    print("\n All Transactions:")
    print(table)

# Menu Utama (Main Menu)
while True:
    print("\n∘ ₊ ✧ ────── WELCOME TO THE NETFLIX STREAMING SERVICE 📺 ────── ✧ ₊ ∘")
    role = input("\nWhat role do you want to log in to? (admin/member): ").lower()
    
    if role in ["admin", "member"]:
        if login(role):
            if role == "admin":
                admin_menu()
            else:
                member_menu()
    else:
        print("\n⚠️  Invalid role! Please enter 'admin' or 'member'. ⚠️")
        continue
    
    if input("Do you want to exit? (yes/no): ").lower() == 'yes':
        print("THANK YOU FOR USING OUR NETFLIX MEMBERSHIP SYSTEM! SEE YOU NEXT TIME! ʕ •ɷ•ʔฅ")
        break