"""
Toyota Corolla 1.6 (132hp) Kaç yakar

yakıt deposu hacmi: 55 litre
şehir içi yakıt tüketimi: 8.0lt/100km
benzin fiyatı: 7,91 tl
"""
hacim = float(input("Aracınızın yakıt deposu hacmi kaç litre?: "))
yakitt = float(input("Aracınız şehir içinde 100 km'de kaç lt yakıyor?: "))
benzin_fiyatı = 7.91

yakim = yakitt / 100
yol = (hacim / yakitt) * 100.0
fulldepotl = hacim * benzin_fiyatı


print("Aracınız kilometrede {} lt benzin yakıyor".format(yakim))
print("Aracınız full depoda {} km yol yapıyor".format(yol))
print("Aracınızın deposu full doldurulduğunda {} tl ödemeniz gerekiyor".format(fulldepotl))