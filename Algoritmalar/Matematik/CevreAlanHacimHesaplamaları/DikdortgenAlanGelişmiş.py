def cozum():
    kenar1 = float (input("Dikdörgenin 1.kenarın uzunluğunu giriniz: "))
    kenar2 = float (input("Dikdörgenin 2.kenarın uzunluğunu giriniz: "))
    if kenar1 == kenar2:
        print("Girdiğiniz değerler bir kareye aittir. Lütfen değerleri birbirinden farklı giriniz.")
        cozum()
    else:
        alan = kenar1*kenar2
        print("1 kenarının uzunluğu {} ve diğer kenarının uzunluğu {} olan dikdörtgenin alanı = {}".format(kenar1,kenar2,alan))

cozum()
