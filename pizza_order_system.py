# -*- coding: utf-8 -*-
import csv
from datetime import *
import time


class Pizza:
    def __init__(self, description, price):
        self._description = description
        self._price = price

    def get_description(self):
        return self._description

    def get_cost(self):
        return self._price


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 10.0)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 12.0)


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 14.0)


class DominosPizza(Pizza):
    def __init__(self):
        super().__init__("Dominos Pizza", 8.0)


# Decorator sınıfı
class Decorator(Pizza):
    def __init__(self, component):
        super().__init__(component.get_description(), component.get_cost())
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + super().get_cost()

    def get_description(self):
        return self.component.get_description() + ' ' + super().get_description()


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Zeytin"
        self._price = 1.0


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Mantar"
        self._price = 4.0


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Keçi Peyniri"
        self._price = 6.0


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Et"
        self._price = 8.0


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Soğan"
        self._price = 9.0


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self._description = "ve Mısır"
        self._price= 1.0


def print_menu():
    with open('C:\\Users\\dizge\\Desktop\\Masaustu\\flutter\\Projects\\Python-Bootcamp\\menu.txt', 'r', encoding='utf-8') as menu_list:
        menu = menu_list.read()
    print(menu)


print("""\tMerhaba! Pizza Sipariş Sistemine Hoş Geldiniz. Menü Aşağıda Sunulmuştur.
-------------------------------------------------------------------------------""")

time.sleep(0.5)

print_menu()
global pizza
global sauce



while True:
    # Kullanıcıdan pizza seçimini iste
    pizza_choice = input("Lütfen Pizza Tabanı Seçimi Yapınız: ")

    # Seçilen pizzanın fiyatını hesapla
    if pizza_choice == "1":
        pizza = ClassicPizza()
        break
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
        break
    elif pizza_choice == "3":
        pizza = TurkishPizza()
        break
    elif pizza_choice == "4":
        pizza = DominosPizza()
        break
    else:
        print("Geçersiz bir pizza seçimi yaptınız.")
        continue

time.sleep(0.5)
# Kullanıcıdan sos seçimini iste
while True:
    sauce_choice = input("Lütfen Bir Sos Seçimi Yapınız: ")

    # Seçilen sosun tutarını hesapla
    if sauce_choice == "11":
        sauce = Zeytin(pizza)
        break
    elif sauce_choice == "12":
        sauce = Mantar(pizza)
        break
    elif sauce_choice == "13":
        sauce = KeciPeyniri(pizza)
        break
    elif sauce_choice == "14":
        sauce = Et(pizza)
        break
    elif sauce_choice == "15":
        sauce = Sogan(pizza)
        break
    elif sauce_choice == "16":
        sauce = Misir(pizza)
        break
    else:
        print("Geçersiz bir sos seçimi yaptınız.")
        continue

time.sleep(0.5)
print("---------------------------------------------------")
print(f"Sipariş Özeti: {sauce.get_description()}")
# Pizzanın tutarını ve seçilen sosun tutarını topla
total_price = sauce.get_cost()
time.sleep(0.5)
# Toplam tutarı hesapla ve ekrana yazdır
print(f"Toplam tutar: ${total_price}")
print("---------------------------------------------------")

def get_user_info():
    while True:
        name = input("İsim: ")
        if any(char.isdigit() for char in name):
            print("İsimde sayı kullanılamaz. Tekrar deneyin.")
            continue
        else:
            break

    while True:
        tc = input("TC Kimlik Numarası: ")
        if len(tc) != 11 and tc.isdigit():
            print("TC Kimlik Numarası 11 Haneden Oluşmalıdır.")
            continue
        elif not tc.isdigit():
            print("TC Kimlik Numarası Sadece Sayılardan Oluşmalıdır.")
        else:
            break

    while True:
        card_number = input("Kredi Kartı Numarası: ")
        if not card_number.isdigit():
            print("Kredi kartı numarası sadece sayılardan oluşmalıdır.")
            continue
        else:
            break

    while True:
        card_pw = input("Kredi Kartı Şifresi: ")
        if len(card_pw) != 4 or not card_pw.isdigit():
            print("Kredi kartı şifresi 4 haneli olmalıdır ve sadece sayılardan oluşmalıdır.")
            continue
        else:
            break

    return name, tc, card_number, card_pw

name, tc, card_number, card_pw = get_user_info()
order_time = datetime.now()
order_time = datetime.ctime(order_time)

with open("Siparis_veritabani.csv", mode="a", newline="", encoding='utf-8') as orders_file:
    orders_writer = csv.writer(orders_file, delimiter="|", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    orders_writer.writerow(
        [f"İsim: {name} | TC: {tc} | Kart Numarası: {card_number} | Kart Şifresi: {card_pw} | Sipariş Zamanı: {order_time} | Sipariş İçeriği: {sauce.get_description()} | Tutar: ${total_price}"])
print("Siparişiniz başarıyla oluşturuldu. Teşekkür ederiz!")