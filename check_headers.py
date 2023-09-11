import requests
from termcolor import colored

# Başlıkları ve çözümleri içeren veri yapısı
header_solutions = {
    'X-Frame-Options': {
        'issue': 'Başlık eksik',
        'solution': 'Clickjacking saldırılarını önlemek için "DENY" veya "SAMEORIGIN" değerine sahip bir X-Frame-Options başlığı ekleyin.'
    },
    'Content-Security-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'Siteniz için bir güvenlik politikası belirlemek için bir Content-Security-Policy başlığı ekleyin.'
    },
    'Strict-Transport-Security': {
        'issue': 'Başlık eksik',
        'solution': 'Güvenli HTTPS bağlantılarını zorlamak için bir Strict-Transport-Security başlığı ekleyin.'
    },
    'X-Content-Type-Options': {
        'issue': 'Başlık eksik',
        'solution': 'MIME türü tespitini önlemek için "nosniff" değerine sahip bir X-Content-Type-Options başlığı ekleyin.'
    },
    'X-XSS-Protection': {
        'issue': 'Başlık eksik',
        'solution': 'XSS korumasını etkinleştirmek için "1; mode=block" değerine sahip bir X-XSS-Protection başlığı ekleyin.'
    },
    'Cache-Control': {
        'issue': 'Başlık eksik',
        'solution': 'Önbellekleme davranışını kontrol etmek için bir Cache-Control başlığı ekleyin.'
    },
    'Server': {
        'issue': 'Sunucu bilgisi açığa çıkarıldı',
        'solution': 'Güvenlik için sunucu başlığını kaldırmayı veya gizlemeyi düşünün.'
    },
    'X-Powered-By': {
        'issue': 'Sunucu teknolojisi açığa çıkarıldı',
        'solution': 'Güvenlik için X-Powered-By başlığını kaldırmayı veya gizlemeyi düşünün.'
    },
    'Cross-Origin-Embedder-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'Kaynak yükleme ve gömme politikalarını kontrol etmek için bir Cross-Origin-Embedder-Policy başlığı ekleyin.'
    },
    'Cross-Origin-Opener-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'Belgenin diğer kökenler tarafından nasıl açıldığını kontrol etmek için bir Cross-Origin-Opener-Policy başlığı ekleyin.'
    },
    'Cross-Origin-Resource-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'Hangi kökenlerin kaynaklara erişebileceğini kontrol etmek için bir Cross-Origin-Resource-Policy başlığı ekleyin.'
    },
    'Origin-Agent-Cluster': {
        'issue': 'Başlık eksik',
        'solution': 'Çapraz köken izole isteklerini etkinleştirmek için bir Origin-Agent-Cluster başlığı ekleyin.'
    },
    'Referrer-Policy': {
        'issue': 'Başlık eksik',
        'solution': 'İsteklerle birlikte gönderilen referans bilgisini kontrol etmek için bir Referrer-Policy başlığı ekleyin.'
    },
    'X-DNS-Prefetch-Control': {
        'issue': 'Başlık eksik',
        'solution': 'DNS ön yükleme davranışını kontrol etmek için bir X-DNS-Prefetch-Control başlığı ekleyin.'
    },
    'X-Download-Options': {
        'issue': 'Başlık eksik',
        'solution': 'Dosya indirmelerinin otomatik olarak açılmasını önlemek için "noopen" değerine sahip bir X-Download-Options başlığı ekleyin.'
    },
    'Public-Key-Pins': {
        'issue': 'Başlık eksik',
        'solution': 'Yalnızca geçerli sertifikaların kabul edilmesini sağlamak için Public Key Pinning (PKP) uygulamayı düşünün.'
    },
    'Expect-CT': {
        'issue': 'Başlık eksik',
        'solution': 'Sertifika şeffaflık gereksinimlerini zorlamak için bir Expect-CT başlığı ekleyin.'
    },
}

# HTTP başlıklarını kontrol etmek için fonksiyon
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

if __name__ == "__main__":
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