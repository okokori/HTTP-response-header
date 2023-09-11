import requests
from termcolor import colored

header_solutions = {
    'X-Frame-Options': {
        'issue': 'Başlık eksik',
        'solution': 'Clickjacking saldırılarını önlemek için "DENY" veya "SAMEORIGIN" değerine sahip bir X-Frame-Options başlığı ekleyin.'
    },
    'X-Content-Type-Options': {
        'issue': 'Başlık eksik',
        'solution': 'MIME türü tespitini önlemek için "nosniff" değerine sahip bir X-Content-Type-Options başlığı ekleyin.'
    },
    'X-XSS-Protection': {
        'issue': 'Başlık eksik',
        'solution': 'XSS korumasını etkinleştirmek için "1; mode=block" değerine sahip bir X-XSS-Protection başlığı ekleyin.'
    },
    'X-Download-Options': {
        'issue': 'Başlık eksik',
        'solution': 'Dosya indirmelerinin otomatik olarak açılmasını önlemek için "noopen" değerine sahip bir X-Download-Options başlığı ekleyin.'   
    },
    'Content-Security-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'Siteniz için bir güvenlik politikası belirlemek için bir Content-Security-Policy başlığı ekleyin.'
    },
    'Strict-Transport-Security': {
        'issue': 'Başlık eksik',
        'solution': 'Güvenli HTTPS bağlantılarını zorlamak için bir Strict-Transport-Security başlığı ekleyin.'
    },
    'Server': {
        'issue': 'Sunucu bilgisi açığa çıkarıldı',
        'solution': 'Güvenlik için sunucu başlığını kaldırmayı veya gizlemeyi düşünün.'
    },
    'Referrer-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'İsteklerle birlikte gönderilen referans bilgisini kontrol etmek için bir Referrer-Policy başlığı ekleyin.'
    },
    'Public-Key-Pins': {
        'issue': 'Başlık eksik',
        'solution': 'Yalnızca geçerli sertifikaların kabul edilmesini sağlamak için Public Key Pinning (PKP) uygulamayı düşünün.'
    },
}

def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        results = []
        for header, solution in header_solutions.items():
            header_value = headers.get(header, None)
            if header_value is None:
                results.append({
                    'header': colored(header, 'red'),
                    'issue': colored(solution['issue'], 'white'),
                    'solution': colored(solution['solution'], 'yellow')
                })
        return results
    except Exception as e:
        return [{'error': str(e)}]

def list_available_headers():
    print("Kullanılabilir HTTP Başlıkları:")
    for i, header in enumerate(header_solutions.keys(), start=1):
        print(f"{i}. {header}")

if __name__ == "__main__":
    while True:
        print("\nHTTP Security Headers Analiz Aracı")
        print("1. Kullanılabilir HTTP Başlıklarını Listele")
        print("2. Seçilen HTTP Başlıklarını Kontrol Et")
        print("3. IP veya Alan Adı ile Default Güvenlik Başlıklarını Kontrol Et")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3/4): ")
        if choice == '1':
            list_available_headers()
        elif choice == '2':
            target_url = input("Hedef URL'yi girin: ")
            header_results = check_headers(target_url)
            if 'error' in header_results[0]:
                print(f"Başlıklar kontrol edilirken bir hata oluştu: {header_results[0]['error']}")
            else:
                print("\nGüvenlik Kontrol Sonuçları:")
                for result in header_results:
                    print(f"Başlık: {result['header']}")
                    print(f"Problemi: {result['issue']}")
                    print(f"Çözüm: {result['solution']}\n")
        elif choice == '3':
            ip_or_domain = input("IP veya Alan Adı'nı girin: ")
            # IP veya Alan Adı'na özgü kontrol kodlarını ekleyebilirsiniz.
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek! Lütfen tekrar deneyin.")