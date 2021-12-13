# code by utari8

import random

def game():
    user = input("Masukkan pilihan (batu, gunting, kertas) : ")
    pilihan = ["batu", "gunting", "kertas"]
    computer = random.choice(pilihan)

    print("Kamu memilih ", user,", Komputer memilih ", computer)
    if user == computer:
        print("Kalian memilih pilihan yang sama")
    elif user == "batu":
        if computer == "gunting":
            print("Batu menghancurkan gunting. User Menang!")
        else:
            print("Kertas membungkus batu. Komputer Menang!")
    elif user == "gunting":
        if computer == "batu":
            print("Batu menghancurkan gunting. Komputer Menang!")
        else:
            print("Gunting memotong kertas. User Menang!")
    elif user == "kertas":
        if computer == "batu":
            print("Kertas membungkus batu. User Menang!")
        else:
            print("Gunting memotong kertas. Komputer Menang!")

game()
ask = input("Apakah anda ingin melanjutkan (y/n) : ")
while ask == "y":
    game()
    ask = input("Apakah anda ingin melanjutkan (y/n) : ")
    if ask == "n":
        print("Terimakasih telah bermain")
if ask == "n":
    print("Terimakasih telah bermain")


#code by utari8