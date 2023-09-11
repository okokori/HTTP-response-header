import requests
import time

def http_basliklarini_listele_sadece():
    url = input("HTTP başlıklarını listelemek istediğiniz web sitesinin URL'sini girin: ")
    response = requests.head(url)
    headers = response.headers
    
    print("\n")

    print("HTTP Başlıkları:")
    header_list = list(headers.keys())
    for i, header in enumerate(header_list, start=1):
        header_value = headers[header].split(":")[0]  # ':' karakterinden önceki kısmı al
        print(f"{i}-) {header}")

    print("\n")
    
def istege_bagli_http_basliklarini_kontrol_et():
    url = input("HTTP başlıklarını kontrol etmek istediğiniz web sitesinin URL'sini girin: ")
    headers_to_check = input("Kontrol etmek istediğiniz HTTP başlıklarını virgülle ayırarak girin: ").split(",")
    response = requests.get(url)
    headers = response.headers

    print("HTTP Başlıkları:")
    for header in headers_to_check:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header} başlığı yanıtta bulunamadı.")

    print("\n")

def full_tarama():
    url = input("Taramak istediğiniz web sitesinin URL'sini girin: ")
    response = requests.get(url)
    headers = response.headers
    content = response.content

    # İstediğiniz işlemleri gerçekleştirin

    print("Tarama tamamlandı.\n")

while True:
    print("Seçenekler:")
    print("1. HTTP başlıklarını listele")
    print("2. İsteğe bağlı HTTP başlıklarını kontrol et")
    print("3. Full tarama")
    print("4. Çıkış")

    secim = input("Bir seçenek girin (1, 2, 3, 4): ")

    if secim == "1":
        http_basliklarini_listele_sadece()
    elif secim == "2":
        istege_bagli_http_basliklarini_kontrol_et()
    elif secim == "3":
        full_tarama()
    elif secim == "4":
        print("Çıkış yapılıyor...")
        time.sleep(0) 
        break
    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")