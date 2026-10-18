süper_lig ={"fenerbahçe":"63 puan",
            "galatasaray":"61 puan",
            "beşiktaş":"59 puan",
            "trabzonspor":"57 puan",}

while True:
    takım_ekle = input("lütfen eklemek istediğiniz takımı giriniz : ")
    puan_ekle = input("lütfen eklemek istediğiniz takımın puanını giriniz : ")
    süper_lig.setdefault(takım_ekle,puan_ekle)


    for i,j in süper_lig.items():
        print(i,j)

    seçim = input("devam etmek istiyor musunuz ? (e/h) : ").lower()

    if seçim == "h":
        print("çıkış yaptınız.)")
        break
    else:
        pass