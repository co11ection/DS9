from store import Store
from constants import MENU

store = Store()



def main():
    while True:
        print(MENU)
        choice = input("Введите команду: ")
        if choice == "1":
            store.add_product()
        elif choice == "2":
            store.show_products()
        elif choice == "0":
            print("Программа закрыто")
            break
        

if __name__ == "__main__":
    main()