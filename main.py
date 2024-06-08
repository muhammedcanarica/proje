from Personel import Personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

import pandas as pd

# Sütun genişliği
pd.set_option('display.max_colwidth', None)

# Sütun sayısı
pd.set_option('display.max_columns', None)

# Maksimum satır sayısı
pd.set_option('display.max_rows', None)

# Çerçeve satırlarını genişletme
pd.set_option('display.width', 1000)

def main():
    doktor1 = ""
    doktor2 = ""
    doktor3 = ""
    personel1 = ""
    personel2 = ""
    hemsire1 = ""
    hemsire2 = ""
    hemsire3 = ""
    hasta1 = ""
    hasta2 = ""
    hasta3 = ""
    try:
        personel1 = Personel(1, "Hasan", "Uçar", "Yönetim", 5000)
        personel2 = Personel(2, "Faik", "Duman", "Muhasebe", 6000)
        print(personel1)
        print(personel2)
    except Exception as e:
        print(f'Personel oluşturulurken bir hata oluştu: {e}')

    try:
        doktor1 = Doktor(3, "Muhammed", "Arıca", "Cerrahi", 8000, "Genel Cerrah", 10, "Hacettepe Üniversitesi")
        doktor2 = Doktor(4, "Batuhan", "Marıltı", "Kardiyoloji",9000 , "Kardiyolog", 6,"Uludağ Üniversitesi")
        doktor3 = Doktor(5, "Mustafa", "Cecel", "Pediatri", 8500, "Pediatrist", 3, "Memorial Hastanesi")
        print(doktor1)
        print(doktor2)
        print(doktor3)
    except Exception as e:
        print(f'Doktor oluşturulurken bir hata oluştu: {e}')

    try:
        hemsire1 = Hemsire(6, "Çeçil", "Taş", "Yoğun Bakım", 4500, 40, "Yoğun Bakım Sertifikası", "Memorial Hastanesi")
        hemsire2 = Hemsire(7, "Yunus", "Taş", "Ameliyathane", 4200, 38, "Ameliyathane Sertifikası", "Uludağ Üniversitesi")
        hemsire3 = Hemsire(8, "Şebnem", "Mera", "Dahiliye", 4600, 10, "Dahiliye Sertifikası", "Hacettepe Hastanesi")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)
    except Exception as e:
        print(f'Hemşire oluşturulurken bir hata oluştu: {e}')

    try:
        hasta1 = Hasta(9, "Mesut", "komser", "1992-01-15", "karizma", "hiçbir şey")
        hasta2 = Hasta(10, "Emirhan", "Oğuz", "1985-05-20", "Gut hastalığı", "Diyet")
        hasta3 = Hasta(11, "Zerya", "Tekeş", "2000-07-25", "kırık", "alçıya alma")
        print(hasta1)
        print(hasta2)
        print(hasta3)
    except Exception as e:
        print(f'Hasta oluşturulurken bir hata oluştu: {e}')

    data = [
        {'personel_no': personel1.get_personel_no(), 'ad': personel1.get_ad(), 'soyad': personel1.get_soyad(),
         'departman': personel1.get_departman(), 'maas': personel1.get_maas(), 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': 0, 'calisma_saati': 0, 'sertifika': 0, 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0,
         'tedavi': 0},
        {'personel_no': personel2.get_personel_no(), 'ad': personel2.get_ad(), 'soyad': personel2.get_soyad(),
         'departman': personel2.get_departman(), 'maas': personel2.get_maas(), 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': 0, 'calisma_saati': 0 , 'sertifika': 0, 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0,
         'tedavi': 0},
        {'personel_no': doktor1.get_personel_no(), 'ad': doktor1.get_ad(), 'soyad': doktor1.get_soyad(),
         'departman': doktor1.get_departman(), 'maas': doktor1.get_maas(), 'uzmanlik': doktor1.get_uzmanlik(),
         'deneyim_yili': doktor1.get_deneyim_yili(), 'hastane': doktor1.get_hastane(), 'calisma_saati': 0,
         'sertifika': 0, 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0, 'tedavi': 0},
        {'personel_no': doktor2.get_personel_no(), 'ad': doktor2.get_ad(), 'soyad': doktor2.get_soyad(),
         'departman': doktor2.get_departman(), 'maas': doktor2.get_maas(), 'uzmanlik': doktor2.get_uzmanlik(),
         'deneyim_yili': doktor2.get_deneyim_yili(), 'hastane': doktor2.get_hastane(), 'calisma_saati': 0,
         'sertifika': 0, 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0, 'tedavi': 0},
        {'personel_no': doktor3.get_personel_no(), 'ad': doktor3.get_ad(), 'soyad': doktor3.get_soyad(),
         'departman': doktor3.get_departman(), 'maas': doktor3.get_maas(), 'uzmanlik': doktor3.get_uzmanlik(),
         'deneyim_yili': doktor3.get_deneyim_yili(), 'hastane': doktor3.get_hastane(), 'calisma_saati': 0,
         'sertifika': 0, 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0, 'tedavi': 0},
        {'personel_no': hemsire1.get_personel_no(), 'ad': hemsire1.get_ad(), 'soyad': hemsire1.get_soyad(),
         'departman': hemsire1.get_departman(), 'maas': hemsire1.get_maas(), 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': hemsire1.get_hastane(), 'calisma_saati': hemsire1.get_calisma_saati(),
         'sertifika': hemsire1.get_sertifika(), 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0, 'tedavi': 0},
        {'personel_no': hemsire2.get_personel_no(), 'ad': hemsire2.get_ad(), 'soyad': hemsire2.get_soyad(),
         'departman': hemsire2.get_departman(), 'maas': hemsire2.get_maas(), 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': hemsire2.get_hastane(), 'calisma_saati': hemsire2.get_calisma_saati(),
         'sertifika': hemsire2.get_sertifika(), 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0, 'tedavi': 0},
        {'personel_no': hemsire3.get_personel_no(), 'ad': hemsire3.get_ad(), 'soyad': hemsire3.get_soyad(),
         'departman': hemsire3.get_departman(), 'maas': hemsire3.get_maas(), 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': hemsire3.get_hastane(), 'calisma_saati': hemsire3.get_calisma_saati(),
         'sertifika': hemsire3.get_sertifika(), 'hasta_no': 0, 'dogum_tarihi': 0, 'hastalik': 0, 'tedavi': 0},
        {'personel_no': 0, 'ad': hasta1.get_ad(), 'soyad':hasta1.get_soyad(), 'departman': 0, 'maas': 0, 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': 0, 'calisma_saati':0, 'sertifika': 0, 'hasta_no': hasta1.get_hasta_no(),
         'dogum_tarihi': hasta1.get_dogum_tarihi(), 'hastalik': hasta1.get_hastalik(), 'tedavi': hasta1.get_tedavi()},
        {'personel_no': 0, 'ad': hasta2.get_ad(), 'soyad': hasta2.get_soyad(), 'departman': 0, 'maas': 0, 'uzmanlik': 0, 'deneyim_yili':0 ,
         'hastane': 0, 'calisma_saati': 0, 'sertifika': 0, 'hasta_no': hasta2.get_hasta_no(),
         'dogum_tarihi': hasta2.get_dogum_tarihi(), 'hastalik': hasta2.get_hastalik(), 'tedavi': hasta2.get_tedavi()},
        {'personel_no': 0, 'ad': hasta3.get_ad(), 'soyad': hasta3.get_soyad(), 'departman': 0, 'maas': 0, 'uzmanlik': 0, 'deneyim_yili': 0,
         'hastane': 0, 'calisma_saati': 0, 'sertifika': 0, 'hasta_no': hasta3.get_hasta_no(),
         'dogum_tarihi': hasta3.get_dogum_tarihi(), 'hastalik': hasta3.get_hastalik(), 'tedavi': hasta3.get_tedavi()}
    ]

    df = pd.DataFrame(data)
    df['deneyim_yili'] = df["deneyim_yili"].astype(int)
    print("DataFrame:")
    print(df)

    # Boş olan kısımlara None yazdırma
    df.replace(0, 0, inplace=True)

    # dogum_tarihi sütununu tarih formatına çevirme
    df['dogum_tarihi'] = pd.to_datetime(df['dogum_tarihi'], errors='coerce')

    print("DataFrame with corrected dogum_tarihi:")
    print(df)

    # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplayıp ve yazdırma
    doktor_grup = df[df['uzmanlik'] != 0].groupby('uzmanlik').size()
    print("\nDoktorların uzmanlık alanlarına göre gruplandırılmış toplam sayısı:")
    print(doktor_grup)

    # 5 yıldan fazla deneyimi olanları bulup yazdırma
    doktor_deneyim = df[df['deneyim_yili'] > 5]['deneyim_yili'].count()
    print("\n5 yıldan fazla deneyime sahip doktorların toplam sayısı:", doktor_deneyim)

    # Hasta adına göre alfabetik sıralama yapma
    df_hasta_siralama = df[df['hasta_no'] != 0].sort_values(by='ad')
    print("\nHasta adına göre alfabetik olarak sıralanmış DataFrame:")
    print(df_hasta_siralama)

    # Maaşı 7000 TL üzerinde olanları bulup yazdırma
    maas_ustu = df[df['maas'] > 7000]
    print("\nMaaşı 7000 TL üzerinde olan personeller:")
    print(maas_ustu)

    df_dogum_tarihi = df[df['dogum_tarihi'] >= '1990-01-01']
    print("\nDoğum tarihi 1990 ve sonrası olan hastalar:")
    print(df_dogum_tarihi)

    yeni_df = df[['ad', 'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastalik', 'tedavi']]
    print("\nYeni DataFrame:")
    print(yeni_df)


if __name__ == "__main__":
    main()
