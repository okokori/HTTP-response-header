import requests
from termcolor import colored

# HTTP başlıklarını kontrol etmek için fonksiyon
def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        results = []

        # X-Frame-Options başlığını kontrol et
        xfo_header = headers.get('X-Frame-Options', None)
        if xfo_header is None:
            results.append({
                'header': colored('X-Frame-Options', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Clickjacking saldırılarını önlemek için "DENY" veya "SAMEORIGIN" değerine sahip bir X-Frame-Options başlığı ekleyin.', 'yellow')
            })

        # Content-Security-Policy başlığını kontrol et
        csp_header = headers.get('Content-Security-Policy', None)
        if csp_header is None:
            results.append({
                'header': colored('Content-Security-Policy', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Siteniz için bir güvenlik politikası belirlemek için bir Content-Security-Policy başlığı ekleyin.', 'yellow')
            })

        # Strict-Transport-Security başlığını kontrol et
        hsts_header = headers.get('Strict-Transport-Security', None)
        if hsts_header is None:
            results.append({
                'header': colored('Strict-Transport-Security', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Güvenli HTTPS bağlantılarını zorlamak için bir Strict-Transport-Security başlığı ekleyin.', 'yellow')
            })

        # X-Content-Type-Options başlığını kontrol et
        xcto_header = headers.get('X-Content-Type-Options', None)
        if xcto_header is None:
            results.append({
                'header': colored('X-Content-Type-Options', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('MIME türü tespitini önlemek için "nosniff" değerine sahip bir X-Content-Type-Options başlığı ekleyin.', 'yellow')
            })

        # X-XSS-Protection başlığını kontrol et
        xss_header = headers.get('X-XSS-Protection', None)
        if xss_header is None:
            results.append({
                'header': colored('X-XSS-Protection', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('XSS korumasını etkinleştirmek için "1; mode=block" değerine sahip bir X-XSS-Protection başlığı ekleyin.', 'yellow')
            })

        # Cache-Control başlığını kontrol et
        cache_header = headers.get('Cache-Control', None)
        if cache_header is None:
            results.append({
                'header': colored('Cache-Control', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Önbellekleme davranışını kontrol etmek için bir Cache-Control başlığı ekleyin.', 'yellow')
            })

        # Server başlığını kontrol et
        server_header = headers.get('Server', None)
        if server_header is not None:
            results.append({
                'header': colored('Server', 'red'),
                'issue': colored('Sunucu bilgisi açığa çıkarıldı', 'white'),
                'solution': colored('Güvenlik için sunucu başlığını kaldırmayı veya gizlemeyi düşünün.', 'yellow')
            })

        # X-Powered-By başlığını kontrol et
        powered_by_header = headers.get('X-Powered-By', None)
        if powered_by_header is not None:
            results.append({
                'header': colored('X-Powered-By', 'red'),
                'issue': colored('Sunucu teknolojisi açığa çıkarıldı', 'white'),
                'solution': colored('Güvenlik için X-Powered-By başlığını kaldırmayı veya gizlemeyi düşünün.', 'yellow')
            })

        # Cross-Origin-Embedder-Policy başlığını kontrol et
        coep_header = headers.get('Cross-Origin-Embedder-Policy', None)
        if coep_header is None:
            results.append({
                'header': colored('Cross-Origin-Embedder-Policy', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Kaynak yükleme ve gömme politikalarını kontrol etmek için bir Cross-Origin-Embedder-Policy başlığı ekleyin.', 'yellow')
            })

        # Cross-Origin-Opener-Policy başlığını kontrol et
        coop_header = headers.get('Cross-Origin-Opener-Policy', None)
        if coop_header is None:
            results.append({
                'header': colored('Cross-Origin-Opener-Policy', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Belgenin diğer kökenler tarafından nasıl açıldığını kontrol etmek için bir Cross-Origin-Opener-Policy başlığı ekleyin.', 'yellow')
            })

        # Cross-Origin-Resource-Policy başlığını kontrol et
        corp_header = headers.get('Cross-Origin-Resource-Policy', None)
        if corp_header is None:
            results.append({
                'header': colored('Cross-Origin-Resource-Policy', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Hangi kökenlerin kaynaklara erişebileceğini kontrol etmek için bir Cross-Origin-Resource-Policy başlığı ekleyin.', 'yellow')
            })

        # Origin-Agent-Cluster başlığını kontrol et
        oac_header = headers.get('Origin-Agent-Cluster', None)
        if oac_header is None:
            results.append({
                'header': colored('Origin-Agent-Cluster', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Çapraz köken izole isteklerini etkinleştirmek için bir Origin-Agent-Cluster başlığı ekleyin.', 'yellow')
            })

        # Referrer-Policy başlığını kontrol et
        referrer_header = headers.get('Referrer-Policy', None)
        if referrer_header is None:
            results.append({
                'header': colored('Referrer-Policy', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('İsteklerle birlikte gönderilen referans bilgisini kontrol etmek için bir Referrer-Policy başlığı ekleyin.', 'yellow')
            })

        # X-DNS-Prefetch-Control başlığını kontrol et
        dns_prefetch_header = headers.get('X-DNS-Prefetch-Control', None)
        if dns_prefetch_header is None:
            results.append({
                'header': colored('X-DNS-Prefetch-Control', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('DNS ön yükleme davranışını kontrol etmek için bir X-DNS-Prefetch-Control başlığı ekleyin.', 'yellow')
            })

        # X-Download-Options başlığını kontrol et
        download_header = headers.get('X-Download-Options', None)
        if download_header is None:
            results.append({
                'header': colored('X-Download-Options', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Dosya indirmelerinin otomatik olarak açılmasını önlemek için "noopen" değerine sahip bir X-Download-Options başlığı ekleyin.', 'yellow')
            })

        # Public Key Pinning (PKP) başlığını kontrol et
        pkp_header = headers.get('Public-Key-Pins', None)
        if pkp_header is None:
            results.append({
                'header': colored('Public-Key-Pins', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Yalnızca geçerli sertifikaların kabul edilmesini sağlamak için Public Key Pinning (PKP) uygulamayı düşünün.', 'yellow')
            })

        # Expect-CT başlığını kontrol et
        expect_ct_header = headers.get('Expect-CT', None)
        if expect_ct_header is None:
            results.append({
                'header': colored('Expect-CT', 'red'),
                'issue': colored('Başlık eksik', 'white'),
                'solution': colored('Sertifika şeffaflık gereksinimlerini zorlamak için bir Expect-CT başlığı ekleyin.', 'yellow')
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