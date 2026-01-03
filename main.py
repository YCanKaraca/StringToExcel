Nace_Kodlari=[
    [11107,"Börülce yetiştirilmesi"],
    [11107,"Fasulye (taze ve kuru) yetiştirilmesi"],
    [11107,"Taze baklagil sebzelerin yetiştirilmesi"],
    [11107,"Taze baklagil sebzelerin yetiştirilmesi"],
    [11107,"Mercimek yetiştirilmesi"],
    [11107,"Barbunya yetiştirilmesi"],
    [11107,"Baklagillerin yetiştirilmesi"],
    [11107,"Acı bakla yetiştirilmesi"],
    [11107,"Nohut yetiştirilmesi"],
    [11107,"Diğer baklagillerin yetiştirilmesi"],
    [11107,"Araka yetiştirilmesi"],
    [11107,"Bezelye yetiştirilmesi"],
    [11112,"Darı yetiştirilmesi"],
    [11112,"Süpürge darısı yetiştirilmesi"],
    [11112,"Buğday yetiştirilmesi"],
    [11112,"Dane mısır yetiştirilmesi"],
    [11112,"Kaplıca buğdayı yetiştirilmesi"],
    [11112,"Triticale yetiştirilmesi"],
    [11112,"Kuş yemi bitkisi yetiştirilmesi"],
    [11112,"Tahılların yetiştirilmesi"],
    [11112,"Sorgum yetiştirilmesi"],
    [11112,"Yulaf yetiştirilmesi"],
    [11112,"Çavdar yetiştirilmesi"],
    [11112,"Kara buğdayın yetiştirilmesi"],
    [11112,"Arpa yetiştirilmesi"],
    [11114,"Tohumluk haşhaş yetiştirilmesi"],
    [11114,"Soya fasulyesi yetiştirilmesi"],
    [11114,"Kolza yetiştirilmesi"],
    [11114,"Kanola ve kolza tohumu yetiştirilmesi"],
    [11114,"Nijer tohumu yetiştirilmesi"],
    [11114,"Aspir tohumu yetiştirilmesi"],
    [11114,"Pamuk çekirdeği yetiştirilmesi"],
    [11114,"Keten tohumu yetiştirilmesi"],
    [11114,"Diğer yağlı tohumların yetiştirilmesi"],
    [11114,"Ayçiçeği tohumu yetiştirilmesi"],
    [11114,"Hardal tohumu yetiştirilmesi"],
    [11114,"Susam tohumu yetiştirilmesi"],
    [11114,"Kene otu tohumu (hint yağı çekirdeği) yetiştirilmesi"],
    [11114,"Yer fıstığı yetiştirilmesi"],
    [11114,"Yağlı tohumların yetiştirilmesi"],
    [11214,"Çeltik (kabuklu pirinç) yetiştirilmesi"],
    [11317,"Şeker pancarı yetiştirilmesi"],
    [11317,"Şekerpancarı yetiştirilmesi"],
    [11317,"Şeker pancarı tohumu yetiştirilmesi"],
    [11318,"Hint yer elması (yam) yetiştirilmesi"],
    [11318,"Sahlep yetiştirilmesi"],
    [11318,"Patates yetiştirilmesi"],
    [11318,"Tatlı patates yetiştirilmesi"],
    [11318,"Kök ve yumruları tüketilen sebzelerin yetiştirilmesi"],
    [11318,"Salep yetiştirilmesi"],
    [11318,"Yer elması yetiştirilmesi"],
    [11318,"Manyok yetiştirilmesi"],
    [11320,"Domates yetiştirilmesi"],
    [11320,"Acur yetiştirilmesi"],
    [11320,"Yer kirazı (altın çilek) yetiştirilmesi"],
    [11320,"Altın çilek yetiştirilmesi"],
    [11320,"Kabak yetiştirilmesi"],
    [11320,"Patlıcan yetiştirilmesi"],
    [11320,"Tatlı mısır yetiştirilmesi"],
    [11320,"Hıyar ve kornişon yetiştirilmesi"],
    [11320,"Lif kabağı yetiştirilmesi"],
    [11320,"Kantalup kavunu yetiştirilmesi"],
    [11320,"Sivri ve dolmalık biberler yetiştirilmesi"]
]

def excel_gibi_yazdir(liste):
    if type(liste)!=type(list()):
        return "Girilen veriler bir liste değildir. Lütfen liste giriniz."
    elif type(liste[0])!=type(list()):
        return "Girilen listenin alt elemanları da liste olmak zorundadır."
    else:
        liste_eleman_sayisi=len(liste)
        alt_eleman_sayisi=len(liste[0])
        uzunluk=list()
        #uzunluk[0]=14
        #uzunluk[1]=54
        for sayi in range(alt_eleman_sayisi):
            uzunluk.append(max([len(str(eleman[sayi])) for eleman in liste])+2)
        metin="|"
        for ust_sayi in range(liste_eleman_sayisi):
            for alt_sayi in range(alt_eleman_sayisi):
                metin+=str(liste[ust_sayi][alt_sayi]).center(uzunluk[alt_sayi])+"|"
            metin+="\n|"

    return metin[:-2]

print(excel_gibi_yazdir(Nace_Kodlari))


