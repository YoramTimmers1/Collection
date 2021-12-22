Kleuren = ["oranje","groen","bruin","blauw"]

def MnM(Kleuren):
    HoeveelMnMkleuren = input("hoeveel kleuren wil je :")
    import random
    for i in range(int(HoeveelMnMkleuren)):
        print(random.choice(Kleuren))
MnM(Kleuren)